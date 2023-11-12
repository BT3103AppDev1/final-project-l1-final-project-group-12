<template>
  <div class="EquityBoxcontainer">
    <div class="box">
      <div class="box-header">
        <div class="header-text">
          <h3 class="boxh3">
            <img class="icon" :src="imageSrc" alt="" />
            {{ header }}
          </h3>
        </div>
      </div>

      <hr class="custom-hr" />

      <table class="table">
        <tr v-for="(row, rowIndex) in rows" :key="rowIndex">
          <td>{{ rowIndex + 1 }}</td>
          <button
            class="indivStockButton"
            v-for="(cell, cellIndex) in row"
            :key="cellIndex"
            @click="navToStock(cell)"
          >
            {{ cell }}
          </button>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Box",
  props: {
    imageSrc: String,
    header: String,
    rows: Array,
  },
  methods: {
    async navToStock(cellValue) {
      try {
        const apiUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/yfinance/ticker/${cellValue}`;
        const ticker = await axios.get(apiUrl);
        console.log(ticker);
        // Redirect to a new page and pass the search term as a parameter
        this.$router.push({
          name: "SearchResults",
          params: { searchTerm: ticker.data }, // Use ticker.data to get the response data
        });
      } catch (error) {
        console.error("Error converting search term to ticker:", error);
        alert("Company name or ticker not found!");
        // Handle the error here
      }
    },
  },
};
</script>

<style scoped>
.EquityBoxcontainer {
  height: auto;
  border-radius: 13px;
}

.box {
  border-radius: 13px;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  font-weight: bold;
  font-size: 1.5vw;
  width: 40vw;
  padding: 15px 0px 10px 15px;
}

.box table td {
  padding: 15px;
  font-size: 1.6vw;
}
.box-header {
  vertical-align: middle;
}

.boxh3 {
  font-size: 2vw;
  align-self: center;
  margin-top: 0.8vw;
}

.header-text .icon {
  max-width: 40px;
  margin-right: 10px;
  padding-left: 10px;
}

.custom-hr {
  border: none;
  border-top: 2px solid #d0d0d0;
  margin-right: 4%;
}

.indivStockButton {
  padding-top: 0.8vw;
  border: none;
  background-color: transparent;
  cursor: pointer;
  font-size: 1.6vw;
  font-weight: bold;
  cursor: pointer;
  text-align: left;
}

.indivStockButton:hover {
  color: #133ae4; /* Change the color on hover */
  text-decoration: underline;
  background-color: transparent;
  box-shadow: none;
}
</style>
