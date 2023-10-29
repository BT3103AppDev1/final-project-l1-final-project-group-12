<template>
  <div class="user-profile">

    <img src="@/assets/editIcon.png" class="user-image" />

    <div class="user-details">
      
      <div class="user-info">
        <div class="username">JohnDoe</div>
        
        <img src="@/assets/editIcon.png" class="edit-button" @click="editProfile" />
      </div>
        
      <div class="email">john.doe@example.com</div>

    </div>

  </div>
</template>

<script>
export default {
  methods: {
    editProfile() {
      // Add your logic for handling the edit image button click here
    },
  },
};
</script>

<style>
/* Your component-specific styles here */

.user-profile {
  display: flex;
  align-items: center;
  margin-top: 3%;
}

.user-image {
  width: 30%;
  height: 30%;
  border-radius: 50%;
  margin-right: 6%;
  box-shadow: 6px 6px 6px rgba(0, 0, 0, 0.1);

}

.user-details {
  display: flex;
  flex-direction: column;
}

.user-info {
  display: flex;
  align-items: center;
}

.username {
  font-weight: bold;
  font-size: 150%;
}

.edit-button {
  width: 5%;
  height: 5%;
  margin-left: auto;
  cursor: pointer;
  margin-bottom: 9%;
}

.edit-button:hover {
  transform: scale(1.2);
}

.email {
  color: #828282;
  font-weight: bold;
  font-size: 150%;
}
</style>
