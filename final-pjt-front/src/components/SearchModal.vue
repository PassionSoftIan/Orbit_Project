<template>
  <div>
    <a :href='"http://localhost:8080/MovieDetail/"+this.title.id'>
    {{this.title.title}}
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

</style>