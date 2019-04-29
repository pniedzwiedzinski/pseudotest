<template>
  <div class="entry">
    <div class="task_info">
      <div class="status" :class="status"></div>
      <div class="task_name">{{title}}</div>
      <div v-if="id!==undefined" class="job_id">({{id}})</div>
    </div>
    <div class="quickview">
      <div v-if="status==='pending'">Sprawdzanie...</div>
      <div v-if="status==='error'" class="results">
        <Info
          text="Sprawdzanie twojego zadania zostało przerwane ponieważ algorytm nie mógł zostać przetworzony. Sprawdź poprawność zapisu."
        />Przerwanie
      </div>
      <div class="results" v-else>
        <div :key="key" v-for="(result, key) in results">
          <Check v-if="result===1"/>
          <Fail v-else/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Check from "./Check.vue";
import Fail from "./Fail.vue";
import Info from "./Info.vue";

export default {
  name: "HistoryEntry",
  props: {
    title: String,
    id: String,
    status: String,
    results: Array
  },
  components: {
    Check,
    Fail,
    Info
  }
};
</script>

<style scoped>
.entry {
  height: 56px;

  display: flex;
  align-items: center;
}

.entry:hover {
  background: #eee;
}

.task_info {
  flex: 1;
  display: flex;
  align-items: center;
}

.task_name {
  margin: 10px;
}

.job_id {
  opacity: 0.6;
}

.status {
  height: 56px;
  width: 15px;
}

.status.pass {
  background: #78ff9e;
}

.status.fail {
  background: #ff6c6c;
}

.status.pending {
  background: #ffee55;
}

.status.error {
  background: #ab78ff;
}

.quickview {
  margin-right: 15px;
  color: rgba(59, 59, 59, 0.61);
}

.results {
  display: flex;
  flex-direction: row;
  align-items: center;
}
</style>

