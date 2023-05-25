<template>
  <div class="other">
    <br>
    <br>
    <br>
    <h1>{{other_information.username}} 님의 프로필</h1>
    <div v-if="updateFollowingStatus">
      <button @click="follow">팔로우</button>
    </div>
    <div v-else>
      <button @click="unfollow">언팔로우</button>
    </div>
    <hr>
    <br>
    <h2>작성 리뷰</h2>
    <hr>
    <div>
      <div v-for="review in other_information.myreviews" :key="review.id">
        <br>
        <a :href="URL+review.movie">
          {{review.movie_title}}
        </a>
        <br>
        내용: {{ review.content }}
        <br>
        평점: {{ review.vote }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const URL = 'http://localhost:8080/MovieDetail/'



export default {
  name: 'OtherProfileView',
  data() {
    return {
      URL,
      other_information: null,
    };
  },
  props: ['nickname'],
  computed: {
    updateFollowingStatus() {
      const check = this.$route.params.userpk;
      for (let i = 0; i < this.$store.state.followings_information.length; i++) {
        // console.log('if전')
        // console.log(this.$store.state.followings_information[i].id)
        // console.log(check + '입니다')
        // console.log(typeof(check) + '체크타입')
        // console.log(typeof(this.$store.state.followings_information[i].id))
        if (this.$store.state.followings_information[i].id === Number(check)) {
          console.log('if문 통과');
          return false;
        }
      }
      console.log('이거')
      return true;
    },
  },
  methods: {
    otherProfile() {
      const params = this.$route.params.userpk;

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/myaccounts/profile/${params}/`,
      })
        .then((res) => {
          this.other_information = res.data;
        })
        .catch((err) => {
          console.log(typeof err.request.status);
          if (err.request.status === 404){
            this.$router.push('/NotFound')
          }
        });
    },
    follow() {
      const params = this.$route.params.userpk;
      const Token = this.$store.state.Token;
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/myaccounts/following/${params}/`,
        headers: {
          Authorization: 'Token ' + Token,
        },
      }).then(() => {
        this.$store.dispatch('userChange');
      });
    },
    unfollow() {
      const params = this.$route.params.userpk;
      const Token = this.$store.state.Token;
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/myaccounts/following/${params}/`,
        headers: {
          Authorization: 'Token ' + Token,
        },
      }).then(() => {
        this.$store.dispatch('userChange');
      });
    },
  },
  created() {
    this.otherProfile();
  },
}

</script>

<style>
.other {
  background-image: url('../../public/images/Space.gif');
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
  overflow-x: hidden;
  height: 91.3vh;
  width: 100vw;
}
</style>