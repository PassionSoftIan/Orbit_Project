<template>
  <div
    class="card mb-3"
    style="max-width: 540px; background-color: rgb(240, 230, 220)"
  >
    <div class="row g-0">
      <div class="col-md-4">
        <router-link
          :to="{ name: 'MovieDetail', params: { moviepk: movie.id } }"
        >
          <img
            :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path"
            class="img-fluid rounded-start"
            alt="..."
        /></router-link>
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <router-link
            :to="{ name: 'MovieDetail', params: { moviepk: movie.id } }"
            class="title"
          >
            <h5 class="card-title">
              {{ movie.title }}({{ movie.release_date.slice(0, 4) }})
            </h5>
          </router-link>

          <p class="card-text">{{ movie.tagline }}</p>

          <h6>
            TMDB {{ movie.vote_average / 2 }} / Orbit
            {{
              movie.ours_vote / movie.vote_count
                ? (movie.ours_vote / movie.vote_count).toFixed(2)
                : 0
            }}
          </h6>
          <hr />
          <div class="stars-wrapper">
            <h2 class="site">TMDB</h2>
            <span
              class="Stars"
              :style="`--rating: ${(movie.vote_average / 2).toFixed(2)}`"
            ></span>
          </div>
          <div class="stars-wrapper">
            <h2 class="site">Orbit</h2>
            <span
              class="Stars"
              :style="`--rating:  ${
                movie.ours_vote / movie.vote_count
                  ? (movie.ours_vote / movie.vote_count).toFixed(2)
                  : 0
              }`"
            ></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // name: "Movielistitem",
  data() {
    return {};
  },
  props: {
    movie: Object,
  },
};
</script>

<style>
.title {
  color: black;
  text-decoration: none;
}
:root {
  --star-size: 75px;
  --star-color: #fff;
  --star-background: #fc0;
}
.stars-wrapper {
  display: flex;
  justify-content: center;
  height: 50px;
  width: 100%;
}
.site {
  margin-top: 10px;
  margin-left: 35px;
  color: slategray;
}
.Stars {
  --percent: calc(var(--rating) / 5 * 100%);
  display: flex;
  justify-content: flex-end;
  align-items: center;
  font-size: var(--star-size);
  /* font-family: Times; */
  line-height: 1;
  width: 100%;
  margin-bottom: 1.8px;
  padding-right: 17px;
  /* z-index: 1; */
}
.Stars::before {
  content: "★★★★★";
  letter-spacing: 1px;
  background: linear-gradient(
    90deg,
    var(--star-background) var(--percent),
    var(--star-color) var(--percent)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: flex;
  align-items: center;
}
.card-body {
  height: 0px;
}
* {
  position: relative;
  box-sizing: border-box;
}
</style>
