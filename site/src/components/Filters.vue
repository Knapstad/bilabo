<template>
  <div class="filter-wrap">
    <div class="label">Sted:</div>
    <div class="filter-section">
      <div v-for="item in locations()" :key="item">
        <FilterItem :item="item" :type="'locations'" />
      </div>
    </div>
    <div class="label">Merke:</div>
    <div class="filter-section">
      <div v-for="item in makes()" :key="item">
        <FilterItem :item="item" :type="'makes'" />
      </div>
    </div>
  </div>
</template>

<script>
import FilterItem from "@/components/FilterItem.vue";
// console.log(item);

export default {
  name: "Filters",
  components: {
    FilterItem,
  },
  props: ["data"],
  data() {
    return {
      items: ["Oslo", "Bergen", "Stavanger"],
    };
  },
  methods: {
    locations: function () {
      let cars = Object.values(this.data["data"]).flat();
      cars = cars
        .map((a) => a.location)
        .flat()
        .filter((v, i, a) => a.indexOf(v) === i);
      return cars;
    },
    makes: function () {
      let cars = Object.values(this.data["data"]).flat();
      cars = cars
        .map((a) => a.make)
        .flat()
        .filter((v, i, a) => a.indexOf(v) === i);
      return cars;
    },
  },
};
</script>

<style scoped>
.filter-wrap {
  margin: auto;
  display: flex;
  padding: 1rem;
  width: fit-content;
  background: var(--main-medium-light);
  color: white;
  margin-top: 1rem;
  box-shadow: 2px 2px 3px #000;
  border-radius: 2px;
}
.filter-section {
  display: grid;
  grid-template-rows: repeat(3, 2.2rem);
  grid-auto-flow: column;
}
.label {
  margin-left: 1rem;
}
</style>