<template>
  <div class="counter">
    <div class="box"></div>
    <button @click="increment">+1</button>
    <button @click="decrement">-1</button>
    <span class="score">Score: {{ count }}</span>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    item: Number,
    index: Number,
  },
  data() {
    return {
      count: this.item,
    };
  },
  methods: {
    increment() {
      // console.log(this.count);
      this.count++;
      axios
        .put("http://127.0.0.1:5000/api/hello/inc/" + (this.index + 1))
        .then((res) => console.log(res))
        .catch((err) => console.log(err));
    },
    decrement() {
      // console.log(this.count);
      this.count--;
      axios
        .put("http://127.0.0.1:5000/api/hello/dec/" + (this.index + 1))
        .then(console.log(this.index + 1))
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style>
.counter {
  margin: 10px;
}

.box {
  width: 200px;
  height: 200px;
  background-color: coral;
}

.score {
  display: inline-block;
  margin: 3px 0 0 40px;
}

button {
  margin: 3px 5px;
  padding: 3px 10px;
  color: #fff;
  background-color: cornflowerblue;
  border-radius: 10px;
}
</style>
