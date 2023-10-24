<template>
  <div class="body">
    <div class="market-overview">
      <h1>Market Overview</h1>
      <button class="view-watchlist-button">View Watchlist</button>
    </div>
  </div>
  <br />
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
