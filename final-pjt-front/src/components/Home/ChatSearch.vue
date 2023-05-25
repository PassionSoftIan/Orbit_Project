<template>
  <div>
    <p style="font-size: 20px; color: blue">삐빅-! 아무 말이나 해주시면 관련 영화를 추천 해드릴게요</p>
    <p style="font-size: 20px">한 번 검색에 코인 5개 소모!</p>
    <p style="font-size: 20px">포인트 획득은 게임으로!</p>
    <input
      type="text"
      name="searchbar"
      id="searchbar"
      v-model="searchkeyword"
      @keydown.enter="search"
      class="search"
    />
    <img type="button" src="@/assets/coin/coin_image.png/" class="icon" @click="search">

    <br />
  </div>
</template>

<script>
export default {
  name: "ChatSearch",
  data() {
    return {
      searchkeyword: "",
    };
  },
  methods: {
    search() {
      const coins = -5
      const payload = {
        coins,
      }

      if (this.$store.state.coins >= 5) {
        if (this.searchkeyword.length === 0) {
          alert("검색어를 입력해 주세요");
          return;
        }
        this.$emit("search", this.searchkeyword);
      } else {
        alert("코인이 부족합니다.")
        console.log('여기까지는 옴')
        return
      }
      return this.$store.dispatch('coinChange', payload)

    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* .icon {
  background: "@/assets/coin/coin_transparent.png/";
  background-color: transparent;
  background-size: 100%;
  align-content: center;
  width: 35px;
  height: 100%;
} */
.icon {
  width: 30px;
  height: 100%;
  margin-left: 4px;
  margin-bottom: 2.5px;
}
.search {
  height: 28px;
  background-color: honeydew;

}

</style>
