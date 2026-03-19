/** @odoo-module **/

import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";
import { Component, onWillStart, onMounted, useRef, useState } from "@odoo/owl";
import { loadJS } from "@web/core/assets";

export class SupplyForecastDashboard extends Component {
    static template = "supply_forecast.SupplyForecastDashboard";

    setup() {
        this.rpc = rpc;
        this.demandChartRef = useRef("demandChart");
        this.productsChartRef = useRef("productsChart");
        this.state = useState({
            data: {
                total_forecasted: "0",
                pending_confirmations: 0,
                accuracy_avg: "0%",
                graph_demand: { labels: [], datasets: [] },
                graph_products: { labels: [], datasets: [] }
            },
        });

        onWillStart(async () => {
            await loadJS("/web/static/lib/Chart/Chart.js");
            const data = await this.rpc("/web/dataset/call_kw/supply.forecast/get_dashboard_data", {
                model: "supply.forecast",
                method: "get_dashboard_data",
                args: [],
                kwargs: {},
            });
            Object.assign(this.state.data, data);
        });

        onMounted(() => {
            this.renderCharts();
        });
    }

    renderCharts() {
        const { graph_demand, graph_products } = this.state.data;
        
        // Configuración común de Chart.js
        Chart.defaults.color = '#475569';
        Chart.defaults.font.family = "'Inter', 'sans-serif'";

        // Demand Chart
        if (this.demandChartRef.el) {
            new Chart(this.demandChartRef.el, {
                type: 'line',
                data: graph_demand,
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: 'rgba(30, 41, 59, 0.9)',
                            padding: 12,
                            borderRadius: 8
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            grid: { color: '#f1f5f9' },
                            border: { display: false }
                        },
                        x: {
                            grid: { display: false },
                            border: { display: false }
                        }
                    }
                }
            });
        }

        // Products Chart
        if (this.productsChartRef.el) {
            new Chart(this.productsChartRef.el, {
                type: 'bar',
                data: graph_products,
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    indexAxis: 'y',
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        x: {
                            beginAtZero: true,
                            grid: { color: '#f1f5f9' },
                            border: { display: false }
                        },
                        y: {
                            grid: { display: false },
                            border: { display: false }
                        }
                    }
                }
            });
        }
    }
}

registry.category("actions").add("supply_forecast_dashboard", SupplyForecastDashboard);
