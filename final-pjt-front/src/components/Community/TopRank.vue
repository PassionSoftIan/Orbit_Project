<template>
<div class="page-single movie_list">
	<div class="container">
		<div class="row ipad-width2">
			<div class="col-md-4 col-sm-12 col-xs-12">
				<div class="movie-item-style-2">
					<img :src="`https://image.tmdb.org/t/p/w300/`+Movie.poster_path" alt="">
					<div class="mv-item-infor text-light">
						<h6><router-link :to="{name:'MovieDetail', params:{moviepk:Movie.id}}">{{Movie.title}} <span>({{Movie.release_date.slice(0,4)}})</span></router-link></h6>
						<p class="rate"><i class="ion-android-star"></i><span>{{Movie.vote_average}}</span> /10</p>
						<p class="describe">{{Movie.tagline}}</p>
						<!-- <p class="run-time"> Run Time: 2h21’    .     <span>MMPA: PG-13 </span></p> -->
            <span>개봉일 : {{Movie.release_date}}</span>
						<!-- <p>Director: <a href="#">Joss Whedon</a></p>
						<p>Stars: <a href="#">Robert Downey Jr.,</a> <a href="#">Chris Evans,</a> <a href="#">  Chris Hemsworth</a></p> -->
            <p> 장르 :
            <span
            v-for="ger in Movie.genre"
            :key="ger.id">
            {{ger.name}}
            </span></p>
					</div>
				</div>
			</div>
		</div>
  <hr>
	</div>
</div>
  <!-- <div>
    <router-link :to="{name:'MovieDetail', params:{moviepk:Movie.id}}">

    <p>{{Movie.title}}</p>
    <p>{{Movie.overview}}</p>
    <p>{{Movie.genre}}</p>

  
    <img :src="`https://image.tmdb.org/t/p/w500/`+Movie.poster_path" alt="">

    <p>{{Movie.vote_average}}</p>
    <p>수익: {{Movie.revenue}}</p>
    
    </router-link>
    <hr>
  </div> -->
</template>

<script>

export default {
  name:"TopRank",
  data(){
    return{
      imgurl: 'https://image.tmdb.org/t/p/w500/' 
    }
  },

  props:{
    Movie:Object
  },
  

}
</script>

<style scoped>
hr {
    background:pink;
    height:5px;
    border:0;
}
.row{
  *zoom: 1;
}
.page-single {
  /* background-color: #020d18; */
  padding: 75px 0;
}

.movie_list .movie-item-style-2 img{
  width: 30%;
}
@media (max-width: 767px) {
  .movie_list .movie-item-style-2 img{
    width: auto;
  }
}

.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 15px;
  padding-right: 15px;
}
@media (min-width: 768px) {
  .container {
    width: 750px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 970px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1170px;
  }
}

.row {
  margin-left: -15px;
  margin-right: -15px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 15px;
  padding-right: 15px;
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
}
.movie_list .movie-item-style-2 img,
.movie_single .movie-item-style-2 img,
.userfav_list .movie-item-style-2 img {
  width: 30%;
}
@media (max-width: 767px) {
  .movie_list .movie-item-style-2 img,
  .movie_single .movie-item-style-2 img,
  .userfav_list .movie-item-style-2 img {
    width: auto;
  }
}
.movie-item-style-2 {
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  overflow: hidden;
  margin-bottom: 30px;
}
@media (max-width: 767px) {
  .movie-item-style-2 {
    display: flex;
    flex-direction: column;
  }
}
.movie-item-style-2 img {
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
  margin-right: 30px;
  -webkit-transition: all 0.5s ease-out;
  -moz-transition: all 0.5s ease-out;
  -o-transition: all 0.5s ease-out;
  transition: all 0.5s ease-out;
}
@media (max-width: 767px) {
  .movie-item-style-2 img {
    margin-right: 0;
    margin-bottom: 15px;
  }
}
@media (max-width: 767px) {
  .movie-item-style-2 .mv-item-infor {
    max-width: 180px;
    margin: 0 auto;
  }
}
.movie-item-style-2 .mv-item-infor h6 {
  margin-bottom: 10px;
}
.movie-item-style-2 .mv-item-infor h6 router-link {
  font-family: 'Dosis', sans-serif;
  font-size: 14px;
  color: #ffffff;
  font-weight: bold;
  text-transform: uppercase;
}
.movie-item-style-2 .mv-item-infor h6 router-link span {
  color: #abb7c4;
}
.movie-item-style-2 .mv-item-infor .describe {
  padding-bottom: 25px;
  border-bottom: 1px solid #405266;
  margin-bottom: 25px;
}
.movie-item-style-2 .mv-item-infor .run-time span {
  margin-left: 15px;
  margin-right: 15px;
}
.movie-item-style-2 .mv-item-infor .rate {
  font-size: 12px;
}
.movie-item-style-2 .mv-item-infor .rate i {
  color: #f5b50a;
  font-size: 22px;
  margin-right: 5px;
}
.movie-item-style-2 .mv-item-infor .rate span {
  color: #ffffff;
  font-size: 16px;
  font-weight: 400;
}
.movie-item-style-2 .mv-item-infor p {
  margin-bottom: 0;
}
.movie-item-style-2 .mv-item-infor p a {
  color: #4280bf;
}
.movie-item-style-2 .mv-item-infor p a:hover {
  color: #dcf836;
}

</style>