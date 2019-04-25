<template>
  <div class="entry">
    <div class="task_info">
      <div class="status" v-bind:class="status"></div>
      <div class="task_name">{{title}}</div>
      <div class="job_id">({{id}})</div>
    </div>
    <div class="quickview">
      <p v-if="status==='pending'">Sprawdzanie...</p>
      <p v-if="status==='error'">Przerwanie</p>
      <div class="results" v-else>
        <div v-for="result in results">
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
    Fail
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
}
</style>

