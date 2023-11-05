const express = require("express");
const cors = require("cors");
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(
  cors({
    origin: "*",
  })
);
// Import the routes
const yfinanceRoutes = require("./routes/yfinanceRoutes");
const readDataRoutes = require("./routes/readDataRoutes");
const updateDataRoutes = require("./routes/updateDataRoutes");
const deleteDataRoutes = require("./routes/deleteDataRoutes");
const optimiseDataRoutes = require("./routes/optimiseDataRoutes");
//const watchlistDataRoutes = require("./routes/watchlistDataRoutes");

// Use the routes with a prefix (if you desire)

app.use("/api/yfinance", yfinanceRoutes);
app.use("/api/read", readDataRoutes);
app.use("/api/update", updateDataRoutes);
app.use("/api/delete", deleteDataRoutes);
app.use("/api/optimise", optimiseDataRoutes);
//app.use("/api/watch", watchlistDataRoutes);

//... Your other server configurations ...

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
