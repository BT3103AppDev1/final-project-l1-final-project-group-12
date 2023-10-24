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
    font-weight: bold;
    font-size: large;
    width: 200%; 
    max-width: 800px; 
  }
  
  .box table td {
    padding: 15px;
  }
  
  .header-text .icon {
    max-width: 30px; /* Adjust size of icon */
    margin-right: 10px; 
    padding-left: 10px;
  }
  </style>
  