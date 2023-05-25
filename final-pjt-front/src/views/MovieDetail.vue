<template>
  <!-- <div v-if="moviedetail">
    
    <p>졔목 :  {{this.moviedetail.title}}</p>
    <p>줄거리 :  {{this.moviedetail.overview}}</p>
    
    <img :src="`https://image.tmdb.org/t/p/w500/`+moviedetail.poster_path" alt="">

    <p>평점 : {{this.moviedetail.vote_average}}</p>
    <p>관객수 : {{this.moviedetail.popularity}}</p>

    <hr>
    <p>스틸컷</p>
    <div v-for="img in this.stillCut"
    :key='img.img_url'>
    <img :src="'https://image.tmdb.org/t/p/w300'+img.img_url" alt="">
    </div>

    <hr>
    youtube
    <div v-for="key in this.youtubeKey"
    :key="key.key">
    {{key.key}}
    <iframe 
    width="560"
    height="315"
    :src="`https://www.youtube.com/embed/`+key.key"
    title="YouTube video player" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen></iframe>

    </div>
    <hr>
    <h1>actor</h1>
    <div v-for='actor in this.actors'
    :key="actor.id">
    {{actor.name}}
    <img :src="`https://image.tmdb.org/t/p/w300`+actor.profile_path" alt="">
    </div>
    <hr>
    <h1>director</h1>
    {{this.director.name}}
    <img :src="`https://image.tmdb.org/t/p/w300`+this.director.profile_path" alt="">

    <hr>

    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
  </div> -->
      <div>
    

    <section id="banner" class="clearfix">
      <div id="banner_content_wrapper">
        <div id="poster">
          <img
            class="featured_image"
            :src="`https://image.tmdb.org/t/p/w500/`+this.moviedetail.poster_path"
            alt="IT Chapter 2 poster"
          />
        </div>
        <div class="content">
          <h2 class="title">{{this.moviedetail.title}}</h2>
          <div class="card-description">
          <p class="info">
            {{this.moviedetail.vote_average}}/10<span>|</span>{{this.moviedetail.release_date}}<span>|</span>
            <span v-for="ger in this.moviedetail.genre"
            :key="ger.id">{{ger.name}}</span>
          </p>
          <p class="discription">
            {{moviedetail.tagline}}
          </p>
          <p class="discription">
            {{moviedetail.overview}}
          </p>
          </div>

          <!-- 더보기 버튼 작업중 -->
          <input type="checkbox" class="content__more-btn">
          <!-- 더보기 버튼 작업중 -->

          
        </div>
      </div>
        <!-------//////////// 스틸컷 시작-->
    <section id="top_movies" class="clearfix">
      <div class="wrapper">
        <header class="clearfix">
          <h2>Still Cut</h2>

        </header>

        
          <div class="post">
            <swiper
              class="swiper"
              :options="swiperOption">
            <swiper-slide v-for="img in this.stillCut"
            :key='img.img_url'>
            <img :src="'https://image.tmdb.org/t/p/w300'+img.img_url" alt="">
            </swiper-slide>
                <div
                  class="swiper-pagination"
                  slot="pagination">
                </div>
                <div class="swiper-button-prev" slot="button-prev"></div>
                <div class="swiper-button-next" slot="button-next"></div>
            <swiper-slide v-for="key in this.youtubeKey"
            :key="key.key">
                <iframe 
                width="300"
                height="169"
                :src="`https://www.youtube.com/embed/`+key.key"
                title="YouTube video player" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                allowfullscreen></iframe>
            </swiper-slide>
              </swiper>
        </div>
        <!-------//////////// 스틸컷 끝-->
      </div>
    </section>

        <h3>Reviews</h3>
    <div class="comments-container">
      <ul id="comments-list" class="comments-list">
    <ReadReviewVue v-for="review of Reviews" :key="review.id" :review="review" :accounts="accounts" @reload="reload" @like="reload"/>
      </ul>
    </div>
    <CreateReviewVue :movie_id="this.$route.params.moviepk" :accounts="accounts" @created="reload"/>
    </section>

    <p>영화 자체 평점 : {{moviedetail.ours_vote / moviedetail.vote_count ? moviedetail.ours_vote / moviedetail.vote_count : 0 }}</p>
    <ReadReviewVue v-for="review of Reviews" :key="review.id" :review="review" :accounts="accounts" @reload="reload" @like="reload"/>
    <CreateReviewVue :movie_id="this.$route.params.moviepk" :accounts="accounts" @created="reload"/>



  </div>
