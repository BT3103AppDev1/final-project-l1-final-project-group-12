<template>
  <div>
    <ScrollableTable :headers="tableHeaders" :rows="tableRows" />
  </div>
</template>

<script>
import ScrollableTable from "./ScrollableTable.vue";
import axios from "axios";

export default {
  components: {
    ScrollableTable,
  },
  data() {
    return {
      tableHeaders: [
        "#",
        "Symbol",
        "Name",
        "Price (Intraday)",
        "Change",
        "% Change",
        "Volume",
        "3-month Avg Vol",
        "Market Cap",
        "PE Ratio (TTM)",
      ],
      tableRows: Array.from({ length: 25 }, () => Array(9).fill(" ")),
    };
  },

  mounted() {
    // Make an API request to fetch data
    axios
      .get("/api/yfinance/mostActivesData")
      .then((response) => {
        // Assuming the API response is an array of data
        this.tableRows = response.data;
      })
      .catch((error) => {
        console.error("API request failed:", error);
      });
  },
};
</script>
