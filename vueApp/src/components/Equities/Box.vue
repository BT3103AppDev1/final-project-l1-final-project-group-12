<template>
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
  
  <style>
  .box {
    border-radius: 13px;
    box-shadow: 0 5px 5px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
    margin-right: 2%;
    padding: 1%;
    padding-left: 1%;
    font-weight: bold;
    font-size: large;
    width: 250%;
  }
  
  .box table td {
    padding: 10px; /* Adjust the amount of padding to control the space between columns */
  }
  
  .header-text .icon {
    max-width: 30px; /* Adjust the size of the icon */
    margin-right: 10px; /* Adjust the margin as needed */
  }
  </style>
  