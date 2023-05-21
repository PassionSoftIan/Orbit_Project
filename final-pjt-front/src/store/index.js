import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// 로컬스토리지 저장 위해 import(인식)
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  // persistedstate plugin(인식)
  plugins: [
    createPersistedState(),
  ],
  state: {
    MovieStore:null,
    GenreStore:null,
    Token: null,
  },
  getters: {
  },
  mutations: {
    MOVIE_TO_STORE(state, payload){
      state.MovieStore = payload
      
    },
    GENRE_TO_STORE(state, payload){
      state.GenreStore = payload
    },
    // auth(회원가입, 로그인) (인식)
    SAVE_TOKEN(state, Token){
      state.Token = Token
      console.log(state.Token)
    },
    // Logout (인식)
    RESET_STATE(state) {
      state.Token = null
    },
  },
  actions: {
    MovieToStore(){
      
    axios({
      method:'get',
      url:`${API_URL}/api/v1/movie/alltitle/`
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
      url:`${API_URL}/api/v1/genre/`
    })
    .then(res=>{
      this.commit('GENRE_TO_STORE',res.data)
    })
    .catch(err => {
      console.log(err)
    })
  },
  // 회원가입 (인식)
  signUp(context, payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then(res => {
        context.commit('SAVE_TOKEN', res.data.key)
        console.log("여긴 signUp", res.data.key)
        location.reload()
      })
      .catch(err => {
        console.log(err)
        alert("8자 이상 써주세요")
      })
  },
  // 로그인 (인식)
  logIn(context, payload) {
    const username = payload.username
    const password = payload.password
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        context.commit('SAVE_TOKEN', res.data.key)
        location.reload()
      })
      .catch(err => console.log(err))
  },
  // 로그아웃 (인식)
  logOut() {
    this.commit('RESET_STATE')
    localStorage.removeItem('vuex')
  },
  },
  modules: {
  }
})
