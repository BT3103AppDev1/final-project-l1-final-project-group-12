<template>
  <div class="statistics-table">
    <div v-if="getOptimizedStatus || !hasData">
      <!-- Content -->
      <div class="statistics-content">
        <div
          class="column"
          v-for="(column, columnIndex) in columns"
          :key="columnIndex"
        >
          <div class="row" v-for="(row, rowIndex) in column" :key="rowIndex">
            <div class="cell">
              
                <span>{{ row.label }}</span>
                <button class="infoBtw">
                  <img src="@/assets/infoIcon.png" alt="Button Image" />
                  <span class="tooltiptext"> {{ row.info }}</span>
                </button>
            </div>

            <div class="cell" v-if="!hasData">0</div>
            <div
              class="cell"
              v-else-if="isNaN(statisticsData[row.header]) || isStatisticsOptimizing">
              Loading..
            </div>
            <div class="cell" v-else>
              {{ parseFloat(statisticsData[row.header]).toFixed(2) }}
              {{ row.symbol }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="optimising-item" v-else>Optimising...</div>
  </div>
</template>

<script>
import { getAuth, onAuthStateChanged } from "firebase/auth";
import axios from "axios";

export default {
  data() {
    return {
      fetching: true,
      useremail: "",
      columns: [
        [
          { label: "Expected Alpha", header: "alpha", symbol: "", info: "Measures return on investment above whats's expected based on risk" },
          { label: "Overall Beta", header: "beta", symbol: "", info: "Volatility relative to benchmark"},
          { label: "Market Return", header: "marketReturn", symbol: "%" , info: "Gain or loss realized by your portfolio, attributed to overall market performance"},
          { label: "Portfolio Return", header: "portfolioReturn", symbol: "%" , info: "Gain or loss realized by your portfolio"},
        ],

        [
          { label: "Portfolio Value", header: "portfolioValue", symbol: "" , info: "Current worth of your investment portfolio"},
          { label: "Risk-Free Rate", header: "rfRate", symbol: "%" , info: "Return on an investment with zero risk of financial loss"},
          { label: "Sharpe Ratio", header: "sharpeRatio", symbol: "" , info: "Risk-adjusted performance of an investment portfolio, evaluating its return in relation to its level of risk"},
          { label: "Std Deviation", header: "stdDev", symbol: "" , info: "Measures deviation from the mean of returns to assess the volatility and risk associated with a portfolio's returns"},
        ],
        [{ label: "Variance", header: "variance", symbol: "" , info: "Degree of the variability of returns in a portfolio, providing insight into the overall risk and stability of the investment"}],
      ],
    };
  },

  props: {
    objective: String,
    optimizingStatus: Boolean,
    hasData: Boolean,
    updateOptimisePortfolio: Function,
    getOptimizedStatus: Boolean,
    isStatisticsOptimizing: Boolean,
    statisticsData: Object,
    updateStatistics: Function,
  },

  async created() {
    const auth = getAuth();
    onAuthStateChanged(auth, async (user) => {
      if (user) {
        this.useremail = user.email;
        const objective = this.objective;
        await this.fetchStatistics(objective);

        const watchCallback = async () => {
          const newObjective = this.objective;
          if (!this.getOptimizedStatus && !this.optimizingStatus && this.hasData) {
            await this.updateOptimisePortfolio(newObjective);
          }
          await this.fetchStatistics(newObjective);
        };

        this.$watch("objective", watchCallback);
      } else {
        console.error("User not authenticated");
      }
    });
  },

  methods: {
    async fetchStatistics(obj) {
      console.log("Fetching Statistics: ", obj);
      let apiUrl;
      try {
        if (obj) {
          apiUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/read/portfolioInfo/${this.useremail}/${obj}`;
        } else {
          apiUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/read/portfolioInfo/${this.useremail}/""`;
        }

        const querySnapshot = await axios.get(apiUrl);
        this.updateStatistics(obj, querySnapshot.data);
        console.log("Updated Statistics - ",obj, querySnapshot.data)


      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },

  },
};
</script>


<style scope>
.statistics-table {
  height: 33vw;
  border-radius: 25px;
  background-color: white;
  box-shadow: 0 8px 10px rgba(0, 0, 0, 0.3);

  /* Content */
}
.statistics-content {
  display: flex;
  font-weight: bold;
  font-size: 120%;
  margin-top: 1%;

  padding-top: 2%;
}

.column {
  flex: 1;
}

.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  text-align: center;
}

.cell {
  padding-top: 30%;

  border-right: 1px solid #ccc; /* Add right border */
}

.row .cell:last-child {
  border-right: none;
}

.optimising-item {
  height: 33vw;
  margin-top: 0.1vw;
  border-radius: 25px;
  background-color: white;
  box-shadow: 0 8px 10px rgba(0, 0, 0, 0.3);
  display: flex;
  flex-direction: column; /* Set flex-direction to column */
  position: relative; /* Add relative positioning to the container */
  text-align: center;
  justify-content: center;
  font-size: 2vw;
  color: rgb(101, 100, 100);
}

/* info button */
.cell .infoBtw {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: inline;
  margin: 0;
  transition: none;
}

.cell .infoBtw img {
  max-width: 6vh;
  max-height: auto;
  position: static; /* or position: relative; */
  padding:0;
}

.cell .tooltiptext {
  visibility: hidden;
  width: 500%;
  background-color: #e6e6e6;
  color: #454444;
  text-align: left;
  border-radius: 1vh;
  padding: 10% 15%;

  /* Position the tooltip */
  position: absolute;
  z-index: 1;
}

.infoBtw:hover .tooltiptext {
  visibility: visible;
}

.cell .infoBtw:hover {
  box-shadow: none !important;
  transform: translateY(0) !important;
}


</style>
