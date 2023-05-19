
<template>
  <div>
    <router-link :to="{name:'MovieDetail', params:{moviepk:Movie.id}}">

    <p>{{Movie.title}}</p>
    <p>{{Movie.overview}}</p>
    <p>{{Movie.genre}}</p>

  
    <img :src="`https://image.tmdb.org/t/p/w500/`+Movie.poster_path" alt="">

    <p>{{Movie.vote_average}}</p>
    <p>수익: {{Movie.revenue}}</p>
    
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