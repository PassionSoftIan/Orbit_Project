<template>
<div class="signup">
  
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
        <div class="button">
        <button @click="signUp">제출</button>
        <button @click="OnClick">Login Page</button>
        </div>
    </div>
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
  margin-top: 10%;
  justify-content: center;
  /* align-items: center; */
  height: 300px;
  color: antiquewhite;
  font-size: 20px;
}
.signup {
  /* 배경 */
  background-image: url('../../public/images/Game.gif');
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
  overflow-x: hidden;
  height: 100vh;
  width: 100vw;
}
.button {
  display: flex;
  justify-content: flex-end;
  
}
</style>