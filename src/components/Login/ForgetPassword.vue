<template>
  <div class="popup">
    <div class="inner-popup">
      <center class="buttonContainer">
        <button
          class="closeButton"
          aria-label="Dismiss alert"
          type="button"
          @click="closepopup"
        >
          <span aria-hidden="true">&times;</span>
        </button>
      </center>

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
import { sendPasswordResetEmail } from "firebase/auth";
import { auth } from "../../usersController.js";
import { ref } from "vue";
const email = ref("");

export default {
  name: "ForgetPasswordPopup",
  emits: ["closepopupbox"],
  data() {
    return {
      email: "", // Define the email property
      errorMessage: "", // Define the errorMessage property
    };
  },
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

<style>
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
.popup-close {
  height: 6vh;
  width: 70%;
  color: white;
  font-size: 2vw;
  border-radius: 2vh;
  background-color: #272f51;
  width: 75%;
}

.popup-close:hover {
  transform: translateY(-2px);
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
}

.buttonContainer {
  align-items: right;
  margin-left: 100%;
}

.close-button {
  height: 100px;
  width: 20px;
  color: black;
  font-size: 1vw;
  background-color: white;
}

.close-button:hover {
  transform: translateY(-2px);
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
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
</style>
