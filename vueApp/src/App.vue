<script>
import Equities from "./views/Equities.vue"
import SearchResults from "./views/SearchResults.vue";

export default{
    name: 'App',
    components:{
    Equities,
    SearchResults
}
}
</script>

<template>
    <div id="app">
      <div class="market-header">
        <router-view></router-view> <!-- This is where routed components will be displayed -->
      </div>
    </div>
  </template>
  
  
  
  <style scoped>
  /* Your scoped styles */
  </style>
  

<style scoped>

</style>
