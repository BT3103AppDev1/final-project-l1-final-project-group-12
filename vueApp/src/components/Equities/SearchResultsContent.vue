<template>
    <div class="body">
      <h1>{{ searchTerm }}</h1>
      <div v-if="isLoading">Loading...</div>
      <div v-else>
        <ul>
          <li v-for="(price, date) in data.Open" :key="date">
            <p>Date: {{ date }}</p>
            <p>Open Price: {{ price }}</p>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      searchTerm: String,
    },
    data() {
      return {
        isLoading: true,
        data: null,
      };
    },
    created() {
      // Fetch data from the API based on searchTerm
      const apiUrl = `http://localhost:3000/api/yfinance/historicalData/${this.searchTerm}?period=1Y&interval=1d`;
      fetch(apiUrl)
        .then((response) => response.json())
        .then((data) => {
          this.data = data; // Store the API response data
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
    margin: 4% 3.5% 0% 2%;
    padding: 0 0 3% 1.5%;
    font-family: Arial, Helvetica, sans-serif;
  }
  </style>
  