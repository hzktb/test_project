<template>
  <div class="wrapper">
    <Counter
      v-for="(item, index) in counters"
      :key="index"
      v-bind:item="item.value"
      :index="index"
    />
  </div>
</template>

<script>
import axios from "axios";
import Counter from "./components/Counter";
export default {
  name: "App",
  components: {
    Counter,
  },
  data() {
    return {
      counters: [],
    };
  },
  mounted: function() {
    axios
      .get("http://127.0.0.1:5000/api/hello")
      .then((res) => (this.counters = res.data))
      .catch((err) => console.log(err));
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.wrapper {
  margin: 0 auto;
  width: 500px;
  display: flex;
  flex-wrap: wrap;
}
</style>
