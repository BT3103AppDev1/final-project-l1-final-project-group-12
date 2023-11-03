<template>
  <div class="table-container">
    <table id="scrollable-table" class="auto-index">
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Ticker</th>
          <th>Price</th>
          <th></th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(item, index) in this.watchlistData" :key="item.ticker">
          <td>{{ index + 1 }}</td>
          <td>{{ item.name }}</td>
          

          <td>
            <button class="btw" @click="deleteItem(item.ticker)">
              <img src="@/assets/deleteIcon.png" alt="Delete" />
            </button>
          </td>
          <td>{{this.stockPrices[item.ticker]}}</td>
        </tr>
      </tbody>
    </table>

    <!-- Display message if watchlist is empty -->
    <p v-if="hasData == false" class="no-stocks-message">
      You have not added any stocks to your watchlist.
    </p>
  </div>
</template>

<script>
import { getAuth, onAuthStateChanged } from "firebase/auth";
import axios from 'axios';

export default {
  data() {
    return {
      ticker: "",
      useremail: "",
      watchlistData: [],
      hasData: false,
      stockPrices: {} // Initialize stockPrices

    };
  },

  async created() {
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
      if (user) {
        
        this.useremail = user.email;
        console.log(this.useremail)
        this.fetchData()
          .then(() => {
            // this.getStockPrice();
            console.log(this.watchlistData)
          });

        // Call fetchData every 5 seconds
        setInterval(this.getStockPrice, 5000);
      } else {
        console.error('User not authenticated');
      }
    });
  },



  methods: {
    async deleteItem(ticker) {
      const apiUrl = `http://localhost:3000/api/watch/delete/${this.useremail}/${ticker}`;
      await axios.delete(apiUrl);

      this.$emit('refresh-request');
    },
  
  async fetchData() {
    console.log(this.useremail)
    try {
      
      const apiUrl = `http://localhost:3000/api/watch/read/${this.useremail}`;
      console.log(apiUrl);
      const querySnapshot = await axios.get(apiUrl);
      this.watchlistData = querySnapshot.data;

      this.hasData = this.watchlistData.length > 0;
      console.log(this.watchlistData)

    } catch (error) {
      console.error("Error fetching data:", error);
    }
  },

  async getStockPrice() {
    try {
      for (const item of this.watchlistData) {
        const apiUrl = `http://localhost:3000/api/yfinance/curentPrice/${item.ticker}`;
        const response = await axios.get(apiUrl);
        const price = response.data;

        this.stockPrices[item.ticker] = price;
      }
    } catch (error) {
      console.error("Error fetching stock price:", error);
    }
  },
}};

</script>


<style scoped>
/* Box */
.table-container {
  height: 33vw;
  overflow-y: auto;
  border-radius: 25px;
  justify-content: center;
  background-color: white;
  box-shadow: 0 8px 10px rgba(0, 0, 0, 0.3);
  margin-bottom: 0;
}

/* Table */
#scrollable-table {
  width: 90%;
  background-color: white;
  border-collapse: collapse;
  margin: 0 auto;
}

#scrollable-table th,
#scrollable-table td {
  padding: 0.3vw;
  text-align: center;
  border-bottom: 2px solid #d0d0d0;
  padding-bottom: 2.7%;
  padding-top: 2.7%;
  font-size: 1.7vw;
  font-weight: bold;
}

#scrollable-table th {
  padding-top: 2vw;
  background-color: white;
}

#scrollable-table thead th {
  position: sticky;
  top: 0;
}

/* Add styles for input elements within table cells */
#scrollable-table input[type="number"] {
  width: 25%;
  padding: 0.6vw;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 1.2vw;
  font-weight: bold;
  text-align: center;
}

#scrollable-table input[type="number"]:focus {
  outline: none; /* Remove the default focus outline */
  border-color: #007bff; /* Change border color when focused */
}

/* No Trades message */
.no-stocks-message {
  color: #bfbfbf; /* Change the color to your desired color */
  border-bottom: none !important;
  padding-top: 11vw !important;
  text-align: center;
  font-size: 1.8vw;
  font-weight: bold;
  padding-left: 10%;
  padding-right: 10%;
}

/* Delete/Edit Button */
.btw {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: inline;
  margin-right: 0.5vw;
}

.btw img:hover {
  transform: scale(1.3); /* Increase the value to make it scale more */
  transition: transform 0.2s ease-in-out; /* Add a smooth transition effect */
}

.btw img {
  width: 1.8vw;
  height: auto;
}

#saveButton img {
  width: 2vw;
  height: auto;
}

#cancelButton img {
  width: 1.5vw;
  height: auto;
}
</style>
