<template>
  <div class="profile-container">
    <component
      :is="currentComponent"
      @changeComponent="handleChangeComponent"
      @closePopup="handleClose"
      @signOut="emitSignOut"
      @accountDeleted="emitSignOut"
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
      console.log("");
      this.emitSignOut();
    },
  },
};
</script>

