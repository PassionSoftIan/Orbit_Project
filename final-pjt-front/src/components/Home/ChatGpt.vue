<template>
  <div class="chat">
    <span v-for="(char, index) in visibleChars" :key="index">
      <span v-if="char"  class="answer">{{ char }}</span>
    </span>
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      visibleChars: []
    };
  },
  mounted() {
    this.animateText();
  },
  methods: {
    animateText() {
      let index = 0;
      const intervalId = setInterval(() => {
        this.$set(this.visibleChars, index, this.message[index]);
        index++;
        if (index >= this.message.length) {
          clearInterval(intervalId);
          this.$emit("print_clear")
        }
      }, 30); // 각 글자를 표시하는 간격 (200ms로 설정됨)
    }
  }
};
</script>

<style>
.chat {
  background-color: chocolate;
  border: solid;
}
.answer {
  font-size: 20px;
}
</style>
