<template>
  
  <div id="logged" v-if="user">
    <div class="topnav" :class="{ 'responsive': isResponsive }" id="myTopnav">

      <div class="nav-links" id="nav">
        <router-link to="/portfolio" :class="{ 'active': $route.path === '/portfolio' }"><b>Equities</b></router-link>
        <router-link to="/portfolio" :class="{ 'active': $route.path === '/portfolio' }"><b>Portfolio</b></router-link>
        <router-link to="/portfolio" :class="{ 'active': $route.path === '/portfolio' }"><b>User</b></router-link>      
      </div>
    </div>
  </div>

</template>

<script>
import { getAuth, onAuthStateChanged } from 'firebase/auth'

export default {
  name: 'NavBar',
  data() {
    return {
      user: false,
      isResponsive: false,
    }
  },

  computed: {
    currentRoute() {
      return this.$route.path;
    },
  },
  
  mounted() {
    const auth = getAuth()
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.user = user
      }
    })
  }
}
</script>


<style>
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