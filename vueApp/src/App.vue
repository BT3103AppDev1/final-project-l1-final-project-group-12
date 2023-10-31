<!-- <template>
  <router-view />
</template>

<script>
import Equities from "./views/Equities.vue";
import SearchResults from "./views/SearchResults.vue";
import Watchlist from './views/Watchlist.vue';

export default {
  name: "App",
};
</script>


<style scoped>
/* Your scoped styles */
</style> -->

<template>   
  <div class="topnav" :class="{ 'responsive': isResponsive }" id="myTopnav">
    <!-- Logo -->
    <div class="logo-container">
       <router-link to="/" class="logo"><img src="./assets/logo/whiteLogo.png" alt="Logo"></router-link> 
    </div>



    <!-- Navigation links -->
    <div class="nav-links">
      <router-link to="/equities" :class="{ 'active': $route.path === '/equities' }"><b>Equities</b></router-link>
      <router-link to="/portfolio" :class="{ 'active': $route.path === '/portfolio' }"><b>Portfolio</b></router-link>
      <router-link to="/user" :class="{ 'active': $route.path === '/user' }">
        <b v-if="isLoggedIn">{{this.displayName}}</b>
        <b v-else>User</b>
      </router-link>
      <button v-if="isLoggedIn" @click="signOut"> signOut</button>              
    </div>
  </div>
  <router-view/>
</template>

<script>
import { auth } from './firebasefunc.js'
import { getAuth, onAuthStateChanged, signOut } from 'firebase/auth'
import {ref} from "vue"
const displayName =ref("")
export default {
name: 'App',

computed: {
  currentRoute() {
    return this.$route.path;
  },
},

methods: {
  signOut() {
    signOut(auth)
    .then(() => {
      // user signed-out
      this.isLoggedIn = false
      this.displayName =  ""
      this.$router.push('/login');
    })
  }
},

data() {
  return {
    isResponsive: false,
    isLoggedIn: false,
    displayName: '',
  };
},

mounted(){
      onAuthStateChanged(auth, (user) => {
        if (user) {
          this.useremail = auth.currentUser.email
          this.isLoggedIn= true
          this.displayName =  auth.currentUser.email
        }
  })
}

};
</script>