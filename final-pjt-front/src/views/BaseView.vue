<template>
  <div id="BaseView">
  <b-navbar toggleable="lg" type="dark" variant="dark" class="sticky-top" >
    <div class="container">
    <router-link to="/" class="navbar-brand">
    <h1 class="logo">Orbit</h1>
    </router-link>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav class='justify-content-between' >
      <b-navbar-nav>
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/community" class="nav-link">Community</router-link>
        <router-link to="/game" class="nav-link">Game</router-link>
      </b-navbar-nav>
      <b-navbar-nav class="button">
        <SearchModalDisplay class="nav-link"/>
        <router-link to="/profile" class="nav-link" id="profile">Profile</router-link>
        <button @click="logOut" class="logout">Logout</button>
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
  font-family: 'orbit';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;


  position: relative;
}

#profile {
  display: inline-block;
  padding: 10px 20px;
  background-color: black;
  color: antiquewhite;
  text-decoration: none;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  font-size: 16px;
}

.logo {
  color: aqua;
  /* text-align: center;
  text-size-adjust: 10px; */
}


/* .logo {
  display: flex;
  align-content: flex-start;
  height: 130px;
  width: auto;
} */

.button {
  display: flex;
  align-items: center;
  justify-content: center;
}

.profile {
  background-color: transparent;
  height: 40px;
  color: antiquewhite;

}
.logout {
  background-color: transparent;
  color: antiquewhite;
  height: 40px;
  margin-left: 10px;
}


</style>