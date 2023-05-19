<template>
  <div>
    <p>응답 출력</p>
    <p>{{ chatgpt_answer }}</p>
  </div>
</template>

<script>
export default {
  name: "ChatGpt",
  props: {
    chatgpt_answer: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
