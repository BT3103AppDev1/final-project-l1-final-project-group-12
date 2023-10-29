<template>
  <div id="addToWatchlist">
    <form id="watchlistForm">
      <h2 class="titleOfWatchlistForm">Add to Watchlist</h2>
      <input
        type="text"
        id="stock1"
        required="yes"
        placeholder="Search by company name/code"
      />
      <button type="button" class="add-button"  @click="savetofs()">
        <img src="@/assets/star.png" alt="" class="star-icon" />
        <span class="add-text">Add</span>
      </button>
    </form>
  </div>
</template>

<script>
import { addInstrument } from "@/firebasefunc.js";
import { COLLECTION_NAMES } from "@/firebaseConfig.js";
import firebaseApp from "@/firebase.js";
import { getAuth, onAuthStateChanged } from 'firebase/auth'

export default {
  data() {
    return {
      stockName: "",

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
    async savetofs() {
      console.log("Saving");
      let stock = document.getElementById("stock1").value;

      const stockData = {
        Stock: stock,
        // Add other data fields as needed
      };

      await addInstrument(COLLECTION_NAMES.WISHLIST, this.useremail, stockData);

      // Reset placeholder
      document.getElementById("watchlistForm").reset();

      this.$emit("added");
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
