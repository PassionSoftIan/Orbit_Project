<template>
  <div>
    <h1>Log In</h1>
    <button @click="OnClick">signup</button>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  methods: {
    OnClick(){
      this.$emit("signUp")
    }
  }
}
</script>

<style>

</style>