<template>
  <div>
    <div v-if="showPopup" class="popup" @click.stop="">
      <div class="popup-content" @click.stop="">
        <h3>Specify Risk</h3>
        <div class="slider-container">
          <input type="range" v-model="sliderValue" @input="updateSpeechBubble" min="0" max="100">
          <div class="speech-bubble" :style="{ left: `${sliderValue}%`, top: '25px' }">
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
    };
  },
  methods: {
    closeSliderPopup() {
      this.$emit('closePopup'); 
    },
    
    handleDocumentClick(event) {
      this.clickCount++;

      // Check if the click occurred outside the popup
      if (!this.$el.contains(event.target) && this.clickCount >= 2) {
        this.closeSliderPopup();
      }
    },
    
  },
  mounted() {
    // Attach a click event listener to the document if the popup is visible
    if (this.showPopup) {
      document.addEventListener('click', this.handleDocumentClick);
    }
  },
  beforeUnmount() {
    // Remove the click event listener when the component is unmounted
    document.removeEventListener('click', this.handleDocumentClick);
  },
  
};
</script>


<style scoped>
.popup {
  position: absolute;
  top: 50px;
  left: 50%;
  transform: translateX(-50%);
  width: 300px;
  background-color: #fff;
  border: 1px solid #ccc;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 20px;
  text-align: center;
  z-index: 999;
}

.popup-content {
  cursor: default; /* Prevent the cursor from changing when clicking inside the popup */
}

.slider-container {
  position: relative;
  margin-top: 20px;
}

input[type="range"] {
  width: 100%;
}

.speech-bubble {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  padding: 5px 10px;
  background-color: #333;
  color: #fff;
  border-radius: 5px;
  font-size: 14px;
  display: block;
}

button {
  margin-top: 10px;
}
</style>
