<template>
  <router-view />
</template>

<script>
export default {
  name: "App",

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
