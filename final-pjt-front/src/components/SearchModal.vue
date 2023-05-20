<template>
  <div>
    <hr>
    <a :href='"http://localhost:8080/MovieDetail/"+this.title.id'>
    <img :src="'https://image.tmdb.org/t/p/w500/'+this.title.poster_path" class='cover' alt="">
    <p> 
    {{this.title.title}}
    {{this.title.vote_average}}
    {{this.title.revenue}}
    </p>
    </a>
    
        
  </div>
</template>
<script>
export default {
  
  name:'SearchModal',
  data(){
    return{
      title:this.Title
    }
  },
  props:{
    Title:Object
  },
  
}
</script>

<style>
.cover {
  width: 54px;
  height: 96px;
  object-fit: contain;}

</style>