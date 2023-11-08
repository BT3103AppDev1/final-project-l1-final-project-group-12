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

### 5. Get Top 5 Gainers 

- Endpoint: `/topGainersData`
- Method: `GET`
- URL Params: `NONE`

#### Usage:

```
curl http://<your-server-url>/api/yfinance/topGainersData
```

### 6. Get Top 5 Losers 

- Endpoint: `/topLosersData`
- Method: `GET`
- URL Params: `NONE`

#### Usage:

```
curl http://<your-server-url>/api/yfinance/topLosersData
```

### 7. Get Market Cap for Stock 

- Endpoint: `/marketCapData/:ticker`
- Method: `GET`
- URL Params: `NONE`

#### Usage:

```
curl http://<your-server-url>/api/yfinance/marketCapData/AAPL
```

### 8. Get Average Volume for Stock 

- Endpoint: `/averageVolumeData/:ticker`
- Method: `GET`
- URL Params: `NONE`

#### Usage:

```
curl http://<your-server-url>/api/yfinance/averageVolumeData/AAPL
```

### 9. Get Percentage Change for Stock 

- Endpoint: `/percentageChange/:ticker`
- Method: `GET`
- URL Params: `NONE`

#### Usage:

```
curl http://<your-server-url>/api/yfinance/percentageChange/AAPL
```

### 10. Get ticker based on stock name 

- Endpoint: `/ticker/:stockName`
- Method: `GET`
- URL Params: `NONE`

#### Usage:

```
curl http://<your-server-url>/api/yfinance/ticker/Apple
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

- Endpoint: `/read/portfolioInfo/:userEmail/:objectiveOfRead`
- Method: `GET`
- URL Params:
  - `userEmail`(**required**)
  - `objectiveOfRead` (**required**)
    - standard (`returns the portfolio the user made`)
    - alpha (`returns the portfolio that maximises alpha`)
    - beta (`returns the portfolio that minimises beta`)
    - balance (`returns the portfolio that maximises Sharpe Ratio`)

#### Usage:

```
curl http://<your-server-url>/api/read/portfolioInfo/john.doe@example.com/standard
```

### 3. Get All Trades for a User

- Endpoint: `/read/allTrades/:userEmail/:objectiveOfRead`
- Method: `GET`
- URL Params:
  - `userEmail`(**required**)
  - `objectiveOfRead` (**required**)
    - standard (`returns the portfolio the user made`)
    - alpha (`returns the portfolio that maximises alpha`)
    - beta (`returns the portfolio that minimises beta`)
    - balance (`returns the portfolio that maximises Sharpe Ratio`)

#### Usage:

```
curl http://<your-server-url>/api/read/allTrades/john.doe@example.com
```

### 4. Get Specific Trade Details

- Endpoint: `/read/trade/:userEmail/:ticker/:objectiveOfRead`
- Method: `GET`
- URL Params:
  - `userEmail` (**required**)
  - `ticker` (**required**)
  - `objectiveOfRead` (**required**)
    - standard (`returns the portfolio the user made`)
    - alpha (`returns the portfolio that maximises alpha`)
    - beta (`returns the portfolio that minimises beta`)
    - balance (`returns the portfolio that maximises Sharpe Ratio`)

#### Usage:

```
curl http://<your-server-url>/api/read/trade/john.doe@example.com/AAPL
```

## API Endpoints for Create and Update Portfolio/Trades data

### 1. Create a portfolio on user creation

- Endpoint: `/update/createPortfolio/:userEmail`
- Method: `POST`
- URL Params: `userEmail` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/post/createPortfolio/john.doe@example.com
```

### 2. Create a Trade or Update a trade

This method uses both post and put because I am lazy. Live with it

- Endpoint: `/update/updateTrade/:userEmail`
- Method: `POST` and `Put`
- URL Params:
  - `userEmail` (**required**)
- Response Body Params:
  - `ticker` (**required**)
  - `buyQty` (**required**)
  - `buyPrice` (**required**)

**Error responses**:
| Code | Status | Client Side Action |
| ---- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 500 | Error | Throw an error to ask user check their stock ticker and form values |

---

#### Usage:

```
curl http://<your-server-url>/api/update/updateTrade/john.doe@example.com
```

### 3. Update all Portfolio Data

This function is used to update the portfolio data to its latest metrics.
Ideally, it should be used after setting a trade or updating a trade

- Endpoint: `/update/updatePortfolio/:userEmail`
- Method: `GET`
- URL Params: `userEmail` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/update/updatePortfolio/john.doe@example.com
```

## API Endpoints for Deleting a trade from the portfolio

### 1. Delete Trade

- Endpoint: `/delete/trade/:userEmail/:ticker/:objectiveOfDelete`
- Method: `DELETE`
- URL Params:
  - `userEmail` (**required**)
  - `ticker` (**required**)
  - `objectiveOfRead` (**required**)
    - standard (`returns the portfolio the user made`)
    - alpha (`returns the portfolio that maximises alpha`)
    - beta (`returns the portfolio that minimises beta`)
    - balance (`returns the portfolio that maximises Sharpe Ratio`)

#### Usage:

```
curl http://<your-server-url>/api/delete/trade/john.doe@example.com/AAPL/standard
curl http://<your-server-url>/api/delete/trade/john.doe@example.com/AAPL/alpha
curl http://<your-server-url>/api/delete/trade/john.doe@example.com/AAPL/beta
curl http://<your-server-url>/api/delete/trade/john.doe@example.com/AAPL/balance
```

## API Endpoints for optimising the portfolio

### 1. Optimise Trade

- Endpoint: `/optimise/:userEmail/:objectiveForUpdate`
- Method: `POST`
- URL Params:
  - `userEmail` (**required**)
  - `objectiveForUpdate` (**required**)
    - alpha
    - beta
    - balance

#### Usage:

```
curl http://<your-server-url>/api/optimise/john.doe@example.com/alpha
curl http://<your-server-url>/api/optimise/john.doe@example.com/beta
curl http://<your-server-url>/api/optimise/john.doe@example.com/balance
```

## API Endpoints for Watchlist

### 1. Read the watchlist

- Endpoint: `/watch/read/:userEmail`
- Method: `GET`
- URL Params:
  - `userEmail` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/watch/read/john.doe@example.com
```

### 2. Add a stock to the watchlist

- Endpoint: `/watch/add/:userEmail/:ticker`
- Method: `POST`
- URL Params:
  - `userEmail` (**required**)
  - `ticker` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/watch/add/john.doe@example.com/AAPL
```

### 3. Delete a stock from the watchlist

- Endpoint: `/watch/delete/:userEmail/:ticker`
- Method: `DELETE`
- URL Params:
  - `userEmail` (**required**)
  - `ticker` (**required**)

#### Usage:

```
curl http://<your-server-url>/api/watch/delete/john.doe@example.com/AAPL
```
