<template>
  <div class="body">
    <div class="header">
      <h1>{{ searchTerm }}</h1>
      <button type="button" class="add-button" @click="savetofs">
        <img src="@/assets/starIcon.png" alt="" class="star-icon" />
        <span class="add-text">Add To Watchlist</span>
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

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem; /* Adjust the margin as needed */
}

.add-button {
  background-color: #272f51;
  color: #fff;
  border: none;
  border-radius: 10px;
  width: 20%;
  height: 2.5vw;
  font-size: 1.2vw;
  cursor: pointer;

}

.add-text {
  position: relative;
  top: -4px;
  font-weight: bold;
}

.star-icon {
  width: 1.7vw;
  height: 1.7vw;
  margin-right: 5px;
}

</style>
