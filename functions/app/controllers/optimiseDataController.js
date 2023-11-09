const firebaseApp = require("../firebase");
const { getFirestore, doc, setDoc } = require("firebase/firestore");
const { convertTradeData } = require("./changeTradeStructureController"); // Import the function to convert JS object to Python Trade class
const {
  readSpecificTrade,
  readAllTrades,
  readPortfolioInfo,
} = require("./readDataController");
const { updatePortfolioData } = require("./changePortfolioStructureController");

const db = getFirestore(firebaseApp);

// Helper to create or update trades, and then update the portfolio when trades are set
async function helperUpdateTrade(
  userEmail,
  ticker,
  name,
  buyQty,
  buyPrice,
  beta,
  objectiveOfUpdate
) {
  const tradesId = `${userEmail}_trades_${objectiveOfUpdate}`;
  const tradeId = `${userEmail}_${ticker}`;
  const tradeRef = doc(db, "trades", tradesId, "trades", tradeId);
  // Construct the trade data
  const newTrade = {
    tradeKey: tradeId,
    ticker: ticker,
    name: name,
    buyPrice: buyPrice,
    buyQty: buyQty,
    beta: beta,
  };

  // Add/Update the returned trade data in Firestore
  await setDoc(tradeRef, newTrade);
}

async function optimisePortfolio(userEmail, objectiveOfUpdate) {
  // Get the Trades Data
  const allTradesData = await readAllTrades(userEmail);
  // Get the old Portfolio data
  const oldPortfolioData = await readPortfolioInfo(userEmail);

  // Update the portfolio data by giving old data and the updated trades data
  const updatedFields = await updatePortfolioData(
    oldPortfolioData,
    allTradesData,
    objectiveOfUpdate
  );

  //Updates all the trades for the objective
  updatedTradesData = updatedFields.trades;
  for (let trade of updatedTradesData) {
    await helperUpdateTrade(
      userEmail,
      trade.ticker,
      trade.name,
      trade.buyQty,
      trade.buyPrice,
      trade.beta,
      objectiveOfUpdate
    );
  }
  const portfolioData = {
    alpha: updatedFields.alpha,
    beta: updatedFields.beta,
    marketReturn: updatedFields.marketReturn,
    portfolioReturn: updatedFields.portfolioReturn,
    portfolioValue: updatedFields.portfolioValue,
    rfRate: updatedFields.rfRate,
    sharpeRatio: updatedFields.sharpeRatio,
    stdDev: updatedFields.stddev,
    trades: `/trades/${userEmail}_trades_${objectiveOfUpdate}`,
    userId: userEmail,
    variance: updatedFields.variance,
  };

  const portfolioId = `${userEmail}_portfolio_${objectiveOfUpdate}`;
  const portfolioRef = doc(db, "portfolios", portfolioId);
  await setDoc(portfolioRef, portfolioData); //  overwrite the document
}
module.exports = {
  optimisePortfolio,
};
