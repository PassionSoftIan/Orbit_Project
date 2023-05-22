<template>
<div class="box">
  <a
  v-for='Movie in this.Movies.data'
  :key="Movie.id"
    href="">
    <router-link :to="{name:'MovieDetail', params:{moviepk:Movie.id}}">
    <img :src="`https://image.tmdb.org/t/p/original/`+Movie.poster_path" alt="">
    </router-link>
    </a>
</div>
</template>

<script>

export default {
  name:"TopRank",


  props:{
    Movies:Object
  },
  

}
</script>

<style scoped>
img {
  max-width: 97%;
  
  width: 97%;
  height: 97%;
}
  .box {
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(6, minmax(100px, 1fr));
  }
  
  .box a {
    transition: transform .3s;  
  }
  
  .box a:hover {
    transition: transform .3s;
    -ms-transform: scale(1.4);
    -webkit-transform: scale(1.4);  
    transform: scale(1.4);
  }
  
  .box img {
    border-radius: 2px;
  }
</style>