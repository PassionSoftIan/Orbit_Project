<template>
  <div class="home">
    <h1>Home</h1>
    <br>
    <ChatSearch />
    <ChatGpt />
    <ChatMovieList />
  </div>
</template>

<script>
// @ is an alias to /src
import ChatSearch from '@/components/Home/ChatSearch.vue'
import ChatGpt from '@/components/Home/ChatGpt.vue'
import ChatMovieList from '@/components/Home/ChatMovieList.vue'

export default {
  name: 'HomeView',
  components: {
    ChatSearch,
    ChatGpt,
    ChatMovieList,
  },
}
</script>
