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
      <component
        :is="isChecked ? 'PieChart' : 'PortfolioTable'"
        :SuggestedQty="SuggestedQty"
        :key="refreshComp"
        :portfolioData="portfolioData"
        :hasData="hasData"
        @refresh-request="fetchData"
      />
    </template>
  
  
  <script>
  import '@/style/Portfolio/PortfolioAssetView.css'
  import { extractData } from '@/firebasefunc.js'

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
    },

    data() {
      return {
        isChecked: false,
        refreshComp: 0,
        portfolioData: [],
        hasData: true,
      };
    },

    created() {
      this.fetchData(); // Fetch data when the component is created
    },

    computed: {
      
    },

    methods: {
      
      toggleSwitch() {
        this.isChecked = !this.isChecked;
      },

      async fetchData() {
          try {
            this.portfolioData = await extractData();
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

          } else {
            return {};

          }
      }

    },



  };
  </script>
  
  