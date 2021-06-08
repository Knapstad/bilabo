<template>
  <section class="home">
  <a href="#content" class="skip">Hopp over filter</a>
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
    <div v-else >
      <Filters :data="cars" :flat="locations"/>
      <main id="content" class="carcontainer">
        <article class="car" v-for="(car, index) in flatCars.sort(this.compare)" :key="index">
          <Car class :car="car" />
        </article>
      </main>
    </div>
    <Footer />
  </section>
</template>

<script>
import Car from "@/components/Car.vue";
import Filters from "@/components/Filters.vue";
import Footer from "@/components/Footer.vue";
import axios from "axios";


export default {
  name: "Home",
  components: {
    Car,
    Filters,
    Footer,
  },
  data() {
    return {
      cars: null,
      loading: true,
    };
  },
  metaInfo: {
    title: "Bilabonnement samlet på en side | Bilabonnement.app",
    meta: [
      { charset: "utf-8" },
      {
        name: "description",
        content:
          "En oversikt over flere bilabonnement leverandører på en side. Vi gjør det enkelt å finne det billigste bilabonnementet",
      },
      {
        name: "viewport",
        content: "width=device-width, initial-scale=1, min-scale=1",
      },
      { name: "twitter:card", content: "summary" },
      {
        name: "twitter:title",
        content: 'Bilabonnement.app | Bilabonnement samlet på en side"',
      },
      {
        name: "twitter:description",
        content:
          "En samling og oversikt over flere bilabonnement på en side. Gjør det enkelt å finne den billigste bilen",
      },
      // image must be an absolute path
      {
        name: "twitter:image",
        content:
          "https://res.cloudinary.com/db0kzjtgs/image/upload/v1598880211/site_drfi7i.jpg",
      },
      // Facebook OpenGraph
      {
        property: "og:title",
        content: 'Bilabonnement.app | Bilabonnement samlet på en side"',
      },
      { property: "og:site_name", content: 'Bilabonnement.app x"' },
      { property: "og:type", content: "website" },
      {
        property: "og:image",
        content:
          "https://res.cloudinary.com/db0kzjtgs/image/upload/v1598880211/site_drfi7i.jpg",
      },
      {
        property: "og:description",
        content:
          "En samling og oversikt over flere bilabonnement på en side. Gjør det enkelt å finne den billigste bilen",
      },
    ],
  },
  methods: {
    compare: function (a, b) {
      const carA = parseInt(a.price);
      const carB = parseInt(b.price);
      if (carA < carB) {
        return -1;
      }
      if (carA > carB) {
        return 1;
      }
      return 0;
    },
  },
  computed: {
    flatCars: function () {
      let cars = this.locations;
      let locs = this.$store.state.locations;
      let makes = this.$store.state.makes;
      if (locs.length > 0) {
        cars = cars.filter((car) =>
          car.location.some((location) => locs.includes(location))
        );
      }
      if (makes.length > 0) {
        cars = cars.filter((car) => makes.includes(car.make));
      }
      return cars;
    },
    locations: function () {
      let cars = Object.values(this.cars["data"]).flat();
      let locs = this.$store.state.locations;
      if (locs.length > 0) {
        cars = cars.filter((car) =>
          car.location.some((location) => locs.includes(location))
        );
      }
      return cars;
    },
  },

  mounted() {
    axios
      .get("https://europe-west1-bilabo.cloudfunctions.net/give_car")
      .then((response) => (this.cars = response))
      .finally(
        () => (
          (this.loading = false),
          window.dataLayer.push({
            event: "loadingDone",
          })
        )
      );
  },
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
  display: flex;
  flex-direction: column;
  height: 100%;
}

.skip {
        position: absolute;
        top: -1000px;
        left: -1000px;
        height: 1px;
        width: 1px;
        text-align: left;
        overflow: hidden;
    }
    
    a.skip:active, 
    a.skip:focus, 
    a.skip:hover {
      left: 0; 
        top: 0;
        width: auto; 
        height: auto; 
        overflow: visible; 
        color: white;
        font-size: 2em;
    }
@media only screen and (max-width: 2400px) {
  .carcontainer {
    grid-template-columns: 30% 30% 30%;
  }
}
@media only screen and (max-width: 900px) {
  .carcontainer {
    grid-template-columns: 49% 49%;
    padding: 0;
  }
}

.loading {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin: auto;
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
