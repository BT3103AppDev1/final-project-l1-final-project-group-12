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
import WatchlistHeader from "../components/Watchlist/WatchlistHeader.vue";
import AddToWatchlist from "../components/Watchlist/AddToWatchlist.vue";
import WatchlistTable from "../components/Watchlist/WatchlistTable.vue";

export default {
  components: {
    WatchlistHeader,
    AddToWatchlist,
    WatchlistTable,
  },
};
</script>

<style scoped>

.watchlist-container {
  display: flex;
  margin: 2% 2.5% 0% 3%;

  font-family: Arial, Helvetica, sans-serif;
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
