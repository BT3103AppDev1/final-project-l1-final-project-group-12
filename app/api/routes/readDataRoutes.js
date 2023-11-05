// app\api\routes\readDataRoutes.js

const express = require("express");
const router = express.Router();

const {
  readUserInfo,
  readPortfolioInfo,
  readAllTrades,
  readSpecificTrade,
} = require("../../controllers/readDataController");

// Endpoint to read user information
router.get("/userInfo/:userEmail", async (req, res) => {
  try {
    const data = await readUserInfo(req.params.userEmail);
    if (data) {
      res.json(data);
    } else {
      res.status(404).send("User not found");
    }
  } catch (error) {
    console.error(error.stack);
    res.status(500).send("Server error");
  }
});

// Endpoint to read portfolio information
router.get("/portfolioInfo/:userEmail/:objectiveOfRead", async (req, res) => {
  try {
    const data = await readPortfolioInfo(
      req.params.userEmail,
      req.params.objectiveOfRead
    );
    if (data) {
      res.json(data);
    } else {
      res.status(404).send("Portfolio not found");
    }
  } catch (error) {
    res.status(500).send("Server error");
  }
});

// Endpoint to read all trades of a user
router.get("/allTrades/:userEmail", async (req, res) => {
  try {
    const data = await readAllTrades(req.params.userEmail);
    if (data) {
      res.json(data);
    } else {
      res.status(404).send("Trades not found");
    }
  } catch (error) {
    res.status(500).send("Server error");
  }
});

// Endpoint to read a specific trade's details
router.get("/trade/:userEmail/:ticker", async (req, res) => {
  try {
    const data = await readSpecificTrade(
      req.params.userEmail,
      req.params.ticker
    );
    if (data) {
      res.json(data);
    } else {
      res.status(404).send("Trade not found");
    }
  } catch (error) {
    res.status(500).send("Server error");
  }
});

module.exports = router;
