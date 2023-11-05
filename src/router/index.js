import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import Portfolio from "@/views/Portfolio.vue";
import Equities from "@/views/Equities.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },

  {
    path: "/portfolio",
    name: "Portfolio",
    component: Portfolio,
  },

  {
    path: "/equities",
    name: "Equities",
    component: Equities,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
