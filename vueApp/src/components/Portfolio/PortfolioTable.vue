<template>
  <div class="table-container">
    <table id="scrollable-table" class="auto-index">
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>BuyPrice</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Expected <br> Return</th>
          <th></th>
        </tr>
      </thead>
 
      <tbody>
        <tr v-for="(item, index) in portfolioData" :key="item.ticker">
          <td>{{ index + 1 }}</td>
          <td>{{ item.name }}</td>
                                                    <!-- TODO: Add ticker -->
          <!-- Buy Price -->
          <td>
            <!-- Display Buy Price input field if in editing state -->
            <template v-if="item.editing">
              <input v-model="updatedBuyPrice" type="number" />
            </template>
            <!-- Display Buy Price if not in editing st ate -->
            <template v-else>
              {{ parseFloat(item.buyPrice).toFixed(2) }}
            </template>
          </td>

          <!-- Stock Price -->
          <td>
            <template v-if="isNaN(this.stockPrices[item.ticker]) ">Loading..</template>
            <template v-else>{{ parseFloat(this.stockPrices[item.ticker]).toFixed(2) }}</template>
          </td>        

          <!-- Buy Quantity -->
          <td>
            <!-- Display Buy Quantity input field if in editing state -->
            <template v-if="item.editing">
              <input v-model="updatedBuyQuantity" type="number" />
            </template>
            <!-- Display Buy Quantity if not in editing state -->
            <template v-else>
              {{ item.buyQty }}
            </template>
          </td>


          <!-- P/L -->
          <td>
            <template v-if="isNaN(this.stockPrices[item.ticker])">Loading..</template>
            <template v-else>{{ calculateProfitLoss(item).toFixed(2) }}</template>
          </td>


          <!-- Button -->
          <td>
            <!-- Display Edit button only if not in editing state -->
            <button v-if="!item.editing" @click="editItem(index)" class="btw">
              <img src="@/assets/editIcon.png" alt="Edit" />
            </button>
            <!-- Display Save and Cancel buttons if in editing state -->
            <template v-else>
              <button @click="saveItem(index)" class="btw" id="saveButton">
                <img src="@/assets/tickIcon.png" alt="Save" />
              </button>
              <button @click="cancelEdit(index)" class="btw" id="cancelButton">
                <img src="@/assets/crossIcon.png" alt="Cancel" />
              </button>
            </template>
            <!-- Display Delete button if not in editing state -->
            <button v-if="!item.editing" @click="deleteItem(item.ticker)" class="btw">
              <img src="@/assets/deleteIcon.png" alt="Delete" />
            </button>
          </td>

        </tr>
      </tbody>
    </table>

    <!-- Display message if portfolioData is empty -->
    <p v-if="hasData == false" class="no-trades-message">
      You have not added any trades to your portfolio. To gain portfolio insights, please add your open trades.
    </p>
  
  </div>
</template>

<script>
import { getAuth, onAuthStateChanged } from 'firebase/auth'
import axios from 'axios';

export default {
  data() {
    return {
      updatedBuyQuantity: 0,
      updatedBuyPrice: 0,
      totalProfitLoss: 0,
    };
  },

  

  async mounted() {
      const auth = getAuth();
      onAuthStateChanged(auth, (user) => {
          if (user) {
              this.useremail = user.email;

          } else {
              this.useremail = ''; // Ensure it's cleared when the user signs out
          }
      });
  },

  props: {
    portfolioData: Array,
    stockPrices: Object,
    hasData: Boolean,
  },

  methods: {
    editItem(index) {
      const item = this.portfolioData[index];
      
      item.editing = true;
      this.updatedBuyQuantity = item.buyQty;
      this.updatedBuyPrice = item.buyPrice;
    },

    async saveItem(index) {
      const item = this.portfolioData[index];
      
      // Update item data with the new values
      const updatedData = {
        ticker: item.ticker,
        buyPrice: this.updatedBuyPrice,
        buyQty: this.updatedBuyQuantity,
      };
      
      const userConfirmed = window.confirm("Are you sure you want to proceed?");
      
      if (userConfirmed) {
        const apiAddUrl = `http://localhost:3000/api/update/updateTrade/${this.useremail}`;
        const apiDeleteUrl = `http://localhost:3000/api/delete/trade/${this.useremail}/${item.ticker}`;
        
        try {
          axios.delete(apiDeleteUrl).then(() => {
          axios.put(apiAddUrl, updatedData).then(() => {
            this.$emit('refresh-request');
      
            });
          })

          // Update the data in the Vue component
          item.buyPrice = this.updatedBuyPrice;
          item.buyQty = this.updatedBuyQuantity;

        } catch (error) {
          console.error('Fail to updating trade: ', error )
        }
        item.editing = false;
      } else {
        this.cancelEdit(index)
      }
      
      
    },

    cancelEdit(index) {
      const item = this.portfolioData[index];

      // Revert the updated values back to the original values
      this.updatedBuyPrice = item.buyPrice;
      this.updatedBuyQuantity = item.buyQty;
      
      item.editing = false;
    },

    async deleteItem(ticker) {
      const userConfirmed = window.confirm("Are you sure you want to proceed?");
      if (userConfirmed) {
        try {
          const apiUrl = `http://localhost:3000/api/delete/trade/${this.useremail}/${ticker}`;
          await axios.delete(apiUrl);

          this.$emit('refresh-request');

        } catch (error) {
          console.error('Fail to delete trade: ', error )
        }
      }
    },

    

    emitTotalPL() {
      this.$emit('total-pl-updated', this.totalPL);
    },

  },

  computed: {
    calculateProfitLoss() {
      return (item) => {
        return (item.buyQty * this.stockPrices[item.ticker]) - (item.buyQty * item.buyPrice);   //TODO: update price
      };
    },
    totalPL() {
      return this.portfolioData.reduce((total, item) => {
        return total + this.calculateProfitLoss(item);
      }, 0);
    },

  },

  watch: {
    totalPL: 'emitTotalPL',
  },

};
</script>




<style>
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
    border-bottom: 2px solid #D0D0D0;
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
  border-color: #007BFF; /* Change border color when focused */
}


/* No Trades message */
.no-trades-message {
  color: #BFBFBF; /* Change the color to your desired color */
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
    height: auto 
  }

  #cancelButton img {
    width: 1.5vw; 
    height: auto 
  }
  
</style>