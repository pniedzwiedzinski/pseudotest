<template>
  <div>
    <div class="info">
      <img class="icon" src="@/assets/warning.svg" alt>
    </div>
    <div class="more_info">{{text}}</div>
  </div>
</template>

<script>
export default {
  name: "Info",
  props: {
    text: String
  }
};
</script>

<style scoped>
.more_info {
  z-index: 99;
  display: none;
  background: #fff;
  padding: 20px;
  width: 250px;
  text-align: left;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.25);
}

.info {
  filter: invert(0.5);
  margin: 3px;
}

.info:hover + .more_info {
  display: block;
  position: absolute;
  margin-left: 40px;
}

.icon {
  height: 21px;
}
</style>

