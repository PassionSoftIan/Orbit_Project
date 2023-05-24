<template>
  <div v-if="moviedetail">
    
    <p>졔목 :  {{this.moviedetail.title}}</p>
    <p>줄거리 :  {{this.moviedetail.overview}}</p>
    
    <img :src="`https://image.tmdb.org/t/p/w500/`+moviedetail.poster_path" alt="">

    <p>평점 : {{this.moviedetail.vote_average}}</p>
    <p>관객수 : {{this.moviedetail.popularity}}</p>

    <hr>
    <p>스틸컷</p>
    <div v-for="img in this.stillCut"
    :key='img.img_url'>
    <img :src="`https://image.tmdb.org/t/p/w300`+img.img_url" alt="">
    </div>

    <hr>
    youtube
    <div v-for="key in this.youtubeKey"
    :key="key.key">
    <iframe 
    width="560"
    height="315"
    :src="`https://www.youtube.com/embed/`+key.key"
    title="YouTube video player" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen></iframe>

    </div>
    <hr>
    <h1>actor</h1>
    <div v-for='actor in this.actors'
    :key="actor.id">
    {{actor.name}}
    <img :src="`https://image.tmdb.org/t/p/w300`+actor.profile_path" alt="">
    </div>
    <hr>
    <h1>director</h1>
    {{this.director.name}}
    <img :src="`https://image.tmdb.org/t/p/w300`+this.director.profile_path" alt="">

    <hr>
    <h3>Reviews</h3>
    <ReadReviewVue v-for="review of Reviews" :key="review.id" :review="review" :accounts="accounts" @reload="reload" @like="reload"/>
    <CreateReviewVue :movie_id="this.$route.params.moviepk" :accounts="accounts" @created="reload"/>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
  </div>
</template>

<script>
import axios from 'axios'
import CreateReviewVue from '../components/CRUD/CreateReview.vue'
import ReadReviewVue from '../components/CRUD/ReadReview.vue'

export default {
  name:'MovieDetail',
   components: {
    CreateReviewVue,
    ReadReviewVue
  },
  computed:{
    Token(){
        return this.$store.state.Token
    }
  },
  data(){
    return{
      moviedetail:null,
      Reviews:null,
      accounts:null,
      youtubeKey:null,
      stillCut:null,
      actors:null,
      director:null
    }
  },
  methods:{
    movieDetailMethod(){
      const params = this.$route.params.moviepk
      const token = this.$store.state.Token

      // 영화 디테일
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movie/${params}`
      })
      .then(res =>{
        this.moviedetail = res.data
      })
      .catch(err => {
        console.log(err)
      })

      // 리뷰
      axios({
        method:"get",
        url:`http://127.0.0.1:8000/api/v1/review/${params}`
      })
      .then((res)=>{
        this.Reviews = res.data
      })
      .catch((err)=>{
        console.log(err)
      })

      // 유저
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/user/`,
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then((res)=>{
        this.accounts = res.data
        // console.log(this.accounts)
      })
      .catch((err)=>{
        console.log(err)
        // console.log(token)
      })
      axios({
        method:"get",
        url:`http://127.0.0.1:8000/api/v1/youtubeNstill/${params}`
      })
      .then((res)=>{
        // console.log(res.data)
        this.youtubeKey = res.data.youtube
        this.stillCut = res.data.still
        // console.log(this.youtubeNstill)
        // console.log(this.stillCut)

      })
      .catch((err)=>{
        console.log(err)
      })

      // axios({
      //   method:'get',
      //   url: `https://api.themoviedb.org/3/movie/${params}/credits/language=ko-KR`,
      //   params:{
      //     API:'9784d9d6e5d8a8e331ba3979590355d0'
      //   },
      // })
      // .then((res)=>{
      //   console.log(res)
      // })
      // .catch((err)=>{
      //   console.log(err)
      // })
      const options = {
        method: 'GET',
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5Nzg0ZDlkNmU1ZDhhOGUzMzFiYTM5Nzk1OTAzNTVkMCIsInN1YiI6IjYzZDMzODA4ZTcyZmU4MDA3Y2E0ODc1MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.faSHvKNZf94MQj5ksh1kKhSzexW-yGkb_E-ayasFFxk'
        }
      };

      fetch(`https://api.themoviedb.org/3/movie/${params}/credits?language=en-US`, options)
        .then(response => response.json())
        .then(response => {
          this.actors = response.cast.slice(0,10)
          console.log(this.actors)
          
          for(let crew of response.crew){
            if(crew.job==="Director"){
              this.director= crew
              break
            }
          }
          })
        .catch(err => console.error(err));
          },
    reload(){
      this.movieDetailMethod()
    }
  },
  created(){
    this.movieDetailMethod()

  }
}
</script>

<style>

</style>