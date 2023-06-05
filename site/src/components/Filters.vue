<template>
  <div class="filter-accordian">
    <p>Filter</p>
    <details class="filter-group">
      <summary class="label">Sted</summary>
      <div class="filter-section">
        <div v-for="item in locations()" :key="item">
          <FilterItem :item="item" :type="'locations'" />
        </div>
      </div>
    </details>
    <details class="filter-group">
      <summary class="label">Merke</summary>
      <div class="filter-section">
        <div v-for="item in makes().sort()" :key="item">
          <FilterItem :item="item" :type="'makes'" />
        </div>
      </div>
    </details>
    <details class="filter-group">
      <summary class="label">Type</summary>
      <div class="filter-section">
        <div v-for="item in drive()" :key="item">
          <FilterItem :item="item" :type="'drive'" />
        </div>
      </div>
    </details>
    <details class="filter-group">
      <summary class="label">Leverandør</summary>
      <div class="filter-section">
        <div v-for="item in sites()" :key="item">
          <FilterItem :item="item" :type="'sites'" />
        </div>
      </div>
    </details>

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
  props: ["data", "flat"],
  data() {
    return {
    };
  },
  created() {
    let qp = new URLSearchParams(window.location.search);
    for (let i of qp.keys()) {
      let filters = qp.get(i).split(",")
      filters.forEach(filter =>
        this.$store.commit("addFilter", [i, filter.toLowerCase()]))
    }
  },
  methods: {
    locations: function () {
      let cars = Object.values(this.data["data"]).flat();
      cars = cars
        .map((a) => a.location)
        .flat()
        .map((a) => a.toLowerCase())
        .filter((v, i, a) => a.indexOf(v) === i);
      return cars;
    },
    makes: function () {
      let cars = Object.values(this.flat).flat();
      cars = cars
        .map((a) => a.make.toLowerCase().trim())
        .flat()
        .map((a) => a.replace("citröen", "citroën"))
        .filter((v, i, a) => a.indexOf(v) === i);
      return cars;
    },
    sites: function () {
      let cars = Object.values(this.flat).flat();
      cars = cars
        .map((a) => a.site.toLowerCase().trim())
        .flat()
        .filter((v, i, a) => a.indexOf(v) === i);
      return cars;
    },
    drive: function () {
      let cars = Object.values(this.flat).flat();
      cars = cars
        .map((a) => a.drive.toLowerCase().trim().replace("Electric", "Elektrisk").replace("PHV", "Hybrid") || "Hydrogen")
        .flat()
        .filter((v, i, a) => a.indexOf(v) === i);
      return cars;
    },
  },
};
</script>

<style scoped>
p {
  margin-block-start: 0;
  margin-block-end: 5px;
  font-size: x-large;
}

summary {
  align-self: flex-start;
}

summary.label {
  font-size: x-large;
}

.filter-wrap {
  display: flex;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.filter-accordian {
  margin: auto;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  width: fit-content;
  min-width: 86%;
  background: var(--main-medium-light);
  color: whitesmoke;
  margin-top: 1rem;
  box-shadow: 2px 2px 3px #000;
  border-radius: 2px;
}

.filter-group {
  display: flex;
  flex-direction: column;
  margin-right: 3px;

  padding-bottom: 5px;
  padding-right: 5px;
}

.filter-section {
  display: grid;
  grid-template-rows: repeat(3, 2.2rem);
  grid-auto-flow: column;
}

.label {
  background: var(--main-dark);
  padding-left: 5px;
  border-radius: 2px 2px 1px 1px;
  width: 100%;
  overflow: hidden;
}

@media only screen and (max-width: 900px) {
  .filter-section {
    grid-template-rows: repeat(3, 2rem);

  }

  .filter-wrap {
    width: 100%;
    margin: 0;
    padding: 0;
    padding-bottom: .5rem;
    flex-wrap: wrap;
  }
}

@media only screen and (max-width: 700px) {
  .filter-section {
    grid-template-rows: repeat(4, 2rem);
  }

  .filter-wrap {
    width: 90%;
    margin: 0;
    padding: 0;
    padding-bottom: .5rem;
    flex-wrap: wrap;
  }

  .filter-accordian {
    min-width: 86%;
    /* margin: 0; */
    /* padding: 0; */
    margin-block-end: 5px;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
  }
}

@media only screen and (max-width: 600px) {
  .filter-section {
    grid-template-rows: repeat(5, 2rem);
  }

  .filter-wrap {
    width: 90%;
    margin: 0;
    padding: 0;
    padding-bottom: .5rem;
    flex-wrap: wrap;
  }
}

@media only screen and (max-width: 500px) {
  .filter-section {
    grid-template-rows: repeat(7, 2rem);
  }

  .filter-wrap {
    width: 100%;
    margin: 0;
    padding: 0;
    padding-bottom: .5rem;
    flex-wrap: wrap;
  }
}

@media only screen and (max-width: 360px) {
  .filter-section {
    grid-template-rows: repeat(10, 1.5rem);
    /* grid-auto-flow: columns; */
  }

  .filter-wrap {
    width: 100%;
    margin: 0;
    padding: 0;
    flex-wrap: wrap;
  }
}
</style>