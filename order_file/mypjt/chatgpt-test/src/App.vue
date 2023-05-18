<template>
  <div id="app">
    <div v-if="false">
      <img
        src="./assets/loading.gif"
        alt="loading"
        id="loading"
        v-show="is_loading"
      />
      <label v-for="genre of genres" :key="genre">
        <input type="checkbox" v-model="genre[1]" /> {{ genre[0] }}
      </label>
      <br />
      <br />
      <p>{{ select.join(", ") }}</p>
      <button @click="sendchatgpt">추천받기</button>
      <hr />
      <a
        target="_blank"
        :href="`https://www.google.com/search?q=영화 ${movie}`"
        v-for="movie of answer"
        :key="`${movie}`"
        class="movie-title"
      >
        {{ movie }}
      </a>
    </div>
    <HelloWorldVue />
  </div>
</template>

<script>
import axios from "axios";
import HelloWorldVue from "./components/HelloWorld.vue";
export default {
  name: "App",
  components: { HelloWorldVue },
  data() {
    return {
      is_loading: false,
      response: "",
      genres: [
        ["action", false],
        ["comedy", false],
        ["slapstick", false],
        ["romcom", false],
        ["thriller", false],
        ["horror", false],
        ["war film", false],
        ["musical film", false],
        ["melodrama", false],
        ["science fiction film", false],
      ],
      select: [],
    };
  },
  methods: {
    sendchatgpt() {
      if (this.is_loading) return;
      if (this.select.length === 0) {
        alert("장르를 선택해 주세요");
        return;
      }
      // for (let index in this.genres) {
      //   const genre = [this.genres[index][0], false];
      //   this.genres[index] = genre;
      // }
      for (let genre of this.genres) {
        genre[1] = false;
      }
      this.select = [];
      this.is_loading = true;
      this.response = "";
      console.log("gpt에몽 도와줘");
      const chatgptapiurl = "https://api.openai.com/v1/completions";
      const api_key = "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";

      axios({
        url: chatgptapiurl,
        method: "post",
        headers: {
          Authorization: ` Bearer ${api_key}`,
          // Content-Type: "application/json"
        },
        data: {
          model: "text-davinci-003",
          prompt: this.request,
          max_tokens: 500,
          temperature: 1,
        },
      })
        .then((response) => {
          this.is_loading = false;
          console.log("chatgpt : 도와드렸습니다~");
          // console.log(response);
          this.response = response.data.choices[0].text;
        })
        .catch((error) => {
          this.is_loading = false;
          console.log(error);
        });
    },
  },
  computed: {
    // select() {
    //   const selectedgenre = this.genres
    //     .filter((genre) => genre[1])
    //     .map((genre) => genre[0]);
    //   return selectedgenre;
    // },
    request() {
      return `Suggest 20 just movie titles that span ${this.select.join(
        ", "
      )} genres. you just answer movie title. I don't want to know movie's genre`;
    },
    answer() {
      return this.response
        .split("\n")
        .map((movie) => movie.slice(3, movie.length));
    },
  },
  watch: {
    genres: {
      handler() {
        this.select = this.genres
          .filter((genre) => genre[1])
          .map((genre) => genre[0]);
      },
      deep: true,
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#loading {
  position: fixed;
  left: 50%;
  transform: translate(-50%, 0);
  top: 50%;
}
.movie-title {
  margin: 10px;
}
</style>
