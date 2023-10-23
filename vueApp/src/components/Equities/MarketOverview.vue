<template>
  <div class="body">
    <div class="market-overview">
      <h1>Market Overview</h1>
      <button class="view-watchlist-button">View Watchlist</button>
    </div>

    <div class="box-container">
      <!-- Loop through the containers -->
      <div v-for="(container, index) in containers" :key="index" class="box">
        <div class="box-header">
          <div class="icon">
            <img :src="container.imageSrc" alt="" />
          </div>
          <div class="header-text">
            <h3>{{ container.header }}</h3>
          </div>
        </div>

        <hr class="custom-hr" />

        <table class="table">
          <!-- Table content for the container -->
          <tr v-for="(row, rowIndex) in container.rows" :key="rowIndex">
            <td>{{ rowIndex + 1 }}</td>
            <td v-for="(cell, cellIndex) in row" :key="cellIndex">
              {{ cell }}
            </td>
          </tr>
        </table>
      </div>
    </div>
    <br />
  </div>
</template>

<style>
.body {
  margin-left: 3%;
  margin-right: 3%;
  font-family: Arial, Helvetica, sans-serif;
}
.market-overview {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.view-watchlist-button {
  background-color: #272f51;
  width: 20%;
  color: white;
  border: none;
  padding: 0.75%;
  border-radius: 10px;
  cursor: pointer;
  font-size: 120%;
  font-weight: bold;
}
</style>
