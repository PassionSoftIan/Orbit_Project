<template>
  <!-- 사용 안함 -->
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
  computed:{
    user_pk(){
        return this.$store.state.user_pk
    }
  },
  data() {
    return {
      game_url: null,
    };
  },
  methods: {
    end() {
      this.$emit("end");
    },
  },
  created(){
    this.game_url = `http://127.0.0.1:8000/game/${this.game}/${this.user_pk}`
  }
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
