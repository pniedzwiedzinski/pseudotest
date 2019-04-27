<template>
  <div id="app">
    <Header/>
    <Logo/>
    <Send v-on:submit-success="addTest" v-on:submit-fail="testFailed"/>
    <History :tests="tests" v-if="tests.length!==0"/>
    <p v-else>Sprawdź swoje rozwiązanie!</p>
  </div>
</template>

<script>
import History from "./components/History.vue";
import Header from "./components/Header.vue";
import Logo from "./components/Logo.vue";
import Send from "./components/Send.vue";
import { openDB } from "idb";

export default {
  name: "app",
  components: {
    History,
    Header,
    Logo,
    Send
  },
  data() {
    return {
      tests: [],
      db: ""
    };
  },
  methods: {
    addTest: async function() {
      this.db.add("tests", {
        title: "Zadanie 1.1",
        id: "2s9fv2h2",
        status: "fail",
        results: [0, 1, 1]
      });
      this.tests = await this.db.getAll("tests");
    },
    testFailed: async function() {
      this.db.add("tests", {
        title: "Zadanie 1.5",
        id: "2s9fv2h0",
        status: "fail",
        results: [0, 1, 1]
      });
      this.tests = await this.db.getAll("tests");
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
    this.db = db;
    this.tests = await db.getAll("tests");
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
