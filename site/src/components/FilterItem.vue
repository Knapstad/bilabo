<template>
  <div class="filter" :class="{active: isActive}" @click="active">{{item}}</div>
</template>

<script>
export default {
  name: "FilterItem",
  props: ["item", "type"],
  data() {
    return {
      isActive: false,
    };
  },
  methods: {
    active: function () {
      if (this.isActive) {
        console.log(this.item);
        this.$store.commit("removeFilter", [this.type, this.item]);
      }
      if (!this.isActive) {
        console.log(this.item);
        console.log(this.type);
        this.$store.commit("addFilter", [this.type, this.item]);
      }
      this.isActive = !this.isActive;
    },
  },
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
  cursor: pointer;
}
.active {
  background: var(--main-medium-light);
  box-shadow: inset 2px 2px 3px #000;
}
.filter:hover {
  background: var(--main-medium-light);
}
@media only screen and (max-width: 900px) {
  .filter {
    font-size: 12px;
    padding: 1px;
    margin: 4px;
    text-align: center;
  }
}
</style>