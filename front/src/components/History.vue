<template>
  <div class="history">
    <h3 class="header">Poprzednie wyniki</h3>
    <div class="entries">
      <HistoryEntry 
        v-for="test in tests.slice().reverse()" 
        :key="test.id" 
        :title="test.title" 
        :id="test.id" 
        :status="test.status" 
        :results="test.results"
        @click.native="$emit('open-test',test.id)"/>
    </div>
  </div>
</template>

<script>
import HistoryEntry from "./HistoryEntry.vue";

export default {
  name: "History",
  components: {
    HistoryEntry
  },
  props: {
    tests: Array
  }
};
</script>

<style scoped>
.header {
  text-align: left;
  margin-left: -40px;
}
</style>