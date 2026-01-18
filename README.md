# 📊 Statistical Distribution Fitting Tool

A Streamlit web application designed to help users fit various statistical distributions to their data. This tool allows for quick visualization, parameter estimation, and quality assessment of different probability distributions against user-provided datasets.

## ✨ Features

- **Data Input Flexibility**:
  - Enter raw data manually (comma or space-separated).
  - Upload CSV files and select specific columns for analysis.
- **Multiple Distributions**: Support for fitting 10+ standard distributions including:
  - Normal, Gamma, Weibull, Exponential, Beta, Lognormal, Chi-square, Laplace, Cauchy, and Uniform.
- **Automatic Fitting**: Calculates the optimal parameters for the selected distribution using Maximum Likelihood Estimation (MLE).
- **Interactive Adjustments**: Manually fine-tune fitted parameters using sliders to see how they affect the curve in real-time.
- **Visualization**:
  - Displays a histogram of your data.
  - Overlays the fitted probability density function (PDF) curve.
- **Goodness of Fit Metrics**:
  - **Mean Absolute Error (MAE)**: Measures the average vertical distance between the histogram and the PDF.
  - **Maximum Error**: Identifies the largest deviation point.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed (preferably 3.8 or higher).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RebantaGupta/Streamlit-Project.git
   cd Streamlit-Project
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

Run the application using the Streamlit CLI:

```bash
streamlit run Project_RVG.py
```

The app will open automatically in your default web browser at `http://localhost:8501`.

## 📦 Dependencies

The project relies on the following Python libraries (see `requirements.txt`):
- `streamlit`: For the web interface.
- `numpy`: For numerical operations.
- `pandas`: For data manipulation and CSV handling.
- `scipy`: For statistical distribution functions and fitting.
- `matplotlib`: For generating plots and charts.

## 🛠️ Usage Guide

1. **Load Data**: Open the sidebar tab "Data Input" to paste your numbers or upload a CSV file.
2. **Select Distribution**: Switch to the "Distribution Selection" tab in the sidebar and choose a distribution type (e.g., Normal, Gamma).
3. **Analyze**: The main area will show the fitted parameters and a plot.
4. **Refine**: Expand the "Manual Parameter Adjustment" section to tweak the values if the automatic fit isn't perfect.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source.
