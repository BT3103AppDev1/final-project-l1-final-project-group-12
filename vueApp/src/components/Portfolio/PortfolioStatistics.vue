<template>

    <div class="statistics-table">
        
        <!-- Button -->
        <div class="time-view-button">
        <button
          v-for="button in buttons"
          :key="button"
          class="top-button"
          :class="{ active: selectedButton === button }"
          @click="selectButton(button)"
        >
          {{ button }}
        </button>
      </div>

      <!-- Content -->
      <div class="statistics-content">
        <div class="column" v-for="(column, columnIndex) in columns" :key="columnIndex">
          <div class="row" v-for="(row, rowIndex) in column" :key="rowIndex">
            <div class="cell">{{ row.label }}</div>
            <div class="cell">{{ row.value }}</div>
          </div>
        </div>
      </div>
    </div>

  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedButton: '1Y',
        buttons: ['1Y', '6M', '7D'],
        columns: [
          [
            { label: 'Absolute Return', value: '5%' },
            { label: "Market's Benchmark", value: '10%' },
            { label: 'Expected Alpha', value: '10%' },
            { label: 'Active Shares', value: '10%' },
          ],
          [
            { label: 'Overall Beta', value: '10%' },
            { label: 'Sharpe Ratio', value: '10%' },
            { label: 'Std Deviation', value: '10%' },
            { label: 'Variance', value: '10%' },
          ],
          [
            { label: 'Riskiest Stock', value: '10%' },
            { label: 'Beta of Stock', value: '10%' },
          ],
        ],
      };
    },
    methods: {
      selectButton(button) {
        this.selectedButton = button;
      },
    },
  };
  </script>
  
  
  <style>
  .statistics-table {
    height: 33vw;
    border-radius: 25px;
    background-color: white;
    box-shadow: 0 8px 10px rgba(0, 0, 0, 0.3);

/* Content */
  }
  .statistics-content {
    display: flex;
    font-weight: bold;
    font-size:120%;
    margin-top:1%;
  }
  
  .column {
    flex: 1;
  }
  
  .row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    text-align: center;
  }
  
  .cell {
    padding-top: 20%;

    border-right: 1px solid #ccc; /* Add right border */
  }

  .row .cell:last-child {
    border-right: none;
  }

/* button */
  .time-view-button {
  padding-left: 2%;
  padding-top: 2%;
}

.top-button {
  background-color: #D9D9D9;
  color: black;
  font-weight:bold;
  font-size: 100%;
  border: none;
  border-radius: 2vh;
  padding: 1% 1%;
  margin-right: 0.5%;
  cursor: pointer;
}

.top-button.active {
  background-color: #272F51; /* Change to the desired color when clicked */
  color: white;
}

/* Add a hover animation */
.top-button:hover {
  background-color: #A5A5A5; /* Change to the desired hover color */
  transition: background-color 0.3s;
}
  </style>
  