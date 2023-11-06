<template>
  
    <div class="toggleContainer">

      <!-- Toggle Switch -->
      <div class="toggle-switch" @click="toggleSwitch">
        <input type="checkbox" v-model="isChecked" class="checkbox">
        <div class="slider">
          <div v-if="isChecked" class="left-icon">
            <img src='@/assets/tableIcon.png' alt="Table Icon">
          </div>
          <div v-else class="right-icon">
            <img src='@/assets/piechartIcon.png' alt="Pie Chart Icon">
          </div>
        </div>
      </div>
    </div>

  
    <div v-if="!status">
      <!-- Table / PieChart  -->
      <PortfolioTable
        v-if="!isChecked"
        :portfolioData="portfolioData"
        :stockPrices="stockPrices"
        :hasData="hasData"
        :objective="objective"
        :status="status"
        @refresh-request="refresh"
        @total-pl-updated="emitTotalPL"
      />

      <PieChart
        v-else
        :portfolioData="portfolioData"
        :hasData="hasData"
        @refresh-request="refresh"
      />

    </div>

    <div class = assetView-container v-else>
      Optimising...
    </div>

   
    </template>
  
  
  <script>
  import { getAuth, onAuthStateChanged } from 'firebase/auth'
  import axios from 'axios';

  import PortfolioTable from '@/components/Portfolio/PortfolioTable.vue'
  import PieChart from '@/components/Portfolio/PortfolioPieChart.vue'

  export default {
    name: 'PortfolioAssetView',
    components: {
      PortfolioTable,
      PieChart
    },

    props: {
      objective: String,
      status: Boolean,
      updateOptimisePortfolio: Function,
      getOptimizedStatus: Boolean,
    },

    data() {
      return {
        isChecked: false,
        portfolioData: [],
        stockPrices: {},
        hasData: true,

        useremail: '',
      };
    },

    created() {
      const auth = getAuth();

      // Create an async function to handle user authentication and data fetching
      const handleUserAuthentication = async (user) => {
        if (user) {
          this.useremail = user.email;

          await this.fetchData();
          await this.getStockPrice();

          // Get stock price every 5 seconds
          setInterval(async () => {
            await this.getStockPrice();
          }, 5000);

          const watchCallback = async () => {
            if (!this.getOptimizedStatus && this.hasData){
              await this.updateOptimisePortfolio(this.objective);
            }
            await this.fetchData();
          };

          this.$watch('objective', watchCallback);
        } else {
          console.error('User not authenticated');
        }
      };

      // Pass the async function as the callback to onAuthStateChanged
      onAuthStateChanged(auth, handleUserAuthentication);
    },

    methods: {
      
      toggleSwitch() {
        this.isChecked = !this.isChecked;
      },

      async refresh() {
        await this.fetchData();

        this.$emit('refresh-request', this.hasData);
      },

      async fetchData() {
        let apiUrl;
        try {
            if (this.objective) {
              apiUrl = `http://localhost:3000/api/read/allTrades/${this.useremail}/${this.objective}`;
            } else {
              apiUrl = `http://localhost:3000/api/read/allTrades/${this.useremail}/""`;
            }
            console.log("Fetching Portfolio Data: ", apiUrl)
            const querySnapshot = await axios.get(apiUrl);
            this.portfolioData = querySnapshot.data;

            this.hasData = this.portfolioData.length > 0;
            this.$emit('has-data', this.hasData);

          } catch (error) {
            console.error("Error fetching data:", error);
          }
      }, 

      async getStockPrice() {   
        try {
          for (const item of this.portfolioData) {
              const apiUrl = `http://localhost:3000/api/yfinance/curentPrice/${item.ticker}`;
              const response = await axios.get(apiUrl);
              const price = response.data;

              this.stockPrices[item.ticker] = price;          
          };

        } catch (error) {
          console.error("Error fetching stock price:", error);
        }

      },

      emitTotalPL(totalPL) {
        this.$emit('total-pl-updated', totalPL);
      },

    },
    emits: ["total-pl-updated", "refresh-request", "has-data"],



  };
  </script>
  
  


  <style>
  /* Toggle Switch */
  .toggleContainer {
     margin-left: 21%;
     margin-top: 9.3%;  
    position: absolute; 
    top: 0;   
  }
  
  .toggle-switch {
    width: 7vw;
    height: 3vw;
    background-color: #ccc;
    border-radius: 15vw;
  }
  
  .checkbox {
    opacity: 0;
    width: 0;
    height: 0;
  }
  
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ebfcf9;
    border: 0.35vh solid #272F51;
    border-radius: 1000vw;
    transition: 0.4s;
    display: flex; /* Use flexbox to control the positioning */
    align-items: center; /* Vertically center content */
    justify-content: space-between; /* Spread content to the ends of the slider */
    overflow: hidden;
  }

  /* Slider Images */
.left-icon img {
  width: 35%; /* Set the desired width */
  height: auto; /* Set the desired height */
  margin: 5%;
  margin-top: 7%;
}

.right-icon img {
  width: 35%; /* Set the desired width */
  height: auto; /* Set the desired height */
  position: absolute;
  right: 0;
  top:0;
  margin-top: 2%;
  margin-right:4%
  
}
  .slider:before {
    position: absolute;
    content: "";
    height: 130%;
    width: 60%;
    background-color: #272F51;
    border-radius: 200%;
    transition: 0.4s;
  }
   
  input:checked + .slider:before {
    transform: translateX(2.7vw);
  }

  .assetView-container {
    height: 33vw;
    margin-top: 0.1vw;
    border-radius: 25px;
    background-color: white;
    box-shadow: 0 8px 10px rgba(0, 0, 0, 0.3);
    display: flex;
    flex-direction: column; /* Set flex-direction to column */
    position: relative; /* Add relative positioning to the container */
  }
</style>