# Developer Guide: Accessing the YFinance API

This guide provides instructions on how to access the API endpoints exposed by the `yfinance_controller.js` for retrieving stock statistics, historical data, and options data from Yahoo Finance.

## Getting Started

Ensure that you have the server running which hosts the `yfinance_controller.js` file.

Requirements:

- Node.js v18.16.0

## API Endpoints

### 1. Get Stock Statistics [DEPRECATED]

- Endpoint: `/stock-statistics/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Example: `/stock-statistics/AAPL`

#### Usage:

```bash
curl http://<your-server-url>/stock-statistics/AAPL
```

### 2. Get Historical Data

- Endpoint: `/historical-data/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Query Params:
  - period (optional) - Possible values: '1D', '5D', '3M', '6M', '1Y', '5Y'. Default: `1Y`
  - interval (optional) - Possible values: '1d', '1wk', '1mo'. Default: `1d`
- Example: `/historical-data/AAPL?period=1Y&interval=1d`

#### Usage:

```
curl http://<your-server-url>/historical-data/AAPL?period=1Y&interval=1d
```

3. Get Options Data

- Endpoint: `/options-data/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Example: `/options-data/AAPL`

#### Usage:

```
curl http://<your-server-url>/options-data/AAPL
```
