<template>
  <div class="community">
    <h1>Community</h1>
    <div>

      <button @click="TopRanks('Top100')" :disabled="this.CommunityBarValue==='Top100'">Top 10</button> |
      <button @click="TopRanks('Genre')" :disabled="this.CommunityBarValue==='Genre'">장르</button> |
      <button @click="TopRanks('Revenue')" :disabled="this.CommunityBarValue==='Revenue'">수익</button> |

      <!-- 탑10 영화 출력 -->
      <p>Top Rank</p>
      <hr>
      <div v-if="this.CommunityBarValue === 'Top100'">
      <TopRank
      v-for="Movie in Movies"
      :key="Movie.id"
      :Movie='Movie'
      />
      </div>

      <!-- 장르별 랜덤 출력 -->
      <div v-else-if="this.CommunityBarValue === 'Genre'">
        <ul>
          <button
          v-for="genre in this.$store.state.GenreStore"
          :key='genre.id'
          @click="OnClickGenre(genre.id)"
          >{{genre.name}}</button>
        </ul>
      <div v-if='GenreRandom'>
      <TopRank
      v-for="Movie in GenreRandom"
      :key="Movie.id"
      :Movie='Movie'
      />
      </div>
      </div>


      <!-- 수익 탑탠 출력 -->
      <div v-else-if="this.CommunityBarValue === 'Revenue'">
      <TopRank
      v-for="Movie in Movies"
      :key="Movie.id"
      :Movie='Movie'
      />
      </div>



      </div>
  </div>
</template>

<script>
import TopRank from '../components/Community/TopRank.vue'
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'CommunityView',
  data(){
    return{
      Movies:null,
      CommunityBarValue: null,
      GenreRandom:null
    }
  },
  components:{
    TopRank,
  },
  methods:{
    
    // 클릭 했을때 다른 탭으로 넘어감
    CommunityBarOnClick(value){
      if(this.CommunityBarValue === value){
        console.log('stop')
      }
      else {
        this.CommunityBarValue = value
        
      }
      

    },

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
        this.Movies = res.data
      })
      .catch(err =>{
        console.log(err)
      })

    }},

    // random으로 장르에서 가져오기
    OnClickGenre(id){
      const params = {
        genre: id,
        page: '1',
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
        console.log(typeof random)
        console.log( randommovie)

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
  }
}
</script>

<style>

</style>