<template>
  <Navigation />
  <div class="body">
    <MarketOverview />
    <div class="side-by-side-container">
      <TopGainers />
      <TopLosers />
    </div>
    <br /><br />
    <MarketSearch />
    <br />
    <MarketTable />
  </div>
</template>

<script>
import Navigation from "../components/Navigation.vue";
import MarketOverview from "../components/Equities/MarketOverview.vue";
import TopGainers from "../components/Equities/TopGainers.vue";
import TopLosers from "../components/Equities/TopLosers.vue";
import MarketSearch from "../components/Equities/MarketSearch.vue";
import MarketTable from "../components/Equities/MarketTable.vue";

export default {
  components: {
    Navigation,
    MarketOverview,
    TopGainers,
    TopLosers,
    MarketSearch,
    MarketTable,
  },
};
</script>
<style scoped>
.body {
  margin: 1% 3.5% 0% 2%;
  padding: 0 0 3% 1.5%;
  font-family: Arial, Helvetica, sans-serif;
}
.side-by-side-container {
  gap: 8%;
  width: 65%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
