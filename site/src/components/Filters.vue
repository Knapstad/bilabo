<template>
  <div class="filter-wrap">
    <div class="label">Sted:</div>
    <div v-for="item in locations()" :key="item">
      <FilterItem :item="item" />
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
  },
};
</script>

<style scoped>
.filter-wrap {
  display: flex;
  justify-content: center;
  padding-top: 50px;
}
.label {
  margin-top: auto;
  margin-bottom: auto;
}
</style>