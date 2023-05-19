<template>
  <div class="community">
    <h1>Community</h1>
    <div>

      <button @click="CommunityBarOnClick('Top100') " :disabled="this.CommunityBarValue==='Top100'">Top 100</button> |
      <button @click="CommunityBarOnClick('Genre')" :disabled="this.CommunityBarValue==='Genre'">장르</button> |
      <button @click="CommunityBarOnClick('Revenue')" :disabled="this.CommunityBarValue==='Revenue'">수익</button> |


      <p>Top Rank</p>
      <hr>
      <div v-if="this.CommunityBarValue === 'Top100'">
      <TopRank
      v-for="Movie in Movies"
      :key="Movie.id"
      :Movie='Movie'
      />
      </div>
      <div v-else-if="this.CommunityBarValue === 'Genre'">
        <p>Genre</p>

      </div>
      <div v-else-if="this.CommunityBarValue === 'Revenue'">
        <p>Revenue</p>
      </div>

      </div>
  </div>
</template>

<script>
import TopRank from '../components/Community/TopRank.vue'
import axios from 'axios'

export default {
  name: 'CommunityView',
  data(){
    return{
      Movies:null,
      CommunityBarValue: 'Top100'
    }
  },
  components:{
    TopRank,
  },
  methods:{
    CommunityBarOnClick(value){
      if(this.CommunityBarValue === value){
        event.preventDefault()
        console.log('stop')
      }
      else {
        this.CommunityBarValue = value
        
      }
      

    },
    TopRanks(){
      const params = {
        order_by: 'title',
        page: '1',
      }
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/api/v1/movie/',
        params:params
      })
      .then(res =>{
        this.Movies = res.data
        console.log("HI")
        
      })
      .catch(err =>{
        console.log(err)
      })

    }
  },
  created(){
    this.TopRanks()
  }
}
</script>

<style>

</style>