<template>
  <div id="app">
    <h1>Pseudo</h1>
    <Button text="Prześlij"/>
    <History/>
  </div>
</template>

<script>
import Button from './components/Button.vue'
import History from './components/History.vue'

export default {
  name: 'app',
  components: {
    Button,
    History
  }
}
</script>

<style>
#app {
  font-family: 'Roboto', Helvetica, Arial, sans-serif;
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
