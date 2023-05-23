<template>
  <div>
    <br>
    <br>
    <br>
    <button @click="coinUp" >coin up</button>
    <p>{{coin}}</p>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  data(){
    return {
      count: 0
    }
  },
  computed: {
    coins() {
      return this.count
    } 
  },
  methods: {
    coinUp(){
      this.count += 1
      const coins = this.count

      const payload = {
        coins,
      }
      this.$store.dispatch('coinUp', payload)
    },
  }
  

}
</script>

<style>
</style>