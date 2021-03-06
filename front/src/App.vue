<template>
  <div id="app">
    <div v-if="!taskSelection">
      <Header v-if="openedTest===null"/>

      <Header v-else logo button :buttonEvent="()=>taskSelection=true"/>

      <div class="flex-column-center" v-if="openedTest===null">
        <Logo class="main-logo-margin"/>
        <Button
          class="main-button-margin"
          @click.native="taskSelection=true"
          text="Wybierz zadanie"
        />
      </div>

      <div class="test-details" v-else>
        <p>
          {{openedTest.title}}
          <span>{{openedTest.id}}</span>
        </p>
        <div class="entries entries--short">
          <HistoryEntry
            v-for="(result, key) in openedTest.results"
            :key="key"
            :title="`Test #${key+1}`"
            :status="result?'pass':'fail'"
          />
        </div>
      </div>

      <History
        :class="openedTest===null?'margin-auto pb-100':''"
        @open-test="openTest"
        :tests="tests"
        v-if="tests.length!==0"
      />
      <div v-else class="margin-auto">
        <h2 class="check-your-solution">Sprawdź swoje rozwiązanie!</h2>
        <p>
          Prześlij swój algorytm zapisany w
          <a
            href="https://github.com/pniedzwiedzinski/pseudo"
          >pseudokodzie</a> i sprawdź jego poprawność.
        </p>
      </div>
      <div class="cc">
        Icons made by
        <a
          href="https://www.flaticon.com/authors/smashicons"
          title="Smashicons"
        >Smashicons</a> from
        <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by
        <a
          href="http://creativecommons.org/licenses/by/3.0/"
          title="Creative Commons BY 3.0"
          target="_blank"
        >CC 3.0 BY</a>
      </div>
    </div>

    <div v-if="taskSelection">
      <Header logo/>
      <div class="container">
        <div>
          <h3 style="display: inline-block">Wybierz zadanie:</h3>
          <select @change="selectTask($event)" name="task" id="task" style="display: inline-block">
            <option v-for="task in tasks" :key="task.name" :value="task.name">{{task.name}}</option>
          </select>
        </div>
        <Task :task="selectedTask.description"/>
        <Send :taskId="selectedTask.id" @submit-success="addTest" @submit-fail="testFailed"/>
      </div>
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
      host: "https://pseudotest.herokuapp.com",
      tests: [],
      openedTest: null,
      db: null,
      taskSelection: false,
      tasks: [],
      selectedTask: [],
      pendingTasks: []
    };
  },
  methods: {
    addTest: async function(id) {
      const newTask = {
        title: this.selectedTask.name,
        id: id,
        status: "pending",
        results: [],
        time: Date.now()
      };
      this.db.add("tests", newTask);
      this.pendingTasks.push(newTask);
      this.tests = await this.db.getAllFromIndex("tests", "time");
      this.taskSelection = false;
      this.selectedTask = this.tasks[0];
    },
    testFailed: async function(error) {
      alert(error);
    },
    openTest: function(id) {
      for (const test of this.tests) {
        if (test.id === id) {
          this.openedTest = test;
        }
      }
    },
    selectTask: function(event) {
      const name = event.target.value;
      for (const task of this.tasks) {
        if (task.name === name) {
          this.selectedTask = task;
        }
      }
    },
    refreshPending: async function() {
      for (const pendingTask of this.pendingTasks) {
        const db = this.db;
        const pendingTasks = this.pendingTasks;
        fetch(this.host + "/get/" + pendingTask.id)
          .then(r => r.json())
          .then(response => {
            if (response.status === "error") {
              db.transaction("tests", "readwrite")
                .objectStore("tests")
                .put(Object.assign(pendingTask, { status: "error" }));
              pendingTasks.splice(pendingTasks.indexOf(pendingTask), 1);
              return this.db.getAllFromIndex("tests", "time");
            } else if (Array.isArray(response.status)) {
              if (response.status.includes(0)) {
                db.transaction("tests", "readwrite")
                  .objectStore("tests")
                  .put(
                    Object.assign(pendingTask, {
                      status: "fail",
                      results: response.status
                    })
                  );
              } else {
                db.transaction("tests", "readwrite")
                  .objectStore("tests")
                  .put(
                    Object.assign(pendingTask, {
                      status: "pass",
                      results: response.status
                    })
                  );
              }
              pendingTasks.splice(pendingTasks.indexOf(pendingTask), 1);
              return this.db.getAllFromIndex("tests", "time");
            }
          })
          .then(refreshedTests => {
            this.tests = refreshedTests;
            this.openedTest = this.tests[this.tests.length - 1]; //possible fix in the future
          });
      }
      setTimeout(this.refreshPending, 5000);
    }
  },
  created: async function() {
    fetch(this.host + "/tasks/")
      .then(r => r.json())
      .then(response => {
        this.tasks = response;
        this.selectedTask = this.tasks[0];
      });
    const db = await openDB("Pseudotest", 1, {
      upgrade(db) {
        const store = db.createObjectStore("tests", {
          keyPath: "id"
        });
        store.createIndex("time", "time");
      }
    });
    this.db = db;
    this.tests = await this.db.getAllFromIndex("tests", "time");
    this.pendingTasks = this.tests.filter(test => test.status === "pending");
    this.refreshPending();
  }
};
</script>

<style>
*,
*::after,
*::before {
  box-sizing: border-box;
}
body {
  margin: 0;
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
  min-height: 100vh;
}
#app > div {
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 100%;
  min-height: 100vh;
}
.container {
  min-width: 80vw;
  margin: 100px 20px 0;
}
.flex-column-center {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.check-your-solution {
  font-size: 24px;
}
.margin-auto {
  margin: auto;
}
.pb-100 {
  padding-bottom: 100px;
}
#app .main-button-margin {
  margin: 60px 0 0;
}
.main-logo-margin {
  margin: 60px 0 0;
}
select {
  margin-left: auto;
  display: block;
}
.entries {
  width: 800px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.25);
}
.entries--short {
  width: 400px;
}
.test-details {
  margin: 100px 0;
}

.cc {
  margin: 60px 0px 40px;
}
</style>
