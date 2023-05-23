<template>
  <div class="signup-container">
    <div>
      <h1>Sign Up</h1>
        <br>
        <label for="username">username: </label>
        <input type="text" id="username" @keydown.enter="signUp" v-model="username">
        <br>
        <br>
        <label for="password1">password: </label>
        <input type="password" id="password1" @keydown.enter="signUp" v-model="password1">
        <br>
        <br>
        <label for="password2">password confirm: </label>
        <input type="password" id="password2" @keydown.enter="signUp" v-model="password2">
        <br>
        <br>
        <label for="nick_name">닉네임: </label>
        <input type="text" id="nickname" @keydown.enter="signUp" v-model="nick_name">
        <br>
        <br>
        <button @click="signUp">회원가입</button>
        <button @click="OnClick">login</button>
    </div>
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
      nick_name: "",
    }
  },
  methods: {
    signUp(){
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const nick_name = this.nick_name ? this.nick_name : this.username

      const payload = {
        username, password1, password2, nick_name
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
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  color: #f2f2f2;
}
</style>