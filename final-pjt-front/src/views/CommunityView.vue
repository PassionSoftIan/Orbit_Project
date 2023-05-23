<template>
  <div class="community">
    <h1>Community</h1>
      <!-- 탑10 영화 출력 -->
    <section class="main-container" >
      <div class="location" id="home" 
      v-for='Movies in this.allMovies'
      :key='Movies.name'>
          <h1 id="home" v-if="Movies.name==='Top100'">Top20</h1>
          <h1 id="home" v-else>{{Movies.name}}</h1>
            <TopRank :Movies="Movies"/>

      </div>
    </section>
  </div>
</template>

<script>

import axios from 'axios'
import _ from 'lodash'
import TopRank from '../components/Community/TopRank.vue'

export default {
  name: 'CommunityView',
  components:{
    TopRank
  },
  data(){
    return{
      allMovies:[],
      Movies:null,
      CommunityBarValue: null,
      GenreRandom:null
    }
  },
  methods:{

    // 전체 영화 탑10만 보여주도록함
    TopRanks(value){
      if(this.CommunityBarValue === value){
        console.log('stop')
      }
      else{
      let order = 'vote_average'
      this.CommunityBarValue = value
      if (value === 'Genre'){
        return 1
      }
      if (value==='Revenue'){
        order = 'revenue'}

      const params = {
        order_by: order,
        page: '0',
      }
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/api/v1/movie/',
        params:params
      })
      .then(res =>{
        const Movies = {'name':value, 'data':res.data}
        this.allMovies.push(Movies)
        this.Movies = res.data
      })
      .catch(err =>{
        console.log(err)
      })

    }},

    // random으로 장르에서 가져오기
    OnClickGenre(id,name){
      const params = {
        genre: id,
        page: '0',
      }
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/api/v1/movie/',
        params:params
      })
      .then(res =>{
        const random = _.sampleSize(_.range(0, res.data.length), 10)
        var randommovie = []
        random.forEach(element => {
          randommovie.push(res.data[element])
        });
        const Movies = {'name':name, 'data':_.sortBy(randommovie,'vote_average').reverse()}
        this.allMovies.push(Movies)

        this.GenreRandom = _.sortBy(randommovie,'vote_average').reverse()


        
      })
      .catch(err =>{
        console.log(err)
      })

      console.log(id)
    }
    
  },
  created(){
    this.TopRanks('Top100')
    this.TopRanks('Revenue')
    this.$store.state.GenreStore.forEach(element => {
      this.OnClickGenre(element.id,element.name)
    });
    
  }
}
</script>

<style>

:root {
  --primary: #141414;
  --light: #F3F3F3;
  --dark: 	#686868;
}

.community {
  margin: 0;
  padding: 0;
}

.main-container {
  padding: 50px;
}

</style>