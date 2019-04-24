<template>
  <div id="app">
    <Header/>
    <Logo/>
    <input ref="file" type="file">
    <Button @click.native="send" text="Prześlij"/>
    <History v-if="tests.length!==0"/>
    <p v-else>
      Sprawdź swoje rozwiązanie!
    </p>
  </div>
</template>

<script>
import Button from "./components/Button.vue";
import History from "./components/History.vue";
import Header from "./components/Header.vue";
import Logo from "./components/Logo.vue";
import { openDB } from "idb";

const host = "http://ec2-52-29-167-193.eu-central-1.compute.amazonaws.com";

export default {
  name: "app",
  components: {
    Button,
    History,
    Header,
    Logo
  },
  data(){
    return{
      tests:[],
    }
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
  },
  created: async function() {
    const db = await openDB("Pseudotest", 1, {
      upgrade(db) {
        db.createObjectStore("tests", {
          keyPath: "id",
          autoIncrement: true
        });
      }
    });
    this.tests = await db.getAll('tests');
  }
};
</script>

<style>
*,
*::after,
*::before {
  box-sizing: border-box;
}
#app {
  font-family: "Roboto", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  color: #2c3e50;
  margin: 0 40px;
}
</style>
