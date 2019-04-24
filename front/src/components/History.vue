<template>
  <div class="history">
    <h3 class="header">Poprzednie wyniki</h3>
    <div class="entries">
      <div class="entry">
        <div class="status pass"></div>
        <div class="task_name">Zadanie 1.2</div>
        <div class="job_id">(sd8d93bh)</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "History"
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
  margin-top: 60px;
  width: 800px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.25);
}

.entry {
  height: 56px;

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
  height: 100%;
  width: 15px;
}

.status.pass {
  background: #78ff9e;
}
</style>