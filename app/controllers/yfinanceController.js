const { spawn } = require("child_process");

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

// Connector method to get stock statistics
const getCurrentPrice = async (req, res) => {
  console.log("Controller connected");
  const { ticker } = req.params;
  try {
    const output = await executePythonScript("../services/stockData.py", [
      "get_current_price",
      ticker,
    ]);
    res.json(JSON.parse(output));
  } catch (error) {
    res.status(500).send(error);
  }
};
// Connector method to get stock statistics
const getStockStatistics = async (req, res) => {
  console.log("Controller connected");
  const { ticker } = req.params;
  try {
    const output = await executePythonScript("../services/stockData.py", [
      "get_stock_statistics",
      ticker,
    ]);
    res.json(JSON.parse(output));
  } catch (error) {
    res.status(500).send(error);
  }
};
// Connector method to get historical data
const getHistoricalData = async (req, res) => {
  const { ticker } = req.params;
  const { period, interval } = req.query;
  try {
    const output = await executePythonScript("../services/stockData.py", [
      "get_historical_data",
      ticker,
      period,
      interval,
    ]);
    res.json(JSON.parse(output));
  } catch (error) {
    res.status(500).send(error);
  }
};

// Connector method to get options data
const getOptionsData = async (req, res) => {
  const { ticker } = req.params;
  try {
    const output = await executePythonScript("../services/stockData.py", [
      "get_options_data",
      ticker,
    ]);
    res.json(JSON.parse(output));
  } catch (error) {
    res.status(500).send(error);
  }
};

module.exports = {
  getCurrentPrice,
  getStockStatistics,
  getHistoricalData,
  getOptionsData,
};
