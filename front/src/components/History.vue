<template>
  <div class="history">
    <h3 class="header">Poprzednie wyniki</h3>
    <div class="entries">
      <HistoryEntry title="Zadanie 1.2" id="2s9fv2h3" status="pass" :results="[1, 1, 1]"/>
      <HistoryEntry title="Zadanie 1.2" id="2s9fv2h3" status="fail" :results="[1, 0, 1]"/>
      <HistoryEntry title="Zadanie 1.2" id="2s9fv2h3" status="pending"/>
      <HistoryEntry title="Zadanie 1.2" id="2s9fv2h3" status="error"/>
    </div>
  </div>
</template>

<script>
import HistoryEntry from "./HistoryEntry.vue";

export default {
  name: "History",
  components: {
    HistoryEntry
  }
};
</script>

<style scoped>
.history {
  position: relative;
}

.header {
  position: absolute;
  left: -40px;
}

.entries {
  width: 800px;

  margin-top: 60px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.25);
}
</style>