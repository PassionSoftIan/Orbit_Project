import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// 로컬스토리지 저장 위해 import(인식)
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  // persistedstate plugin로 로컬 스토리지에 vuex 상태 저장(인식)
  plugins: [
    createPersistedState(),
  ],
  state: {
    MovieStore:null,
    GenreStore:null,
    // user 값들 저장(인식)
    Token: null,
    coins: null,
    user_pk: null,
    username_information: null,
    nick_information: null,
    myreviews_information: null,
    followings_information: null,
    followers_information: null,
    like_reviews_information: null,

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
      state.coins = null
      location.reload()
    },
    // 유저 PK값 저장 (인식)
    SAVE_PK(state, pk) {
      state.user_pk = pk
      console.log(state.user_pk)
    },
    // coin 값, information 저장 (인식)
    INFORMATION_UPDATE(state, information) {
      state.coins = information.coins
      state.nick_information = information.nick_name
      state.username_information = information.username
      state.myreviews_information = information.myreviews
      state.followings_information = information.followings
      state.followers_information = information.followers
      state.like_reviews_information = information.like_reviews
      // console.log(state.like_reviews_information)
      // console.log(state.coins)
      console.log(information)
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
  // 회원가입 + 회원가입 이후 pk를 vuex에 저장(인식)
  signUp(context, payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    const nick_name = payload.nick_name
    // 회원가입 이후 vuex에 토큰 저장(인식)
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
      // 회원가입 이후 vuex에 유저 pk 저장(인식)
      .then(key => {
        console.log(key)
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
              Authorization: 'Token ' + key
              }
            })
            .then(async res => {
              context.commit('SAVE_PK', res.data.pk)
              // 회원가입 이후 vuex에 유저의 information 저장(인식)
              return axios({
                method: 'get',
                url: `${API_URL}/myaccounts/profile/${this.state.user_pk}/`,                
              })
              .then(res => {
                this.commit('INFORMATION_UPDATE', res.data)
                location.reload()
                console.log(res.data.pk)
              })
            })
            .catch(err => console.log(err))
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
    .then(async res => {
      context.commit('SAVE_TOKEN', res.data.key)
      return axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
              Authorization: 'Token ' + res.data.key
              }
            })
          })
            .then(async res => {
              context.commit('SAVE_PK', res.data.pk)
              // 로그인 이후 vuex에 유저의 information 저장(인식)
              return axios({
                method: 'get',
                url: `${API_URL}/myaccounts/profile/${this.state.user_pk}/`,                
              })
              .then(res => {
                this.commit('INFORMATION_UPDATE', res.data)
                location.reload()
                console.log(res.data.pk)
              })
            })
            .catch(err => console.log(err))
  },
  // 로그아웃 (인식)
  logOut() {
    this.commit('RESET_STATE')
    localStorage.removeItem('vuex')
  },

  // 코인 값 바꾸기 (인식)
  async coinChange(context, payload) {
    const coins = payload.coins
    const user_pk = this.state.user_pk

    try {
      await axios({
        method: 'put',
        url: `${API_URL}/myaccounts/profile/${user_pk}/`,
        data: {
          coins
        }
      })
      // 코인 값 바꾸고 vuex에도 저장 (인식)
      const res = await axios({
        method: 'get',
        url: `${API_URL}/myaccounts/profile/${user_pk}/`,
      })
      this.commit('INFORMATION_UPDATE', res.data)
    } catch (err) {
      return console.log(err)
    }
  },
  // vuex 유저 상태 변화 action (인식)
  userChange() {
    axios({
      method: 'get',
      url: `${API_URL}/myaccounts/profile/${this.state.user_pk}/`,                
    })
    .then(res => {
      this.commit('INFORMATION_UPDATE', res.data)
      console.log(res.data.pk)
      })
      .catch(err => console.log(err))
  },

  },
  modules: {
  }
})
