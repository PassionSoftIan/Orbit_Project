<template>
    <div class="middle">
      <hr>
    <p>아래는 추천 영화 중 저희가 가지고 있는 영화 입니다</p>
    <div class="card-wrapper">
    <ChatMovieListItemVue
      :movie="movie"
      v-for="movie of movie_list"
      :key="movie.id"
    />
  </div>
  </div>
</template>

<script>
import ChatMovieListItemVue from "./ChatMovieListItem.vue";
export default {
  name: "MovieList",
  components: {
    ChatMovieListItemVue,
  },
  props: {
    movie_list: Array,
  },
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card-wrapper {
  display: inline-block;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  
}
</style>
