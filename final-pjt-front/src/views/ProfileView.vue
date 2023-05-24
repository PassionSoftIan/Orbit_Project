<template>
  <div>
    <br>
    <br>
    <br>
    <h1>{{ nick_name }} 님 환영합니다! </h1>
    <hr>
    <br>

    
    <h2>아이디</h2>
    <br>
    <br>


    <h2>내 코인: {{ coins }}</h2>
    <br>
    <br>


    <h2>내가 쓴 리뷰</h2>
    <hr>
    <div>
      <div v-for="review in myreviews" :key="review.id">
        {{ review }}
      </div>
    </div>
    <br>
    <br>


    <h2>나를 팔로우 한 사람</h2>
    <hr>
    <div>
      <div v-for="follower in followers" :key="follower.id">
        {{ follower }}
      </div>
    </div>
    <br>
    <br>


    <h2>내가 팔로우 한 사람</h2>
    <hr>
    <div>
      <div v-for="following in followings" :key="following.id">
        {{ following }}
      </div>
    </div>
    <br>
    <br>


    <h2>내가 좋아요 한 리뷰</h2>
    <hr>
    <div>
      <div v-for="like_review in like_reviews" :key="like_review.id">
        {{ like_reviews }}
      </div>
    </div>
    <br>
    <br>


    <!-- <h3>내가 좋아요 한 영화</h3>
    <hr>
    <div>
      <div v-for="review in myreviews" :key="review.id">
        {{ review }}
      </div>
    </div> -->


    <button @click="coinUp" >coin up</button>
    <button @click="coinDown" >coin down</button>
    <p>{{ coins }}</p>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  data(){
    return {
    }
  },
  computed: {
    coins() {
      return this.$store.state.coins
    },
    username() {
      return this.$store.state.username_information
    },
    nick_name() {
      return this.$store.state.nick_information
    },
    myreviews() {
      return this.$store.state.myreviews_information
    },
    followings() {
      return this.$store.state.followings_information
    },
    followers() {
      return this.$store.state.followers_information
    },
    like_reviews() {
      return this.$store.state.like_reviews_information
    },
  },
  methods: {
    // 코인 값들 변환 (인식)
    coinUp(){
      const coins = 1

      const payload = {
        coins,
      }
      this.$store.dispatch('coinChange', payload)
    },
    coinDown(){
      const coins = -1

      const payload = {
        coins,
      }
      this.$store.dispatch('coinChange', payload)
    },
  }
  

}
</script>

<style>
</style>