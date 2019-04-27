<template>
  <div>
    <input ref="file" type="file">
    <Button @click.native="send" text="Prześlij"/>
  </div>
</template>

<script>
import Button from "./Button.vue";

const host = "http://ec2-52-29-167-193.eu-central-1.compute.amazonaws.com";

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
        formData.append("task", "add");
        fetch(host + "/submit/", { method: "POST", body: formData })
          .then(r => r.json())
          .then(response => {
            if (response.status == "success") {
              this.$emit("submit-success", response.body);
            }
          })
          .catch(err => {this.$emit("submit-fail", err)});
      }
    }
  }
};
</script>

<style scoped>
</style>

