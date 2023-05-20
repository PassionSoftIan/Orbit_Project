<template>
  <div id="BaseView">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/community">COMMUNITY</router-link> |
      <router-link to="/game">Game</router-link> | <SearchModalDisplay/>
      <router-link to="/logout">logout</router-link> |
      <!-- <router-link to="/login">Login</router-link> |
      <router-link to="/signup">Sign Up</router-link> -->
    </nav>
    <router-view/>
  </div>
</template>

<script>

import SearchModalDisplay from '@/components/SearchBar/SearchModalDisplay.vue'

export default {
  name:'BaseView',
  components:{
    SearchModalDisplay
  },

  methods:{


    // 영화 타이틀과 id를 store에 저장
    MovieToStore(){

      this.$store.dispatch('MovieToStore')

    },
    // 장르타이틀과 id를 store에 저장
    GenreToStore(){

    this.$store.dispatch('GenreToStore')
    },

  },
  created(){
    this.GenreToStore(),
    this.MovieToStore()
  },

}
</script>

<style>
#BaseView {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

</style>