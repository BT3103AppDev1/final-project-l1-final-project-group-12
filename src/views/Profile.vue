<template>
  <div class="profile-container">
    <component
      :is="currentComponent"
      @changeComponent="handleChangeComponent"
      @closePopup="handleClose"
      @signOut="emitSignOut"
      @accountDeleted="handleAccountDeleted"
    />
  </div>
</template>

<script>
import ProfilePage from "@/components/profile/ProfilePage.vue";
import DeleteAccount from "@/components/profile/DeleteAccount.vue";
import ChangePassword from "@/components/profile/ChangePassword.vue";

export default {
  components: {
    ProfilePage,
    DeleteAccount,
    ChangePassword,
  },
  data() {
    return {
      currentComponent: "ProfilePage",
    };
  },
  methods: {
    handleClose() {
      console.log("Profile hit for close");
      this.$emit("close");
    },
    handleChangeComponent(component) {
      this.currentComponent = component;
    },
    emitSignOut() {
      this.$emit("requestSignOut");
    },
    handleAccountDeleted() {
      this.emitSignOut(); // Sign out the user
      this.$emit("close"); // Close the Profile popup
    },
  },
};
</script>

