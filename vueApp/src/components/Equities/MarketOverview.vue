<template>
  <div class="market-overview">
    <h1>Market Overview</h1>
    <button class="view-watchlist-button">View Watchlist</button>
  </div>
  <br />
</template>

<style>
h1 {
  font-size: 3vw;
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
  font-size: 1.5vw;
  font-weight: bold;
}
</style>
