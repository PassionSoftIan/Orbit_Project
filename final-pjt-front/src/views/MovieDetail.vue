<template>
  <div v-if="this.moviedetail">
    
    <p>{{this.moviedetail.title}}</p>
    <p>{{this.moviedetail.overview}}</p>
  
    <img :src="`https://image.tmdb.org/t/p/w500/`+Movie.poster_path" alt="">

    <p>{{this.moviedetail.vote_average}}</p>
    <p>{{this.moviedetail.popularity}}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'MovieDetail',
  data(){
    return{
      moviedetail:null
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
        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
      }
    }
  ,
  created(){
    this.movieDetailMethod()
  }
}
</script>

<style>

</style>