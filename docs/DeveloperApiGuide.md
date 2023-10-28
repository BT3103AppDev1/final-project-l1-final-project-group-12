# Developer Guide: Accessing the YFinance API

This guide provides instructions on how to access the API endpoints exposed by the routes.

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

```
curl http://<your-server-url>/api/stockStatistics/AAPL
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
curl http://<your-server-url>/api/historicalData/AAPL?period=1Y&interval=1d
```

3. Get Options Data

- Endpoint: `/optionsData/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Example: `/optionsData/AAPL`

#### Usage:

```
curl http://<your-server-url>/api/optionsData/AAPL
```

4. Get Latest Stock Price

- Endpoint: `/curentPrice/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)
- Example: `/curentPrice/AAPL`

#### Usage:

```
curl http://<your-server-url>/api/curentPrice/AAPL
```

## API Endpoints for Reading Firestore Data

1. Get User Information

- Endpoint: `/userInfo/:userEmail`
- Method: `GET`
- URL Params: `userEmail` (**required**)
- Example: `/userInfo/john.doe@example.com`

#### Usage:

```
curl http://<your-server-url>/api/read/user/john.doe@example.com
```

2. Get Portfolio Information

- Endpoint: `/portfolioInfo/:userEmail`
- Method: `GET`
- URL Params: `userEmail`(**required**)
- Example: `/portfolioInfo/john.doe@example.com`

#### Usage:

```
curl http://<your-server-url>/api/read/portfolio/john.doe@example.com
```

3. Get All Trades for a User

- Endpoint: `/allTrades/:userEmail`
- Method: `GET`
- URL Params: `userEmail`(**required**)
- Example: `/allTrades/john.doe@example.com`

#### Usage:

```
curl http://<your-server-url>/api/read/trades/john.doe@example.com
```

4. Get Specific Trade Details

- Endpoint: `/trade/:userEmail/:userId/:ticker`
- Method: `GET`
- URL Params:
  - `userEmail` (**required**)
  - `userId` (**required**)
  - `ticker` (**required**)
- Example: `/trade/john.doe@example.com/12345/AAPL`

#### Usage:

```
curl http://<your-server-url>/api/read/trade/john.doe@example.com/1234/AAPL
```
