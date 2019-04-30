<template>
  <div class="send">
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
  methods: {
    send: function() {
      if (this.$refs["file"].files) {
        let formData = new FormData();
        formData.append("file", this.$refs["file"].files[0]);
        formData.append("task", 1);
        fetch(host + "/submit/", { method: "POST", body: formData })
          .then(r => r.json())
          .then(response => {
            if (response.result === "error") {
              console.error(response.message);
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