</template>

<script>
import axios from 'axios'
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";
import CreateReviewVue from '../components/CRUD/CreateReview.vue'
import ReadReviewVue from '../components/CRUD/ReadReview.vue'

export default {
  name:'MovieDetail',
   components: {
    CreateReviewVue,
    ReadReviewVue,
    Swiper,
    SwiperSlide
  },
  computed:{
    Token(){
        return this.$store.state.Token
    },

  },
  data(){
    return{
      moviedetail:null,
      Reviews:null,
      accounts:null,
      youtubeKey:null,
      stillCut:null,
      actors:null,
      director:null,
      swiperOption: { 
        slidesPerView: 5, 
        spaceBetween: 30, 
        loop: false, 

        navigation: { 
            nextEl: '.swiper-button-next', 
            prevEl: '.swiper-button-prev' 
        } 
},
    }
  },
  methods:{
    movieDetailMethod(){
      const params = this.$route.params.moviepk
      const token = this.$store.state.Token

      // 영화 디테일
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movie/${params}`
      })
      .then(res =>{
        this.moviedetail = res.data
      })
      .catch(err => {
        console.log(err)
      })

      // 리뷰
      axios({
        method:"get",
        url:`http://127.0.0.1:8000/api/v1/review/${params}`
      })
      .then((res)=>{
        this.Reviews = res.data
      })
      .catch((err)=>{
        console.log(err)
      })

      // 유저
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/user/`,
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then((res)=>{
        this.accounts = res.data
        // console.log(this.accounts)
      })
      .catch((err)=>{
        console.log(err)
        // console.log(token)
      })
      axios({
        method:"get",
        url:`http://127.0.0.1:8000/api/v1/youtubeNstill/${params}`
      })
      .then((res)=>{
        // console.log(res.data)
        this.youtubeKey = res.data.youtube
        this.stillCut = res.data.still
        // console.log(this.youtubeNstill)
        // console.log(this.stillCut)

      })
      .catch((err)=>{
        console.log(err)
      })

      // axios({
      //   method:'get',
      //   url: `https://api.themoviedb.org/3/movie/${params}/credits/language=ko-KR`,
      //   params:{
      //     API:'9784d9d6e5d8a8e331ba3979590355d0'
      //   },
      // })
      // .then((res)=>{
      //   console.log(res)
      // })
      // .catch((err)=>{
      //   console.log(err)
      // })
      const options = {
        method: 'GET',
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5Nzg0ZDlkNmU1ZDhhOGUzMzFiYTM5Nzk1OTAzNTVkMCIsInN1YiI6IjYzZDMzODA4ZTcyZmU4MDA3Y2E0ODc1MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.faSHvKNZf94MQj5ksh1kKhSzexW-yGkb_E-ayasFFxk'
        }
      };

      fetch(`https://api.themoviedb.org/3/movie/${params}/credits?language=en-US`, options)
        .then(response => response.json())
        .then(response => {
          this.actors = response.cast.slice(0,10)
          console.log(this.actors)
          
          for(let crew of response.crew){
            if(crew.job==="Director"){
              this.director= crew
              break
            }
          }
          })
        .catch(err => console.error(err));
          },
    reload(){
      this.movieDetailMethod()
    }
  },
  created(){
    this.movieDetailMethod()

  }
}
</script>

<style >
  /*color variables
   main= #1E1E1E
   secondery= #333333
   highlight= #073254



*/
* {
  box-sizing: border-box;
}
body,
html {
  font-family: "Open Sans", sans-serif;
}
.clearfix:before,
.clearfix:after {
  content: " ";
  display: table;
}
.clearfix:after {
  clear: both;
}
.wrapper {
  width: 1440px;
  max-width: 90%;
  margin: 0 auto;
}
h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: 300;
}
body a:hover {
  color: #01b6d6 !important;
}


