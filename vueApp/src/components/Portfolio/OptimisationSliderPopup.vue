<template>
    <div>
      <div v-if="showPopup" class="popup" @click.stop="">
        <div class="popup-content" @click.stop="">
          <h3>Specify Risk</h3>
          <div class="slider-container">
            <input type="range" v-model="sliderValue" @input="updateSpeechBubble" min="0" max="100">
            <div class="speech-bubble" :style="{ left: `${sliderValue}%`, top: '50%' }">
              {{ sliderValue }}%
            </div>
            <button @click="closeSliderPopup">Generate</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      showPopup: Boolean,
    },
    data() {
      return {
        sliderValue: 0, 
        clickCount: 0,   
        mouseDownInside: true,
      };
    },
    methods: {
      closeSliderPopup() {
          this.$emit('closePopup'); 
          
      },
      
      handleDocumentClick(event) {
        // Check if the click occurred outside the popup
        if (!this.$el.contains(event.target) && this.clickCount >= 1 && !this.mouseDownInside) {
          this.closeSliderPopup();
        }
      },
  
      handleMouseDownInside(event) {
        if (this.$el.contains(event.target)) {
          this.mouseDownInside = true;
        }
      },
  
      handleMouseUpInside(event) {
        if (!this.$el.contains(event.target) ) {
          this.clickCount++;
        }
        this.mouseDownInside = false;
      },
  
      
    },
    mounted() {
      // Attach a click event listener to the document if the popup is visible
      if (this.showPopup) {
        document.addEventListener('click', this.handleDocumentClick);
        document.addEventListener('mousedown', this.handleMouseDownInside);
        document.addEventListener('mouseup', this.handleMouseUpInside);
      }
    },
    beforeUnmount() {
      // Remove the click event listener when the component is unmounted
      document.removeEventListener('click', this.handleDocumentClick);
      document.removeEventListener('mousedown', this.handleMouseDownInside);
      document.removeEventListener('mouseup', this.handleMouseUpInside);
    },
    
  };
  </script>
  
  
  <style>
  .popup {
    position: absolute;
    left: 59%;
    transform: translateX(-50%);
    width: 22%;
    background-color: #fff;
    border: 1px solid #ccc;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    padding: 1.5%;
    text-align: center;
    z-index: 999;
    font-size: 3vh;
  }
  
  .popup-content {
    cursor: default; /* Prevent the cursor from changing when clicking inside the popup */
  }
  
  .slider-container {
    position: relative;
    margin-top: 0;
  }
  
  input[type="range"] {
    width: 100%;
  }
  
  .speech-bubble {
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-30%);
    padding: 2% 3%;
    background-color: #333;
    color: #fff;
    border-radius: 20%;
    font-size: 1.9vh;
    display: block;
  }
  
  </style>
  