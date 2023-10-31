const express = require("express");
const router = express.Router();

const {
  addTradeToWatchlist,
  readWatchlist,
  // Add more exported functions if needed
} = require("../../controllers/watchlistDataController");

// Route to add a stock to the watchlist
router.post("/add/:userEmail/:ticker", async (req, res) => {
  try {
    const { userEmail, ticker } = req.params;

    await addTradeToWatchlist(userEmail, ticker);
    res.status(200).send("Watchlist updated or created!");
  } catch (error) {
    console.error("Error adding trade to watchlist:", error);
    res.status(500).send("Internal Server Error");
  }
});

// Route to read stocks from the watchlist
router.get("/read/:userEmail", async (req, res) => {
  try {
    const userEmail = req.params.userEmail;
    if (!userEmail) {
      return res.status(400).send("User email is required.");
    }
    const stocks = await readWatchlist(userEmail);
    res.status(200).json(stocks);
  } catch (error) {
    console.error("Error reading watchlist:", error);
    res.status(500).send("Internal Server Error");
  }
});

module.exports = router;
