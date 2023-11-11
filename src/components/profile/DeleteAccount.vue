<template>
  <div class="profile_container">
    <!-- Header -->
    <div class="profileHeader">
      <button @click="closeDeleteAccount" class="back-button">←</button>
      <h1 class="profileHeader_main">Delete Account</h1>
    </div>

    <!-- User Info -->
    <div class="profileUser">
      <img src="@/assets/logo/main.png" alt="" class="profileUser_picture" />
      <div id="profileUser_details">
        <h3 class="profileUser_details_email">
          {{ user?.email || "No email" }}
        </h3>
      </div>
    </div>
    <h4 class="warningHeader">
      We would store your trades data for up to 3 days, but this action cannot
      be reversed!! <br />Are you sure?
    </h4>
    <button @click="deleteAccount" class="deleteAccount">Delete</button>
  </div>
</template>

<script>
import { getAuth, deleteUser, onAuthStateChanged } from "firebase/auth";
import { getFirestore, deleteDoc, doc } from "firebase/firestore";

export default {
  props: {
    profilePicture: {
      type: String,
      default: "@/assets/logo/main.png",
    },
  },
  data() {
    return {
      user: false,
    };
  },
  methods: {
    closeDeleteAccount() {
      this.$emit("changeComponent", "ProfilePage");
    },
    async deleteAccount() {
      const auth = getAuth();
      const db = getFirestore();
      const user = auth.currentUser;

      if (user) {
        try {
          this.$emit("accountDeleted");
          await deleteUser(user);

          console.log("Account deleted successfully");
        } catch (error) {
          if (error.code === "auth/requires-recent-login") {
            alert(
              "Please log in again to verify your identity before deleting your account."
            );
          }
          this.$emit("accountDeletionFailed", error);
          console.error("Error deleting account:", error);
        }
      } else {
        console.error("No user is signed in.");
      }
    },

    created() {
      const auth = getAuth();
      onAuthStateChanged(auth, (user) => {
        if (user) {
          this.user = user;
        } else {
          this.user = null;
        }
      });
    },
  },
  mounted() {
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.user = user;
      }
    });
  },
};
</script>

<style scoped>
.profile_container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-content: center;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 45%;
  height: 40%;
  max-width: 80%;
  max-height: 80%;
  background-color: white;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  z-index: 1000;
  font-family: "Inter", sans-serif;
  overflow: auto;
}

.profileHeader {
  flex-grow: 0.5;
  display: flex;
  align-items: center;
}

.profileHeader_main {
  text-align: left;
  font-size: 3vh;
}

.back-button {
  width: 5vw;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 5vh;
  text-align: left;
  vertical-align: middle;
  margin-right: 1%;
}

.profileUser {
  width: 100%;
  text-align: center;
}

.profileUser_picture {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 1px solid #333;
  background-color: #272f51;
}

.profileUser_details {
  display: flex;
  align-items: center;
}

.profileUser_details_email {
  align-items: center;
  color: #272f51;
  font-size: 3vh;
}
.warningHeader {
  font-size: 1vw;
  color: red;
  text-align: center;
}

.deleteAccount {
  font-size: 1.2vw;
  border-radius: 10px;
  width: 200px;
  height: 50px;
  align-self: center;
  color: white;
  background-color: red;
}

/* Dynamic Media Queries for various devices */
@media (max-width: 600px) {
  .profileHeader {
    height: 5vh;
  }
  .profileHeader_main {
    margin: none;
    text-align: left;
    font-size: 1.5vh;
  }
  .back-button {
    font-size: 1.5vh;
  }
  .profileUser_picture {
    width: 1.5vh;
    height: 1.5vh;
  }
  .profileUser_details_email {
    font-size: 1vh;
  }
  .actionItems button {
    font-size: 1.75vh;
  }
}

@media (max-width: 1200px) {
  .profileHeader {
    height: 5vh;
  }
  .profileHeader_main {
    margin: none;
    text-align: left;
    font-size: 1.5vh;
  }
  .back-button {
    font-size: 1.5vh;
  }
  .profileUser_picture {
    width: 1.5vh;
    height: 1.5vh;
  }
  .profileUser_details_email {
    font-size: 1vh;
  }
  .actionItems button {
    font-size: 1.75vh;
  }
}
</style>