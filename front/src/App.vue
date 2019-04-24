<template>
  <div id="app">
    <h1>Pseudo</h1>
    <input ref="file" type="file">
    <Button @click.native="send" text="Prześlij"/>
    <History/>
  </div>
</template>

<script>
import Button from "./components/Button.vue";
import History from "./components/History.vue";

const host = "http://ec2-52-29-167-193.eu-central-1.compute.amazonaws.com";

export default {
  name: "app",
  components: {
    Button,
    History
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
              console.log(response.message);
            }
          })
          .catch(err => console.log(err));
      }
    }
  }
};
</script>

<style>
#app {
  font-family: "Roboto", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
