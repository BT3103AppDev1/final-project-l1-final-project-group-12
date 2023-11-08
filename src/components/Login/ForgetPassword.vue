<template>
  <div class="popup">
    <div class="inner-popup">
      <button
        class="close-button"
        aria-label="Dismiss alert"
        type="button"
        @click="closepopup"
      >
        <span aria-hidden="true">&times;</span>
      </button>

      <slot />
      <p class="InsertEmail">
        Please enter the email
        <span class="break-point">you used to register your account</span>
      </p>
      <input
        class="InsertEmail"
        type="email"
        v-model="email"
        placeholder="Key in your email"
      />
      <button class="popup-close" @click="requestPasswordReset">
        Request Password Reset
      </button>
      <p class="QuestionsText">
        Questions? Email us at helpdesk@smartfollio.com
      </p>
      <p v-if="errorMessage">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
// import '@/style/Login/Login.css'
import { sendPasswordResetEmail } from "firebase/auth";
import { auth } from "./../../usersController.js";
import { ref } from "vue";
const email = ref("");

export default {
  name: "ForgetPasswordPopup",
  emits: ["closepopupbox"],
  methods: {
    closepopup() {
      this.$emit("closepopupbox", false);
    },
    requestPasswordReset() {
      sendPasswordResetEmail(auth, this.email)
        .then((link) => {
          this.$emit("closepopupbox", false);
          // this.$parent.$options.methods.togglePopup()
        })
        .catch((error) => {
          const errorMessage = error.message;
          console.log(errorMessage);
        });
    },
  },
};
</script>

<style scoped>
.popup {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 99;
  background-color: rgba(0, 0, 0, 0.2);

  display: flex;
  align-items: center;
  justify-content: center;
}

.inner-popup {
  background-color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  padding: 32px;
  height: 40vh;
  width: 80vh;
}
button.popup-close {
  height: 6vh;
  width: 70%;
  color: white;
  font-size: 2vw;
  border-radius: 2vh;
  background-color: #272f51;
  width: 75%;
}
button.close-button {
  height: 30px;
  width: 30px;
  margin-left: 90%;
  color: black;
  font-size: 1vw;
  background-color: white;
}
.InsertEmail {
  margin-top: 0px;
  margin-bottom: 0px;
  font-size: 2vw;
  text-align: center;
  width: 75%;
}
.QuestionsText {
  font-size: 1.5vw;
  color: #7e7e7e;
  margin-top: 0px;
  margin-bottom: 0px;
}
.break-point::before {
  content: "\a";
  display: block;
}

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