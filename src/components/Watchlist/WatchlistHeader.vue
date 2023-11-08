<template>
  <div class="header">
    <div class="back-button">
      <button @click="goBackToEquities()">
        <img src="@/assets/backIcon.png" alt="" class="back-icon" />
      </button>
    </div>
    <h1>My Watchlist</h1>
  </div>
</template>

<script>
export default {
  methods: {
    goBackToEquities() {
      this.$router.push('/equities'); // Navigate to the "/equities" route
    },
  },
};
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
}

h1 {
  font-size: 3vw;
  margin-left: 10px; /* Adjust the margin as needed */
}

.back-button {
  display: flex;
  align-items: center;
}

.back-button button {
  background: none;
  border: none;
  cursor: pointer;
}

.back-icon {
  width: 3vw; /* Adjust the width of the back icon */
  height: 3vw; /* Adjust the height of the back icon */
  margin-right: 1.5vw;
}
</style>
