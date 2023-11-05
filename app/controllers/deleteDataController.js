const firebaseApp = require("../firebase");

const { getFirestore, doc, deleteDoc } = require("@firebase/firestore");
const db = getFirestore(firebaseApp);
const { readSpecificTrade } = require("./readDataController");

async function deleteSpecificTrade(userEmail, ticker) {
  const tradesId = `${userEmail}_trades`;
  const tradeId = `${userEmail}_${ticker}`;

  // Read the trade first to check its existence
  const existingTrade = await readSpecificTrade(userEmail, ticker);
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
