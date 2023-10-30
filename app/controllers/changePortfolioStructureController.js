const { execSync } = require("child_process");
const path = require("path");

function convertTradeData(tradeData) {
  // Convert the JavaScript object to a JSON string
  const tradeDataString = JSON.stringify(tradeData);

  // Path to the Trade.py file
  const pythonScriptPath = path.join(__dirname, "..", "models", "Trade.py");

  // Command to run the Python script with the trade data
  const command = `python ${pythonScriptPath} "${tradeDataString}"`;

  // Execute the Python script and get the output
  const output = execSync(command).toString();

  // Parse the output JSON string to a JavaScript object and return
  return JSON.parse(output);
}

module.exports = { convertTradeData };
