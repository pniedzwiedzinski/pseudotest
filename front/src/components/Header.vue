<template>
  <header>
    <div>
      <Logo v-if="logo"/>
    </div>
    <div class="header-links">
      <a href="https://github.com/pniedzwiedzinski/pseudotest/" target="_blank" rel="nofollow">
        pseudotest
        <img src="@/assets/GitHub.png" alt="Github icon">
      </a>
      <a
        href="https://github.com/pniedzwiedzinski/pseudotest/issues/new?assignees=&labels=bug&template=bug_report.md"
      >
        zgłoś błąd
        <img src="@/assets/warning.svg" alt>
      </a>
      <Button id="send-button" text="Prześlij" v-if="button" @click.native="buttonEvent"/>
    </div>
  </header>
</template>

<script>
import Logo from "@/components/Logo.vue";
import Button from "@/components/Button.vue";

export default {
  name: "Header",
  components: {
    Logo,
    Button
  },
  props: {
    logo: Boolean,
    button: Boolean,
    buttonEvent: Function
  }
};
</script>

<style scoped>
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 20px 0;
}
.header-links {
  display: flex;
  align-items: center;
}
img {
  vertical-align: middle;
  margin-left: 8px;
}
a {
  text-decoration: none;
  margin: 20px;
  color: black;
}
</style>
