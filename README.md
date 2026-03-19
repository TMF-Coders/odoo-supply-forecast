# AI Supply Chain Optimizer (Vertex AI)

Enterprise-grade demand forecasting and inventory optimization powered by **Google Vertex AI (TimesFM)**.

## 🚀 Overview
The **AI Supply Chain Optimizer** is designed for modern Odoo 19 environments that require precision in inventory management. By leveraging the latest breakthroughs in Time Series Foundation Models (TimesFM), it provides accurate predictions even for products with sparse data or high volatility.

## ✨ Key Features
- **AI-Powered Forecasting**: Uses Google Vertex AI's TimesFM Zero-Shot model.
- **Dynamic Safety Stock**: Adjust buffers based on 90%, 95%, or 99% Service Level targets.
- **Explainable AI (XAI)**: Every replenishment recommendation includes a detailed rationale.
- **Lead Time Sync**: Automatically calculates orders based on supplier delivery reliability.
- **Odoo 19 Native**: Fully compatible with the latest Odoo ORM and UI patterns.

## 🛠️ Requirements
- **Python Libraries**: `pandas`, `scipy`, `google-cloud-aiplatform`.
- **Google Cloud Platform**: A Vertex AI enabled project and a valid Service Account.

## 📦 Installation
1. Install the required python dependencies in your Odoo environment.
2. Place the module in your `addons_path`.
3. Go to `Apps` and search for "AI Supply Chain Optimizer".
4. Click **Activate**.

## ⚙️ Configuration
1. Navigate to **Inventory > Settings**.
2. Locate the **Vertex AI Parameters** section.
3. Configure your Project ID, Location, and Upload your JSON Service Account Key.
4. Set the default Forecast Horizon (e.g., 30 days).

## 👨‍💻 Author
**TMFCoders SL**  
[tmfcoders.com](https://tmfcoders.com)  

## 📄 License
Licensed under **OPL-1**.
