const express = require("express");
const router = express.Router();
const {
  deleteSpecificTrade,
} = require("../../controllers/deleteDataController");

// Route to delete a specific trade based on user's email and ticker
router.delete(
  "/trade/:userEmail/:ticker/:objectiveOfDelete",
  async (req, res) => {
    try {
      const { userEmail, ticker, objectiveOfDelete } = req.params;

      await deleteSpecificTrade(userEmail, ticker, objectiveOfDelete);

      res.status(200).json({
        success: true,
        message: "Trade deleted successfully!",
      });
    } catch (error) {
      res.status(400).json({
        success: false,
        message: error.message,
      });
    }
  }
);

module.exports = router;
