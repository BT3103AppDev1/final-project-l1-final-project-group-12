<template>
  <div class="topnav" :class="{ responsive: isResponsive }" id="myTopnav">
    <!-- Logo -->
    <div class="logo-container">
      <router-link to="/" class="logo">
        <img src="@/assets/logo/whiteLogo.png" alt="Logo" />
      </router-link>
    </div>

    <!-- Navigation links -->
    <div class="nav-links">
      <router-link
        to="/equities"
        :class="{ active: $route.path === '/equities' }"
        ><b>Equities</b></router-link
      >

      <router-link
        to="/portfolio"
        :class="{ active: $route.path === '/portfolio' }"
        ><b>Portfolio</b></router-link
      >

      <!-- This div will toggle the profile popup -->
      <div @click="toggleProfilePopup" :class="{ active: showProfilePopup }">
        <b>User</b>
      </div>
    </div>
  </div>

  <!-- Profile Popup component -->
  <div class="profile-popup-container" v-if="showProfilePopup">
    <ProfilePage @close="toggleProfilePopup" />
  </div>

  <router-view />
</template>

<script>
import ProfilePage from "@/components/ProfilePage.vue";
//import { getAuth, onAuthStateChanged } from 'firebase/auth'
export default {
  name: "Navigation",
  components: {
    ProfilePage, // Make sure to declare the imported component here
  },
  data() {
    return {
      showProfilePopup: false,
      //     user: false,
      //     isResponsive: false,
    };
  },
  methods: {
    toggleProfilePopup() {
      this.showProfilePopup = !this.showProfilePopup;
    },
    // other methods
  },
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
};
</script>

<style>
.topnav {
  overflow: hidden;
  background-color: #272f51;
}

/* Styles for all navigation items */
.nav-links a,
.nav-links div {
  color: #f2f2f2;
  float: right;
  text-align: center;
  padding: 2.15vw 3.2vw;
  text-decoration: none;
  font-size: 1.6vw;
  cursor: pointer; /* Change cursor to indicate clickable */
}

/* Hover styles */
.nav-links a:hover,
.nav-links div:hover {
  background-color: #ddd;
  color: black;
}

/* Active state styles */
.nav-links a.active,
.nav-links div.active {
  background-color: #3e4a68; /* Adjust to your active link background color */
  text-decoration: underline;
  text-decoration-thickness: 0.3vw;
}
.profile-popup-container {
  position: fixed; /* Overlay the entire screen */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center; /* Center the child horizontally */
  align-items: center; /* Center the child vertically */
  background-color: rgba(0, 0, 0, 0.5); /* Dimmed background */
  z-index: 10; /* Make sure it's above other content */
}

/* Responsive adjustments */
@media screen and (max-width: 600px) {
  .nav-links a:not(:first-child),
  .nav-links div:not(:first-child) {
    display: none;
  }
  .nav-links a.icon,
  .nav-links div.icon {
    float: right;
    display: block;
  }
  .nav-links.responsive a,
  .nav-links.responsive div {
    float: none;
    display: block;
    text-align: left;
  }
}
</style>
