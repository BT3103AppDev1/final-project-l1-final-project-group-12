<template>
  <div class="profile_container">
    <!-- Header -->
    <div class="profileHeader">
      <button @click="closeProfilePage" class="back-button">←</button>
      <h1 class="profileHeader_main">My Profile</h1>
      <button @click="emitSignOut" class="logout-button">Log Out</button>
    </div>

    <!-- User Info -->
    <div class="profileUser">
      <img src="@/assets/logo/main.png" alt="" class="profileUser_picture" />
      <div id="profileUser_details">
        <h3 class="profileUser_details_email">
          Email: {{ user?.email || "No email" }}
        </h3>
      </div>
    </div>

    <!-- Action Items -->
    <div class="actionItems">
      <button
        class="actionButton"
        id="changePassword"
        @click="navigateToChangePassword"
      >
        Change Password
      </button>

      <button
        class="actionButton"
        id="deleteAccount"
        @click="navigateToDeleteAccount"
      >
        Delete Account
      </button>
    </div>
    <ChangePassword
      v-if="currentComponent === 'ChangePassword'"
      @close="handleComponentChange('ProfilePage')"
    />
    <DeleteAccount
      v-if="currentComponent === 'DeleteAccount'"
      @close="handleComponentChange('ProfilePage')"
    />
  </div>
</template>
  
<script>
import ChangePassword from "@/components/profile/ChangePassword.vue";
import DeleteAccount from "@/components/profile/DeleteAccount.vue";
import { getAuth, onAuthStateChanged } from "firebase/auth";

export default {
  name: "ProfilePage",
  components: {
    ChangePassword,
    DeleteAccount,
  },
  data() {
    return {
      showChangePassword: false,
      user: false,
    };
  },
  props: {
    isVisible: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    closeProfilePage() {
      this.$emit("closePopup");
    },
    emitSignOut() {
      this.$emit("signOut");
    },
    navigateToChangePassword() {
      this.$emit("changeComponent", "ChangePassword");
    },
    navigateToDeleteAccount() {
      this.$emit("changeComponent", "DeleteAccount");
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

.profileAllContent {
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.profileHeader {
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
.logout-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 3vh;
  font-weight: bold;
  font-family: "Inter", sans-serif;
  margin-left: auto;
}

.profileUser {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  margin-left: 8%;
}

.profileUser_picture {
  width: 80px;
  height: 80px;
  margin-left: auto;
  border-radius: 50%;
  border: 1px solid #333;
  margin: 3%;
  background-color: #272f51;
}

.profileUser_details {
  display: flex;
  align-items: center;
}

.profileUser_details_email {
  align-items: left;
  margin: 0;
  color: grey;
  font-size: 1.5vh;
}

.edit-button {
  background: none;
  border: none;
  cursor: pointer;
  margin-left: auto;
  margin-right: 20%;
  margin-bottom: auto;
  font-size: 1.2vw;
  width: 10%;
  height: 30%;
  vertical-align: middle;
}

.actionItems {
  flex-grow: 1;
}

.actionItems button {
  border: none;
  border-top: 1px solid #000000;
  border-radius: 0;
  display: block;
  width: 100%;
  height: 50%;
  font-size: 1.2vw;
  text-align: left;
  background: none;
  cursor: pointer;
}

.actionItems button:hover {
  background-color: #f2f2f2;
}

#deleteAccount {
  color: red;
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
  .logout-button {
    font-size: 1.75vh;
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
  .logout-button {
    font-size: 1.75vh;
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