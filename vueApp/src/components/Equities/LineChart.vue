<template>
    <div class="chart-container">
      <line-chart :data="chartData"></line-chart>
    </div>
  </template>
  
  <script>
  export default {
    props: ['chartData'],
  };
  </script>