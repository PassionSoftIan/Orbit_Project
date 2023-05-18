<template>
  <div>
    <p>{{ movie.title }}</p>
    <p>{{ movie.overview }}</p>
    <hr />
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
