<template>
  <div id='SearchModalDisplay'>
    <b-button @click="ModalReset" variant='Dark' ><img class='search-icon' src="@/images/searchicon3.png" alt=""></b-button>

      <b-modal v-model="modalShow">제목 검색: 
        <input type="text" @input='changeKeyword' @keyup="SearchTitle">
        <div v-if='SearchTitleList'>
          <SearchModal
          v-for="Title in SearchTitleList"
          :key="Title.id"
          :Title="Title"
          
          />
          
        </div>
        <div v-else-if='this.TitleSearch==""'>
          <p>검색어를 입력해주세요</p>
        </div>
        <div v-else>
          <p>값이 없습니다</p>
        </div>
        
        </b-modal></div>
</template>

<script>
import _ from 'lodash'

import SearchModal from '@/components/SearchBar/SearchModal.vue'

export default {
  name:'SearchModalDisplay',
  data(){
    return {
      modalShow: false,
      TitleSearch: "",
      SearchTitleList:null
      }
  },
  components:{
    SearchModal
  },
  methods:{
    ModalReset(){
      if (!this.modalShow){
        this.SearchTitleList = null
        this.modalShow = !this.modalShow
      }
    },
    SearchTitle(){
      let NameIn = []
      let NameStart = []
      if(this.TitleSearch){

        this.$store.state.MovieStore.forEach(element => {
          if(element.title.startsWith(this.TitleSearch)){
            NameStart.push(element)
          }
          else if(element.title.includes(this.TitleSearch)){
            NameIn.push(element)
          }}


        );
        let SearchTitleList = []

        if (NameStart[0]||NameIn[0]){
          
          let NameStartUp = NameStart.filter((item)=>{
            return item.revenue >= 10000
          })
          let NameStartDown = NameStart.filter((item)=>{
            return item.revenue < 10000
          })
          let NameInUp = NameIn.filter((item)=>{
            return item.revenue >= 10000
          })
          let NameInDown = NameIn.filter((item)=>{
            return item.revenue < 10000
          })
          NameStartUp = _.sortBy(NameStartUp,['vote_average','revenue']).reverse()
          NameStartDown = _.sortBy(NameStartDown,['vote_average','revenue']).reverse()
          NameInUp = _.sortBy(NameInUp,['vote_average','revenue']).reverse()
          NameInDown = _.sortBy(NameInDown,['vote_average','revenue']).reverse()

          SearchTitleList = SearchTitleList.concat(NameStartUp,NameStartDown,NameInUp,NameInDown)

          this.SearchTitleList = SearchTitleList.slice(0,5)
          

          return
        }
      

      
      
      }
      this.SearchTitleList = null
      


    },

    changeKeyword(e){
      this.TitleSearch = e.target.value
    },
  }
}
</script>

<style>

.search-icon {
  background-color: black;
  width: 25px;
}
</style>