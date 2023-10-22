const express = require("express");
const router = express.Router();

// Import the functions from your controller
const {
  getStockStatistics,
  getHistoricalData,
  getOptionsData,
} = require("../../controllers/yfinanceController");

// Route to get stock statistics
router.get("/stock-statistics/:ticker", getStockStatistics);

// Route to get historical data
router.get("/historical-data/:ticker", getHistoricalData);

// Route to get options data
router.get("/options-data/:ticker", getOptionsData);

module.exports = router;
