<template>
  <div class="table-container">
    <table id="scrollable-table" class="auto-index">
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>BuyPrice</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>
            Expected <br />
            Return
          </th>
          <th></th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(item, index) in portfolioData" :key="item.ticker">
          <td>{{ index + 1 }}</td>
          <td class="wrapped-cell">{{ item.name }}</td>
          <!-- TODO: Add ticker -->
          <!-- Buy Price -->
          <td>
            <!-- Display Buy Price input field if in editing state -->
            <template v-if="item.editing">
              <input v-model="updatedBuyPrice" type="number" />
            </template>
            <!-- Display Buy Price if not in editing st ate -->
            <template v-else>
              ${{ formatNumberWithCommas(item.buyPrice) }}
            </template>
          </td>

          <!-- Stock Price -->
          <td>
            <template v-if="isNaN(this.stockPrices[item.ticker])"
              >Loading..</template
            >
            <template v-else>{{
              formatNumberWithCommas(this.stockPrices[item.ticker])
            }}</template>
          </td>

          <!-- Buy Quantity -->
          <td>
            <!-- Display Buy Quantity input field if in editing state -->
            <template v-if="item.editing">
              <input v-model="updatedBuyQuantity" type="number" />
            </template>
            <!-- Display Buy Quantity if not in editing state -->
            <template v-else>
              {{ parseFloat(item.buyQty).toFixed(2) }}
            </template>
          </td>

          <!-- P/L -->
          <td>
            <template v-if="isNaN(this.stockPrices[item.ticker])"
              >Loading..</template
            >
            <template v-else>
              <span
                :style="{
                  color: calculateProfitLoss(item) < 0 ? '#DA5151' : '#62D639',
                }"
              >
                {{ calculateProfitLoss(item) >= 0 ? "+$" : "-$"
                }}{{
                  formatNumberWithCommas(Math.abs(calculateProfitLoss(item)))
                }}
              </span>
            </template>
          </td>

          <!-- Button -->
          <td>
            <template v-if="objective == ''">
              <!-- Display Edit button only if not in editing state -->
              <button v-if="!item.editing" @click="editItem(index)" class="btw">
                <img src="@/assets/editIcon.png" alt="Edit" />
              </button>
              <!-- Display Save and Cancel buttons if in editing state -->
              <template v-else>
                <button @click="saveItem(index)" class="btw" id="saveButton">
                  <img src="@/assets/tickIcon.png" alt="Save" />
                </button>
                <button
                  @click="cancelEdit(index)"
                  class="btw"
                  id="cancelButton"
                >
                  <img src="@/assets/crossIcon.png" alt="Cancel" />
                </button>
              </template>
            </template>
            <!-- Display Delete button if not in editing state -->
            <button
              v-if="!item.editing"
              @click="deleteItem(item.ticker)"
              class="btw"
            >
              <img src="@/assets/deleteIcon.png" alt="Delete" />
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Display message if portfolioData is empty -->
    <p v-if="hasData == false" class="no-trades-message">
      You have not added any trades to your portfolio. To gain portfolio
      insights, please add your open trades.
    </p>
  </div>
  <Loading ref="Loading" />
</template>

<script>
import { getAuth, onAuthStateChanged } from "firebase/auth";
import axios from "axios";
import Loading from "@/components/Loading.vue";

