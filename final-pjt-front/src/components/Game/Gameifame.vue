<template>
  <div class="gamecontainer" @click="end">
    <iframe :src="game_url" frameborder="0" :class="`_${game}`"></iframe>
  </div>
</template>

<script>
export default {
  name: "Gameifame_",
  props: {
    game: String,
  },
  data() {
    return {
      game_url: `http://127.0.0.1:8000/game/${this.game}`,
    };
  },
  methods: {
    end() {
      this.$emit("end");
    },
  },
};
</script>

<style>
.gamecontainer {
  height: 100%;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}
._tetris {
  width: 510px;
  height: 660px;
}
._snake {
  height: 350px;
  width: 480px;
}
._2048 {
  height: 500px;
  width: 470px;
}
</style>
