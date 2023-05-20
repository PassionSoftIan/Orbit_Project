<template>
  <div>
    <h1>Sign Up</h1>
    <button @click="OnClick">login</button>
  </div>
</template>

<script>
export default {
  name: "SignUp",
  methods: {
    OnClick(){
      this.$emit("logIn")
    }
  }

}
</script>

<style>

</style>