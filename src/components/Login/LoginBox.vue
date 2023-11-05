<template>
    <div class="container">
        
        <div class="titlecontainer">
            <div class="flex-item"> 
                <a href="#" v-bind:style="{color: (currentForm === 'login') ? 'lightblue' : 'white'}" @click.prevent="toggleForm('login')"> Login </a> 
            </div>
            <div class="flex-item"> 
                <a href="#" v-bind:style="{color: (currentForm === 'register') ? 'lightblue' : 'white'}"  @click.prevent="toggleForm('register')"> Sign Up </a> 
            </div>
        </div>

    <form v-if="currentForm === 'register'" class="register-form" @submit.prevent="signUp">
        <input type="email"    placeholder="Email"    required v-model="email">
        <input type="password" placeholder="Password" required v-model="password">
        <button class="SignwithGoogle" @click="signInWithGoogle"> Sign In With Google </button>
        <button>Sign Up</button>
    </form>

    <form v-else class="register-form" @submit.prevent="loginuser">
        <input type="email"    placeholder="Email"    required v-model="email">
        <input type="password" placeholder="Password" required v-model="password">
        <button class="SignwithGoogle" @click="signInWithGoogle"> Sign In With Google </button>
        <button>Login</button>
    </form>

        <a ref="#" class="flex-item" @click="togglePopup"> Forget Password ? </a>    

        <ForgetPasswordPopup v-show="this.buttonTrigger == true" @closepopupbox="togglePopup"> 
        </ForgetPasswordPopup> 


    </div>
</template>

<script> 
import ForgetPasswordPopup from './ForgetPassword.vue'
import {ref} from 'vue'
import firebase from '@/uifire.js'
import 'firebase/compat/auth'
import * as firebaseui from 'firebaseui'
import 'firebaseui/dist/firebaseui.css'
import {createUserWithEmailAndPassword,signInWithEmailAndPassword, GoogleAuthProvider, signInWithPopup} from "firebase/auth"
import {useRouter} from 'vue-router'
import { auth } from './../../firebasefunc.js'
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
    name: 'LoginBox',
    components: {
        ForgetPasswordPopup
    },
    data() {
        return {
            currentForm:'login',
            buttonTrigger: false,
            email:    '',
            password: ''
        }
    },
    methods: {
        toggleForm(params) {
            this.currentForm = params
        },

        togglePopup() {
            this.buttonTrigger = !this.buttonTrigger
        },

        signUp() {
            // register new user
            createUserWithEmailAndPassword(auth,this.email,this.password)
            .then((credential) => {
                // registered and signed in
                console.log(credential.user)
                this.$router.push('/portfolio');
            })
            .catch((error) => {
                console.log(error.code)
                alert(error.message)
            })
        },

        loginuser(){
            signInWithEmailAndPassword(auth,this.email,this.password)
            .then((credential) => {
                // registered and signed in
                console.log(credential.email);
                this.$router.push('/portfolio');
            })
            .catch((error) => {
                console.log(error.code)
                alert(error.message)
            })
        },

        signInWithGoogle(){
            const provider = new GoogleAuthProvider();
            signInWithPopup(auth,provider)
            .then((result) => {
                console.log(result.user)
                this.$router.push('/portfolio');
            })
            .catch((error)=>{
                console.log(error.code)
                alert(error.message)
            })
        }
    },

}


</script>
