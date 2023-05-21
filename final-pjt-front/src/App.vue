<template>
  <div v-if="isAuthenticated">
    <BaseView />
  </div>
  <div v-else>
    <LoginView v-show="!isSignUp" @signUp="toggle"/>
    <SignUpView v-show="isSignUp" @logIn="toggle"/>
  </div>
</template>

<script>
import BaseView from "@/views/BaseView.vue"
import LoginView from "@/views/LoginView.vue"
import SignUpView from "@/views/SignUpView.vue"

export default {
  components: {
    BaseView,
    LoginView,
    SignUpView,
  },
  data() {
    return {
      isSignUp: false,
    }
  },
  methods: {
    toggle(){
      this.isSignUp=!this.isSignUp
    },
  },
  computed: {
    isAuthenticated(){
      return this.$store.state.Token
    }
  }
}
</script>

<style>

</style>