<template>

  <div class="statistics-table">
      
    <!-- Content -->
    <div class="statistics-content">
      <div class="column" v-for="(column, columnIndex) in columns" :key="columnIndex">
        <div class="row" v-for="(row, rowIndex) in column" :key="rowIndex">
          <div class="cell">{{ row.label }}</div>
          <div class="cell">{{ parseFloat(statisticsData[row.header]).toFixed(2) }} {{ row.symbol }}</div>
        </div>
      </div>
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
      selectedButton: '1Y',
      buttons: ['1Y', '6M', '7D'],   
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

  async created() {
    const auth = getAuth()
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.useremail = user.email;
        this.fetchStatistics();

      } else {
        console.error('User not authenticated')
      }
    })
  },

  methods: {

    async fetchStatistics() {
        try {
          const apiUrl = `http://localhost:3000/api/read/portfolioInfo/${this.useremail}`;
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
