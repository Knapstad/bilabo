<template>
  <div class="filter" :class="{active: isActive}" @click="active">{{item}}</div>
</template>

<script>
export default {
  name: "FilterItem",
  props: ["item"],
  data() {
    return {
      isActive: false
    };
  },
  methods: {
    active: function() {
      if (this.isActive) {
        this.$store.commit("removeLocation", this.item);
      }
      if (!this.isActive) {
        this.$store.commit("addLocation", this.item);
      }
      this.isActive = !this.isActive;
    }
  }
};
</script>

<style scoped>
.filter-wrap {
  display: flex;
}
.filter {
  border-radius: 2px;
  background: var(--main-medium-dark);
  color: white;
  padding: 5px;
  margin: 5px;
  box-shadow: 2px 2px 3px #000;
}
.active {
  background: var(--main-medium-light);
  color: black;
  padding: 5px;
  margin: 5px;
  box-shadow: inset 2px 2px 3px #000;
}
</style>