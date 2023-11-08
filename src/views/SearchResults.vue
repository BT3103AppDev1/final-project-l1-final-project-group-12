<template>
  <Navigation />
  <div>
    <!-- Show searched stock name on indiv -->
    <search-results-content :searchTerm="$route.params.searchTerm" />
  </div>
</template>

<script>
import Navigation from "../components/Navigation.vue";
import SearchResultsContent from "@/components/Equities/SearchResultsContent.vue";

export default {
  components: {
    Navigation,
    SearchResultsContent,
  },
};
</script>
