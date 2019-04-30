<template>
  <div v-if="isLoading">Loading…</div>

  <div v-else class="send">
    <input ref="file" type="file">
    <Button @click.native="send" text="Prześlij"/>
  </div>
</template>

<script>
import Button from "./Button.vue";

const host = "https://pseudotest.herokuapp.com";

export default {
  name: "Send",
  components: {
    Button
  },
  props: {
    taskId: Number
  },
  data() {
    return {
      isLoading: false
    };
  },
  methods: {
    send: function() {
      if (this.$refs["file"].files.length !== 0) {
        this.isLoading = true;
        let formData = new FormData();
        formData.append("file", this.$refs["file"].files[0]);
        formData.append("task", this.taskId);
        fetch(host + "/submit/", { method: "POST", body: formData })
          .then(r => r.json())
          .then(response => {
            this.isLoading = false;
            if (response.result === "error") {
              alert(response.message);
            } else {
              this.$emit("submit-success", response.message);
            }
          })
          .catch(err => {
            this.$emit("submit-fail", err);
          });
      }
    }
  }
};
</script>

<style scoped>
.send {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}
#app button {
  margin: 0;
}
</style>

