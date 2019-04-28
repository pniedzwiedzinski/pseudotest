<template>
  <div>
    <p>{{task.title}}</p>
    <p>{{task.body}}</p>
  </div>
</template>

<script>
export default {
  name: "Task",
  props: {
    task: Object
  }
};
</script>

