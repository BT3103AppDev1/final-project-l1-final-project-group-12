<template>
  <div class="container">
    <div class="titlecontainer">
      <div class="flex-item">
        <a 
          href="#"
          v-bind:style="{
            color: currentForm === 'login' ? '#38D3B4' : 'white',
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
            color: currentForm === 'register' ? '#38D3B4' : 'white',
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
        <svg
          xmlns="http://www.w3.org/2000/svg"
          x="0px"
          y="0px"
          width="50"
          height="50"
          viewBox="0 0 48 48"
        >
          <path
            fill="#FFC107"
            d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"
          ></path>
          <path
            fill="#FF3D00"
            d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"
          ></path>
          <path
            fill="#4CAF50"
            d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"
          ></path>
          <path
            fill="#1976D2"
            d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"
          ></path>
        </svg>
        <h2>Login with Google</h2>
      </button>
      <button class="custom-button">Sign Up</button>
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
        <svg
          xmlns="http://www.w3.org/2000/svg"
          x="0px"
          y="0px"
          width="50"
          height="50"
          viewBox="0 0 48 48"
        >
          <path
            fill="#FFC107"
            d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"
          ></path>
          <path
            fill="#FF3D00"
            d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"
          ></path>
          <path
            fill="#4CAF50"
            d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"
          ></path>
          <path
            fill="#1976D2"
            d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"
          ></path>
        </svg>
        <h2>Login with Google</h2>
      </button>
      <button class = "custom-button" >Login</button>
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
import { auth } from "./../../firebasefunc.js";
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
    toggleForm(params) {
      this.currentForm = params;
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
          auth;
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
.SignwithGoogle {
  cursor: pointer;
  transition: all 0.3s ease;
}

.SignwithGoogle:hover {
  transform: translateY(-2px);
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
}

.SignwithGoogle:active {
  transform: translateY(1px);
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
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

.flex-item {
  cursor: pointer;
}


@media screen and (max-width: 800px) {
svg {
  height: 30px;
  width:30px
}
}
</style>
