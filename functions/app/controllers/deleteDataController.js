const firebaseApp = require("../firebase");

const { getFirestore, doc, deleteDoc } = require("@firebase/firestore");
const db = getFirestore(firebaseApp);
const { readSpecificTrade } = require("./readDataController");

async function deleteSpecificTrade(userEmail, ticker, objectiveOfDelete = "") {
  let tradesId = `${userEmail}_trades`;
  if (objectiveOfDelete == "alpha") {
    tradesId = `${userEmail}_trades_alpha`;
  } else if (objectiveOfDelete == "beta") {
    tradesId = `${userEmail}_trades_beta`;
  } else if (objectiveOfDelete == "balance") {
    tradesId = `${userEmail}_trades_balance`;
  }

  // Each trade in the trades collection
  const tradeId = `${userEmail}_${ticker}`;

  // Read the trade first to check its existence
  const existingTrade = await readSpecificTrade(
    userEmail,
    ticker,
    objectiveOfDelete
  );
  if (!existingTrade) {
    throw new Error("No such trade found!");
  }

  // Delete the trade from Firestore
  const tradeRef = doc(db, "trades", tradesId, "trades", tradeId);
  await deleteDoc(tradeRef);
  console.log("Trade deleted successfully!");
}

module.exports = {
  deleteSpecificTrade,
};
