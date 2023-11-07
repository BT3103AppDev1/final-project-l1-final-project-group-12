<template>
  <div class="password_container">
    <!-- Header -->
    <div class="passwordHeader">
      <button @click="closeChangePassword" class="back-button">←</button>
      <h1 class="passwordHeader_main">Change Password</h1>
    </div>

    <!-- Password Form -->
    <div class="profilePasswords">
      <img src="@/assets/logo/main.png" alt="" class="profileUser_picture" />
      <div v-if="isOAuthUser">
        <p class="oauth-message">
          It looks like you've signed in using a social account. To change your
          password, please visit your social account's settings page.
        </p>
      </div>
      <form @submit.prevent="changePassword" class="password-form">
        <div class="form-group">
          <label for="newPassword">New Password</label>
          <input
            id="newPassword"
            type="password"
            v-model="newPassword"
            :disabled="isOAuthUser"
            required
          />
        </div>
        <div class="form-group">
          <label for="confirmPassword">Confirm New Password</label>
          <input
            id="confirmPassword"
            type="password"
            v-model="confirmPassword"
            :disabled="isOAuthUser"
            required
          />
        </div>
        <button
          type="submit"
          class="submit_ChangePassword"
          :disabled="isOAuthUser"
        >
          Update Password
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import {
  getAuth,
  reauthenticateWithCredential,
  EmailAuthProvider,
  updatePassword,
} from "firebase/auth";

export default {
  props: {
    profilePicture: {
      type: String,
      default: "@/assets/logo/main.png",
    },
  },
  data() {
    return {
      newPassword: "",
      confirmPassword: "",
      isOAuthUser: false,
    };
  },
  created() {
    this.checkAuthProvider();
  },
  methods: {
    closeChangePassword() {
      this.$emit("changeComponent", "ProfilePage");
    },
    checkAuthProvider() {
      const auth = getAuth();
      const user = auth.currentUser;
      if (user) {
        // Check if the user signed in using an OAuth provider
        const providerData = user.providerData;
        this.isOAuthUser = providerData.some(
          (provider) => provider.providerId !== "password"
        );
      }
    },
    async changePassword() {
      const auth = getAuth();
      const user = auth.currentUser;

      if (user) {
        try {
          if (this.newPassword != this.confirmPassword) {
            alert("Passwords do not match");
          } else {
            await updatePassword(user, this.newPassword);
            alert("Password updated successfully!");
          }
          this.closeChangePassword();
        } catch (error) {
          // Handle errors here, such as re-authentication if needed or showing a message for weak password
          alert(error.message);
        }
      } else {
        // No user is signed in.
        alert("No user is signed in to update the password.");
      }
    },
  },
};
</script>


<style scoped>
.password_container {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 45%;
  height: 40%;
  max-width: 80%;
  max-height: 100%;
  background-color: white;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  z-index: 1000;
  font-family: "Inter", sans-serif;
  overflow: auto;
}

.passwordHeader {
  flex-grow: 0.5;
  flex-shrink: 1.2;
  display: flex;
  align-items: center;
}

.passwordHeader_main {
  text-align: left;
  font-size: 3vh;
}

.profilePasswords {
  flex-shrink: 1.2;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 100%;
  margin: 0 auto;
}

.back-button {
  width: 5vw;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 3rem;
  text-align: left;
  vertical-align: middle;
  margin-right: 1%;
}
.profileUser_picture {
  width: 10%;
  height: 10%;
  margin-left: auto;
  border-radius: 50%;
  border: 1px solid #333;
  margin: 3%;
  background-color: #272f51;
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.form-group label {
  min-width: 50%;
  display: block;
  margin-bottom: 5px;
}

.form-group input {
  box-sizing: border-box;
  padding: 10px;
}

.form-group input,
.submit_ChangePassword {
  word-wrap: break-word;
}

.submit_ChangePassword {
  font-size: 1.2vw;
  border-radius: 10px;
  width: 200px;
  height: 50px;
  align-self: center;
  color: white;
  background-color: #272f51;
}

.oauth-message {
  font-size: 1.2vw;
  color: red;
}

/* Dynamic Media Queries for various devices */
@media (max-width: 600px) {
  .passwordHeader {
    height: 5vh;
  }
  .passwordHeader_main {
    margin: none;
    text-align: left;
    font-size: 1.5vh;
  }
  .back-button {
    font-size: 1.5vh;
  }
  .logout-button {
    font-size: 1.75vh;
  }
  .profileUser_picture {
    width: 1.5vh;
    height: 1.5vh;
  }
  .submit_ChangePassword {
    font-size: 1.75vh;
  }
}

@media (max-width: 1200px) {
  .passwordHeader {
    height: 5vh;
  }
  .passwordHeader_main {
    margin: none;
    text-align: left;
    font-size: 1.5vh;
  }
  .back-button {
    font-size: 1.5vh;
  }
  .logout-button {
    font-size: 1.75vh;
  }
  .profileUser_picture {
    width: 1.5vh;
    height: 1.5vh;
  }
  .submit_ChangePassword {
    font-size: 1.75vh;
  }
}
</style>