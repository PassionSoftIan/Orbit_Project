<template>
  <div id="BaseView">
  <b-navbar toggleable="lg" type="dark" variant="dark" class="sticky-top" >
    <div class="container">
    <router-link to="/" class="navbar-brand"><img src="../images/logo2.png" style="width: 50%; height: auto;" class='logo' alt=""></router-link>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav class='justify-content-between' >
      <b-navbar-nav>
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/community" class="nav-link">Community</router-link>
        <router-link to="/game" class="nav-link">Game</router-link>
      </b-navbar-nav>
      <b-navbar-nav>
        <button @click="logOut">Logout</button>
        <SearchModalDisplay class="nav-link"/>
        <p class="nav-link">Profile</p>
      </b-navbar-nav>
    </b-collapse>
    </div>
  </b-navbar>
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
    // logout 후 페이지 새로고침 기능(인식)
    logOut() {
      this.$store.dispatch('logOut')
      // location.reload()
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
  /* color: #2c3e50; */
  color: red;

  position: relative;
}

</style>