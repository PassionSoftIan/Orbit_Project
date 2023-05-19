
<template>
  <div>
    <router-link :to="{name:'MovieDetail', params:{moviepk:Movie.id}}">
      기본 라우터
    <p>{{Movie.title}}</p>
    <p>{{Movie.overview}}</p>
  
    <img :src="`https://image.tmdb.org/t/p/w500/`+Movie.poster_path" alt="">

    <p>{{Movie.vote_average}}</p>
    <p>{{Movie.popularity}}</p>
    
    </router-link>
    <hr>
  </div>
</template>

<script>

export default {
  name:"TopRank",
  data(){
    return{
      imgurl: 'https://image.tmdb.org/t/p/w500/' 
    }
  },

  props:{
    Movie:Object
  },
  

}
</script>

<style>

</style>