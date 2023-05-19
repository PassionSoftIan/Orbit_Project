<template>
  <div class="game">
    <h1>Game</h1>
    <button @click="select_game('tetris')">Tetris</button>
    <button @click="select_game('snake')">Snake</button>
    <button @click="select_game('2048')">2048</button>

    <GameifameVue v-if="game" :game="game" @end="end" />
  </div>
</template>

<script>
import GameifameVue from "../components/Game/Gameifame.vue";
export default {
  name: "GameView",
  components: {
    GameifameVue,
  },
  data() {
    return {
      game: null,
    };
  },
  methods: {
    select_game(game_name) {
      this.game = game_name;
    },
    end() {
      this.game = null;
    },
  },
};
</script>

<style></style>
