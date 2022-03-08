<template>
  <div>
    <button @click="exec('left')" class="button" type="button">Налево</button>
    <button @click="exec('move')" class="button" type="button">Вперёд</button>
    <button @click="exec('right')" class="button" type="button">Направо</button>
    <h3 v-if="loading">Команда выполняется...</h3>
    <h3 v-if="result" class="success">{{ result }}</h3>
    <h3 v-if="error" class="error">{{ error }}</h3>
  </div>
</template>

<script>
export default {
  name: "RoverControl",
  data() {
    return {
      loading: false,
      result: "",
      error: "",
    };
  },
  methods: {
    async exec(command) {
      this.result = "";
      this.error = "";
      this.loading = true;

      const response = await fetch(`/${command}`);
      const json = await response.json();
      if (response.ok) {
        this.result = json.result;
      } else {
        this.error = json.error;
      }
      this.loading = false;
    },
  },
};
</script>

<style scoped>
.button {
  margin: 0 8px;
  padding: 12px 6px;
  background-color: cornflowerblue;
  color: white;
}
.success {
  color: mediumseagreen;
}
.error {
  color: firebrick;
}
</style>
