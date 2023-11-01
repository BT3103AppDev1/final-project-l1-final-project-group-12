const express = require("express");
const router = express.Router();
const {
  updateUserInfo,
  createPortfolio,
  updateTrade,
  updatePortfolio,
} = require("../../controllers/createDataController");

// Route to update user information
router.post("/user/:userEmail", async (req, res) => {
  try {
    const { userEmail } = req.params;
    const userData = req.body; // assuming the user data will be sent in the request body

    await updateUserInfo(userEmail, userData);

    res.status(200).json({
      success: true,
      message: "User data updated successfully!",
    });
  } catch (error) {
    res.status(400).json({
      success: false,
      message: error.message,
    });
  }
});

// Route to create a new portfolio for the user
router.post("/createPortfolio/:userEmail", async (req, res) => {
  try {
    const { userEmail } = req.params;

    await createPortfolio(userEmail);

    res.status(200).json({
      success: true,
      message: "Portfolio created successfully!",
    });
  } catch (error) {
    res.status(400).json({
      success: false,
      message: error.message,
    });
  }
});

// Route to update or add a new trade
router.put("/updateTrade/:userEmail", async (req, res) => {
  try {
    const { userEmail } = req.params;
    const { ticker, buyQty, buyPrice } = req.body; // assuming these details will be sent in the request body

    await updateTrade(userEmail, ticker, buyQty, buyPrice);

    res.status(200).json({
      success: true,
      message: "Trade updated successfully!",
    });
  } catch (error) {
    res.status(400).json({
      success: false,
      message: error.message,
    });
  }
});

// Route to update the portfolio after setting trades
router.put("/updatePortfolio/:userEmail", async (req, res) => {
  try {
    const { userEmail } = req.params;

    await updatePortfolio(userEmail);

    res.status(200).json({
      success: true,
      message: "Portfolio updated successfully!",
    });
  } catch (error) {
    res.status(400).json({
      success: false,
      message: error.message,
    });
  }
});

module.exports = router;
