<template>
  <div class="community">
    <h1>Community</h1>
    <div>

      <button>Top 100</button> |
      <button>장르</button> |
      <button>수익</button> |
      <button>자체 평점</button> |
      <button>랜덤</button> |

      <p>Top Rank</p>
      <hr>
      
      <TopRank
      v-for="Movie in Movies"
      :key="Movie.id"
      :Movie='Movie'
      />

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
      Movies:null
    }
  },
  components:{
    TopRank,
  },
  methods:{
    TopRanks(){
      const params = {
        order_by: 'popularity',
        page: '1',
      }
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/api/v1/movie/',
        params:params
      })
      .then(res =>{
        this.Movies = res.data
        
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