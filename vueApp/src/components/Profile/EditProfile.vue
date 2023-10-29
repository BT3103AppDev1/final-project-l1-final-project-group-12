<template>
    <div class="action-content">
      <img src="@/assets/crossIcon.png" class="action-image" />
      <p class="action-description">Change your account password.</p>
  
      <div class="input-container">
        <div class="input-header">Current Password: </div>
        <input type="password" v-model="topBox" placeholder="Enter your current password" />
      </div>
  
      <div class="input-container">
        <div class="input-header">New Password: </div>
        <input type="password" v-model="bottonbox" placeholder="Enter your new password" />
      </div>
  
      <div class="button-container1">
        <button class="submit-button" @click="submit">Submit</button>
        <button class="cancel-button" @click="cancel">Cancel</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        topBox: "",
        bottonbox: "",
      };
    },
    methods: {
      submit() {
        // Add your submit logic here
      },
      cancel() {
        // Add your cancel logic here
      },
    },
  };
  </script>
  
  <style scoped>
  .action-content {
    text-align: center;
  }
  
  .action-image {
    width: 15%;
    border-radius: 50%;
  }
  
  .action-description {
    font-size: 120%;
    margin: 0.3%;
    font-weight: bold;
  }
  
  .input-container {
    margin: 2.5%;
    display: flex;
    justify-content: right;
    align-items: center; 
    margin-right:20%
  }
  
  .input-header {
    font-weight: bold;
    font-size: 120%;
    margin-right:3%;
  }
  
  input {
    width: 70%;
    border-radius: 10px;
    border: none;
  }

  input::placeholder {
    font-weight: bold; /* You can set the font-weight as needed */
    font-size: 120%;
  }
  
  .button-container1 {
    display: flex;
    justify-content: center;
    margin-top: 2%;
  }
  
  .submit-button,
  .cancel-button {
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    margin: 0 5%;
    margin-top:3%;
    box-shadow: 6px 6px 8px rgba(0, 0, 0, 0.5);
    border-radius: 19px;
    font-weight: bold;
  }

  .submit-button {
    color: white;
    background: #272F51;
  }
  
  .cancel-button {
    color: black;
    background: #EFEFEF;
  }

  .submit-button:hover,
  .cancel-button:hover {
    opacity: 0.8;
  }
  </style>
  