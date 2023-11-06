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
import { sendPasswordResetEmail } from "firebase/auth";
import { auth } from "./../../firebasefunc.js";
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

<style scope>
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

button {
  cursor: pointer;
  transition: all 0.3s ease;
}

button:hover {
  transform: translateY(-2px);
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
}

button:active {
  transform: translateY(1px);
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
