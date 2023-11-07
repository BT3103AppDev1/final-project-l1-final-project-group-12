<template>
  <div class="topnav" :class="{ responsive: isResponsive }" id="myTopnav">
    <div class="logo-container">
      <router-link to="/" class="logo">
        <img src="@/assets/logo/whiteLogo.png" alt="Logo" />
      </router-link>
    </div>

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
      <div @click="handleLoginClick" :class="{ active: showProfilePopup }">
        <b>{{ displayName || "Log In" }}</b>
      </div>
    </div>
  </div>

  <div class="profile-popup-container" v-if="isLoggedIn && showProfilePopup">
    <Profile @close="toggleProfilePopup" @requestSignOut="signOut" />
  </div>
  <router-view />
</template>

<script>
import Profile from "@/views/Profile.vue";
import {
  getAuth,
  onAuthStateChanged,
  signOut as firebaseSignOut,
} from "firebase/auth";
import { useRouter } from "vue-router";

export default {
  name: "Navigation",
  components: {
    Profile,
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  data() {
    return {
      isResponsive: false,
      isLoggedIn: false,
      displayName: "",
      showProfilePopup: false,
    };
  },
  methods: {
    handleLoginClick() {
      if (!this.isLoggedIn) {
        this.router.push("/login");
      } else {
        this.toggleProfilePopup();
      }
    },
    signOut() {
      const auth = getAuth();
      firebaseSignOut(auth).then(() => {
        // User signed-out
        this.isLoggedIn = false;
        this.displayName = "";
        this.$router.push("/login");
      });
    },
    toggleProfilePopup() {
      this.showProfilePopup = !this.showProfilePopup;
    },
  },
  mounted() {
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.isLoggedIn = true;
        this.displayName = user.email || user.displayName;
      } else {
        // User is signed out
        this.isLoggedIn = false;
        this.displayName = "";
      }
    });
  },
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
