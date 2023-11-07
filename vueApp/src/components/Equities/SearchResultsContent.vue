<template>
  <div class="body">
    <div class="header">
      <h1>{{ searchTerm }}</h1>
      <button class="add-button" @click="confirmAndAdd()">
      <img src="@/assets/starIcon.png" alt="" class="star-icon" />
        <span class="add-text">Add to Watchlist</span>
      </button>
    </div>
    <div v-if="isLoading">Loading...</div>
    <div v-else>
      <LineChart :chartData="chartData" :chartOptions="chartOptions"></LineChart>
    </div>
  </div>
</template>

<script>
import LineChart from './LineChart.vue';
import { getAuth, onAuthStateChanged } from "firebase/auth";
import axios from "axios";

export default {
  props: {
    searchTerm: String,
  },
  components: {
    'LineChart': LineChart, // Register the new component
  },
  data() {
    return {
      isLoading: true,
      data: null,
      chartData: {}, // Initialize the chart data object
      ticker: this.searchTerm,
      useremail: "",
    };
  },
  created() { // Use the created hook for fetching data
    // Fetch data from the API based on searchTerm
    const apiUrl = `http://localhost:3000/api/yfinance/historicalData/${this.searchTerm}?period=1Y&interval=1d`;
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
      const confirmation = window.confirm(
        "Are you sure you want to add this ticker to your watchlist?"
      );
      if (confirmation) {
        this.saveToWatchlist();
      }
    },

    async saveToWatchlist() {
      const watchData = {
        ticker: this.ticker,
        // Add other data fields as needed
      };
      console.log("Saving " + this.ticker + " to Watchlist");

      const apiUrl = `http://localhost:3000/api/watch/add/${this.useremail}/${this.ticker}`;
      console.log(apiUrl);

      try {
        // Make a POST request to updateTrade endpoint
        await axios.post(apiUrl, watchData);
        // Reset placeholder
        this.ticker = ""; // Clear the input field
        this.$emit("added");
      } catch (error) {
        alert("Error: " + error.response.data);
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
  padding-bottom: 3vw;
  justify-content: space-between;
  align-items: center;
}

.add-button {
  background-color: #272f51;
  color: #fff;
  border: none;
  padding: 1vw 3vw;
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
  top: -4px;
  font-weight: bold;
}

</style>