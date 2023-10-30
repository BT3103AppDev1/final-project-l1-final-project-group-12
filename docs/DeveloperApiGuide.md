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

### 1. Get Stock Statistics [`DEPRECATED`]

This function is no longer supported due to Yahoo Finance shutting down access to .info api

- Endpoint: `/yfinance/stockStatistics/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)

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

#### Usage:

```
curl http://<your-server-url>/api/yfinance/historicalData/AAPL?period=1Y&interval=1d
```

### 3. Get Options Data

- Endpoint: `/yfinance/optionsData/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/yfinance/optionsData/AAPL
```

### 4. Get Latest Stock Price

- Endpoint: `/curentPrice/:ticker`
- Method: `GET`
- URL Params: `ticker` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/yfinance/curentPrice/AAPL
```

## API Endpoints for Reading Firestore Data

### 1. Get User Information [`DEPRECATED`]

This function is no longer supported as Users database is obsolete.

- Endpoint: `/read/userInfo/:userEmail`
- Method: `GET`
- URL Params: `userEmail` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/read/userInfo/john.doe@example.com
```

### 2. Get Portfolio Information

- Endpoint: `/read/portfolioInfo/:userEmail`
- Method: `GET`
- URL Params: `userEmail`(**required**)

#### Usage:

```
curl http://<your-server-url>/api/read/portfolioInfo/john.doe@example.com
```

### 3. Get All Trades for a User

- Endpoint: `/read/allTrades/:userEmail`
- Method: `GET`
- URL Params: `userEmail`(**required**)

#### Usage:

```
curl http://<your-server-url>/api/read/allTrades/john.doe@example.com
```

### 4. Get Specific Trade Details

- Endpoint: `/read/trade/:userEmail/:ticker`
- Method: `GET`
- URL Params:
  - `userEmail` (**required**)
  - `ticker` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/read/trade/john.doe@example.com/AAPL
```

## API Endpoints for Create and Update Portfolio/Trades data

### 1. Create a portfolio on user creation

- Endpoint: `/post/createPortfolio/:userEmail`
- Method: `POST`
- URL Params: `userEmail` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/post/createPortfolio/john.doe@example.com
```

### 2. Create a Trade or Update a trade

This method uses both post and put because I am lazy. Live with it

- Endpoint: `/post/updateTrade/:userEmail/:ticker/:buyQty/:buyPrice`
- Method: `POST`
- URL Params:
  - `userEmail` (**required**)
  - `ticker` (**required**)
  - `buyQty` (**required**)
  - `buyPrice` (**required**)

### 3. Get ALL Portfolio Data

- Endpoint: `/get/getPortfolioData/:userEmail`
- Method: `GET`
- URL Params: `userEmail` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/get/getPortfolioData/john.doe@example.com
```

## API Endpoints for Deleting a trade from the portfolio

### 1. Delete Trade

- Endpoint: `/delete/trade/:userEmail/:ticker`
- Method: `DELETE`
- URL Params:
  - `userEmail` (**required**)
  - `ticker` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/delete/trade/john.doe@example.com/AAPL
```
