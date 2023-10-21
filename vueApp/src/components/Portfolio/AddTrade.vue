
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
  import { addInstrument } from '@/firebasefunc.js';
  import { COLLECTION_NAMES } from '@/firebaseConfig.js';

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

            await addInstrument(COLLECTION_NAMES.EQUITY_PORTFOLIO, tradeData);

            // Reset placeholder
            document.getElementById('userForm').reset();
            this.tradeQuantity = null;
            this.pricePerTrade = null;

            this.$emit("added")
            
     }

    },
  };
</script>




<style >
  #addTradeContainer h1 {
    margin-top: 0;
}

#addTradeContainer {
    position: absolute; 
    margin-top: -6.5%; 
    width: 25.5%

}


/* Add Trades */
.titleOfDiv {
    font-size: 2.5vw;
}

 #userForm {
    text-align: center;
    background-color: white;
    width: 100%;
    height: 28vw;
    border-radius: 25px;
    box-shadow: 1px 8px 10px rgba(0, 0, 0, 0.3);
    padding-top: 14%;
}

input {
    background-color: #F3F3F3;
}

#userForm input[type="text"],
#userForm input[type="number"] {
    width: 70%; 
    height: 7%; 
    margin: 1.2% 0; 
    font-size: 1.25vw; 
    font-weight: 600;
    padding-left: 4%;
    border-radius: 5px; 
    border: none;
}

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0%;
}

input::placeholder {
    color: #C2C1C1;
}


#tradecost {
    text-align: center;
    margin-top: 1%; /* Adjust the margin-top value to move it closer to the input box */
    font-weight: bold; /* Make the text bold if needed */
    font-size:2vw;
}

#savebutton {
    width: 45%; 
    height: 18%; 
    background-color: #272F51; 
    color: white; 
    font-size: 1.8vw;
    font-weight: 700;
    border-radius: 20px;
    cursor: pointer; 
}

#savebutton:hover {
    background-color: #475281; /* Change the button color on hover */
}


/* Total Profit */
#profitContainer {
    background-color: #3a446e;
    color: white;
    width: 96%;
    border-radius: 1.5vh;
    text-align: right;
    padding-right: 5%;
    padding-top: 0.1%;
    padding-bottom: 0.1%;
    margin-top: 4%; 
    font-size: 1.15vw;
}

#profitContainer h3 {
    margin-bottom: 0vw; /* Adjust the margin-bottom value as needed */
    color: rgb(222, 222, 222);
}

#totalProfit {
    color: #02dbfd;
}

</style>

  