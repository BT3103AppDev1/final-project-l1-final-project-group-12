const express = require("express");
const app = express();

// Import the routes
const yfinanceRoutes = require("./routes/yfinanceRoutes");
const readDataRoutes = require("./routes/readDataRoutes");

// Use the routes with a prefix (if you desire)
app.use("/api/yfinance", yfinanceRoutes);
app.use("/api/read", readDataRoutes);

//... Your other server configurations ...

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
