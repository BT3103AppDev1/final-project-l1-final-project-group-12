<template>
    <div class="app-container">

        <div class="title-button-container">
            <span>{{ portfolioTitle }}</span>
        
            <button @click="toggleStatistics" id="portfolioButton">{{ buttonLabel }}</button>
        </div>

        <!-- Optimisation Tabs  -->
        <div class="Optimisation-container">
          <OptimisationTab @update-selected-tab-index="updateSelectedTabIndex" @slider-value-updated="handleSliderValue"/>
        </div>


    <!-- Asset View & Add Trade  -->
    <div v-if="!showStatistics" class="portfolioDisplay">
        <div class="table">
            <PortfolioAssetView :selectedTabIndex="selectedTabIndex" :sliderValue="sliderValue" :key="refreshComp"/>
        </div>
        <div class="addTrade">
            <AddTrade :key="refreshComp" @added = "change"/>
        </div>
    </div>

    <!-- Statistic Table  -->
    <div v-else class="right-icon">
        <PortfolioStatistics />
        
    </div>

  </div>

</template>
  

<script>
  import PortfolioAssetView from '@/components/Portfolio/PortfolioAssetView.vue'
  import AddTrade from '@/components/Portfolio/AddTrade.vue'
  import PortfolioStatistics from '@/components/Portfolio/PortfolioStatistics.vue'
  import OptimisationTab from '@/components/Portfolio/OptimisationTab.vue'

  
  export default {
    name: 'App',
    components: {
        PortfolioAssetView,
        AddTrade,
        PortfolioStatistics,
        OptimisationTab,
    },

    data() {
      return {
        isChecked: false,
        refreshComp: 0,
        showStatistics: false,
        selectedTabIndex: 1,
        sliderValue: 0,
      };
    },

    computed: {
      buttonLabel() {
        return this.showStatistics ? 'Back to Portfolio' : 'View Portfolio Statistics';
      },

      portfolioTitle() {
        return this.showStatistics ? 'Portfolio Statistics' : 'My Portfolio';
      },
    },

    methods: {
      change() {
        this.refreshComp += 1
      },

      updateSelectedTabIndex(index) {
      this.selectedTabIndex = index; // Update selectedTabIndex in the parent component
      this.change()
    },
          
      toggleStatistics() {
        this.showStatistics = !this.showStatistics;
        },

      handleSliderValue(sliderValue) {
        this.sliderValue = sliderValue;
        console.log('Slider value received:', sliderValue);
      },
    },

    emits: ['slider-value-updated'],
    
  };
    

  </script>
  


  <style>
  .app-container {
    padding: 1.6vw;
    margin-top: 1.3%;
  }
  
  .title-button-container {
      display: flex;
      margin-left: 2%;
      font-size: 3vw;
      font-weight: bold;
  }
  
  /* Statistic Button */
  #portfolioButton {
      width: 27%;
      justify-content: flex-end;
      margin-left: auto;
      margin-bottom: 1.5vw; 
      height: 3vw; 
      background-color: #272F51; 
      color: white; 
      border: none;
      border-radius: 15px; 
      box-shadow: 0 7px 7px rgba(0, 0, 0, 0.3);
      font-size: 1.6vw; 
      font-weight: 700;
      cursor: pointer;
  }
  
  #portfolioButton:hover {
    background-color: #475281; /* Change the button color on hover */
  }
  
  /* Optimisation Tab */
  .Optimisation-container {
      display: flex;
      width: 72%;
      justify-content: space-between; /* Spread buttons evenly */
      margin-top: 0vw;
    }

    /* Portfolio Display */
    .portfolioDisplay {
        display: flex;
        align-items: flex-start;
      }
      
      .table {
        width: 72%;
      }
      
      .addTrade {
        width: 26%;
        margin-left: auto;
      }
  </style>