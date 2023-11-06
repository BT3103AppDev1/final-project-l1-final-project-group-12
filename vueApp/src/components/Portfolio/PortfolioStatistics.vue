<template>

  <div class="statistics-table">
    <div v-if="!optimizingStatus">    
    <!-- Content -->
    <div class="statistics-content">
      <div class="column" v-for="(column, columnIndex) in columns" :key="columnIndex">
        <div class="row" v-for="(row, rowIndex) in column" :key="rowIndex">
          <div class="cell">{{ row.label }}</div>

          <div class="cell" v-if="!hasData">0</div>
          <div class="cell" v-else-if="isNaN(statisticsData[row.header] && !isStatisticsOptimizing)">Loading..</div>
          <div class="cell" v-else>{{ parseFloat(statisticsData[row.header]).toFixed(2) }} {{ row.symbol }}</div>
        </div>
      </div>
    </div>
  </div>

  <div v-else>
      Optimising...
  </div>

  </div>
  

</template>

<script>
import { getAuth, onAuthStateChanged } from 'firebase/auth'
import axios from 'axios';

export default {
  data() {
    return {
      fetching: true,
      useremail: '', 
      columns: [
        [
          { label: 'Expected Alpha',  header: 'alpha', symbol: ''},
          { label: "Overall Beta",  header: 'beta', symbol: ''},
          { label: 'Market Return' ,  header: 'marketReturn', symbol: '%'},
          { label: 'Portfolio Return' ,  header: 'portfolioReturn', symbol: '%'},
        ],

        [
          { label: 'Portfolio Value' ,  header: 'portfolioValue', symbol: ''},
          { label: 'Risk-Free Rate' ,  header: 'rfRate', symbol: '%'},
          { label: 'Sharpe Ratio' ,  header: 'sharpeRatio', symbol: ''},
          { label: 'Std Deviation' ,  header: 'stdDev', symbol: ''},
        ],
        [
          { label: 'Variance' ,  header: 'variance', symbol: ''},
        ],
      ],
      statisticsData: {},
      test: {},
    };
  },

  props: {
      objective: String,
      optimizingStatus: Boolean,
      hasData: Boolean,
      updateOptimisePortfolio: Function,
      getOptimizedStatus: Boolean,
      isStatisticsOptimizing: Boolean,
    },

    async created() {
      const auth = getAuth();
      onAuthStateChanged(auth, async (user) => {
        if (user) {
          this.useremail = user.email;
          await this.fetchStatistics();

          const watchCallback = async () => {
            if (!this.getOptimizedStatus && this.hasData){
              console.log(this.optimizingStatus)
              await this.updateOptimisePortfolio(this.objective);
              console.log(this.optimizingStatus)
            }
            await this.fetchStatistics(); 
          };

          this.$watch('objective', watchCallback);

        } else {
          console.error('User not authenticated');
        }
      });
    },

  methods: {

    async fetchStatistics() {
      console.log("Fetching Statistics: ", this.objective)
      let apiUrl;
        try {
          if (this.objective) {
            apiUrl = `http://localhost:3000/api/read/portfolioInfo/${this.useremail}/${this.objective}`;
          } else {
            apiUrl = `http://localhost:3000/api/read/portfolioInfo/${this.useremail}/""`;
          }

          const querySnapshot = await axios.get(apiUrl);
          this.statisticsData = querySnapshot.data;

        } catch (error) {
          console.error("Error fetching data:", error);
        }
    }, 

    

  },
};
</script>


<style>
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
  font-size:120%;
  margin-top:1%;
  
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

</style>
