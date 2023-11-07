<template>
  <div class="body">
    <div class="header">
      <h1>{{ searchTerm }}</h1>
      <button class="add-button" @click="addToWatchlist">
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