const { execSync } = require("child_process");
const path = require("path");

function updatePortfolioData(oldPortfolioData, allTradesData) {
  const data = {
    ...oldPortfolioData,
    allTradesData: allTradesData,
  };

  const dataString = JSON.stringify(data);

  // Path to the Portfolio.py file
  const pythonScriptPath = path.join(__dirname, "..", "models", "Portfolio.py");

  // Command to run the Python script with the user email data
  const command = `python ${pythonScriptPath} "${dataString}"`;

  // Execute the Python script and get the output
  const output = execSync(command).toString();

  // Parse the output JSON string to a JavaScript object and return
  return JSON.parse(output);
}

module.exports = { updatePortfolioData };
