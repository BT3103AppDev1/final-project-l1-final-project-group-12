<template>
    <div class="chart-container">
      <line-chart :data="chartData" :options="chartOptions"></line-chart>
    </div>
  </template>
  
  <script>
  export default {
    props: ['chartData', 'chartOptions'],
  };
  </script>