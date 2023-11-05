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
  const TABS = [
  "Current Portfolio",
  "Maximize Returns",
  "Minimize Risk",
  "Balance Portfolio"
  ];

    export default {
        name: 'App',       

      data() {
        return {
          buttons: TABS,
          selectedButton: TABS[0],
          selectedTabIndex: 1,

        };
      },

    methods: {
      selectButton(index) {
        this.selectedButton = this.buttons[index];
        this.selectedTabIndex = index + 1;
        
        this.$emit('update-selected-tab-index', this.selectedTabIndex);
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