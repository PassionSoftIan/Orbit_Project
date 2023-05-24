<template>
  <div class="profile">
    <!-- 해당 페이지 인식에게 문의 -->
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
        <!-- {{ review }} -->
        <br>
        <a :href="URL_movie+review.movie">
          {{review.movie_title}}
        </a>
        <br>
        내용: {{ review.content }}
        <br>
        별점: {{ review.vote }}
      </div>
    </div>
    <br>
    <br>


    <h2>나를 팔로우 한 사람</h2>
    <hr>
    <div>
      <div v-for="follower in followers" :key="follower.id">
        <a :href="URL_others+follower.id">
          {{ follower.nick_name }}
        </a>
      </div>
    </div>
    <br>
    <br>


    <h2>내가 팔로우 한 사람</h2>
    <hr>
    <div>
      <div v-for="following in followings" :key="following.id">
        <a :href="URL_others+following.id">
          {{ following.nick_name }}
        </a>
      </div>
    </div>
    <br>
    <br>


    <h2>내가 좋아요 한 리뷰</h2>
    <hr>
    <div>
      <div v-for="like_review in like_reviews" :key="like_review.id">
        <br>
        <a :href="URL_movie+like_reviews[0].movie">
          {{ like_reviews[0].movie_title }}
        </a>
        <br>
        {{ like_reviews[0].user.nick_name }}
        <br>
        {{ like_reviews[0].content }}
        <br>
        {{ like_reviews[0].created_at }}
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


    <button @click="coinUp">coin up</button>
    <button @click="coinDown" >coin down</button>
    <p>{{ coins }}</p>
  </div>
</template>

<script>
const URL_movie = 'http://localhost:8080/MovieDetail/'
const URL_others = 'http://localhost:8080/others/'

export default {
  name: 'ProfileView',
  data(){
    return {
      URL_movie,
      URL_others,
    }
  },
  computed: {
    // myaccounts 정보(인식)
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
    // movie 정보(인식)
    title() {
      return this.$store.state.MovieStore
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
.profile {
  color: aquamarine;
}

/* .button {
  background-color:rgb(211, 63, 174)
} */
</style>