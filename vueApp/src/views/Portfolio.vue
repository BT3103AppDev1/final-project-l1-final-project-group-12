<template>
    <div class="app-container">

        <div class="title-button-container">
            <span>{{ portfolioTitle }}</span>
        
            <button @click="toggleStatistics" id="portfolioButton">{{ buttonLabel }}</button>
        </div>

        <!-- Optimisation Tabs  -->
        <div class="Optimisation-container">
        <button
            v-for="(tab, index) in buttons"
            :key="index"
            :class="{ 'selected-Optimisation-tab': tab === selectedButton }"
            @click="selectButton(index)"
            class="Optimisation-tab"
            >
            <span class="Optimisation-tab-line">{{ tab.split(' ')[0] }}</span>
            <span class="Optimisation-tab-line">{{ tab.split(' ')[1] }}</span>
        </button>

    </div>

    <!-- Pop-up Window for the Customize Risk Button -->
    <div v-if="showOptimisationSlider" class="right-icon">
      <OptimisationSlider :showPopup="showOptimisationSlider" @closePopup="showOptimisationSlider = false" />
    </div>

    <!-- Asset View & Add Trade  -->
    <div v-if="!showStatistics" class="portfolioDisplay">
        <div class="table">
            <PortfolioAssetView :selectedTabIndex="selectedTabIndex" :key="refreshComp"/>
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
  import OptimisationSlider from '@/components/Portfolio/OptimisationSliderPopup.vue'

  const TABS = [
  "Current Portfolio",
  "Maximize Returns",
  "Minimize Risk",
  "Balance Portfolio",
  "Customize Risk",
  ];
  
  export default {
    name: 'App',
    components: {
        PortfolioAssetView,
        AddTrade,
        PortfolioStatistics,
        OptimisationSlider,
    },

    data() {
      return {
        isChecked: false,
        refreshComp: 0,
        buttons: TABS,
        selectedButton: TABS[0],
        selectedTabIndex: 1,
        showStatistics: false,
        showOptimisationSlider: false,
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

      selectButton(index) {
        this.selectedButton = this.buttons[index];
        this.refreshComp += 1
        this.selectedTabIndex = index + 1;
        
        if (index === 4) {
          this.showOptimisationSlider = true;
          
        } else {
          this.showOptimisationSlider = false;
          
        }
          
      },

      toggleStatistics() {
      this.showStatistics = !this.showStatistics;
        },

    },

  }
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
    .Optimisation-tab {
      flex: 1; 
      background-color: #cdcdd0;
      color: white;
      margin: 1vw 0.5vw;
      padding: 0.8vw 0; 
      border: 1vw;
      border-radius: 1.2vw;
      cursor: pointer;
      font-size: 1.6vw;
      font-weight: bold;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    
    .Optimisation-tab-line {
      line-height: 1; /* Adjust line-height to control spacing between lines */
    }
    
    button.selected-Optimisation-tab {
      background-color: #bde4fa;
      color: #4e5ea4;
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