<template>
    <div class="middle">
  
    <p>여기는 movielist</p>
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
