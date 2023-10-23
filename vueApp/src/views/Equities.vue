<template>
    <div class="app-container">
      <MarketOverview />
      <div class="side-by-side-container">
        <Trending />
        <TopGainers />
        <TopLosers />
      </div>
    </div>
  </template>
  
  <script>
  import MarketOverview from '../components/Equities/MarketOverview.vue';
  import Trending from '../components/Equities/Trending.vue';
  import TopGainers from '../components/Equities/TopGainers.vue';
  import TopLosers from '../components/Equities/TopLosers.vue';
  
  export default {
    components: {
      MarketOverview,
      Trending,
      TopGainers,
      TopLosers
    }
  }
  </script>
  
  <style>
  .app-container {
    padding: 20px; /* Add padding for spacing */
    width: 100%;
    margin-right: 2px;
  }
  
  .side-by-side-container {
    display: flex; 
    gap: 10%; 

  }

  </style>
  