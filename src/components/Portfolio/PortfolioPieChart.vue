<template>
  <div class="pie-chart-container">
    
    <!-- Conditionally render the chart or grey circle -->
    <div v-if="hasData">
      <div id="chart-container" class="center">
        <apexchart ref="chart" 
          type="pie" 
          width="600" 
          :options="chartOptions" 
          :series="series"></apexchart>
      </div>
    </div>
    
    <!-- No Data -->
    <div v-else class="emptyPieChart">  </div>
    <p v-if="!hasData" class="message">
      You have not added any trades to your portfolio. To gain portfolio insights, please add your open trades.
    </p>

  </div>
</template>

  

<script scope>
import VueApexCharts from 'vue3-apexcharts';

export default {
  props: {
    portfolioData: Array,
    hasData: Boolean,
  },

  components: {
    apexchart: VueApexCharts,
  },
  
  data() {
    return {
      series: [],
      chartOptions: {
        chart: {
          width: 380,
          type: 'pie',
        },
        labels: [],
        tooltip: {
          y: {
            formatter: function (value) {
              return `$${value.toLocaleString()}`;
            },
          },
        },
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200,
              },
              legend: {
                position: 'bottom',
              },
            },
          },
        ],
      },
    };
  },

  async created() {
    await this.initializeChartData();
  },

  watch: {
    portfolioData: 'initializeChartData',
  },

  methods: {
    async initializeChartData() {
      this.series = [];
      this.chartOptions.labels = [];
      
      this.portfolioData.forEach((item) => {
        const stock = item.name;
        const value = parseFloat(item.buyPrice * item.buyQty);
        this.series.push(value);
        this.chartOptions.labels.push(stock);
      });
    },

  
  },

  }
</script>





<style scope>
.pie-chart-container {
  height: 33vw;
  margin-top: 0.1vw;
  padding-left: 13vw;
  padding-right: 13vw;
  border-radius: 25px;
  background-color: white;
  box-shadow: 0 8px 10px rgba(0, 0, 0, 0.3);
  display: flex;
  flex-direction: column; /* Set flex-direction to column */
  justify-content: flex-start; /* Align items at the top of the container */
  align-items: center;
  position: relative; /* Add relative positioning to the container */
}

#chart-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Circular element styles */
.emptyPieChart {
  width: 23vw;
  height: 23vw;
  background-color: #dddcdc;
  border-radius: 50%;
  margin: auto;
  position: absolute;
  top: 2vh;
  left: 0;
  right: 0;
}

.message {
  text-align: center;
  margin-top: 60%; /* Use percentage for responsiveness */
  font-size: 1.6vw;
  font-weight: bold;
  color: #BFBFBF;
  max-width: 100% !important;
}
</style>
  
  
  
  