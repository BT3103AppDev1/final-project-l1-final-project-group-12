<template>
  <div class="market-header">
    <h1>Market (Most Actives)</h1>
    <form id="marketSearch" class="search-form">
      <input
        type="text"
        id="searchInput"
        required=""
        placeholder="Search by company name/code"
        v-model="searchTerm"
      />
      <br /><br />

      <button id="searchButton" type="button" @click="runMarketSearch()">
        Search
      </button>
      <br /><br />
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      searchTerm: "",
    };
  },
  methods: {
    async runMarketSearch() {
      console.log("Button Clicked");

      try {
        const apiUrl = `http://localhost:3000/api/yfinance/ticker/${this.searchTerm}`;
        const ticker = await axios.get(apiUrl);
        console.log(ticker)
        // Redirect to a new page and pass the search term as a parameter
        this.$router.push({
          name: "SearchResults",
          params: { searchTerm: ticker.data }, // Use ticker.data to get the response data
        });
      } catch (error) {
        console.error("Error converting search term to ticker:", error);
        // Handle the error here
      }
    },
  },
};
</script>


<style scoped>
.market-header {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.search-form {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

#searchInput {
  margin-right: 1vw;
  margin-top: 0.5vw;
  width: 28vw;
  height: 32%;
  border-radius: 0.75vw;
  border-color: #fffdfd;
  font-weight: bold;
  font-size: 1.4vw;
  background-color: white;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.1);
  padding-left: 0.75vw;
}

#searchInput::placeholder {
  color: #cbcbcb;
  font-size: 1.2vw;
}

#searchButton {
  background-color: #272f51;
  width: 35%;
  color: white;
  border: none;
  padding: 0.75%;
  border-radius: 10px;
  cursor: pointer;
  font-size: 1.6vw;
  height: 40%;
  font-weight: bold;
  margin-right: 0.5vw;
  margin-top: 0.5vw;
}
</style>
