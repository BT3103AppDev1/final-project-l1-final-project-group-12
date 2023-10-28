const firebaseApp = require("../firebase");
const { getFirestore, doc, setDoc } = require("firebase/firestore");
const { convertTradeData } = require("./changeStructureController"); // Import the function to convert JS object to Python Trade class
const { readSpecificTrade } = require("./readDataController");

const db = getFirestore(firebaseApp);

// Function to create or update user information
async function updateUserInfo(userEmail, userData) {
  console.log("This function is deprecated.");
  const userRef = doc(db, "users", userEmail);
  await setDoc(userRef, userData);
  console.log("User data updated or created!");
}

// Function to create portfolio information

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
}

// Function to create or update trades
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

  // Add/Update the returned trade data in Firestore
  await setDoc(tradeRef, tradeData);
  console.log("Trade data updated or created!");
}

module.exports = { updateTrade };

module.exports = {
  updateUserInfo,
  createPortfolio,
  updateTrade,
};
