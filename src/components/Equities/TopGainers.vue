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
import axios from "axios";

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

          header: "Top Gainers Today",
          rows: Array(5).fill(["Loading..."]),
        },
      ],
    };
  },
  mounted() {
    // Make an HTTP GET request to the API endpoint
    axios
      .get(
        "https://smartfolio-7gt75z5x3q-as.a.run.app/api/yfinance/topGainersData"
      )
      .then((response) => {
        // Update the rows of the "Top Gainers" container with the API data
        this.containers[0].rows = response.data;
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  },
};
</script>
