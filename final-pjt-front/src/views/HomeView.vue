<template>
  <div class="home">
    <h1>Orbit AI</h1>
          <img
        src="../assets/loading.gif"
        alt="loading"
        id="loading"
        v-show="is_loading"
      />
    <br />
    <ChatSearch @search="search" />
    <hr />
    <ChatGpt v-if="chatgpt_answer" :message="chatgpt_answer" @print_clear="print_movie"/>
    <ChatMovieList v-if="get_chatgpt_answer" :movie_list="response_movie_list" />
  </div>
</template>

<script>
// @ is an alias to /src
import ChatSearch from "@/components/Home/ChatSearch.vue";
import ChatGpt from "@/components/Home/ChatGpt.vue";
import ChatMovieList from "@/components/Home/ChatMovieList.vue";
import axios from "axios";

export default {
  name: "HomeView",
  components: {
    ChatSearch,
    ChatGpt,
    ChatMovieList,
  },
  data() {
    return {
      chatgpt_answer: null,
      movie_list: {},
      response_movie_list: [],
      get_chatgpt_answer: false,
      is_loading:false,
    };
  },
  methods: {
    search(searchkeyword) {
      console.log("도와줘");
      this.chatgpt_answer = null;
      this.movie_list = {};
      this.response_movie_list = [];
      this.get_chatgpt_answer = false;
      this.is_loading = true;
      const ChatGPTURL = "https://api.openai.com/v1/chat/completions";
      const API_KEY = "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";

      axios({
        method: "post",
        url: ChatGPTURL,
        headers: {
          Authorization: ` Bearer ${API_KEY}`,
        },
        data: {
          model: "gpt-3.5-turbo",
          messages: [
            {
              role: "user",
              content: `너는 지금부터 챗봇이자, 영화 추천 프로그램이야
            ${searchkeyword}라고 요청이 왔어 요청에 맞게 대답하고 이와 관련해서 한국 제목의 영화 적어도 10개 이상 추천해 줘`,
            },
          ],
        },
      })
        .then((response) => {
          this.is_loading = false;
          this.chatgpt_answer = response.data.choices[0].message.content
          this.change_answer_to_object();
        })
        .catch((error) => {
          this.is_loading = false;
          console.log("chatgpt 응답 에러");
          console.log(error);
        });
    },
    change_answer_to_object() {
      const ChatGPTURL = "https://api.openai.com/v1/completions";
      const API_KEY = "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";

      axios({
        url: ChatGPTURL,
        method: "post",
        headers: {
          Authorization: ` Bearer ${API_KEY}`,
        },
        data: {
          model: "text-davinci-003",
          prompt: `"${this.chatgpt_answer}"라는 대화 내용에서 영화 한글 제목인 것들만 숫자없이 줄바꿈으로 구분해 줘`,
          max_tokens: 2000,
          temperature: 0,
        },
      })
        .then((res) => {
          this.movie_list = {};
          console.log(res.data.choices[0].text);
          for (let movie_title of res.data.choices[0].text.split("\n")) {
            this.movie_list[movie_title] = "";
          }
          this.get_movie(this.movie_list);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    get_movie(params) {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/v1/movie/title/",
        params: params,
      })
        .then((res) => {
          console.log(res);
          this.response_movie_list = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    print_movie(){
      this.get_chatgpt_answer = true
    }
  },
};
</script>

<style scoped>
#loading {
  position: fixed;
  left: 50%;
  transform: translate(-50%, 0);
  top: 50%;
}
</style>