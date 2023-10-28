const firebaseApp = require("../firebase");
const {
  getFirestore,
  collection,
  doc,
  getDoc,
  query,
  where,
  getDocs,
} = require("firebase/firestore");

const db = getFirestore(firebaseApp);

async function readUserInfo(userEmail) {
  const userRef = doc(db, "users", userEmail);
  const userDoc = await getDoc(userRef);
  if (!userDoc.exists()) {
    console.log("No such user found!");
    return;
  }
  return userDoc.data();
}

async function readPortfolioInfo(userEmail) {
  const portfolioId = `${userEmail}_portfolio`;
  const portfolioRef = doc(db, "portfolios", portfolioId);
  const portfolioDoc = await getDoc(portfolioRef);
  if (!portfolioDoc.exists()) {
    console.log("No such portfolio found!");
    return;
  }
  return portfolioDoc.data();
}

async function readAllTrades(userEmail) {
  const tradesId = `${userEmail}_trades`;
  const tradesQuery = query(collection(db, "trades", tradesId, "trades"));
  const tradesSnapshot = await getDocs(tradesQuery);
  const trades = [];
  tradesSnapshot.forEach((trade) => {
    trades.push({ id: trade.id, ...trade.data() });
  });
  return trades;
}

async function readSpecificTrade(userEmail, userId, ticker) {
  const tradesId = `${userEmail}_trades`;
  const tradeId = `${userId}_${ticker}`;
  const tradeRef = doc(db, "trades", tradesId, "trades", tradeId);
  const tradeDoc = await getDoc(tradeRef);
  if (!tradeDoc.exists()) {
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
