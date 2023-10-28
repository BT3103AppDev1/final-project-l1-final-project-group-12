// Manual tests for yfinance Routes. Test are not complete

const request = require("supertest");
const app = require("../api/routes/yfinanceRoutes.js"); // import your Express app

describe("YFinance Routes", () => {
  it("should get current price for a ticker", async () => {
    const response = await request(app).get("/curentPrice/AAPL");
    expect(response.statusCode).toBe(200);
    // Additional checks based on the expected response can be added
  });

  it("should get historical data for a ticker", async () => {
    const response = await request(app).get(
      "/historicalData/AAPL?period=1Y&interval=1d"
    );
    expect(response.statusCode).toBe(200);
    // Additional checks based on the expected response can be added
  });

  it("should get options data for a ticker", async () => {
    const response = await request(app).get("/optionsData/AAPL");
    expect(response.statusCode).toBe(200);
    // Additional checks based on the expected response can be added
  });
});
