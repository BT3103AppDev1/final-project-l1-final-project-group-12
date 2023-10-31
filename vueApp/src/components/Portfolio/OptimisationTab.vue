<template>

    <button
            v-for="(tab, index) in buttons"
            :key="index"
            :class="{ 'selected-Optimisation-tab': tab === selectedButton }"
            @click="selectButton(index)"
            class="Optimisation-tab"
            >
            <span class="Optimisation-tab-line">{{ tab.split(' ')[0] }}</span>
            <span class="Optimisation-tab-line">{{ tab.split(' ')[1] }}</span>
    </button>


</template>

<script>
import { getAuth, onAuthStateChanged } from 'firebase/auth'
import axios from 'axios';

  const TABS = [
  "Current Portfolio",
  "Maximize Returns",
  "Minimize Risk",
  "Balance Portfolio"
  ];


    export default {
        name: 'App',
        components: {

        },
        

        data() {
      return {
        buttons: TABS,
        selectedButton: TABS[0],
        selectedTabIndex: 1,
        useremail: '',
      };
    },

    async mounted() {
      const auth = getAuth();
      onAuthStateChanged(auth, (user) => {
          if (user) {
              this.useremail = user.email;

          } else {
              this.useremail = ''; // Ensure it's cleared when the user signs out
          }
      });
    },

    methods: {
      selectButton(index) {
        this.selectedButton = this.buttons[index];
        this.selectedTabIndex = index + 1;

        this.SuggestedQty(this.selectedTabIndex);
        
        this.$emit('update-selected-tab-index', this.selectedTabIndex);
      },

      async SuggestedQty(selectedTabIndex) {            //TODO: PUT OPTIMIZED QTY HERE
        let objective = "";

        if (this.selectedTabIndex == 2) {
          objective = "alpha";
        
        } else if (this.selectedTabIndex == 3) {
          objective = "beta";

        } else{
          objective = "balance";
        }

        const apiUrl = `http://localhost:3000/api/optimise/${this.useremail}/${objective}`;
        console.log(apiUrl)
        //const response = await axios.post(apiUrl);
        console.log(response)
          
      },

    },
    emits: ['update-selected-tab-index'],
}



</script>

<style>
.Optimisation-tab {
      flex: 1; 
      background-color: #cdcdd0;
      color: white;
      margin: 1vw 0.5vw;
      padding: 0.8vw 0; 
      border: 1vw;
      border-radius: 1.2vw;
      cursor: pointer;
      font-size: 1.6vw;
      font-weight: bold;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    
    .Optimisation-tab-line {
      line-height: 1; /* Adjust line-height to control spacing between lines */
    }
    
    button.selected-Optimisation-tab {
      background-color: #bde4fa;
      color: #4e5ea4;
    }
</style>