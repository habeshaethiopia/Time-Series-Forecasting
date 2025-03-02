# Time Series Forecasting for Portfolio Management Optimization



## **Project Overview**
This project aims to leverage time series forecasting models to enhance portfolio management strategies for Guide Me in Finance (GMF) Investments. By analyzing historical financial data for Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY), we develop predictive models to forecast future market trends, optimize asset allocation, and maximize returns while minimizing risks.

---

## **Objective**
The primary objective is to:
1. Preprocess and analyze historical financial data.
2. Develop and evaluate time series forecasting models (ARIMA, SARIMA, LSTM).
3. Forecast future stock prices for TSLA, BND, and SPY.
4. Optimize a sample investment portfolio based on the forecasts.

---

## **Dataset**
- **Source:** YFinance Python library.
- **Assets:** 
  - **TSLA:** High-growth, high-risk stock in the consumer discretionary sector (Automobile Manufacturing).
  - **BND:** A bond ETF tracking U.S. investment-grade bonds, providing stability and income.
  - **SPY:** An ETF tracking the S&P 500 Index, offering broad U.S. market exposure.
- **Time Period:** January 1, 2015, to January 31, 2025.
- **Features:**
  - Date: Trading day timestamp.
  - Open, High, Low, Close, Adj Close: Daily price metrics.
  - Volume: Total number of shares/units traded each day.

---

## **Tasks**

### **Task 1: Preprocess and Explore the Data**
- Extract historical financial data using YFinance.
- Clean and preprocess the data:
  - Handle missing values.
  - Normalize or scale the data if required.
- Conduct exploratory data analysis (EDA):
  - Visualize closing prices over time.
  - Calculate and plot daily percentage changes to observe volatility.
  - Analyze rolling means and standard deviations for short-term trends.
  - Perform outlier detection and seasonality analysis.

### **Task 2: Develop Time Series Forecasting Models**
- Build forecasting models for TSLA using ARIMA, SARIMA, or LSTM.
- Split the dataset into training and testing sets.
- Train and evaluate the models using metrics such as MAE, RMSE, and MAPE.
- Optimize model parameters using techniques like grid search or auto_arima.

### **Task 3: Forecast Future Market Trends**
- Use the trained models to forecast TSLA's future stock prices for 6-12 months.
- Analyze the results:
  - Identify long-term trends (upward, downward, or stable).
  - Assess volatility and risk using confidence intervals.
  - Outline potential market opportunities and risks.

### **Task 4: Optimize Portfolio Based on Forecast**
- Forecast future prices for BND and SPY.
- Combine the data into a single DataFrame containing daily closing prices for all assets.
- Compute annual returns, covariance matrix, and portfolio weights.
- Optimize the portfolio to maximize the Sharpe Ratio:
  - Adjust allocations to balance risk and return.
  - Include cumulative return charts and risk-return analysis.

---

## **Expected Outcomes**
- Competence in time series forecasting methods (ARIMA, SARIMA, LSTM).
- Experience in handling real-world financial data using YFinance.
- Skills in developing, evaluating, and deploying predictive models.
- Insights into risk management and return optimization strategies.

---

## **Usage**
1. Clone the repository:
   ```bash
   git clone https://github.com/habeshaethiopia/Time-Series-Forecasting.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebooks/scripts in the `notebooks/` folder to reproduce the results.

---

## **Repository Structure**
```
time-series-portfolio-optimization/
│
├── data/               # Raw and processed datasets
├── notebooks/          # Jupyter notebooks for analysis and modeling
├── src/                # Python scripts for preprocessing and modeling
├── scripts/            # helper scripts for data extraction and processing
├── README.md           # Project overview and instructions
└── requirements.txt    # List of dependencies
```

---

## **Dependencies**
- Python >= 3.8
- Libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - yfinance
  - statsmodels
  - scikit-learn
  - tensorflow (for LSTM)
  - pmdarima (optional, for auto_arima)

## **References**
 - [YFinance Documentation](https://pypi.org/project/yfinance/)
 - [my report](https://docs.google.com/document/d/1c2l5SAtIC4XbVt6c-dvUnKD5LkETewIJek5uhkvbTuw/edit?usp=sharing)
- [DataCamp: ARIMA](https://www.datacamp.com/tutorial/arima)
- [Machine Learning Mastery: ARIMA](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/)
- [Portfolio Optimization with PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt)
- [BuiltIn: Portfolio Optimization in Python](https://builtin.com/data-science/portfolio-optimization-python)

---

## **Contact**
For questions or feedback, please reach out to [adanemoges6@gmail.com].  

Thank you!