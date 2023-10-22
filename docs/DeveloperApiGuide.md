# Developer Guide: Accessing the YFinance API

This guide provides instructions on how to access the API endpoints exposed by the `yfinance_controller.js` for retrieving stock statistics, historical data, and options data from Yahoo Finance.

## Getting Started

Ensure that you have the server running which hosts the `yfinance_controller.js` file.

## API Endpoints

### 1. Get Stock Statistics

- Endpoint: `/stock-statistics/:ticker`
- Method: `GET`
- URL Params: `ticker` (required)
- Example: `/stock-statistics/AAPL`

#### Usage:

```bash
curl http://<your-server-url>/stock-statistics/AAPL
```
