<template>
  <div class="body">
    <h1>{{ searchTerm }}</h1>
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
  margin: 4% 3.5% 0% 1.5%;
  padding: 0 0 3% 1.5%;
  font-family: Arial, Helvetica, sans-serif;
}


</style>
