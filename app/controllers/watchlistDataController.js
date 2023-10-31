const firebaseApp = require("../firebase");
const {
  getFirestore,
  doc,
  setDoc,
  query,
  collection,
  getDocs,
} = require("firebase/firestore");
const { convertTradeData } = require("./changeTradeStructureController"); // Import the function to convert JS object to Python Trade class

const db = getFirestore(firebaseApp);

// Function to create or update trades, and then update the portfolio when trades are set
async function addTradeToWatchlist(userEmail, ticker) {
  const watchlistId = `${userEmail}_watchlist`;
  const watchedStock = `${userEmail}_${ticker}`;
  const watchlistRef = doc(
    db,
    "watchlist",
    watchlistId,
    "watchedStocks",
    watchedStock
  );

  // Construct the trade data
  const watchListDataJS = {
    tradeKey: watchlistId,
    ticker: ticker,
    name: "",
    buyPrice: 0,
    buyQty: 0,
    beta: 0,
  };

  // Convert the JS trade data to a Python Trade class instance and get the result back as a JS object
  const watchListData = convertTradeData(watchListDataJS);
  const newWatchlistData = {
    ticker: watchListData.ticker,
    name: watchListData.name,
    buyPrice: watchListData.buyPrice,
    buyQty: watchListData.buyQty,
    beta: watchListData.beta,
  };

  // Add/Update the returned trade data in Firestore
  await setDoc(watchlistRef, newWatchlistData);
  console.log("Watchlist updated or created!");
}

async function readWatchlist(userEmail) {
  const watchlistId = `${userEmail}_watchlist`;
  const watchlistQuery = query(
    collection(db, "watchlist", watchlistId, "watchedStocks")
  );
  const watchlistSnapshot = await getDocs(watchlistQuery);
  const stocks = [];
  watchlistSnapshot.forEach((stock) => {
    stocks.push({ id: stock.id, ...stock.data() });
  });
  return stocks;
}

module.exports = {
  readWatchlist,
  addTradeToWatchlist,
};
