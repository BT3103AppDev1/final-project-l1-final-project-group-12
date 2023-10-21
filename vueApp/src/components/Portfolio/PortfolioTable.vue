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
          <th>P/L</th>
          <th></th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(item, index) in portfolioData" :key="item.Stock">
          <td>{{ index + 1 }}</td>
          <td>{{ item.Stock }}</td>
                                                    <!-- TODO: Add ticker -->
          <!-- Buy Price -->
          <td>
            <!-- Display Buy Price input field if in editing state -->
            <template v-if="item.editing">
              <input v-model="updatedBuyPrice" type="number" />
            </template>
            <!-- Display Buy Price if not in editing state -->
            <template v-else>
              {{ parseFloat(item.Buy_Price).toFixed(2) }}
            </template>
          </td>

          <td>0</td>        <!-- TODO: Update Price -->

          <!-- Buy Quantity -->
          <td>
            <!-- Display Buy Quantity input field if in editing state -->
            <template v-if="item.editing">
              <input v-model="updatedBuyQuantity" type="number" />
            </template>
            <!-- Display Buy Quantity if not in editing state -->
            <template v-else>
              {{ SuggestedQty(item.Buy_Quantity, item.Stock) }}
            </template>
          </td>

          <td>0</td>      <!-- TODO: Update P/L -->

          <!-- Button -->
          <td>
            <!-- Display Edit button only if not in editing state -->
            <button v-if="!item.editing" @click="editItem(index)" class="btw">
              <img src="@/assets/editIcon.png" alt="Edit" />
            </button>
            <!-- Display Save and Cancel buttons if in editing state -->
            <template v-else>
              <button @click="saveItem(index)" class="btw" id="saveButton">
                <img src="@/assets/tickIcon.png" alt="Save" />
              </button>
              <button @click="cancelEdit(index)" class="btw" id="cancelButton">
                <img src="@/assets/crossIcon.png" alt="Cancel" />
              </button>
            </template>
            <!-- Display Delete button if not in editing state -->
            <button v-if="!item.editing" @click="deleteItem(item.Stock)" class="btw">
              <img src="@/assets/deleteIcon.png" alt="Delete" />
            </button>
          </td>

        </tr>
      </tbody>
    </table>

    <!-- Display message if portfolioData is empty -->
    <p v-if="hasData == false" class="no-trades-message">
      You have not added any trades to your portfolio. To gain portfolio insights, please add your open trades.
    </p>
  
  </div>
</template>

<script>
import '@/style/Portfolio/PortfolioTable.css';
import { editInstrument, deleteInstrument } from '@/firebasefunc.js';

export default {
  data() {
    return {
      updatedBuyQuantity: 0,
      updatedBuyPrice: 0,
    };
  },

  props: {
    SuggestedQty: Function,
    portfolioData: Array,
    hasData: Boolean,
  },


  methods: {
    editItem(index) {
      const item = this.portfolioData[index];

      item.editing = true;
      this.updatedBuyQuantity = item.Buy_Quantity;
      this.updatedBuyPrice = item.Buy_Price;
    },

    async saveItem(index) {
      const item = this.portfolioData[index];

      // Update item data with the new values
      const updatedData = {
        Buy_Price: this.updatedBuyPrice,
        Buy_Quantity: this.updatedBuyQuantity,
      };
      await editInstrument(item.Stock, updatedData);

      item.editing = false;
      this.$emit('refresh-request');
    },

    cancelEdit(index) {
      const item = this.portfolioData[index];

      // Revert the updated values back to the original values
      this.updatedBuyPrice = item.Buy_Price;
      this.updatedBuyQuantity = item.Buy_Quantity;
      
      item.editing = false;
    },

    async deleteItem(stock) {
      await deleteInstrument(stock);
      
      this.$emit('refresh-request');
    },

  },

};
</script>