export default {
  components: {
    Loading,
  },

  data() {
    return {
      updatedBuyQuantity: 0,
      updatedBuyPrice: 0,
      totalProfitLoss: 0,
      isEditing: false,
    };
  },

  async mounted() {
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.useremail = user.email;
      } else {
        this.useremail = ""; // Ensure it's cleared when the user signs out
      }
    });
  },

  props: {
    portfolioData: Array,
    stockPrices: Object,
    hasData: Boolean,
    status: Boolean,
    objective: String,
  },

  methods: {
    formatNumberWithCommas(number) {
      return number.toLocaleString(undefined, {
        useGrouping: true,
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
      });
    },
    editItem(index) {
      const item = this.portfolioData[index];

      item.editing = true;
      this.updatedBuyQuantity = item.buyQty;
      this.updatedBuyPrice = item.buyPrice;
    },

    async saveItem(index) {
      const item = this.portfolioData[index];

      //Define valid input
      if (
        isNaN(parseFloat(this.updatedBuyPrice)) ||
        isNaN(parseFloat(this.updatedBuyQuantity))
      ) {
        alert("Buy Price or Buy Quantity must be valid numbers."); //TODO: Add PopUp Window
        return;
      } else if (
        this.updatedBuyPrice === "" ||
        this.updatedBuyQuantity === ""
      ) {
        alert("All fields must be filled out.");
        return;
      } else if (this.updatedBuyPrice <= 0 || this.updatedBuyQuantity <= 0) {
        alert("Buy Price or Buy Quantity must be more than 0");
        return;
      }

      // Update item data with the new values
      const updatedData = {
        ticker: item.ticker,
        buyPrice: this.updatedBuyPrice,
        buyQty: this.updatedBuyQuantity,
      };

      const userConfirmed = window.confirm("Are you sure you want to proceed?");

      if (userConfirmed) {
        this.$refs.Loading.onLoading();
        const apiAddUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/update/updateTrade/${this.useremail}`;

        try {
          await this.deleteFromDB(item.ticker);

          console.log("Adding Updated Item");
          await axios.put(apiAddUrl, updatedData);

          this.$refs.Loading.offLoading();
          this.$emit("refresh-request");
        } catch (error) {
          console.error("Fail to updating trade: ", error);
          alert("Fail to updating trade: ", error, "Please try again!");
        }
        item.editing = false;
      } else {
        this.cancelEdit(index);
      }
    },

    cancelEdit(index) {
      const item = this.portfolioData[index];

      // Revert the updated values back to the original values
      this.updatedBuyPrice = item.buyPrice;
      this.updatedBuyQuantity = item.buyQty;

      item.editing = false;
    },

    async deleteItem(ticker) {
      const userConfirmed = window.confirm("Are you sure you want to proceed?");
      if (userConfirmed) {
        try {
          this.$refs.Loading.onLoading();

          await this.deleteFromDB(ticker);

          this.$refs.Loading.offLoading();
          console.log("refresh");
          this.$emit("refresh-request");
        } catch (error) {
          console.error("Fail to delete trade: ", error);
          alert("Fail to delete trade: ", error, "Please try again later!");
        }
      }
    },

    async deleteFromDB(ticker) {
      const apiUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/delete/trade/${this.useremail}/${ticker}/""`;
      const apiAlphaUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/delete/trade/${this.useremail}/${ticker}/alpha`;
      const apiBetaUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/delete/trade/${this.useremail}/${ticker}/beta`;
      const apiBalanceUrl = `https://smartfolio-7gt75z5x3q-as.a.run.app/api/delete/trade/${this.useremail}/${ticker}/balance`;

      try {
        await Promise.all([
          axios.delete(apiUrl),
          axios.delete(apiAlphaUrl),
          axios.delete(apiBetaUrl),
          axios.delete(apiBalanceUrl),
        ]);

        console.log("Delete: All requests completed");
      } catch (error) {
        console.error("Failed to delete trade: ", error);
        //alert('Fail to delete trade: ', error, 'Please try again later!')
      }
    },

    emitTotalPL() {
      this.$emit("total-pl-updated", this.totalPL);
    },
  },

  computed: {
    calculateProfitLoss() {
      return (item) => {
        return (
          item.buyQty * this.stockPrices[item.ticker] -
          item.buyQty * item.buyPrice
        );
      };
    },

    totalPL() {
      return this.portfolioData.reduce((total, item) => {
        return total + this.calculateProfitLoss(item);
      }, 0);
    },
  },

  watch: {
    totalPL: "emitTotalPL",
  },

  emits: ["total-pl-updated", "refresh-request"],
};
</script>




<style scope>
/* Box */
.table-container {
  height: 33vw;
  overflow-y: auto;
  border-radius: 25px;
  justify-content: center;
  background-color: white;
  box-shadow: 0 8px 10px rgba(0, 0, 0, 0.3);
  margin-bottom: 0;
}

/* Table */
#scrollable-table {
  width: 90%;
  background-color: white;
  border-collapse: collapse;
  margin: 0 auto;
}

#scrollable-table th,
#scrollable-table td {
  padding: 1vw;
  text-align: center;
  border-bottom: 2px solid #d0d0d0;
  padding-bottom: 2.7%;
  padding-top: 2.7%;
  font-size: 1.7vw;
  font-weight: bold;
}

#scrollable-table th {
  padding-top: 2vw;
  background-color: white;
}

#scrollable-table thead th {
  position: sticky;
  top: 0;
}

/* Add styles for input elements within table cells */
#scrollable-table input[type="number"] {
  width: 25%;
  padding: 0.6vw;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 1.2vw;
  font-weight: bold;
  text-align: center;
}

#scrollable-table input[type="number"]:focus {
  outline: none; /* Remove the default focus outline */
  border-color: #007bff; /* Change border color when focused */
}

.wrapped-cell {
  max-width: 16vh; /* Set the maximum width of the cell */
  max-height: 4em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: wrap;
}

/* No Trades message */
.no-trades-message {
  color: #bfbfbf; /* Change the color to your desired color */
  border-bottom: none !important;
  padding-top: 11vw !important;
  text-align: center;
  font-size: 1.8vw;
  font-weight: bold;
  padding-left: 10%;
  padding-right: 10%;
}

/* Delete/Edit Button */
.btw {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: inline;
  margin-right: 0.5vw;
}

.btw img:hover {
  transform: scale(1.3); /* Increase the value to make it scale more */
  transition: transform 0.2s ease-in-out; /* Add a smooth transition effect */
}

.btw img {
  width: 1.8vw;
  height: auto;
}

#saveButton img {
  width: 2vw;
  height: auto;
}

#cancelButton img {
  width: 1.5vw;
  height: auto;
}
</style>