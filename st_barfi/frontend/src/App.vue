<!-- 
  We bootstrap our Component to Streamlit with our scoped slot in the top-level App.
  This is where scoped slot passes Streamlit ;`args` data from itself to children MyComponent.
  You should not have to edit this, but are free to do so :)
-->
<template>
  <div id="app">
    <WithStreamlitConnection v-slot="{ args }">
      <block-editor :args="args" />
    </WithStreamlitConnection>
  </div>
</template>

<script>
// "withStreamlitConnection" is a scoped slot. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
import WithStreamlitConnection from "./streamlit/WithStreamlitConnection.vue";
import BlockEditor from "./components/BlockEditor.vue";

export default {
  name: "App",
  components: {
    WithStreamlitConnection,
    BlockEditor,
  },
};
</script>

<style>
body {
  margin: 0;
  height: 85vw;
  width: 100vw;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
