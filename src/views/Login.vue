<template>
  <Navigation/>
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
import Navigation from '@/components/Navigation.vue';
import { createUserWithEmailAndPassword } from 'firebase/auth'
import { getAuth,onAuthStateChanged } from 'firebase/auth'
export default {
  name: 'Login',
  components: {
    LoginBox,
    Navigation
  },
  mounted(){
      const auth = getAuth()
      onAuthStateChanged(auth, (user) => {
        if (user) {
          this.useremail = auth.currentUser.email
          this.isLoggedIn= true
          this.displayName =  auth.currentUser.email
        }
  })
}


};
</script>

<style>

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
.container {
    padding: 1.6vw;
    height:70vh;
    width:350px;
    background-color: #272F51;
    margin-top:1.3%;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
  }
.titlecontainer{
  display: flex;
  justify-content: space-between;
}
.flex-item{
  padding:30px;
  margin:5px;
  font-size: 1.6vw;
  font-weight: bold;
  text-align: center;
  color: white;
}

form.register-form{
  display:flex;
  flex-direction: column;
  justify-content: space-around;
  height: 400px;
  width: 310px;

}
input{
  height:40px;
  border-radius: 5px;
  font-size: 1.2vw;
  text-align: center;
}
    input:nth-child(3){
      font-size: 1.2vw;
      border-radius: 30px;
      width: 90%;
      height: 50px;
      align-self: center;
    }

.SignwithGoogle{
  font-size: 1.2vw;
  border-radius: 35px;
  width: 290px;
  height: 70px;
  align-self: center;
  background-color: white;
}
a.flex-item{
  text-decoration: underline;
}

</style>