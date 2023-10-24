<template>
    <div>
      <div v-if="showPopup" class="popup" @click.stop="">
        <div class="popup-content" @click.stop="">
          <h3>Specify your desired Risk level</h3>

          <div class="slider-container">
            <input type="range" v-model="sliderValue" @input="updateSpeechBubble" min="0" max="100">
            
            <div class="speech-bubble" :style="{ left: `${sliderValue}%`, top: '25%' }">
              {{ sliderValue }}%
            </div>
            
              <button class="generateButton" @click="generateRiskLevel">Generate</button>
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

      generateRiskLevel() {
        this.$emit('slider-value-updated', this.sliderValue);
        this.closeSliderPopup();
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
    box-shadow: 0 10px 10px rgba(0, 0, 0, 0.2);
    padding-left: 1.5%;
    padding-right: 1.5%;
    text-align: center;
    z-index: 999;
    font-size: 100%;
    border-radius: 10px;
  }
  
  .popup-content {
    cursor: default; /* Prevent the cursor from changing when clicking inside the popup */
  }

  /* Slider */
  .slider-container {
    position: relative;
    margin-top: 0;
  }
  
  input[type="range"] {
  width: 100%;
  height:2vh;
  background: #272F51;
  -webkit-appearance: none; /* Remove default styles for WebKit browsers */
}

input[type="range"]::-webkit-slider-thumb {
  background: #587DBD; /* Set the color to #587DBD */
  height:2.7vh;
  width: 12%;
  border-radius: 10vh;
  -webkit-appearance: none;
}
input[type="range"]::-webkit-slider-thumb:hover {
  background: #79a3eb; /* Change the color to your desired color */
}

/* Slider */
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
  

/* Generate button */
  .generateButton {
  background-color: #272F51;
  color: #fff; 
  padding: 1.5% 7%; 
  border: none; 
  border-radius: 20vh; /* Add border radius */
  font-size: 100%; /* Set the font size */
  font-weight: bold;
  cursor: pointer; /* Add a pointer cursor on hover */
  margin-top:6%;
  margin-bottom: 6%
}

.generateButton:hover {
  background-color: #305ca8; /* Change the background color on hover */
}
  </style>
  