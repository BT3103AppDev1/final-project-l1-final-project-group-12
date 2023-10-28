const firebase = require("../firebase");

async function readUserInfo(userEmail) {
  const userRef = firebase.firestore().collection("users").doc(userEmail);
  const userDoc = await userRef.get();
  if (!userDoc.exists) {
    console.log("No such user found!");
    return;
  }
  return userDoc.data();
}

async function readPortfolioInfo(userEmail) {
  const portfolioId = `${userEmail}_portfolio`;
  const portfolioRef = firebase
    .firestore()
    .collection("portfolios")
    .doc(portfolioId);
  const portfolioDoc = await portfolioRef.get();
  if (!portfolioDoc.exists) {
    console.log("No such portfolio found!");
    return;
  }
  return portfolioDoc.data();
}

async function readAllTrades(userEmail) {
  const tradesId = `${userEmail}_trades`;
  const tradesRef = firebase
    .firestore()
    .collection("trades")
    .doc(tradesId)
    .collection("trades");
  const tradesSnapshot = await tradesRef.get();
  const trades = [];
  tradesSnapshot.forEach((trade) => {
    trades.push({ id: trade.id, ...trade.data() });
  });
  return trades;
}

async function readSpecificTrade(userEmail, userId, ticker) {
  const tradesId = `${userEmail}_trades`;
  const tradeId = `${userId}_${ticker}`;
  const tradeRef = firebase
    .firestore()
    .collection("trades")
    .doc(tradesId)
    .collection("trades")
    .doc(tradeId);
  const tradeDoc = await tradeRef.get();
  if (!tradeDoc.exists) {
    console.log("No such trade found!");
    return;
  }
  return tradeDoc.data();
}

module.exports = {
  readUserInfo,
  readPortfolioInfo,
  readAllTrades,
  readSpecificTrade,
};
