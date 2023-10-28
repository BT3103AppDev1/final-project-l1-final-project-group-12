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

      <!-- Table / PieChart  -->
      <PortfolioTable
        v-if="!isChecked"
        :SuggestedQty="SuggestedQty"
        :key="refreshComp"
        :portfolioData="portfolioData"
        :hasData="hasData"
        @refresh-request="fetchData"
        @total-pl-updated="emitTotalPL"
      />

      <PieChart
        v-else
        :SuggestedQty="SuggestedQty"
        :portfolioData="portfolioData"
        :hasData="hasData"
        @refresh-request="fetchData"
      />

     
    </template>
  
  
  <script>
  import { extractData } from '@/firebasefunc.js'
  import { COLLECTION_NAMES } from '@/firebaseConfig.js';
  import firebaseApp from '@/firebase.js'
  import { getAuth, onAuthStateChanged } from 'firebase/auth'

  import PortfolioTable from '@/components/Portfolio/PortfolioTable.vue'
  import PieChart from '@/components/Portfolio/PortfolioPieChart.vue'

  export default {
    name: 'PortfolioAssetView',
    components: {
      PortfolioTable,
      PieChart
    },

    props: {
      selectedTabIndex: Number,
      sliderValue: Number,
    },

    data() {
      return {
        isChecked: false,
        refreshComp: 0,
        portfolioData: [],
        hasData: true,

        userID: '',
      };
    },

    async created() {
      const auth = getAuth()
      onAuthStateChanged(auth, (user) => {
        if (user) {
          this.userID = user.uid;
          this.fetchData()
        } else {
          console.error('User not authenticated')
        }
      })
    },


    methods: {
      
      toggleSwitch() {
        this.isChecked = !this.isChecked;
      },

      async fetchData() {
          try {
            this.portfolioData = await extractData(COLLECTION_NAMES.EQUITY_PORTFOLIO, this.userID);
            this.hasData = this.portfolioData.length > 0;

          } catch (error) {
            console.error("Error fetching data:", error);
          }
      }, 

      SuggestedQty(qty, stock) {            //TODO: PUT OPTIMIZED QTY HERE
          if (this.selectedTabIndex == 1) {
            return parseFloat(qty) * this.selectedTabIndex;

          } else if (this.selectedTabIndex == 2) {
            return {};
          
          } else if (this.selectedTabIndex == 3) {
            return {};

          } else if (this.selectedTabIndex == 4) {
            return {};

          } else {
            console.log(this.sliderValue)

            return {};

          }
      },

      emitTotalPL(totalPL) {
        this.$emit('total-pl-updated', totalPL);
      },

    },
    emits: ["total-pl-updated"],



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

</style>