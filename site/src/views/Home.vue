<template>
  <div class="home">
    <div class="carcontainer">
      <div v-if="loading">Loading...</div>
      <div v-else class="car" v-for="(car, index) in flatCars.sort(this.compare)" :key="index">
        <Car class :car="car" />
      </div>
    </div>
  </div>
</template>

<script>
import Car from "@/components/Car.vue";
// import cars from '../../../cloudFuctions/mycars.json';
import axios from "axios";

export default {
  name: "Home",
  components: {
    Car
  },
  data() {
    return {
      cars: null,
      loading: true
    };
  },
  metaInfo: {
    title: "Bilabonnement.app | Bilabonnement samlet på en side",
    meta: [
      { charset: "utf-8" },
      {
        name: "description",
        content:
          "En samling og oversikt over flere bilabonnement på en side. Gjør det enkelt å finne den billigste"
      },
      {
        name: "viewport",
        content: "width=device-width, initial-scale=1, min-scale=1"
      }
    ]
  },
  methods: {
    compare: function(a, b) {
      const carA = parseInt(a.price);
      const carB = parseInt(b.price);
      if (carA < carB) {
        return -1;
      }
      if (carA > carB) {
        return 1;
      }
      return 0;
    }
  },
  computed: {
    flatCars: function() {
      return Object.values(this.cars["data"]).flat();
    }
  },
  mounted() {
    axios
      .get("https://europe-west1-bilabo.cloudfunctions.net/give_car")
      .then(response => (this.cars = response))
      .finally(() => (this.loading = false));
  }
};
</script>
<style>
.carcontainer {
  justify-content: center;
  display: inline-grid;
  grid-template-columns: 23% 23% 23% 23%;
  padding: 30px;
}
.car {
  background: white;
  box-shadow: 2px 2px 3px #000;
  border-radius: 2px;
  margin: 5px;
  position: relative;
}
@media only screen and (max-width: 2400px) {
  .carcontainer {
    grid-template-columns: 30% 30% 30%;
  }
}
@media only screen and (max-width: 900px) {
  .carcontainer {
    grid-template-columns: 45% 45%;
  }
}
@media only screen and (max-width: 600px) {
  .carcontainer {
    grid-template-columns: 90%;
  }
}
</style>
