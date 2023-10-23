<template>
    <div class="box-container">
      <Box
        v-for="container in containers"
        :key="container.header"
        :imageSrc="container.imageSrc"
        :header="container.header"
        :rows="container.rows"
      />
    </div>
    <br />
  </template>
  
  <script>
  import Box from "@/components/Equities/Box.vue"; 
  
  export default {
    name: "Equities",
    components: {
      Box, 
    },
    data() {
      return {
        containers: [
          {
            imageSrc: "./src/assets/gainIcon.png",
            header: "Top Gainers",
            rows: [["Apple"], ["Apple"], ["Apple"]],
          },
          
        ],
      };
    },
  };
  </script>
  
