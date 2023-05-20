<template>
  <div v-if="moviedetail">
    
    <p>{{this.moviedetail.title}}</p>
    <p>{{this.moviedetail.overview}}</p>
  
    <img :src="`https://image.tmdb.org/t/p/w500/`+moviedetail.poster_path" alt="">

    <p>{{this.moviedetail.vote_average}}</p>
    <p>{{this.moviedetail.popularity}}</p>

    <hr>
    <h3>Reviews</h3>

    <ReadReviewVue v-for="review of Reviews" :key="review.id" :review="review" @reload="reload"/>
    <CreateReviewVue :movie_id="this.$route.params.moviepk" @created="reload"/>
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
    }
  },
  methods:{
    movieDetailMethod(){
      const params = this.$route.params.moviepk

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