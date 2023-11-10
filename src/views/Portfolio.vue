<template>
  <div>
    <NavBar />

    <div class="app-container">
      <div class="title-button-container">
        <span>{{ portfolioTitle }}</span>

        <button @click="toggleStatistics" id="portfolioButton">
          {{ buttonLabel }}
        </button>
      </div>

      <!-- Optimisation Tabs  -->
      <div class="Optimisation-container">
        <OptimisationTab @update-selected-tab-index="getObjective" />
      </div>

      <!-- Asset View & Add Trade  -->
      <div v-if="!showStatistics" class="portfolioDisplay">
        <div class="table">
          <PortfolioAssetView
            :objective="objective"
            ref="PortfolioAssetView"
            :status="getStatus()"
            :getOptimizedStatus="getOptimizedStatus()"
            :updateOptimisePortfolio="updateOptimisePortfolio"
            :portfolioData="getPortfolioData()"
            :stockPrices="getStockPrices()"
            :updatePortfolioData="updatePortfolioData"
            :updateStockPrices="updateStockPrice"
            @total-pl-updated="emitTotalPL"
            @refresh-request="change"
            @has-data="updateHasData"
          />
        </div>
        <div class="addTrade">
          <AddTrade :totalPL="totalPL" ref="AddTrade" @added="added" />
        </div>
      </div>

      <!-- Statistic Table  -->
      <div v-else class="right-icon">
        <PortfolioStatistics
          ref="PortfolioStatistics"
          :objective="objective"
          :optimizingStatus="getStatus()"
          :isStatisticsOptimizing="updatingStatistics"
          :getOptimizedStatus="getOptimizedStatus()"
          :updateOptimisePortfolio="updateOptimisePortfolio"
          :hasData="hasData"
          :statisticsData="getStatistics()"
          :updateStatistics="updateStatistics"
        />
      </div>
    </div>

    <Loading ref="Loading" />
  </div>
</template>
  

<script>
import PortfolioAssetView from "@/components/Portfolio/PortfolioAssetView.vue";
import AddTrade from "@/components/Portfolio/AddTrade.vue";
import PortfolioStatistics from "@/components/Portfolio/PortfolioStatistics.vue";
import OptimisationTab from "@/components/Portfolio/OptimisationTab.vue";
import Loading from "@/components/Loading.vue";
import NavBar from "@/components/Navigation.vue";

import { getAuth, onAuthStateChanged } from "firebase/auth";
import axios from "axios";

