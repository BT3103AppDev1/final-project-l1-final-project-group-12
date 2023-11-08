<template>
  <div class="container">
    <div class="box">
      <div class="box-header">
        <div class="header-text">
          <h3>
            <img class="icon" :src="imageSrc" alt="" />
            {{ header }}
          </h3>
        </div>
      </div>

      <hr class="custom-hr" />

      <table class="table">
        <tr v-for="(row, rowIndex) in rows" :key="rowIndex">
          <td>{{ rowIndex + 1 }}</td>
          <td v-for="(cell, cellIndex) in row" :key="cellIndex">
            {{ cell }}
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "Box",
  props: {
    imageSrc: String,
    header: String,
    rows: Array,
  },
};
</script>

<style scoped>
.container {
  width: 180%; /* Set the width of the parent container */
  display: flex;
  justify-content: space-between;
}

.box {
  border-radius: 13px;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  font-weight: bold;
  font-size: 1.5vw;
  width: 40vw; 
  padding: 0px 0px 10px 15px; 
}


.box table td {
  padding: 15px;
  font-size: 1.6vw;
}

.header-text .icon {
  max-width: 40px;
  margin-right: 10px;
  padding-left: 10px;
}

.custom-hr {
  border: none; /* Remove the default border */
  border-top: 2px solid #d0d0d0; /* Set the custom color (e.g., red) */
  margin-right: 4%;
}


</style>
