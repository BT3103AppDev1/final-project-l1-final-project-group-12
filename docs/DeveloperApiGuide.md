# Developer Guide: Accessing the YFinance API

This guide provides instructions on how to access the API endpoints exposed by the routes.

## Getting Started

Run `npm run server` to start the backend server for local testing
Requirements:

- Node.js v18.16.0

## API Endpoints for Stock Data

```
/api/yfinance
```

### 1. Get Stock Statistics [DEPRECATED]

- Endpoint: `/yfinance/stockStatistics/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Example: `/yfinance/stockStatistics/AAPL`

#### Usage:

```
curl http://<your-server-url>/api/yfinance/stockStatistics/AAPL
```

### 2. Get Historical Data

- Endpoint: `/yfinance/historicalData/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Query Params:
  - period (optional) - Possible values: '1D', '5D', '3M', '6M', '1Y', '5Y'. Default: `1Y`
  - interval (optional) - Possible values: '1d', '1wk', '1mo'. Default: `1d`
- Example: `/yfinance/historicalData/AAPL?period=1Y&interval=1d`

#### Usage:

```
curl http://<your-server-url>/api/yfinance/historicalData/AAPL?period=1Y&interval=1d
```

3. Get Options Data

- Endpoint: `/yfinance/optionsData/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Example: `/yfinance/optionsData/AAPL`

#### Usage:

```
curl http://<your-server-url>/api/yfinance/optionsData/AAPL
```

4. Get Latest Stock Price

- Endpoint: `/curentPrice/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Example: `/curentPrice/AAPL`

#### Usage:

```
curl http://<your-server-url>/api/yfinance/curentPrice/AAPL
```

## API Endpoints for Reading Firestore Data

1. Get User Information

- Endpoint: `/read/userInfo/:userEmail`
- Method: `GET`
- URL Params: `userEmail` (**required**)
- Example: `/read/userInfo/john.doe@example.com`

#### Usage:

```
curl http://<your-server-url>/api/read/userInfo/john.doe@example.com
```

2. Get Portfolio Information

- Endpoint: `/read/portfolioInfo/:userEmail`
- Method: `GET`
- URL Params: `userEmail`(**required**)
- Example: `/read/portfolioInfo/john.doe@example.com`

#### Usage:

```
curl http://<your-server-url>/api/read/portfolioInfo/john.doe@example.com
```

3. Get All Trades for a User

- Endpoint: `/read/allTrades/:userEmail`
- Method: `GET`
- URL Params: `userEmail`(**required**)
- Example: `/read/allTrades/john.doe@example.com`

#### Usage:

```
curl http://<your-server-url>/api/read/allTrades/john.doe@example.com
```

4. Get Specific Trade Details

- Endpoint: `/read/trade/:userEmail/:userId/:ticker`
- Method: `GET`
- URL Params:
  - `userEmail` (**required**)
  - `userId` (**required**)
  - `ticker` (**required**)
- Example: `/read/trade/john.doe@example.com/12345/AAPL`

#### Usage:

```
curl http://<your-server-url>/api/read/trade/john.doe@example.com/1234/AAPL
```
