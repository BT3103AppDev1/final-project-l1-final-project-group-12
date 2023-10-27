# Developer Guide: Accessing the YFinance API

This guide provides instructions on how to access the API endpoints exposed by the `yfinance_controller.js` for retrieving stock statistics, historical data, and options data from Yahoo Finance.

## Getting Started

Run `npm run server` to start the backend server for local testing
Requirements:

- Node.js v18.16.0

## API Endpoints for Stock Data

### 1. Get Stock Statistics [DEPRECATED]

- Endpoint: `/stockStatistics/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Example: `/stockStatistics/AAPL`

#### Usage:

```bash
curl http://<your-server-url>/stockStatistics/AAPL
```

### 2. Get Historical Data

- Endpoint: `/historicalData/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Query Params:
  - period (optional) - Possible values: '1D', '5D', '3M', '6M', '1Y', '5Y'. Default: `1Y`
  - interval (optional) - Possible values: '1d', '1wk', '1mo'. Default: `1d`
- Example: `/historicalData/AAPL?period=1Y&interval=1d`

#### Usage:

```
curl http://<your-server-url>/historicalData/AAPL?period=1Y&interval=1d
```

3. Get Options Data

- Endpoint: `/optionsData/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Example: `/optionsData/AAPL`

#### Usage:

```
curl http://<your-server-url>/optionsData/AAPL
```

4. Get Latest Stock Price

- Endpoint: `/curentPrice/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Example: `/curentPrice/AAPL`

#### Usage:

```
curl http://<your-server-url>/curentPrice/AAPL
```

## API Endpoints for Portfolio Calculations
