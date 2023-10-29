<template>
  <div class="profile-popup">
    <div class="profile-popup-content">
      <div class="header">
        <img src="@/assets/arrowIcon.png" class="close-button" @click="closeProfile" />
        <h1 class="profile-title">{{ header }}</h1>
        
        <button class="logout-button" @click="logout" v-if="showUserProfile">Log out</button>

      </div>

      <div class="user-profile-container" v-if="showUserProfile">
        <UserProfile />
      </div>

      <div class="button-container" v-if="showUserProfile">
        <button class="popup-button" @click="showChangePassword">Change Password</button>
        <button class="popup-button" @click="showDeleteAccount">Delete Account</button>
      </div>

      <div v-else>
        <EditProfile/>
      </div>

    </div>
  </div>
</template>

<script>
import UserProfile from '@/components/Profile/UserProfile.vue';
import EditProfile from '@/components/Profile/EditProfile.vue';

export default {
  components: {
    UserProfile,
    EditProfile
  },

  data() {
    return {
      showUserProfile: true,
      header: 'My Profile',
      changePasswordAction: false,
      deleteAccountAction: false,
      editProfileAction: false,
    };
  },

  methods: {
    closeProfile() {
      this.$emit('close'); // Emit an event to close the profile popup
    },

    logout() {
      // Add your logout logic here
    },

    showChangePassword() {
      this.editProfile();
      this.header = 'Change Password';
      this.changePasswordAction = true;
    },

    showDeleteAccount() {
      this.editProfile();
      this.header = 'Delete Account';
      this.deleteAccountAction = true;
    },

    editProfile() {
      this.updateUserProfile();
      this.header = 'Edit Profile';
      this.editProfileAction = true;
    },

    updateUserProfile() {
      this.showUserProfile = false;
    }

  },
};
</script>

<style>
/* Your component-specific styles here */

.header {
  display: flex;
  align-items: center; /* Align items vertically */
}

.close-button {
  /* Style the close button image */
  cursor: pointer;
  width: 5%;
  height: 3%;
  margin-right: 2%;
}

.close-button:hover {
  transform: scale(1.2); /* Scale up the button on hover */
}

.profile-title {
  
}

.logout-button {
  background: none;
  border: none;
  cursor: pointer;
  font-weight: bold;
  font-size: 150%;
  margin-left: auto;
  padding: 0;
}

.logout-button:hover {
  color: #c6c6c6; /* Change the text color on hover */
}

.profile-popup {
  /* Style the background overlay */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999; /* Adjust the z-index to control the overlay's visibility */
}

.profile-popup-content {
  /* Style the profile popup content */
  background: #fff;
  height: 70%;
  width: 60%;
  padding: 2%;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.user-profile-container {
  display: flex;
  flex-direction: column;
  margin-left: 10%;
}

.button-container {
  display: flex;
  flex-direction: column; /* Stack the buttons on top of each other */
  align-items: center; /* Center the buttons horizontally */
  margin-top: 4%; /* Add spacing between the buttons and user profile */
  justify-content: flex-end;
  flex: 1;
  flex-direction: column;
}

.popup-button {
  background: none; /* Remove background color */
  border: 0.3vh solid #d2d2d2; /* Add a border with your desired color */
  padding: 4% 7%; /* Add padding to the button (0 on left and right, effectively stretching it) */
  padding-bottom: 6%;
  width: 100%; /* Make the button stretch the whole width */
  text-align: left; /* Center the button text */
  justify-content: center;
  cursor: pointer;
  border-right: none;
  border-left: none;
  border-radius: 0;
  font-weight: bold;
  font-size: 130%;
}

.popup-button:hover {
  background-color: #c9c9c9; /* Change the background color on hover */
}

.popup-button:last-child {
  border: none;
}
</style>
