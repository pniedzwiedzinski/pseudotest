<template>
  <div class="button">{{text}}</div>
</template>

<script>
export default {
  name: "Button",
  props: {
    text: String
  }
};
</script>

<style scoped>
.button {
  width: 153px;
  height: 46px;
  padding: 11px;
  margin: 20px;

  font-family: Roboto, arial;
  font-weight: 500;
  font-size: 20px;
  line-height: normal;
  text-align: center;
  letter-spacing: 0.08em;

  cursor: pointer;
  color: #ffffff;
  background: #3c8aff;
  box-shadow: 0px 0px 10px rgba(60, 138, 255, 0.5);
}
</style>
