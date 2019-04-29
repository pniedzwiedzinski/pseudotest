<template>
  <div>
    <p class="task">{{task}}</p>
  </div>
</template>

<script>
export default {
  name: "Task",
  props: {
    task: String
  }
};
</script>

<style scoped>
.task {
  margin: 50px 0;
}
</style>

