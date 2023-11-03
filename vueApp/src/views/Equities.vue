<template>
  <div class="body">
    <MarketOverview />
    <div class="side-by-side-container">
      <TopGainers />
      <TopLosers />
    </div>
    <br /><br />
    <MarketSearch />
    <br>
    <MarketTable />
  </div>
</template>

<script>
import MarketOverview from "../components/Equities/MarketOverview.vue";
import TopGainers from "../components/Equities/TopGainers.vue";
import TopLosers from "../components/Equities/TopLosers.vue";
import MarketSearch from "../components/Equities/MarketSearch.vue";
import MarketTable from '../components/Equities/MarketTable.vue';

export default {
  components: {
    MarketOverview,
    TopGainers,
    TopLosers,
    MarketSearch,
    MarketTable
  },
};
</script>

<style>

html {
  background-color: #f6f6f6;
}

.body {
  margin: 2% 3.5% 0% 2%;
  padding: 0 0 3% 1.5%; 
  font-family: Arial, Helvetica, sans-serif;
}
</style>

<style scoped>
.side-by-side-container {
  display: flex;
  gap: 8%;
  width: 60%;
}
</style>