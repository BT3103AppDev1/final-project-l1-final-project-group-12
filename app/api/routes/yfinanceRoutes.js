const express = require("express");
const router = express.Router();

// Import the functions from your controller
const {
  getCurrentPrice,
  getStockStatistics,
  getHistoricalData,
  getOptionsData,
} = require("../../controllers/yfinanceController");

// Route to get stock statistics
router.get("/curentPrice/:ticker", getCurrentPrice);

// Route to get stock statistics
router.get("/stockStatistics/:ticker", getStockStatistics);

// Route to get historical data
router.get("/historicalData/:ticker", getHistoricalData);

// Route to get options data
router.get("/optionsData/:ticker", getOptionsData);

module.exports = router;
