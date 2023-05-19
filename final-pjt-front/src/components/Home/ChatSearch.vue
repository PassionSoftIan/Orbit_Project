<template>
  <div>
    <p>ChatSearch 에서 인사 드립니다</p>
    <input
      type="text"
      name="searchbar"
      id="searchbar"
      v-model="searchkeyword"
      @keydown.enter="search"
    />
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
      if (this.searchkeyword.length === 0) {
        alert("검색어를 입력해 주세요");
        return;
      }

      this.$emit("search", this.searchkeyword);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
