<template>
    <div class="watchlist-container">
      <div class="watchlist-left">
        <WatchlistHeader />
        <WatchlistTable />
      </div>
      <div class="watchlist-right">
        <AddToWatchlist />
      </div>
    </div>
  </template>
  
  <script>
  import WatchlistHeader from '../components/Watchlist/WatchlistHeader.vue';
  import AddToWatchlist from '../components/Watchlist/AddToWatchlist.vue';
  import WatchlistTable from '../components/Watchlist/WatchlistTable.vue';
  
  export default {
    components: {
      WatchlistHeader,
      AddToWatchlist,
      WatchlistTable
    }
  }
  </script>
  
  <style scoped>

  html {
    background-color: #f6f6f6;
    margin: 0% 1.5% 1.5% 3%;
  }
  .watchlist-container {
    display: flex;
  }
  
  .watchlist-left {
    flex: 1;
    width: 75%;
  }
  
  .watchlist-right {
    margin-top: 6%;
    margin-left: 20px; /* Adjust the margin as needed */
    padding: 2% 2% 2% 2%;
    width: 23%;
  }
  </style>
  