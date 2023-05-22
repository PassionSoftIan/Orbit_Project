<template>
  <carousel
    class="info-carousel"
    :per-page="7"
    :paginationEnabled="false"
    :navigation-enabled="true"
    navigationNextLabel=">"
    navigationPrevLabel="<">
    <slide v-for="Movie in this.Movies.data"
    :key="Movie.id"
    data-name="MySlideName"
    @slideclick="handleSlideClick">
     <router-link :to="{name:'MovieDetail', params:{moviepk:Movie.id}}">
      <img :src="`https://image.tmdb.org/t/p/original/`+Movie.poster_path" alt="">
      </router-link>
    </slide>
  </carousel>

</template>


<script>
import { Carousel, Slide } from 'vue-carousel';
export default {
  name:"TopRank",
    components: {
    Carousel,
    Slide
  },
  methods:{
      handleSlideClick (dataset){
    console.log(dataset.index, dataset.name)
  }
  },


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
  overflow: visible;
}
  .info-carousel {
    /* padding: 2px; */
    margin-block: 10px;
    display: grid;
    grid-gap: 5px;

  }
  
  .info-carousel img {
    transition: transform .3s;  
    
  }
  
  .info-carousel img:hover {
    transition: transform .3s;
    -ms-transform: scale(1.4);
    -webkit-transform: scale(1.4);  
    transform: scale(1.4);
    
  }
  
  .info-carousel img {
    border-radius: 2px;
    
  }
</style>

