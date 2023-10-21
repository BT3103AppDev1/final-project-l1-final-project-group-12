
<template>
    <div id="addTradeContainer">

        <form id="userForm">
            <h1 class="titleOfDiv">Add Trade</h1>

            <input type="text" id="stock1" required="" placeholder="Stock name/code"> <br><br>    
            <input type="number" id="quant1" required="" placeholder="Input Trade Quantity" v-model="tradeQuantity"> <br><br>   
            <input type="number" id="buy1" required="" placeholder="Input Price Per Trade" v-model="pricePerTrade"> <br><br>
  
            <h2 id="tradecost">Total: SGD {{ tradeCost.toFixed(2) }}</h2>

            <button id="savebutton" type="button" @click="savetofs()"> + Add </button><br><br>
                
        </form>
        

        <div id = "profitContainer">
            <h3>Total Profit SGD </h3>
            <h1 id="totalProfit">$XXXX</h1>    <!-- TODO: Total up Profit--> 
        </div>
      
        
    </div>
  </template>
  
  <script>
  import '@/style/Portfolio/AddTrade.css'
  import { addInstrument } from '@/firebasefunc.js';

  export default {
    data() {
      return {
        stockName: '',
        tradeQuantity: null,
        pricePerTrade: null,
        totalCost: 0,
      };
    },

    computed: {
        // Calculate the trade profit based on tradeQuantity and pricePerTrade
        tradeCost() {
        return (this.tradeQuantity || 0) * (this.pricePerTrade || 0);
        },
    },

    watch: {
        tradeQuantity: "calculateTotalCost",
        pricePerTrade: "calculateTotalCost",
        },

    methods: {
        
        // Save to Firebase
        async savetofs() {

            // Get input from placeholder
            let stock = document.getElementById("stock1").value
            let buyPrice = document.getElementById("buy1").value
            let buyQuantity = document.getElementById("quant1").value

            //Define valid input
            if (isNaN(parseFloat(buyPrice)) || isNaN(parseFloat(buyQuantity)) ) {   //TODO: ADD CONTRAINT FOR INVALID STOCK
                alert("Buy Price or Buy Quantity must be valid numbers.");          //TODO: Add PopUp Window
                return;
            } else if (stock.trim() === "" || buyPrice.trim() === "" || buyQuantity.trim() === "") {
                alert("All fields must be filled out.");
                return;
            }      

            // Add Trade
            const tradeData = {
                Stock: stock,
                Code: stock,                            // TO BE EDITED
                Buy_Price: parseFloat(buyPrice),
                Buy_Quantity: parseFloat(buyQuantity),
            };

            await addInstrument(tradeData);

            // Reset placeholder
            document.getElementById('userForm').reset();
            this.tradeQuantity = null;
            this.pricePerTrade = null;

            this.$emit("added")
            
     }

    },
  };
  </script>

  