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
            <th>P/L</th>
            <th></th>
          </tr>
        </thead>
  
        <tbody>
          <tr v-for="(item, index) in portfolioData" :key="item.Stock">
            <td>{{ index + 1 }}</td>
            <td>{{ item.Stock }}</td>
                                                      <!-- TODO: Add ticker -->
            <!-- Buy Price -->
            <td>
              <!-- Display Buy Price input field if in editing state -->
              <template v-if="item.editing">
                <input v-model="updatedBuyPrice" type="number" />
              </template>
              <!-- Display Buy Price if not in editing st ate -->
              <template v-else>
                {{ parseFloat(item.Buy_Price).toFixed(2) }}
              </template>
            </td>
  
            <td>0</td>        <!-- TODO: Update Price -->
  
            <!-- Buy Quantity -->
            <td>
              <!-- Display Buy Quantity input field if in editing state -->
              <template v-if="item.editing">
                <input v-model="updatedBuyQuantity" type="number" />
              </template>
              <!-- Display Buy Quantity if not in editing state -->
              <template v-else>
                {{ SuggestedQty(item.Buy_Quantity, item.Stock) }}
              </template>
            </td>
  
            <td>0</td>      <!-- TODO: Update P/L -->
  
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
              <button v-if="!item.editing" @click="deleteItem(item.Stock)" class="btw">
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
  import { editInstrument, deleteInstrument } from '@/firebasefunc.js';
  import { COLLECTION_NAMES } from '@/firebaseConfig.js';
  
  export default {
    data() {
      return {
        updatedBuyQuantity: 0,
        updatedBuyPrice: 0,
      };
    },
  
    props: {
      SuggestedQty: Function,
      portfolioData: Array,
      hasData: Boolean,
    },
  
  
    methods: {
      editItem(index) {
        const item = this.portfolioData[index];
  
        item.editing = true;
        this.updatedBuyQuantity = item.Buy_Quantity;
        this.updatedBuyPrice = item.Buy_Price;
      },
  
      async saveItem(index) {
        const item = this.portfolioData[index];
  
        // Update item data with the new values
        const updatedData = {
          Buy_Price: this.updatedBuyPrice,
          Buy_Quantity: this.updatedBuyQuantity,
        };
        await editInstrument(COLLECTION_NAMES.EQUITY_PORTFOLIO, item.Stock, updatedData);
  
        item.editing = false;
        this.$emit('refresh-request');
      },
  
      cancelEdit(index) {
        const item = this.portfolioData[index];
  
        // Revert the updated values back to the original values
        this.updatedBuyPrice = item.Buy_Price;
        this.updatedBuyQuantity = item.Buy_Quantity;
        
        item.editing = false;
      },
  
      async deleteItem(stock) {
        await deleteInstrument(COLLECTION_NAMES.EQUITY_PORTFOLIO, stock);
        
        this.$emit('refresh-request');
      },
  
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
      padding-top: 2.2vw;
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