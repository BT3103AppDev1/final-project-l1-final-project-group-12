<template>
  <div id="addToWatchlist">
    <form id="watchlistForm" @submit.prevent="saveToWatchlist">
      <h2 class="titleOfWatchlistForm">Add to Watchlist</h2>
      <input
        type="text"
        v-model="ticker"
        required
        placeholder="Search by company name/code"
      />
      <button type="submit" class="add-button">
        <img src="@/assets/starIcon.png" alt="" class="star-icon" />
        <span class="add-text">Add</span>
      </button>
    </form>
  </div>
</template>

<script>
import { getAuth, onAuthStateChanged } from "firebase/auth";
import axios from "axios";

export default {
  data() {
    return {
      ticker: "",

      // User info
      useremail: "joleneganyuzhen@gmail.com",
    };
  },
  methods: {
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
        await axios.put(apiUrl, watchData);
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
/* Your styles remain the same */
</style>

<style scoped>
.titleOfWatchlistForm {
  font-size: 1.9vw;
}

#watchlistForm {
  text-align: center;
  background-color: white;
  height: 15vw;
  border-radius: 25px;
  box-shadow: 1px 8px 10px rgba(0, 0, 0, 0.3);
  padding-top: 7%;
}

input {
  background-color: #f3f3f3;
  border-radius: 6px;
  width: 80%;
  border: none;
  text-align: center;
  height: 12%;
}

input::placeholder {
  color: #c2c1c1;
}

.add-button {
  background-color: #272f51;
  color: #fff;
  border: none;
  border-radius: 10px;
  width: 50%;
  height: 15%;
  font-size: 1.2vw;
  cursor: pointer;
  margin-top: 8%;
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
