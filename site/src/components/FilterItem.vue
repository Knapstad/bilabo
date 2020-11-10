<template>
  <button role="button" class="filter" :class="{active: isActive}" @click="active">{{item}}</button>
</template>

<script>
export default {
  name: "FilterItem",
  props: ["item", "type"],
  data() {
    return {
      isActive: this.$store.state[this.type].includes(this.item),
    };
  },
  methods: {
    active: function () {
      if (this.isActive) {
        this.$store.commit("removeFilter", [this.type, this.item]);
      }
      if (!this.isActive) {
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
  padding: .4rem;
  margin: .2rem;
  box-shadow: 2px 2px 3px #000;
  /* cursor: pointer; */
  border: none;
  width: 90%;
  font-size: 1rem;
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
    padding: .4rem;
    margin: 4px;
    text-align: center;
  }
}
/* @media only screen and (max-width: 600px) {
  .filter {
    font-size: 12px;
    padding: .2rem;
    margin: 4px;
    text-align: center;
  }
} */
</style>