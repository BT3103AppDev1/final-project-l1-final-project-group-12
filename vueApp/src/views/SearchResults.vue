<template>
  <div>
    <!-- Show searched stock name on indiv stock page -->
    <search-results-content :searchTerm="$route.params.searchTerm" />
    
  </div>
</template>

<script>
import SearchResultsContent from "@/components/Equities/SearchResultsContent.vue";

export default {
  components: {
    SearchResultsContent,
  },
};
</script>


<style scoped>
.body {
  margin: 4% 3.5% 0% 2%;
  padding: 0 0 3% 1.5%; 
  font-family: Arial, Helvetica, sans-serif;
}
</style>
