import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

const Token = '4ec256edcaef9bdd468cff950f8011cdf97a7d32'

export default new Vuex.Store({
  state: {
    MovieStore:null,
    GenreStore:null,
    Token: Token,
  },
  getters: {
  },
  mutations: {
    MOVIE_TO_STORE(state,payload){
      state.MovieStore = payload
      
    },
    GENRE_TO_STORE(state,payload){
      state.GenreStore = payload
    },
  },
  actions: {
    MovieToStore(){
      
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/api/v1/movie/alltitle/'
    })
    .then(res=>{
      this.commit('MOVIE_TO_STORE',res.data)
    })
    .catch(err => {
      console.log(err)
    })
  },
  GenreToStore(){
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/api/v1/genre/'
    })
    .then(res=>{
      this.commit('GENRE_TO_STORE',res.data)
    })
    .catch(err => {
      console.log(err)
    })
  },
  },
  modules: {
  }
})
