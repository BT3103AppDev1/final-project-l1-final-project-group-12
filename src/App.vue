
<template>
  <router-view />
</template>

<script>
import { auth } from "./usersController.js";
import { getAuth, onAuthStateChanged, signOut } from "firebase/auth";
import { ref } from "vue";
const displayName = ref("");
export default {
  name: "App",

  computed: {
    currentRoute() {
      return this.$route.path;
    },
  },

  methods: {
    signOut() {
      signOut(auth).then(() => {
        // user signed-out
        this.isLoggedIn = false;
        this.displayName = "";
        this.$router.push("/login");
      });
    },
  },

  data() {
    return {
      isResponsive: false,
      isLoggedIn: false,
      displayName: "",
    };
  },

  mounted() {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.useremail = auth.currentUser.email;
        this.isLoggedIn = true;
        this.displayName = auth.currentUser.email;
      }
    });
  },
};
</script>