<template>
  <div>
    <NavBar />

    <div class="app-container">

        <div class="title-button-container">
            <span>{{ portfolioTitle }}</span>

            <button @click="toggleStatistics" id="portfolioButton">{{ buttonLabel }}</button>
        </div>

        <!-- Optimisation Tabs  -->
        <div class="Optimisation-container">
          <OptimisationTab 
            @update-selected-tab-index="updateSelectedTabIndex" 
          />
        </div>


    <!-- Asset View & Add Trade  -->
    <div v-if="!showStatistics" class="portfolioDisplay">
        <div class="table">
            <PortfolioAssetView 
              :selectedTabIndex="selectedTabIndex"  
              :key="refreshComp" 
              @total-pl-updated = "emitTotalPL"
              @refresh-request = "updateStatistics"
              />
              
        </div>
        <div class="addTrade">
            <AddTrade 
              :key="refreshComp" 
              :totalPL = "totalPL"
              @added = "change"/>
        </div>
    </div>

    <!-- Statistic Table  -->
    <div v-else class="right-icon">
        <PortfolioStatistics 
          :key="refreshComp"/>
        
    </div>

  </div>
</div>
</template>
  

<script>
  import PortfolioAssetView from '@/components/Portfolio/PortfolioAssetView.vue'
  import AddTrade from '@/components/Portfolio/AddTrade.vue'
  import PortfolioStatistics from '@/components/Portfolio/PortfolioStatistics.vue'
  import OptimisationTab from '@/components/Portfolio/OptimisationTab.vue'
  import NavBar from '@/components/NavBar.vue'

  import { getAuth, onAuthStateChanged } from 'firebase/auth'
  import axios from 'axios';

  export default {
    name: 'App',
    components: {
        PortfolioAssetView,
        AddTrade,
        PortfolioStatistics,
        OptimisationTab,
        NavBar,
    },

    data() {
      return {
        isChecked: false,
        refreshComp: 0,
        showStatistics: false,
        selectedTabIndex: 1,
        totalPL: 0,

        useremail: '',
      };
    },

    async mounted() {
        const auth = getAuth();
        onAuthStateChanged(auth, (user) => {
            if (user) {
                this.useremail = user.email;
                this.checkAndCreatePortfolio();
            } else {
                this.useremail = ''; // Ensure it's cleared when the user signs out
            }
        });
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
        this.updateStatistics();
      },

      updateSelectedTabIndex(index) {
      this.selectedTabIndex = index; // Update selectedTabIndex in the parent component
      this.change()
    },
          
      toggleStatistics() {
        this.showStatistics = !this.showStatistics;
        },


      emitTotalPL(totalPL) {
        this.totalPL = totalPL;
        this.$emit('total-pl-updated', totalPL);
      },

      async checkAndCreatePortfolio() {
        const apiReadPortfolioUrl = `http://localhost:3000/api/read/portfolioInfo/${this.useremail}`;
        const apiCreatePortfolioUrl = `http://localhost:3000/api/update/createPortfolio/${this.useremail}`;
        let existingPortfolio = null;
        try {
            existingPortfolio = await axios.get(apiReadPortfolioUrl);

          } catch (error) {
            console.error('Error during GET request:', error);
          }

          if (!existingPortfolio) { // Check if the portfolio doesn't exist
            try {
              await axios.post(apiCreatePortfolioUrl);
               
            } catch (error) {
              alert('Error: ' + error.response.data);
            }
          } 
      },

      async SuggestedQty() {            //TODO: PUT OPTIMIZED QTY HERE
        console.log(apiURL)
        let objective = "";

        if (this.selectedTabIndex == 2) {
          objective = "alpha";
        
        } else if (this.selectedTabIndex == 3) {
          objective = "beta";

        } else{
          objective = "balance";
        }
        const apiUrl = `http://localhost:3000/api/optimise/${this.useremail}/${objective}`;
        
        const response = await axios.post(apiUrl);
        console.log(response)
          
      },

      async updateStatistics() {
        try {
          const apiUrl = `http://localhost:3000/api/update/updatePortfolio/${this.useremail}`;
          console.log(apiUrl)
          await axios.put(apiUrl);
          

        } catch (error) {
          console.error("Error fetching data:", error);
        }
    }, 

    },

    emits: ["total-pl-updated"],

    
    
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