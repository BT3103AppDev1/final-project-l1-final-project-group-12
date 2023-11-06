<template>   
  <div class="topnav" :class="{ 'responsive': isResponsive }" id="myTopnav">
    <!-- Logo -->
    <div class="logo-container">
       <router-link to="/" class="logo"><img src="@/assets/logo/whiteLogo.png" alt="Logo"></router-link> 
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
import { auth } from './../firebasefunc.js'
import { getAuth, onAuthStateChanged, signOut } from 'firebase/auth'
export default {
  name: 'Navigation',
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
      const auth = getAuth()
      onAuthStateChanged(auth, (user) => {
      if (user) {
        this.user = user
        this.isLoggedIn = true
        this.displayName = auth.currentUser.email
      }
    })
  }
}
  // data() {
  //   return {
  //     user: false,
  //     isResponsive: false,
  //   }
  // },
  // computed: {
  //   currentRoute() {
  //     return this.$route.path;
  //   },
  // },
  
  // mounted() {
  //   const auth = getAuth()
  //   onAuthStateChanged(auth, (user) => {
  //     if (user) {
  //       this.user = user
  //     }
  //   })
  // }
</script>


<style scope>
.topnav {
  overflow: hidden; 
  background-color: #272F51;
}
.nav-links a {
  color: #f2f2f2;
  float: right;
  text-align: center;
  padding: 2.15vw 3.2vw;
  text-decoration: none;
  font-size: 1.6vw; 
}
.nav-links a:hover {
  background-color: #ddd;
  color: black;
  text-decoration-color: black;
}
.nav-links a.active {
  text-decoration:underline;
  text-decoration-thickness: 0.3vw;
}
@media screen and (max-width: 600px) {
  .nav-links a:not(:first-child) {
    display: none;
  }
  .nav-links a.icon {
    float: right;
    display: block;
  }
}
@media screen and (max-width: 600px) {
  .nav-links.responsive {
    position: relative;
  }
  .nav-links.responsive .icon {
    position: absolute;
    right: 0;
    top: 0;
  }
  .nav-links.responsive a {
    float: none;
    display: block;
    text-align: left;
  }
}
</style>