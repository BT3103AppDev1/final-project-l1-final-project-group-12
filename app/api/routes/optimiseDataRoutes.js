const express = require("express");
const router = express.Router();

const {
  optimisePortfolio,
  // Add more exported functions if needed
} = require("../../controllers/optimiseDataController");

// Route to optimise a user's portfolio
router.post("/:userEmail/:objectiveOfUpdate", async (req, res) => {
  try {
    const { userEmail, objectiveOfUpdate } = req.params;
    await optimisePortfolio(userEmail, objectiveOfUpdate);
    res.status(200).json({ message: "Portfolio optimised successfully!" });
  } catch (error) {
    res
      .status(500)
      .json({ message: "Failed to optimise portfolio", error: error.message });
  }
});

module.exports = router;
