<template>
  <div class="container">
    <div class="titlecontainer">
      <div class="flex-item">
        <a
          href="#"
          v-bind:style="{
            color: currentForm === 'login' ? 'lightblue' : 'white',
          }"
          @click.prevent="toggleForm('login')"
        >
          Login
        </a>
      </div>
      <div class="flex-item">
        <a
          href="#"
          v-bind:style="{
            color: currentForm === 'register' ? 'lightblue' : 'white',
          }"
          @click.prevent="toggleForm('register')"
        >
          Sign Up
        </a>
      </div>
    </div>

    <form
      v-if="currentForm === 'register'"
      class="register-form"
      @submit.prevent="signUp"
    >
      <input type="email" placeholder="Email" required v-model="email" />
      <input
        type="password"
        placeholder="Password"
        required
        v-model="password"
      />
      <button class="SignwithGoogle" @click="signInWithGoogle">
        Sign In With Google
      </button>
      <button>Sign Up</button>
    </form>

    <form v-else class="register-form" @submit.prevent="loginuser">
      <input type="email" placeholder="Email" required v-model="email" />
      <input
        type="password"
        placeholder="Password"
        required
        v-model="password"
      />
      <button class="SignwithGoogle" @click="signInWithGoogle">
        Sign In With Google
      </button>
      <button>Login</button>
    </form>

    <a ref="#" class="flex-item" @click="togglePopup"> Forget Password ? </a>

    <ForgetPasswordPopup
      v-show="this.buttonTrigger == true"
      @closepopupbox="togglePopup"
    >
    </ForgetPasswordPopup>
  </div>
</template>

<script>
import ForgetPasswordPopup from "./ForgetPassword.vue";
import { ref } from "vue";
import firebase from "@/uifire.js";
import "firebase/compat/auth";
import * as firebaseui from "firebaseui";
import "firebaseui/dist/firebaseui.css";
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  GoogleAuthProvider,
  signInWithPopup,
} from "firebase/auth";
import { useRouter } from "vue-router";
import { auth } from "./../../usersController.js";
const errMsg = ref("");

// var ui = firebaseui.auth.AuthUI.getInstance()
// if (!ui) {
//     ui = new firebaseui.auth.AuthUI(firebase.auth())
// }
// var uiConfig = {
//     signInSuccessUrl: 'home',
//     signInOptions: [
//     firebase.auth.GoogleAuthProvider.PROVIDER_ID,
//     firebase.auth.EmailAuthProvider.PROVIDER_ID
//     ]
// }
// ui.start('#firebaseui-auth-container', uiConfig)

export default {
  name: "LoginBox",
  components: {
    ForgetPasswordPopup,
  },
  data() {
    return {
      currentForm: "login",
      buttonTrigger: false,
      email: "",
      password: "",
    };
  },
  methods: {
    toggleForm() {
      this.currentForm = this.currentForm === "login" ? "register" : "login";
    },

    togglePopup() {
      this.buttonTrigger = !this.buttonTrigger;
    },

    signUp() {
      // register new user
      createUserWithEmailAndPassword(auth, this.email, this.password)
        .then((credential) => {
          // registered and signed in
          console.log(credential.user);
          this.$router.push("/portfolio");
        })
        .catch((error) => {
          console.log(error.code);
          alert(error.message);
        });
    },

    loginuser() {
      signInWithEmailAndPassword(auth, this.email, this.password)
        .then((credential) => {
          // registered and signed in
          console.log(credential.email);
          this.$router.push("/portfolio");
        })
        .catch((error) => {
          console.log(error.code);
          alert(error.message);
        });
    },

    signInWithGoogle() {
      const provider = new GoogleAuthProvider();
      signInWithPopup(auth, provider)
        .then((result) => {
          console.log(result.user);
          this.$router.push("/portfolio");
        })
        .catch((error) => {
          console.log(error.code);
          alert(error.message);
        });
    },
  },
};
</script>


<style scoped>
.container {
  padding: 1.6vw;
  height: 70vh;
  width: 350px;
  /* background-color: #272F51; */
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
  height: 400px;
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

button {
  font-size: 1.2vw;
  border-radius: 10px;
  width: 200px;
  height: 50px;
  align-self: center;
  background-color: #00ff7f;
}
button.SignwithGoogle {
  font-size: 1.2vw;
  border-radius: 35px;
  width: 290px;
  height: 70px;
  align-self: center;
  background-color: white;
}
a.flex-item {
  text-decoration: underline;
}
</style>