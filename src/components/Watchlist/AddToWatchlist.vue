<template>
  <div id="addToWatchlist">
    <form id="watchlistForm" @submit.prevent="confirmAndAdd">
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
      useremail: "",
    };
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
    async confirmAndAdd() {
      const confirmation = window.confirm(
        "Confirm adding " + this.ticker.toUpperCase() + " to your watchlist?"
      );
      if (confirmation) {
        this.saveToWatchlist();
      }
    },

    async validateInput() {
      try {
        const apiUrlGetTicker = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/yfinance/ticker/${this.ticker}`;
        const currTicker = await axios.get(apiUrlGetTicker);
        return currTicker.data;
      } catch (error) {
        alert("Error: Invalid company name or ticker!");
      }
    },

    async saveToWatchlist() {
      try {
        const currTicker = await this.validateInput();

        const watchData = {
          ticker: currTicker,
        };

        const apiUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/watch/add/${this.useremail}/${currTicker}`;
        await axios.post(apiUrl, watchData);
        alert("Successfully added " + currTicker + " to Watchlist!");
        this.ticker = ""; // Clear the input field
        this.$emit("added");
      } catch (error) {
        console.error(error);
        alert("Please try again!");
      }
    },
  },
};
</script>

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
