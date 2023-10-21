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
  import '@/style/Portfolio/Portfolio.css'
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
  