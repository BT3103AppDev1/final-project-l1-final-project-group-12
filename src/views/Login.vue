<template>
    <div class="mainbody">
  
      <div class="LoginText">
        <p> Diversify Risk, Maximize Returns </p>
        <h2> Smartfolio</h2>
        <h3> Simplicity meets Strategy </h3>
      </div>
      
     <LoginBox/>
    </div>
    </template>
  
  <script>
  import LoginBox from '@/components/Login/LoginBox.vue'
  import { createUserWithEmailAndPassword } from 'firebase/auth'
  import { getAuth } from 'firebase/auth'
  export default {
    name: 'Login',
    components: {
      LoginBox
    },
    methods: {
    }
  
  
  };
  </script>
  
  <style scoped>
  
  .mainbody {
    background-image: linear-gradient(white, #6499FF);
    height:100vh;
    display: flex;
    flex-direction:row;
    justify-content: space-around;
    align-self: center;
  }
  .LoginText{
    align-self: center;
    display: flex;
    flex-direction:column;
    height:100vh;
    margin-top: 300px;
  
  }
  p{
    font-size: 3vw;
    align-self: center;
    margin-bottom: 10px;
    font-family: Arial, Helvetica, sans-serif;
  
  }
  h2{
    font-size: 7vw;
    align-self: center;
    margin-bottom: 0px;
  }
  h3{
    font-size: 2vw;
    align-self: center;
    margin-top: 1px;
  }
  </style>