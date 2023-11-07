<template>   
  <router-view/>
</template>

<script>
import { getAuth, onAuthStateChanged} from 'firebase/auth'
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
},


};
</script>
