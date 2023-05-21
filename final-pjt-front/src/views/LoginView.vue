<template>
  <div v-if='!isAuthenticated'>
    <h1>Log In</h1>
    <label for="username">username: </label>
    <input type="text" id="usernamecheck" v-model="username">
    <br>
    <br>
    <label for="password">password: </label>
    <input type="password" id="password" v-model="password">
    <button @click="LogIn">로그인</button>

    <button @click="OnClick">signup</button>

    <p>{{$store.state.Token}}</p>
  </div>
  <div v-else>
    로딩중
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data(){
    return{
      username: "",
      password: "",
    }
  },
  methods: {
    LogIn(){
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      this.$store.dispatch('logIn', payload)
    },
    OnClick(){
      this.$emit("signUp")
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