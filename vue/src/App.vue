<template>
  <div id="app">
    <AceContainer />
  </div>
</template>

<script>
import AceContainer from './components/AceContainer.vue';

export default {
  name: 'app',
  components: {
    AceContainer,
  },
};
</script>

<style>
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */

body {
    background: #E5E4DF;
    color: #000305;
    font-size: 87.5%; /* Base font size: 14px */
    font-family: 'Trebuchet MS', Trebuchet, 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    line-height: 1.429;
    margin: 0;
    padding: 0;
    text-align: left;
}



</style>
