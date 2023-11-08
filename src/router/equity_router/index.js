import { createRouter, createWebHistory } from "vue-router";
import SearchResults from "@/views/SearchResults.vue";
import Equities from "@/views/Equities.vue";
import Watchlist from "@/views/Watchlist.vue";
import Home from "@/views/Home.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    props: true,
  },
  {
    path: "/equities",
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
  {
    path: "/watchlist",
    name: "Watchlist",
    component: Watchlist,
  },
  // Other routes...
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
