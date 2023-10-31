import { createRouter, createWebHistory } from "vue-router";
import SearchResults from "@/views/SearchResults.vue";
import Equities from "@/views/Equities.vue";

const routes = [
  {
    path: "/",
    name: "Equities",
    component: Equities,
    props: true,
  },
  {
    path: "/search-results/:searchTerm",
    name: "SearchResults",
    component: SearchResults,
    props: true,
  },
  // Other routes...
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
