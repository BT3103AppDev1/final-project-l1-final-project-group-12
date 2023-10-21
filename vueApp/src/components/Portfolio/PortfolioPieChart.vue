<template>
  <div class="pie-chart-container">
    
    <!-- Conditionally render the chart or grey circle -->
    <div v-if="hasData">
      <div id="chart-container" class="center">
        <apexchart ref="chart" type="pie" width="550" :options="chartOptions" :series="series"></apexchart>
      </div>
    </div>
    <div v-else class="emptyPieChart">  </div>
    <p v-if="!hasData" class="message">You have not added any trades to your portfolio. To gain portfolio insights, please add your open trades.</p>
  </div>
</template>

  

<script>
import '@/style/Portfolio/PortfolioPieChart.css'

import VueApexCharts from 'vue3-apexcharts';

export default {
  props: {
    SuggestedQty: Function,
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

  created() {
    this.initializeChartData();
  },

  methods: {
    initializeChartData() {
      this.portfolioData.forEach((item) => {
        const stock = item.Stock;
        const buyPrice = parseFloat(item.Buy_Price * this.getSuggestedQty(item.Buy_Quantity, stock));
        this.series.push(buyPrice);
        this.chartOptions.labels.push(stock);
      });
    },

    getSuggestedQty(qty, stock) {
      return this.SuggestedQty(qty, stock);
    },
  },

  }
</script>

  
  
  
  