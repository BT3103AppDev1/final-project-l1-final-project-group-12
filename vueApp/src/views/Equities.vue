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

    <div class="market-header">
      <h1>Market</h1>
      <form id="marketSearch" class="search-form">
        <input
          type="text"
          id="searchInput"
          required=""
          placeholder="Search by company name/code"
        />
        <br /><br />

        <button id="searchButton" type="button" @click="runMarketSearch()">
          Search</button
        ><br /><br />
      </form>
    </div>

    <div class="market">
      <table class="market-table">
        <!-- Header row (Static) -->
        <thead>
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Price</th>
            <th>%Change</th>
            <th>Market Cap</th>
            <th>Volume</th>
            <!-- Add more header columns as needed -->
          </tr>
        </thead>

        <!-- Dynamic table content -->
        <tr
          v-for="(customDataRow, customDataRowIndex) in customDataRows.rows"
          :key="customDataRowIndex"
        >
          <td>{{ customDataRowIndex + 1 }}</td>
          <td
            v-for="(cell, cellIndex) in customDataRow"
            :key="cellIndex"
            class="box2"
          >
            {{ cell }}
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "Equities",
  data() {
    return {
      containers: [
        {
          imageSrc: "./src/assets/fire.png",
          header: "Trending",
          rows: [["Apple"], ["Apple"], ["Apple"]],
        },
        {
          imageSrc: "./src/assets/gainIcon.png",
          header: "Top Gainers",
          rows: [["Apple"], ["Apple"], ["Apple"]],
        },
        {
          imageSrc: "./src/assets/loseIcon.png",
          header: "Top Losers",
          rows: [["Apple"], ["Apple"], ["Apple"]],
        },
      ],

      customDataRows: {
        rows: [
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          // Add more rows and cells as needed
        ],
      },
    };
  },
};
</script>

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

.box-container {
  display: flex; /* Set the display to flex to make containers appear side by side */
  justify-content: space-between; /* Distribute space between containers */
  border: none;
}

.box {
  width: 30%; /* Adjust the width of individual containers */
  border-radius: 13px;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  margin-right: 2%;
  padding: 1%;
  padding-left: 1%;
  font-weight: bold;
  font-size: large;
}

.box:last-child {
  margin-right: 0;
}

.box img {
  max-width: 90%;
  margin-right: 10px;
}

.box-header {
  display: flex;
  align-items: center; /* Center vertically */
}

/* Style for the icon div */
.box-header .icon {
  max-width: 13%; /* Ensure the icon doesn't exceed the container width */
  margin-right: 10px; /* Adjust the spacing between the icon and header text */
}

/* Style for the header text div */
.box-header .header-text {
  flex-grow: 1; /* Allow the header text to expand and fill available space */
}

.box table td {
  padding: 10px; /* Adjust the amount of padding to control the space between columns */
}

.custom-hr {
  border: none; /* Remove the default border */
  border-top: 2px solid #d0d0d0; /* Set the custom color (e.g., red) */
}

.market {
  width: 97%; /* Adjust the width of individual containers */
  background-color: #ffffff;
  padding: 1.5%;
  border-radius: 13px;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.1);
}

.market-table {
  width: 100%;
  font-weight: bold;
  font-size: 1.8vw;
  border-collapse: collapse;
}

.market-table th,
.market-table td {
  border-bottom: 1px solid #d0d0d0;
  padding: 0.3vw;
  text-align: center;
  padding-bottom: 1.3vw;
  padding-top: 1.3vw;
  font-size: 1.7vw;
  font-weight: bold;
}

.box2 {
  padding-left: 6.5vw;
}

.search-form {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

#searchInput {
  margin-right: 1vw; /* Adjust margin as needed */
  width:28vw;
  height: 32%;
  border-radius: 0.75vw;
  border-color: #FFFDFD;
  font-weight: bold;
  font-size: 1.4vw;
  background-color: white;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.1);
  padding-left: 0.75vw;
}

#searchButton {
  background-color: #272f51;
  width: 35%;
  color: white;
  border: none;
  padding: 0.75%;
  border-radius: 10px;
  cursor: pointer;
  font-size: 100%;
  height: 40%;
  font-weight: bold;
  margin-right: 0.5vw;


}


.market-header {
  display: flex;
  justify-content: space-between;
  width:100%;
}
</style>
