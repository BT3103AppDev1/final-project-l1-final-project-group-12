<template>

  <div class="statistics-table">
      
      <!-- Button -->
      <div class="time-view-button">
      <button
        v-for="button in buttons"
        :key="button"
        class="top-button"
        :class="{ active: selectedButton === button }"
        @click="selectButton(button)"
      >
        {{ button }}
      </button>
    </div>

    <!-- Content -->
    <div class="statistics-content">
      <div class="column" v-for="(column, columnIndex) in columns" :key="columnIndex">
        <div class="row" v-for="(row, rowIndex) in column" :key="rowIndex">
          <div class="cell">{{ row.label }}</div>
          <div class="cell">{{ statisticsData[row.header] }}</div>
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
      useremail: '',
      selectedButton: '1Y',
      buttons: ['1Y', '6M', '7D'],   
      columns: [
        [
          { label: 'Expected Alpha',  header: 'alpha'},
          { label: "Overall Beta",  header: 'beta'},
          { label: 'Market Return' ,  header: 'marketReturn'},
          { label: 'Portfolio Return' ,  header: 'portfolioReturn'},
        ],

        [
          { label: 'Portfolio Value' ,  header: 'portfolioValue'},
          { label: 'Risk-Free Rate' ,  header: 'rfRate'},
          { label: 'Sharpe Ratio' ,  header: 'sharpeRatio'},
          { label: 'Std Deviation' ,  header: 'stdDev'},
        ],
        [
          { label: 'Variance' ,  header: 'variance'},
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
        this.updateStatistics()
      } else {
        console.error('User not authenticated')
      }
    })
  },

  methods: {
    selectButton(button) {
      this.selectedButton = button;
    },

    async fetchStatistics() {
        try {
          const apiUrl = `http://localhost:3000/api/read/portfolioInfo/${this.useremail}`;
          const querySnapshot = await axios.get(apiUrl);
          this.statisticsData = querySnapshot.data;

        } catch (error) {
          console.error("Error fetching data:", error);
        }
    }, 

    async updateStatistics() {
        try {
          const apiUrl = `http://localhost:3000/api/update/updatePortfolio/${this.useremail}`;
          console.log(apiUrl)
          const querySnapshot = await axios.put(apiUrl);
       //   this.test = querySnapshot.data;
        //  console.log(this.test);

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
  padding-top: 20%;

  border-right: 1px solid #ccc; /* Add right border */
}

.row .cell:last-child {
  border-right: none;
}

/* button */
.time-view-button {
padding-left: 2%;
padding-top: 2%;
}

.top-button {
background-color: #D9D9D9;
color: black;
font-weight:bold;
font-size: 100%;
border: none;
border-radius: 2vh;
padding: 1% 1%;
margin-right: 0.5%;
cursor: pointer;
}

.top-button.active {
background-color: #272F51; /* Change to the desired color when clicked */
color: white;
}

/* Add a hover animation */
.top-button:hover {
background-color: #A5A5A5; /* Change to the desired hover color */
transition: background-color 0.3s;
}
</style>
