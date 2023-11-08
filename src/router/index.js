import { createRouter, createWebHistory } from "vue-router";
import { getAuth, onAuthStateChanged } from "firebase/auth";
import { auth } from "./../usersController.js";
import Home from "@/views/Home.vue";
import Portfolio from "@/views/Portfolio.vue";
import Equities from "@/views/Equities.vue";
import User from "@/views/User.vue";
import Login from "@/views/Login.vue";

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

  {
    path: "/portfolio",
    name: "Portfolio",
    component: Portfolio,
    meta: { requiresAuth: true },
  },

  {
    path: "/equities",
    name: "Equities",
    component: Equities,
    meta: { requiresAuth: true },
  },

  {
    path: "/user",
    name: "User",
    component: User,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (getAuth().currentUser) {
      console.log("accessibles");
      next();
      return;
    }
    console.log("restricted");
    next("/login");
  } else {
    console.log("justgo");
    next();
    return;
  }
});

export default router;
