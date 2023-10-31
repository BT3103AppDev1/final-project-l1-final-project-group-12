<template>
    <div class="body">
      <h1>{{ searchTerm }}</h1>
      
      <!-- Display search results here -->
    </div>
  </template>
  
  <script>
  export default {
    props: {
      searchTerm: String,
    },
  };
  </script>
  
  <style scoped>

  </style>
  