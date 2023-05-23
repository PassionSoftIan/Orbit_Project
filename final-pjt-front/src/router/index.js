import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GameView from '../views/GameView.vue'
import CommunityView from '../views/CommunityView.vue'
import MovieDetail from '../views/MovieDetail.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignUpView.vue'
import ProfileView from '../views/ProfileView.vue'
// Store의 Token 값을 가져오기 위해 (인식)
import store from '@/store/'




Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  {
    path: '/game',
    name: 'game',
    component: GameView
  },

  {
    path: '/community',
    name: 'community',
    component: CommunityView
    // // route level code-splitting
    // // this generates a separate chunk (about.[hash].js) for this route
    // // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/MovieDetail/:moviepk',
    name: 'MovieDetail',
    component: MovieDetail
  },
  // login page(인식)
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  // signup page(인식)
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 로그인 여부 확인 및 제한(인식)
router.beforeEach((to, from, next) => {
  // 로그인 여부
  const isLoggedIn = store.state.Token
  // 로그인이 필요한 페이지 지정
  const authPages = ['home', 'community', 'game', 'logout', 'profile']
  // 로그인 이후 login, signup 페이지 이동 방지
  const loginPages = ['login','signup']
  const isLoginPages = loginPages.includes(to.name)
  // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    next({ name: 'login' })
  } else if (isLoginPages && isLoggedIn) {
    next({ name: 'home' })
  } else {
    next()
  }
})
export default router
