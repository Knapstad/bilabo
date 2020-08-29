<template>
  <div class="home">
    <Filters />
    <div class="carcontainer">
      <div v-if="loading" class="loading">
        <div class="loading__letter">L</div>
        <div class="loading__letter">o</div>
        <div class="loading__letter">a</div>
        <div class="loading__letter">d</div>
        <div class="loading__letter">i</div>
        <div class="loading__letter">n</div>
        <div class="loading__letter">g</div>
        <div class="loading__letter">.</div>
        <div class="loading__letter">.</div>
        <div class="loading__letter">.</div>
      </div>
      <div v-else class="car" v-for="(car, index) in flatCars.sort(this.compare)" :key="index">
        <Car class :car="car" />
      </div>
    </div>
  </div>
</template>

<script>
import Car from "@/components/Car.vue";
import Filters from "@/components/Filters.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    Car,
    Filters
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
      let cars = Object.values(this.cars["data"]).flat();
      let locs = this.$store.state.locations;
      if (locs.length == 0) {
        return cars;
      }
      const result = cars.filter(car =>
        car.location.some(location => locs.includes(location))
      );
      return result;
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
  width: 100%;
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

.loading {
  display: flex;
  flex-direction: row;
  margin: auto;
  grid-column: 2;
  margin-top: 30px;
}
.loading__letter {
  font-size: 88px;
  font-weight: normal;
  letter-spacing: 4px;
  animation-name: bounce;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}

.loading__letter:nth-child(2) {
  animation-delay: 0.1s;
}
.loading__letter:nth-child(3) {
  animation-delay: 0.2s;
}
.loading__letter:nth-child(4) {
  animation-delay: 0.3s;
}
.loading__letter:nth-child(5) {
  animation-delay: 0.4s;
}
.loading__letter:nth-child(6) {
  animation-delay: 0.5s;
}
.loading__letter:nth-child(7) {
  animation-delay: 0.6s;
}
.loading__letter:nth-child(8) {
  animation-delay: 0.8s;
}
.loading__letter:nth-child(9) {
  animation-delay: 1s;
}
.loading__letter:nth-child(10) {
  animation-delay: 1.2s;
}

@keyframes bounce {
  0% {
    transform: translateY(0px);
  }
  40% {
    transform: translateY(-40px);
  }
  80%,
  100% {
    transform: translateY(0px);
  }
}

@media (max-width: 700px) {
  .loading__letter {
    font-size: 50px;
  }
}

@media (max-width: 340px) {
  .loading__letter {
    font-size: 40px;
  }
}
</style>
