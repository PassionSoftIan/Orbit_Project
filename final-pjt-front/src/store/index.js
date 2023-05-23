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
    coins: null,
    user_pk: null,
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
    // 유저 PK값 저장 (인식)
    SAVE_PK(state, pk) {
      state.user_pk = pk
      console.log(state.user_pk)
    },
    // coin 값 저장 (인식)
    COIN_UP(state, coins) {
      state.coins = coins
      console.log(state.coins)
    },
    // coin 값 리셋 (인식)
    COIN_RESET(state) {
      state.coins = 0
      console.log(state.coins)
    }
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
    const nick_name = payload.nick_name
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nick_name
      }
    })
    .then(res => {
      context.commit('SAVE_TOKEN', res.data.key)
      return res.data.key
      })
      .then(key => {
        console.log(key)
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
              Authorization: 'Token ' + key
              }
            })
            .then(res => {
              context.commit('SAVE_PK', res.data.pk)
              console.log(res.data.pk)
              location.reload()
            })
      })
      .catch(err => {
        console.log(err)
        alert('가입 조건을 확인해주세요')
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
    // 로그인 되어있는 유저 PK값 가져와서 vuex에 저장 (인식)
    .then(res => {
      context.commit('SAVE_TOKEN', res.data.key)
      return res.data.key
      })
      .then(key => {
        console.log(key)
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
              Authorization: 'Token ' + key
              }
            })
            .then(res => {
              context.commit('SAVE_PK', res.data.pk)
              console.log(res.data.pk)
              location.reload()
            })
      })
      .catch(err => console.log(err))
  },
  // 로그아웃 (인식)
  logOut() {
    this.commit('RESET_STATE')
    localStorage.removeItem('vuex')
  },

  // 코인 상승 (인식)
  coinUp(context, payload) {
    const coins = payload.coins
    // this.commit('COIN_UP', coins)
    axios({
      method: 'put',
      url: `${API_URL}/myaccounts/profile/${this.state.user_pk}/`,
      data: {
        coins
      }
    })
      .then(
        this.commit('COIN_RESET',)
      )
      .catch(err => console.log(err))
  }
  },
  modules: {
  }
})
