<template>
    <div class="statistics-table">
        <div class="TimeView">
            <button class="top-button" :class="{ active: selectedButton === '1Y' }" @click="selectButton('1Y')">1Y</button>
      <button class="top-button" :class="{ active: selectedButton === '6M' }" @click="selectButton('6M')">6M</button>
      <button class="top-button" :class="{ active: selectedButton === '7D' }" @click="selectButton('7D')">7D</button>
        </div>
    <div class="statistics-content">
      <div class="column">
        <div class="row">
          <div class="cell">Absolute Return</div>
          <div class="cell">{{ absoluteReturn }}</div>
        </div>
        <div class="row">
            <div class="cell">Market's Benchmark</div>
          <div class="cell">{{ marketBenchmark }}</div>
        </div>
        <div class="row">
          <div class="cell">Expected Alpha</div>
          <div class="cell">{{ expectedAlpha }}</div>
        </div>
        <div class="row">
          <div class="cell">Active Shares</div>
          <div class="cell">{{ activeShares }}</div>
        </div>
      </div>
  
      <div class="column">
        <div class="row">
          <div class="cell">Overall Beta</div>
          <div class="cell">{{ overallBeta }}</div>
        </div>
        <div class="row">
          <div class="cell">Sharpe Ratio</div>
          <div class="cell">{{ sharpeRatio }}</div>
        </div>
        <div class="row">
          <div class="cell">Std Deviation</div>
          <div class="cell">{{ stdDeviation }}</div>
        </div>
        <div class="row">
          <div class="cell">Variance</div>
          <div class="cell">{{ variance }}</div>
        </div>
      </div>
  
      <div class="column">
        <div class="row">
          <div class="cell">Riskiest Stock</div>
          <div class="cell">{{ riskiestStock }}</div>
        </div>
        <div class="row">
          <div class="cell">Beta of Stock</div>
          <div class="cell">{{ betaOfStock }}</div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
          <div class="cell"></div>
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

      absoluteReturn: '5%',
      marketBenchmark: '10%', 
      expectedAlpha: '10%', 
      activeShares: '10%', 

      overallBeta: '10%', 
      sharpeRatio: '10%', 
      stdDeviation: '10%',
      variance: '10%',

      riskiestStock: '10%',
      betaOfStock: '10%',

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
  .TimeView {
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
  