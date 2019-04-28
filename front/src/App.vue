<template>
  <div id="app">
    <div v-if="!taskSelection">
      <Header v-if="openedTest===null"/>

      <Header v-else logo button :buttonEvent="()=>taskSelection=true"/>

      <div v-if="openedTest===null">
        <Logo/>
        <Button @click.native="taskSelection=true" text="Prześlij"/>
      </div>

      <div v-else>
        <p>
          {{openedTest.title}}
          <span>{{openedTest.id}}</span>
        </p>
        <HistoryEntry v-for="(result, key) in openedTest.results" :key="key" :title="`Test #${key+1}`" :status="result?'pass':'fail'"/>

      </div>

      <History @open-test="openTest" :tests="tests" v-if="tests.length!==0"/>
      <p v-else>Sprawdź swoje rozwiązanie!</p>
    </div>
    <div v-if="taskSelection">
      <Header logo/>
      <select @change="selectTask($event)" name="task" id="task">
        <option v-for="task in tasks" :key="task.title" :value="task.title">{{task.title}}</option>
      </select>
      <Task :task="selectedTask"/>
      <Send @submit-success="addTest" @submit-fail="testFailed"/>
    </div>
  </div>
</template>

<script>
import History from "./components/History.vue";
import HistoryEntry from "./components/HistoryEntry.vue";
import Header from "./components/Header.vue";
import Logo from "./components/Logo.vue";
import Send from "./components/Send.vue";
import Button from "./components/Button.vue";
import Task from "./components/Task.vue";
import { openDB } from "idb";

export default {
  name: "app",
  components: {
    History,
    Header,
    Logo,
    Send,
    Button,
    Task,
    HistoryEntry
  },
  data() {
    return {
      tests: [],
      openedTest: null,
      db: null,
      taskSelection: false,
      tasks: [
        {
          title: "Zadanie 1.1",
          body: "Tutaj mamy sobie treść zadania jako plaintext"
        },
        {
          title: "Zadanie 1.2",
          body: "Tutaj mamy sobie treść zadania jako plaintext 2"
        }
      ],
      selectedTask: null
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
      this.taskSelection = false;
      this.selectedTask = this.tasks[0];
    },
    testFailed: async function() {
      this.db.add("tests", {
        title: "Zadanie 1.5",
        id: "2s9fv2h2",
        status: "pass",
        results: [1, 1, 1]
      });
      this.tests = await this.db.getAll("tests");
      this.taskSelection = false;
      this.selectedTask = this.tasks[0];
    },
    openTest: function(id) {
      for (const test of this.tests) {
        if (test.id === id) {
          this.openedTest = test;
        }
      }
    },
    selectTask: function(event) {
      const title = event.target.value;
      for (const task of this.tasks) {
        if (task.title === title) {
          this.selectedTask = task;
        }
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
    this.db = db;
    this.tests = await db.getAll("tests");
    this.selectedTask = this.tasks[0];
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
