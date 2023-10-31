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

// Function to create or update user information
async function updateUserInfo(userEmail, userData) {
  console.log("This function is deprecated.");
  const userRef = doc(db, "users", userEmail);
  await setDoc(userRef, userData);
  console.log("User data updated or created!");
}

// Function to create portfolio information in firestore

async function createPortfolio(userEmail) {
  const portfolioId = `${userEmail}_portfolio`;
  const portfolioRef = doc(db, "portfolios", portfolioId);

  // Generate an empty portfolio data object
  const portfolioData = {
    alpha: 0,
    beta: 0,
    marketReturn: 0,
    portfolioReturn: 0,
    portfolioValue: 0,
    rfRate: 0,
    sharpeRatio: 0,
    stdDev: 0,
    trades: `/trades/${userEmail}_trades`,
    userId: userEmail,
    variance: 0,
  };

  await setDoc(portfolioRef, portfolioData);
  console.log("Portfolio data updated or created!");

  // Create a document in the 'trades' collection
  const tradesId = `${userEmail}_trades`;
  const tradesRef = doc(db, "trades", tradesId);
  await setDoc(tradesRef, {}); // or add whatever initial data you want for this doc
  console.log("Trades data updated or created!");
}

// Function to create or update trades, and then update the portfolio when trades are set
async function updateTrade(userEmail, ticker, buyQty, buyPrice) {
  const tradesId = `${userEmail}_trades`;
  const tradeId = `${userEmail}_${ticker}`;
  const tradeRef = doc(db, "trades", tradesId, "trades", tradeId);
  let existingTradeData = await readSpecificTrade(userEmail, ticker);
  let updatedBuyQty = buyQty;
  let updatedBuyPrice = buyPrice;

  if (existingTradeData) {
    // Calculate the new buyQty and buyPrice if the trade already exists
    let oldTotal = existingTradeData.buyPrice * existingTradeData.buyQty;
    let newTotal = buyPrice * buyQty;

    updatedBuyQty = existingTradeData.buyQty + buyQty;
    updatedBuyPrice = (oldTotal + newTotal) / updatedBuyQty;

    if (updatedBuyQty < 0) {
      throw new Error("User selling more than what they own");
    }
  }

  // Construct the trade data
  const tradeDataJS = {
    tradeKey: tradeId,
    ticker: ticker,
    name: "", // This will be populated by the Python function
    buyPrice: updatedBuyPrice,
    buyQty: updatedBuyQty,
    beta: 0, // This will be populated by the Python function
  };

  // Convert the JS trade data to a Python Trade class instance and get the result back as a JS object
  const tradeData = convertTradeData(tradeDataJS);
  const newTrade = {
    ticker: tradeData.ticker,
    name: tradeData.name,
    buyPrice: tradeData.buyPrice,
    buyQty: tradeData.buyQty,
    beta: tradeData.beta,
  };

  // Add/Update the returned trade data in Firestore
  await setDoc(tradeRef, newTrade);
  console.log("Trade data updated or created!");
}

async function updatePortfolio(userEmail) {
  // Get the new Trades Data
  const allTradesData = await readAllTrades(userEmail);
  // Get the old Portfolio data
  const oldPortfolioData = await readPortfolioInfo(userEmail);

  // Update the portfolio data by giving old data and the updated trades data
  const updatedFields = await updatePortfolioData(
    oldPortfolioData,
    allTradesData,
    "update"
  );

  const portfolioData = {
    alpha: updatedFields.alpha,
    beta: updatedFields.beta,
    marketReturn: updatedFields.marketReturn,
    portfolioReturn: updatedFields.portfolioReturn,
    portfolioValue: updatedFields.portfolioValue,
    rfRate: updatedFields.rfRate,
    sharpeRatio: updatedFields.sharpeRatio,
    stdDev: updatedFields.stddev,
    trades: `/trades/${userEmail}_trades`,
    userId: userEmail,
    variance: updatedFields.variance,
  };
  const portfolioId = `${userEmail}_portfolio`;
  const portfolioRef = doc(db, "portfolios", portfolioId);
  await setDoc(portfolioRef, portfolioData); //  overwrite the document
}

module.exports = {
  updateUserInfo,
  createPortfolio,
  updateTrade,
  updatePortfolio,
};
