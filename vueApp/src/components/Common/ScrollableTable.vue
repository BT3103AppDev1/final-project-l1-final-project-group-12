<template>
  <div class="table-bg">
  <div class="scrollable-table">
    <table>
      <thead>
        <tr>
          <th v-for="header in headers" :key="header">{{ header }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, rowIndex) in rows" :key="rowIndex">
          <td>{{ rowIndex + 1 }}</td>
          <!-- Display auto-index for each row -->
          <td v-for="(cell, cellIndex) in row" :key="cellIndex">
            {{ cell }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
</template>

<script>
export default {
  props: {
    headers: Array,
    rows: Array,
  },
};
</script>

<style scoped>
.scrollable-table {
  max-height: 40vw; 
  overflow-y: auto; 
}

.table-bg {
  width: 97%; 
  background-color: #ffffff;
  padding: 1.5%;
  border-radius: 13px;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.1);
}

table {
  border-collapse: collapse;
  width: 100%;
}
th,
td {
  border-bottom: 1px solid #d0d0d0;
  text-align: center;
  padding: 1.8vw 1.8vw 1.8vw 1.8vw;
  font-size: 1.7vw;
  font-weight: bold;
}

.scrollable-table::-webkit-scrollbar {
  width: 10px; /* Adjust the scrollbar width to your preference */
}

.scrollable-table::-webkit-scrollbar-thumb {
  background: #6c726c; /* Change the background color of the thumb */
  border-radius: 5px; /* Adjust the border radius to round the thumb */
}

.scrollable-table::-webkit-scrollbar-thumb:hover {
  background: #6c726c; /* Change the background color on hover */
}

.scrollable-table::-webkit-scrollbar-track {
  background: #f1f1f100; /* Change the background color of the track */
}
</style>