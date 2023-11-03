<template>
  <div>
    <!-- Show searched stock name on indiv -->
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
