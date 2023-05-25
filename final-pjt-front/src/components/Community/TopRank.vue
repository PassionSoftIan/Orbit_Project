<template>
<!-- // npm run vue-carousel -->
<div class="swiper-container">
<swiper
    class="swiper"
    :options="swiperOption"
>
    <swiper-slide v-for="Movie in this.Movies.data"
    :key="Movie.id">

    
    <router-link :to="{name:'MovieDetail', params:{moviepk:Movie.id}}">

    <img :src="`https://image.tmdb.org/t/p/original/`+Movie.poster_path" alt="">


    </router-link>

    </swiper-slide>     
    <div
        class="swiper-pagination"
        slot="pagination"
        >
    </div>
    <div class="swiper-button-prev" slot="button-prev"></div>
    <div class="swiper-button-next" slot="button-next"></div>
</swiper>
</div>

</template>


<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";
export default {
  name:"TopRank",
    components: {
      Swiper,
      SwiperSlide
  },
  data(){
    return{
      swiperOption: { 
      slidesPerView: 7, 
      spaceBetween: 10, 
      loop: true,
      breakpoints : true,
      // autoHeight:true,

    navigation: { 
        nextEl: '.swiper-button-next', 
        prevEl: '.swiper-button-prev' 
    } 
  },
    }
  },


  props:{
    Movies:Object
  },
  

}
</script>

<style scoped>

/* .container{width:1200px; max-width:none!important;} */
.swiper{
  display: flex;
}
.swiper-container {
  overflow: visible;
  /* margin: 20px; */
  width:1400px;
  /* max-width:none!important; */
  
}
img {
  width: 100%;
  height:260px;
  object-fit: scale-down;
  overflow: visible;
}

.swiper-slide {
  transition: all 300ms ease-in-out;
  border-radius: 5px;
  margin-block: 10px;
  max-block-size: 50%;
}

.swiper-slide img {
  border-radius: 5px;
  max-width: 18rem;
  cursor: grab;
  
}

.swiper-slide img:active {
  cursor: grabbing;
}

.swiper-slide:hover {
  transform: scale(1.5);
  transition: all 30ms ease-in-out;
  transition-delay: 30ms;
  z-index: 1;
}

.swiper-slide:hover img {
  transition-delay: 300ms;
  box-shadow: 0 0 5px 1px rgba(0,0,0,0.5);
}

@media screen and (max-width: 599px) {
  .swiper-slide img {
    max-width: 14rem;
  }
  .swiper-button-next,
  .swiper-button-prev {
    display: none;
  }
}

@media screen and (max-width: 400px) {
  .swiper-slide img {
    max-width: 10.5rem;
    border-radius: 2px;
  }
}
</style>
