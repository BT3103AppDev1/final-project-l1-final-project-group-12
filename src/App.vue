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
      <router-link to="/user" :class="{ 'active': $route.path === '/user' }"><b>User</b></router-link>      
    </div>
  </div>
  <router-view/>
</template>

<script>
export default {
name: 'App',

computed: {
  currentRoute() {
    return this.$route.path;
  },
},

data() {
  return {
    isResponsive: false,
  };
}

};
</script>
