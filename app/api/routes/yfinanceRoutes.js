const express = require("express");
const router = express.Router();

// Import the functions from your controller
const {
  getCurrentPrice,
  getStockStatistics,
  getHistoricalData,
  getOptionsData,
  getTopGainersData,
  getTopLosersData
} = require("../../controllers/yfinanceController");

// Route to get stock statistics
router.get("/curentPrice/:ticker", getCurrentPrice);

// Route to get stock statistics
router.get("/stockStatistics/:ticker", getStockStatistics);

// Route to get historical data
router.get("/historicalData/:ticker", getHistoricalData);

// Route to get options data
router.get("/optionsData/:ticker", getOptionsData);

//Route to get top gainers data 
router.get("/topGainersData", getTopGainersData)

//Route to get top losers data 
router.get("/topLosersData", getTopLosersData)

module.exports = router;