/*banner*/

#banner {
  /* background: url(https://m.media-amazon.com/images/M/MV5BMjMzODc3NzcxM15BMl5BanBnXkFtZTgwMjk5MjgwODM@._V1_SX1557_CR0,0,1557,999_AL_.jpg); */
  /* background-color: rgb(6, 6, 48); */
  background-size: cover;
  width: 100%;
  padding: 6.5em 0;
}
#banner_content_wrapper {
  width: 1400px;
  max-width: 100%;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  /* align-items: center; */
}
#banner_content_wrapper #poster {
  width: 275px;
  position: relative;
  float: left;
  
}
#poster img {
  width: 100%;
  max-width: 100%;
  border-radius: 0.5em;
}
#banner_content_wrapper #poster .playbutton {
  position: absolute;
  width: 80px;
  left: 50%;
  top: 50%;
  margin: -40px;
}
#banner_content_wrapper .content {
  float: left;
  width: 700px;
  max-width: 90%;
  margin-left: 100px;
}
.content{
  background: rgba(0,0,0,.8);
  padding:1em;
  margin-left:0px;
  border-radius:7px;
  overflow: auto;
  height: 350px;
  
}
.content .title {
  display: inline;
  font-size: 1.7em;
  color: white;
}
.content .ratings {
  display: inline;
  margin-left: 1em;
}
.content .ratings i {
  color: #01b6d6;
  font-size: 1.35em;
  margin: 0 0.15em;
}
.content .ratings i.inactive {
  color: #777;
}
.content .discription {
  color: #999;
  font-size: 1em;
  line-height: 2;
}
.content .info {
  color: #01b6d6;
  font-size: 0.8em;
  font-weight: 700;
  margin-top: 2em;
}
.content .info span {
  margin: 0.5em;
}

.raw {
  width: 100%;
  margin: auto;
}
/* .raw .post {
  width: 14%;
  min-height: 260px;
  float: left;
  margin-right: 2.5%;
} */

/* .raw .post img {
  width: 100%;
  min-height: 260px;
  max-width: 100%;
  border-radius: 0.3em;
} */


.raw .post {
  height: 14%;
  min-width: 260px;
  float: left;
  /* margin-right: 2.5%; */
}

.raw .post img {
  height: 100%;
  min-width: 260px;
  max-height: 100%;
  border-radius: 0.3em;
}

.raw .post .title {
  font-size: 1.25em;
  margin: 1em 0 0 0;
  color: #333333;
}
.raw .post .post_info {
  font-size: 0.75em;
  color: #777;
  margin: 0.5em 0;
}
#top_movies {
  border-bottom: 1px solid #d4d4d4;
}
#top_movies,
#top_shows {
  padding: 3em 0;
}

#top_movies header h2,
#top_movies .view_more {
  display: inline;
}

#top_shows header h2,
#top_shows .view_more {
  display: inline;
}
#top_movies header,
#top_shows header {
  padding: 0 0 1.5em 0;
}

#top_movies header h2,
#top_shows header h2 {
  font-size: 1.7em;
}
#top_movies header .view_more,
#top_shows header .view_more {
  float: right;
  font-size: 0.8em;
  margin: 1.7em 3.5% 0 0;
}


.card-description{
  
  font-size: 20px;
  padding: 1rem;
 
  /* 추가하기 */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical; 
  overflow: hidden;
}

.content__more-btn {
  appearance: none;
  border: 1px solid white;
  padding: 0.5em;
  border-radius: 0.25em;
  cursor: pointer;
  margin: 1rem;
}

.content__more-btn::before {
  content: '줄거리';
  color:white
}

.content__more-btn:checked::before {
  content: '닫기';
  color:white;
  
}

.card-description:has(+ .content__more-btn:checked) {
  -webkit-line-clamp:unset
}



</style>