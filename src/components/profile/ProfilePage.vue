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
        <h3 class="profileUser_details_name">Username</h3>
        <h3 class="profileUser_details_email">Email@email.com</h3>
      </div>

      <button class="edit-button">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="25"
          height="25"
          fill="currentColor"
          class="bi bi-pencil-square"
          viewBox="0 0 16 16"
        >
          <path
            d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
          />
          <path
            fill-rule="evenodd"
            d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
          />
        </svg>
      </button>
    </div>

    <!-- Action Items -->
    <div class="actionItems">
      <button class="actionButton" id="changePassword">Change Password</button>
      <button class="actionButton" id="deleteAccount">Delete Account</button>
    </div>
  </div>
</template>
  
<script>
export default {
  props: {
    isVisible: {
      type: Boolean,
      default: false,
    },
    userName: String,
    userEmail: String,
    profilePicture: String,
  },
  methods: {
    closeProfilePage() {
      this.$emit("close");
    },
    // signOut() {
    //   const auth = getAuth();
    //   firebaseSignOut(auth).then(() => {
    //     // User signed-out
    //     this.isLoggedIn = false;
    //     this.displayName = "";
    //     this.$router.push("/login");
    //   });
    closeProfilePage() {
      this.$emit("close");
    },
    emitSignOut() {
      this.$emit("signOut");
    },
    changePassword() {
      // Implement password change logic
    },
    deleteAccount() {
      // Implement account deletion logic
    },
  },
};
</script>


<style scoped>
.profile_container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: fixed; /* or absolute, depending on context */
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 45%; /* 2/3 of the page */
  height: 40%;
  max-width: 80%; /* You can set a max-width to ensure it doesn't get too wide on larger screens */
  max-height: 80%;
  background-color: white;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* Optional: Adds a shadow for better visibility */
  z-index: 1000; /* Ensure it's above other content */
  font-family: "Inter", sans-serif;
}

.profileAllContent {
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.profileHeader {
  flex-grow: 1;
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.profileHeader_main {
  text-align: left;
}

.back-button {
  width: 5vw;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 3rem;
  text-align: left;
  vertical-align: middle;
}
.logout-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.5rem;
  font-weight: bold;
  font-family: "Inter", sans-serif;
  margin-left: auto;
}
.profileUser {
  flex-grow: 0.5;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  margin-left: 8%;
}

.profileUser_picture {
  width: 80px; /* Adjust size as needed */
  height: 80px; /* Adjust size as needed */
  margin-left: auto;
  border-radius: 50%;
  border: 1px solid #333;
  margin: 3%;
}

.profileUser_details {
  display: flex;
  align-items: center;
}

.profileUser_details_name {
  margin: 0;
  font-size: 1rem; /* Adjust size as needed */
}

.profileUser_details_email {
  align-items: left;
  margin: 0;
  color: grey; /* Adjust color as needed */
  font-size: 1rem;
}

.edit-button {
  background: none;
  border: none;
  cursor: pointer;
  margin-left: auto;
  margin-right: 20%;
  margin-bottom: auto;
  font-size: 1.5rem;
}

.actionItems {
  flex-grow: 1;
}

.actionItems button {
  border: none; /* Removes all default borders */
  border-top: 1px solid #000000; /* Adds just a top border */
  border-radius: 0; /* Removes rounded corners */
  display: block;
  width: 100%;
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
  .profileUser_details_name {
    font-size: 0.75rem;
  }
}

@media (min-width: 1200px) {
  .profileUser_details_name {
    font-size: 1.25rem;
  }
}
</style>