const express = require("express");
const { spawn } = require("child_process");
const router = express.Router();

// Helper function to execute Python script and get output
const executePythonScript = (scriptPath, args) => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python", [scriptPath, ...args]);
    let dataString = "";
    pythonProcess.stdout.on("data", (data) => {
      dataString += data.toString();
    });
    pythonProcess.stderr.on("data", (data) => {
      reject(data.toString());
    });
    pythonProcess.on("close", (code) => {
      resolve(dataString);
    });
  });
};

// Route to get stock statistics
router.get("/stock-statistics/:ticker", async (req, res) => {
  const { ticker } = req.params;
  try {
    const output = await executePythonScript("../scripts/yfinance.py", [
      "get_stock_statistics",
      ticker,
    ]);
    res.json(JSON.parse(output));
  } catch (error) {
    res.status(500).send(error);
  }
});

// Route to get historical data
router.get("/historical-data/:ticker", async (req, res) => {
  const { ticker } = req.params;
  const { period, interval } = req.query;
  try {
    const output = await executePythonScript("../scripts/yfinance.py", [
      "get_historical_data",
      ticker,
      period,
      interval,
    ]);
    res.json(JSON.parse(output));
  } catch (error) {
    res.status(500).send(error);
  }
});

// Route to get options data
router.get("/options-data/:ticker", async (req, res) => {
  const { ticker } = req.params;
  try {
    const output = await executePythonScript("../scripts/yfinance.py", [
      "get_options_data",
      ticker,
    ]);
    res.json(JSON.parse(output));
  } catch (error) {
    res.status(500).send(error);
  }
});

module.exports = router;
