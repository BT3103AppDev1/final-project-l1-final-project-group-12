const { execSync } = require("child_process");
const path = require("path");

async function updatePortfolioData(
  oldPortfolioData,
  allTradesData,
  objectiveOfUpdate
) {
  const data = {
    alpha: oldPortfolioData.alpha,
    beta: oldPortfolioData.beta,
    marketReturn: oldPortfolioData.marketReturn,
    portfolioReturn: oldPortfolioData.portfolioReturn,
    portfolioValue: oldPortfolioData.portfolioValue,
    rfRate: oldPortfolioData.rfRate,
    sharpeRatio: oldPortfolioData.sharpeRatio,
    stdDev: oldPortfolioData.stdDev,
    userId: oldPortfolioData.userId,
    variance: oldPortfolioData.variance,
    allTradesData: allTradesData,
  };

  const dataString = JSON.stringify(data);
  const escapeDataString = JSON.stringify(dataString);

  // Path to the Portfolio.py file
  const pythonScriptPath = path.join(__dirname, "..", "models", "Portfolio.py");

  // Command to run the Python script with the user email data
  const command = `python ${pythonScriptPath} ${escapeDataString} ${objectiveOfUpdate}`;

  // Execute the Python script and get the output
  const output = execSync(command).toString();

  return JSON.parse(output);
}

module.exports = { updatePortfolioData };
