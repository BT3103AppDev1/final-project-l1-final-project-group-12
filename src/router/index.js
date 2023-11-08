import { createRouter, createWebHistory } from "vue-router";
import { getAuth, onAuthStateChanged } from "firebase/auth";
import { auth } from "../usersController.js";
import Home from "@/views/Home.vue";
// import Portfolio from "@/views/Portfolio.vue";
import Equities from "@/views/Equities.vue";
import Login from "@/views/Login.vue";
// import Profile from "@/views/Profile.vue";
import SearchResults from "@/views/SearchResults.vue";
import Watchlist from "@/views/Watchlist.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },

  // {
  //   path: "/portfolio",
  //   name: "Portfolio",
  //   component: Portfolio,
  //   meta: { requiresAuth: true },
  // },


  {
    path: "/equities",
    name: "Equities",
    component: Equities,
    meta: { requiresAuth: false },
  },

  // {
  //   path: "/profile",
  //   name: "Profile",
  //   component: Profile,
  //   meta: { requiresAuth: true },
  // },

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
];


const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (getAuth().currentUser) {
      next();
      return;
    }
    console.log("restricted");
    next("/login");
    console.log("restricted");
    next("/login");
  } else {
    next();
    return;
  }
});

export default router;