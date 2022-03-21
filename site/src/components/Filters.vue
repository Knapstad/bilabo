<template>
<div class="filter-accordian">
    <details open>
    <summary>Filter</summary>
    <div class="filter-wrap">
        <div class="filter-group">
          <div class="label">Sted</div>
          <div class="filter-section">
            <div v-for="item in locations()" :key="item">
              <FilterItem :item="item" :type="'locations'" />
            </div>
          </div>
        </div>
        <div class="filter-group">
          <div class="label">Merke</div>
          <div class="filter-section">
            <div v-for="item in makes().sort()" :key="item">
              <FilterItem :item="item" :type="'makes'" />
            </div>
          </div>
        </div>
        <div class="filter-group">
          <div class="label">Type</div>
          <div class="filter-section">
            <div v-for="item in drive()" :key="item">
              <FilterItem :item="item" :type="'drive'" />
            </div>
          </div>
        </div>
        <div class="filter-group">
          <div class="label">Leverandør</div>
          <div class="filter-section">
            <div v-for="item in sites()" :key="item">
              <FilterItem :item="item" :type="'sites'" />
            </div>
          </div>
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
  created(){
    let qp = new URLSearchParams(window.location.search);
    for(let i of qp.keys()){
      let filters=qp.get(i).split(",")
      filters.forEach(filter =>  
        this.$store.commit("addFilter",[i,filter.toLowerCase()]))
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
        .map((a) => a.drive.toLowerCase().trim()||"Hydrogen")
        .flat()
        .filter((v, i, a) => a.indexOf(v) === i);
      return cars;
    },
  },
};
</script>

<style scoped>
summary {
  align-self: flex-start;
}
.filter-wrap {
  display: flex;
  margin-top: 1rem;
}
.filter-accordian {
  margin: auto;
  display: flex;
  padding: 1rem;
  width: fit-content;
  min-width: 40%;
  background: var(--main-medium-light);
  color: white;
  margin-top: 1rem;
  box-shadow: 2px 2px 3px #000;
  border-radius: 2px;
  
}
.filter-group{
  display: flex;
  flex-direction: column;
  margin-right: 3px;
  box-shadow: 1px 2px 3px #000;
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
  overflow: hidden;}
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
    width: 100%;
    margin: 0;
    padding: 0;
    padding-bottom: .5rem;
    flex-wrap: wrap;
  }
  .filter-accordian {
    width: 100%;
    margin: 0;
    padding: 0;
    margin-block-end: 5px;
    }
}

@media only screen and (max-width: 600px) {
  .filter-section {
    grid-template-rows: repeat(5, 2rem);
  }
  .filter-wrap {
    width: 100%;
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