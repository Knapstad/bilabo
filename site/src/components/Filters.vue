<template>
  <div class="filter-wrap">
    Sted:
    <div v-for="item in items" :key="item">
      <FilterItem :item="item" />
    </div>
  </div>
</template>

<script>
import FilterItem from "@/components/FilterItem.vue";

export default {
  name: "Filters",
  components: {
    FilterItem
  },
  data() {
    return {
      items: ["Oslo", "Bergen", "Stavanger"]
    };
  }
};
</script>

<style scoped>
.filter-wrap {
  display: flex;
  justify-content: center;
}
</style>