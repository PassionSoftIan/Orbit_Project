<template>
  <div>
    <h1>Sign Up</h1>
      <label for="username">username: </label>
      <input type="text" id="username" v-model="username">
      <br>
      <br>
      <label for="password1">password: </label>
      <input type="password" id="password1" v-model="password1">
      <br>
      <br>
      <label for="password2">username: </label>
      <input type="password" id="password2" v-model="password2">
      <br>
      <br>
      <button @click="signUp">회원가입</button>
    <button @click="OnClick">login</button>
  </div>
</template>

<script>
export default {
  name: "SignUp",
  data(){
    return {
      username: "",
      password1: "",
      password2: "",
    }
  },
  methods: {
    signUp(){
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    },
    OnClick(){
      this.$emit("logIn")
    }
  }

}
</script>

<style>

</style>