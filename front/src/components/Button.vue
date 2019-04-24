<template>
  <div class="button">
    {{text}}
  </div>
</template>

<script>
export default {
  name: 'Button',
  props: {
    text: String
  }
}
</script>

<style scoped>
.button {
  width: 153px;
  height: 46px;
  color: #FFFFFF;
  background: #3C8AFF;
  box-shadow: 0px 0px 10px rgba(60, 138, 255, 0.5);

  padding: 11px;
  margin: 20px;

  box-sizing: border-box;

  font-family: Roboto, arial;
  font-weight: 500;
  font-size: 20px;
  line-height: normal;
  text-align: center;
  letter-spacing: 0.08em;
}
</style>
