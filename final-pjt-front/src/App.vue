<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/community">COMMUNITY</router-link> |
      <router-link to="/game">Game</router-link> | 
      <b-button @click="modalShow = !modalShow" variant="primary">Open Modal</b-button>

      <b-modal v-model="modalShow">제목 검색: 
        <input type="text" v-model="TitleSearch" value="한글 제목을 입력해 주세요" @keyup="SearchTitle">
        <div v-if='SearchTitleList'>
          <SearchModal
          v-for="Title in SearchTitleList"
          :key="Title.id"
          :Title="Title"
          
          />
          
        </div>
        <div v-else-if='this.TitleSearch==""'>
          <p>검색어를 입력해주세요</p>
        </div>
        <div v-else>
          <p>값이 없습니다</p>
        </div>
        
        </b-modal>

      <div>



</div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
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

<script>
import _ from 'lodash'

import SearchModal from './components/SearchModal.vue'

export default {
  name:'App',
  components:{
    SearchModal
  },
  data(){
    return {
      modalShow: false,
      TitleSearch: "",
      SearchTitleList:null
      }
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

    // 모달에서 타이틀 검색할 수 있도록하는 기능
    SearchTitle(){
      const SearchTitleList = []
      if(this.TitleSearch){

        this.$store.state.MovieStore.forEach(element => {
          if(element.title.includes(this.TitleSearch)){
            SearchTitleList.push(element)
          }}


        );

        if (SearchTitleList[0]){

        
        this.SearchTitleList = _.sortBy(SearchTitleList,'title').slice(0,5)
        return
        }
      

      
      
      }
      this.SearchTitleList = null
      


    }
  },
  created(){
    this.GenreToStore(),
    this.MovieToStore()
  },

}
</script>
