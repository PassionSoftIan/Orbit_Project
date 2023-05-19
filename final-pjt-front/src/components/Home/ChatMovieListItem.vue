<template>
  <div>
    <router-link :to="{name:'MovieDetail', params:{moviepk:movie.id}}">
    <p>{{ movie.title }}</p>
    <p>{{ movie.overview }}</p>
    </router-link>
    <hr />
    <router-view/>
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

<style></style>
