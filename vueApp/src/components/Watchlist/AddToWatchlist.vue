<template>
    <div id="addToWatchlist">
        <form id="watchlistForm">
            <h2 class="titleOfWatchlistForm">Add to Watchlist</h2>

            <input type="text" id="stock1" required="yes" placeholder="Search by company name/code">
            <button class="add-button">
                <img src="@/assets/star.png" alt="" class="star-icon">
                <span class="add-text">Add</span>
            </button>
        </form>
    </div>
</template>

<script>
import firebaseApp from '@/firebase.js'; // npm install firebase
import { COLLECTION_NAMES } from '@/firebaseConfig.js';
import { getFirestore, collection, addDoc } from 'firebase/firestore';

export default {
  data() {
    return {
      stockName: '',
    };
  },
  methods: {
    async addStock() {
      const db = getFirestore(firebaseApp);

      const stockData = {
        name: this.stockName,
        // Add other data fields as needed
      };

      try {
        // Use COLLECTION_NAMES.WISHLIST to reference the "WISHLIST" collection
        const docRef = await addDoc(collection(db, COLLECTION_NAMES.WISHLIST), stockData);
        console.log('Stock added to Wishlist with ID: ', docRef.id);
        // Clear the input field after successfully adding the stock
        this.stockName = '';
      } catch (error) {
        console.error('Error adding stock to Wishlist: ', error);
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
    background-color: #F3F3F3;
    border-radius: 6px;
    width: 80%;
    border: none;
    text-align: center;
    height: 12%;
}

input::placeholder {
    color: #C2C1C1;
}

.add-button {
    background-color: #272F51;
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
