<template>
  <div class="body">
    <div class="header">
      <div class="header-left">
        <button class="back-button" @click="goBack()">
          <img src="@/assets/backIcon.png" alt="" class="back-icon" />
        </button>
        <h1>{{ searchTerm }}</h1>
      </div>
      <div class="stacked-buttons">
        <button class="add-button" @click="confirmAndAdd">
          <img src="@/assets/starIcon.png" alt="" class="star-icon" />
          <span class="add-text">Add to Watchlist</span>
        </button>
        <br />
        <br />
        <button class="watchlist-button" @click="goToWatchlist()">
          <span class="watchlist-text">View Watchlist</span>
        </button>
      </div>
    </div>
    <div class="period-interval-selector">
      <button
        @click="updatePeriodInterval('1Y', '1D')"
        :class="{ selected: selectedPeriod === '1Y' }"
      >
        1Y
      </button>
      <button
        @click="updatePeriodInterval('5Y', '1D')"
        :class="{ selected: selectedPeriod === '5Y' }"
      >
        5Y
      </button>
      <button
        @click="updatePeriodInterval('10Y', '1D')"
        :class="{ selected: selectedPeriod === '10Y' }"
      >
        10Y
      </button>
      <button
        @click="updatePeriodInterval('max', '1D')"
        :class="{ selected: selectedPeriod === 'max' }"
      >
        Max
      </button>
    </div>
    <div v-if="isLoading">Loading...</div>
    <div v-else>
      <line-chart :data="chartData"></line-chart>
    </div>
  </div>
</template>

<script>
import { getAuth, onAuthStateChanged } from "firebase/auth";
import axios from "axios";

export default {
  props: {
    searchTerm: String,
  },

  data() {
    return {
      isLoading: true,
      data: null,
      chartData: {}, // Initialize the chart data object
      ticker: this.searchTerm,
      useremail: "",
      selectedPeriod: "1Y", // Default period
      selectedInterval: "1d", // Default interval
    };
  },
  created() {
    // Use the created hook for fetching data
    // Fetch data from the API based on searchTerm
    const apiUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/yfinance/historicalData/${this.searchTerm}?period=${this.selectedPeriod}&interval=${this.selectedInterval}`;
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => {
        this.data = data; // Store the API response data

        // Populate the chartData object with date and open prices
        for (const date in this.data.Open) {
          this.chartData[date] = this.data.Open[date];
        }

        this.isLoading = false; // Set isLoading to false
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        this.isLoading = false; // Handle errors and set isLoading to false
      });
  },
  async mounted() {
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.useremail = user.email;
      } else {
        this.useremail = ""; // Ensure it's cleared when the user signs out
      }
    });
  },
  methods: {
    confirmAndAdd() {
      if (this.useremail == "") {
        this.$router.push({ name: "Login" });
      } else {
        const confirmation = window.confirm(
          "Confirm adding " + this.ticker + " to your watchlist?"
        );
        if (confirmation) {
          this.saveToWatchlist();
        }
      }
    },

    goBack() {
      this.$router.go(-1); // Navigate to previous page
    },

    goToWatchlist() {
      this.$router.push("/watchlist"); // Navigate to the "/watchlist" route
    },

    updatePeriodInterval(period, interval) {
      this.selectedPeriod = period;
      this.selectedInterval = interval;
      this.fetchData(); // Call a method to fetch data with the updated period and interval
    },

    async saveToWatchlist() {
      const watchData = {
        ticker: this.ticker,
        // Add other data fields as needed
      };
      // console.log("Saving " + this.ticker + " to Watchlist");
      alert("Successfully added " + this.ticker + " to Watchlist!");

      const apiUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/watch/add/${this.useremail}/${this.ticker}`;
      console.log(apiUrl);

      try {
        // Make a POST request to updateTrade endpoint
        await axios.post(apiUrl, watchData);

        this.$emit("added");
      } catch (error) {
        alert("Error: " + error.response.data);
      }
    },

    async fetchData() {
      this.isLoading = true; // Set isLoading to true while fetching data

      // Construct the API URL with the selected period and interval
      const apiUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/yfinance/historicalData/${this.searchTerm}?period=${this.selectedPeriod}&interval=${this.selectedInterval}`;

      try {
        // Fetch data from the updated API URL
        const response = await axios.get(apiUrl);
        this.data = response.data;

        // Clear existing chartData and populate it with the new data
        this.chartData = {};
        for (const date in this.data.Open) {
          this.chartData[date] = this.data.Open[date];
        }

        this.isLoading = false; // Set isLoading to false
      } catch (error) {
        console.error("Error fetching data:", error);
        this.isLoading = false;
      }
    },
  },
};
</script>

<style scoped>
.body {
  margin: 1.5% 3.5% 0% 1.5%;
  padding: 0 0 3% 1.5%;
  font-family: Arial, Helvetica, sans-serif;
}

.header {
  display: flex;
  padding-bottom: 1vw;
  justify-content: space-between;
  align-items: center;
}

.period-interval-selector {
  display: flex;
  padding-bottom: 3%;
  padding-left: 1%;
  margin-top: -3%;
}

.period-interval-selector button {
  padding: 10px 20px; /* Adjust the padding to make the buttons wider */
  border: 1px solid #ccc;
  border-radius: 7px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.period-interval-selector button:hover {
  background-color: #cfcfcf;
}

.selected {
  background-color: #272f51;
  color: #ffffff; /* Change the text color of the selected button */
  border: none; /* Remove the border on the selected button */
  font-weight: 800;
}

.add-button {
  background-color: #272f51;
  color: #fff;
  border: none;
  padding: 0.5vw 3vw;
  border-radius: 10px;
  font-size: 1.4vw;
  font-weight: bold;
  cursor: pointer;
}

.watchlist-button {
  background-color: #272f51;
  color: #fff;
  border: none;
  padding: 0.85vw 5.3vw;
  border-radius: 10px;
  font-size: 1.4vw;
  font-weight: bold;
  cursor: pointer;
}

.star-icon {
  width: 2.3vw; /* Adjust the width as needed */
  height: 2.3vw; /* Adjust the height as needed */
  margin-right: 1vw; /* Add some space between the star icon and text */
}

.add-text {
  position: relative;
  top: -0.5vw;
  font-weight: bold;
}

.watchlist-text {
  font-weight: bold;
}
.header-left {
  display: flex;
  align-items: center;
  margin-top: -3%;
}

.back-button {
  background: none;
  border: none;
  cursor: pointer;
  margin-right: 10px; /* Adjust the margin as needed */
}

.back-icon {
  width: 3vw; /* Adjust the width of the back icon */
  height: 3vw; /* Adjust the height of the back icon */
  margin-right: 1.5vw;
}

.header h1 {
  margin: 0; /* Remove margin to avoid extra spacing */
  font-size: 3vw; /* Adjust the font size as needed */
}
</style>
