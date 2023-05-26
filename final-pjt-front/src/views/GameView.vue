<template>
  <div class="game">
    <h1>Game</h1>
    <!-- <button @click="select_game('tetris')">Tetris</button>
    <button @click="select_game('snake')">Snake</button>
    <button @click="select_game('2048')">2048</button>

    <GameifameVue v-if="game" :game="game" @end="end" /> -->

    <b-button @click="ModalReset('tetris')" variant="Dark"
      ><img src="@/images/tetris.png" alt=""
    /></b-button>
    <b-button @click="ModalReset('snake')" variant="Dark"
      ><img src="@/images/snake.png" alt=""
    /></b-button>
    <b-button @click="ModalReset('2048')" variant="Dark"
      ><img src="@/images/2048.png" alt=""
    /></b-button>

    <b-modal v-model="modalShow">
      <!-- <input type="text" @input='changeKeyword' @keyup="SearchTitle"> -->
      <iframe
        :src="game_url"
        frameborder="0"
        :class="`_${game}`"
        ref="game_iframe"
      ></iframe>
    </b-modal>
  </div>
</template>

<script>
// import GameifameVue from "../components/Game/Gameifame.vue";
export default {
  name: "GameView",
  components: {
    // GameifameVue,
  },
  computed: {
    user_pk() {
      return this.$store.state.user_pk;
    },
    game_url() {
      return `http://127.0.0.1:8000/game/${this.game}/${this.user_pk}`;
    },
  },
  data() {
    return {
      game: null,
      modalShow: false,
    };
  },
  watch: {
    modalShow: {
      handler(newvalue, oldvalue) {
        if (!newvalue && oldvalue) {
          this.$store.dispatch("userChange");
        }
      },
    },
  },
  methods: {
    select_game(game_name) {
      this.game = game_name;
    },
    end() {
      this.game = null;
    },
    ModalReset(game_name) {
      if (!this.modalShow) {
        this.game = game_name;
        this.SearchTitleList = null;
        this.modalShow = !this.modalShow;
        console.log(this.$refs.game_iframe);
      }
    },
  },
};
</script>

<style scoped>
.game {
  background-image: url("../../public/images/Game.gif");
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
  overflow-x: hidden;
  height: 91.3vh;
  width: 100vw;
}
._tetris {
  width: 470px;
  height: 660px;
}
._snake {
  height: 400px;
  width: 475px;
}
._2048 {
  height: 500px;
  width: 470px;
}
</style>
