<template>
  <Navigation />
  <div class="mainbody">

    <div class="LoginText">
      <p>Diversify Risk, Maximize Returns</p>
      <h2>Smartfolio</h2>
      <h3 class="loginH3">Simplicity meets Strategy</h3>
    </div>

    <LoginBox />
  </div>
</template>

<script>
import LoginBox from "@/components/Login/LoginBox.vue";
import Navigation from "@/components/Navigation.vue";
import { createUserWithEmailAndPassword } from "firebase/auth";
import { getAuth, onAuthStateChanged } from "firebase/auth";
export default {
  name: "Login",
  components: {
    LoginBox,
    Navigation,
  },
  mounted() {
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.useremail = auth.currentUser.email;
        this.isLoggedIn = true;
        this.displayName = auth.currentUser.email;
      }
    });
  },
};
</script>

<style>
.mainbody {
  background-image: linear-gradient(white, #6499ff);
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-self: center;
}

.LoginText {
  align-self: center;
  display: flex;
  flex-direction: column;
  height: 100vh;
  margin-top: 20vh;
}
p {
  font-size: 3vw;
  align-self: center;
  margin-bottom: 10px;
  font-family: Arial, Helvetica, sans-serif;
}
h2 {
  font-size: 7vw;
  align-self: center;
  margin-bottom: 0px;
}
.loginH3 {
  font-size: 2vw;
  align-self: center;
  margin-top: 1px;
}

.loginContainer {
  padding: 1.6vw;
  height: 70vh;
  width: 25%;
  background-color: #272f51;
  margin-top: 1.3%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
}

.titlecontainer {
  display: flex;
  justify-content: space-between;
}
.flex-item {
  padding: 30px;
  margin: 5px;
  font-size: 1.6vw;
  font-weight: bold;
  text-align: center;
  color: white;
}

form.register-form {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 80vh;
  width: 310px;
}
input {
  height: 40px;
  border-radius: 5px;
  font-size: 1.2vw;
  text-align: center;
}
input:nth-child(3) {
  font-size: 1.2vw;
  border-radius: 30px;
  width: 90%;
  height: 50px;
  align-self: center;
}

.SignwithGoogle {
  font-size: 1.2vw;
  border-radius: 35px;
  width: 290px;
  height: 70px;
  align-self: center;
  background-color: white;
}

.SignwithGoogle {
  display: inline-flex;
  align-content: center;
  justify-content: center;
  vertical-align: middle;
}

.SignwithGoogle > h2 {
  margin: 0;
  font-size: 1.5vw;
  vertical-align: middle;
}

a.flex-item {
  text-decoration: underline;
}

.flex-item {
  cursor: pointer;
}
.enterNext {
  font-size: 1.2vw;
  border-radius: 10px;
  width: 200px;
  height: 50px;
  align-self: center;
  background-color: #00ff7f;
}


@supports (font: -apple-system-body) and (-webkit-appearance: none) {
.loginContainer {
  height: 70vh;
  margin-top: 3%;
  background-color: #272f51;
  }
  .titlecontainer{
  margin-top: 5%;
  }
  form.register-form {
    height: 60vh;
    width: 17.5vw;
  }
  .SignwithGoogle {
  font-size: 1.2vw;
  border-radius: 35px;
  width: 17.5vwls
  ;
  height: 70px;
}
}

@media screen and (max-width: 800px) {
  .LoginText{
    visibility:hidden;
    width:0px;
    margin:0px
  }
  .loginContainer{
    margin:3%
  }
  .container {
    width: 40%;
  }
  form.register-form {
    width: 80%;
  }
  input {
    margin-left:10%;
    height: 30px;
    width: 50vw;
  }
  button {
    width: 50vw;
    height: 40px;
  }
  button.SignwithGoogle {
    width: 50vw;
    height: 40px;
  }
}



  
</style>