export default {
  name: "App",
  components: {
    PortfolioAssetView,
    AddTrade,
    PortfolioStatistics,
    OptimisationTab,
    NavBar,
    Loading,
  },

  data() {
    return {
      isChecked: false,
      showStatistics: false,
      totalPL: 0,
      objective: "",

      isAlphaOptimizing: false,
      isBetaOptimizing: false,
      isBalanceOptimizing: false,
      updatingStatistics: false,

      alphaOptimized: false,
      betaOptimized: false,
      balanceOptimized: false,

      hasData: false,

      portfolioData: {"":[], "alpha":[], "beta":[], "balance":[]},
      stockPrices: {},
      statistics: {"":[], "alpha":[], "beta":[], "balance":[]},

      useremail: "",
      existingPortfolio: null,
    };
  },

  async mounted() {
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.useremail = user.email;
        this.checkAndCreatePortfolio();

      } else {
        this.useremail = ""; // Ensure it's cleared when the user signs out
      }
    });
  },

  computed: {
    buttonLabel() {
      return this.showStatistics
        ? "Back to Portfolio"
        : "View Portfolio Statistics";
    },

    portfolioTitle() {
      return this.showStatistics ? "Portfolio Statistics" : "My Portfolio";
    },
  },

  methods: {
    added() {
      this.change(true);
      const addedStock = this.$refs.AddTrade.stockPrice;
      this.stockPrices[addedStock[0]] = addedStock[1];
    },

    // Called when stock added, deleted or edited
    async change(hasData) {
      this.alphaOptimized = false;
      this.betaOptimized = false;
      this.balanceOptimized = false;
      const obj = this.objective;

      await Promise.all([
        this.$refs.PortfolioAssetView.fetchData(obj),
        //portfolioAssetView.getStockPrice(),
      ]);

      if (hasData) {
        this.updatingStatistics = true;
        await this.updateStatistics();

        if (obj != "") {
          await this.updateOptimisePortfolio(obj);
          await this.$refs.PortfolioAssetView.fetchData(obj);
          await this.$refs.PortfolioStatistics.fetchStatistics(obj);
        }
      }
    },

    async checkAndCreatePortfolio() {
      this.$refs.Loading.onLoading();

      const apiReadPortfolioUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/read/portfolioInfo/${this.useremail}/standard`;
      const apiCreatePortfolioUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/update/createPortfolio/${this.useremail}`;
      if (this.existingPortfolio) {
        console.log(
          "Using cached portfolio data:",
          this.existingPortfolio.data
        );
      } else {
        try {
          this.existingPortfolio = await axios.get(apiReadPortfolioUrl);
          console.log("Current Portfolio: ", this.existingPortfolio.data);
          
        } catch (error) {
          console.log("No Portfolio found");
        }
      }

      if (!this.existingPortfolio) {
        // Check if the portfolio doesn't exist
        try {
          console.log("Creating Portfolio..");
          await axios.post(apiCreatePortfolioUrl);
          this.updateOptimisePortfolio("");
        } catch (error) {
          alert("Error: " + error.response.data);
        }
      }

      this.$refs.Loading.offLoading();
    },

    //Update functions
    async updateStatistics() {
      console.log("Updating Portfolio");
      try {
        const apiUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/update/updatePortfolio/${this.useremail}`;
        await axios.put(apiUrl);
        this.updatingStatistics = false;
        console.log("Portfolio Update complete!");
      } catch (error) {
        console.error("Error Updated Portfolio:", error);
      }
    },

    async updateOptimisePortfolio(objective) {
      console.log("Updating Optimised Portfolio..");

      try {
        if (objective == "alpha") {
          this.isAlphaOptimizing = true;

          const apiAlphaUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/optimise/${this.useremail}/alpha`;
          await axios.post(apiAlphaUrl);
          this.isAlphaOptimizing = false;
          this.alphaOptimized = true;
        } else if (objective == "beta") {
          this.isBetaOptimizing = true;

          const apiBetaUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/optimise/${this.useremail}/beta`;
          await axios.post(apiBetaUrl);
          this.isBetaOptimizing = false;
          this.betaOptimized = true;
        } else if (objective == "balance") {
          this.isBalanceOptimizing = true;

          const apiBalanceUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/optimise/${this.useremail}/balance`;
          await axios.post(apiBalanceUrl);
          this.isBalanceOptimizing = false;
          this.balanceOptimized = true;
        }
      } catch (error) {
        console.error("Error Updated Optimised Portfolio:", error);
        this.updateOptimisePortfolio(objective);
      }

      console.log("Portfolio Optimised!");
    },

    updateHasData(newHasData) {
      this.hasData = newHasData;
    },

    updatePortfolioData(objective, newPortfolioData) {
      this.portfolioData[objective] = newPortfolioData;
      console.log(objective, newPortfolioData)

    },

    updateStockPrice(stock,newStockPrice) {
      this.stockPrices[stock] = newStockPrice;
    },

    updateStatistics(objective, newStatistics) {
      this.statistics[objective] = newStatistics;
      console.log(objective, newStatistics)
    },



    // Get functions
    getStatus() {
      if (this.objective == "alpha") {
        return this.isAlphaOptimizing;
      } else if (this.objective == "beta") {
        return this.isBetaOptimizing;
      } else if (this.objective == "balance") {
        return this.isBalanceOptimizing;
      } else {
        return false;
      }
    },

    getOptimizedStatus() {
      if (this.objective == "alpha") {
        return this.alphaOptimized;
      } else if (this.objective == "beta") {
        return this.betaOptimized;
      } else if (this.objective == "balance") {
        return this.balanceOptimized;
      } else {
        return true;
      }
    },

    getPortfolioData() {
      return this.portfolioData[this.objective];
    },

    getStockPrices() {
      return this.stockPrices;
    },

    getStatistics() {
      return this.statistics[this.objective];
    },

    toggleStatistics() {
      this.showStatistics = !this.showStatistics;
    },

    emitTotalPL(totalPL) {
      this.totalPL = totalPL;
      this.$emit("total-pl-updated", totalPL);
    },


    getObjective(index) {
      if (index == 1) {
        this.objective = "";
      } else if (index == 2) {
        this.objective = "alpha";
      } else if (index == 3) {
        this.objective = "beta";
      } else {
        this.objective = "balance";
      }
    },
  },

  emits: ["total-pl-updated", "refresh-request"],
};
</script>
  


  <style scoped>
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
  background-color: #272f51;
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