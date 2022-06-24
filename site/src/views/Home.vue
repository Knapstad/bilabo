<template>
  <section class="home">
  <a href="#content" class="skip">Hopp over filter</a>
    <div v-if="loading" class="loading">
      <div class="loading__letter">L</div>
      <div class="loading__letter">a</div>
      <div class="loading__letter">s</div>
      <div class="loading__letter">t</div>
      <div class="loading__letter">e</div>
      <div class="loading__letter">r</div>
      <div class="loading__letter">.</div>
      <div class="loading__letter">.</div>
      <div class="loading__letter">.</div>
    </div>
    <div v-else >
      <Filters :data="cars" :flat="locations"/>
      
      <main id="content" class="carcontainer">
        <section class="results"><h2>Vi fant {{Object.values(flatCars).flat().length}} {{(flatCars.length > 1) ? "biler" : "bil"}} du kan abonnere på </h2></section>
        <article class="car" v-for="(car, index) in flatCars.sort(this.compare)" :key="index">
          <Car class :car="car" :id="index" />
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
      cars: this.$store.state.cars,
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
          "En oversikt over flere bilabonnementleverandører på en side. Vi gjør det enkelt å finne det billigste bilabonnementet",
      },
      {
        name: "viewport",
        content: "width=device-width, initial-scale=1",
      },
      { name: "twitter:card", content: "summary" },
      {
        name: "twitter:title",
        content: "Bilabonnement.app | Bilabonnement samlet på en side",
      },
      {
        name: "twitter:description",
        content:
          "En samling og oversikt over flere bilabonnement på en side. Gjør det enkelt å finne den billigste bilen",
      },
      {
        name: "twitter:image",
        content:
          "https://res.cloudinary.com/bilabonnement/image/upload/v1655797402/site_drvyh2.png",
      },
      // Facebook OpenGraph
      {
        property: "og:title",
        content: "Bilabonnement.app | Bilabonnement samlet på en side",
      },
      {
        property: "og:url",
        content: 'https://bilabonnemet.app',
      },
      { property: "og:site_name", content: "Bilabonnement.app" },
      { property: "og:type", content: "website" },
      {
        property: "og:image",
        content:
          "https://res.cloudinary.com/bilabonnement/image/upload/c_scale,w_500/v1655797402/site_drvyh2.png",
      },
      {
        property: "og:image:secure_url",
        content:
          "https://res.cloudinary.com/bilabonnement/image/upload/c_scale,w_500/v1655797402/site_drvyh2.png",
      },
      {
        property: "og:description",
        content:
          "En samling og oversikt over flere bilabonnement på en side. Gjør det enkelt å finne den billigste bilen",
      },
      {property: "fb:app_id", content: "381160890208041"},
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
      let sites = this.$store.state.sites;
      let drive = this.$store.state.drive;
      if (locs.length > 0) {
        cars = cars.filter((car) =>
          car.location.some((location) => locs.includes(location))
        );
      }
      if (makes.length > 0) {
        cars = cars.filter((car) => makes.includes(car.make.trim().toLowerCase()));
      }
      if (sites.length > 0) {
        cars = cars.filter((car) => sites.includes(car.site));
      }
      if (drive.length > 0) {
        cars = cars.filter((car) => drive.includes(car.drive.trim().toLowerCase()));
      }
      return cars;
    },
    locations: function () {
      let cars = Object.values(this.$store.state.cars["data"]).flat();
      cars = cars.filter((car) => car.location.length > 0);
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
    if(this.cars=="undefined" || this.cars==null)
    {axios
      .get("https://europe-west1-bilabo.cloudfunctions.net/give_car")
      .then((response) => (this.$store.commit("addData", ["cars", response])),
            )
      .finally(
        () => (
          (this.loading = false),
          (this.cars = this.$store.state.cars),
          (window.sessionStorage.setItem("cars",JSON.stringify(this.$store.state.cars))),
          window.dataLayer = window.dataLayer || [],
          window.dataLayer.push({
            event: "loadingDone",
          })
        )
      );}
      else{this.loading = false,
      window.dataLayer.push({
            event: "loadingDone",
          })
      }
  },
};
</script>
<style>
h2{
font-size: 25px;
margin-bottom: 5px;
}
.carcontainer {
  justify-content: center;
  display: inline-grid;
  grid-template-columns: 23% 23% 23% 23%;
  padding-top: 30px;
  padding-bottom: 30px;
  width: 100%;
}
.results{
  padding-left: 6px;
  font-size: 1.3rem;
  grid-column: 1 / -1;
  }
.car {
  background: #fff;
  box-shadow: 2px 2px 3px #000;
  border-radius: 12px;
  margin: 5px;
  position: relative;
  overflow: hidden;
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
  animation-delay: 0.3s;
}
.loading__letter:nth-child(3) {
  animation-delay: 0.6s;
}
.loading__letter:nth-child(4) {
  animation-delay: 0.9s;
}
.loading__letter:nth-child(5) {
  animation-delay: 1.2s;
}
.loading__letter:nth-child(6) {
  animation-delay: 1.8s;
}
.loading__letter:nth-child(7) {
  animation-delay: 2.1s;
}
.loading__letter:nth-child(8) {
  animation-delay: 2.4s;
}
.loading__letter:nth-child(9) {
  animation-delay: 2.7s;
}
.loading__letter:nth-child(10) {
  animation-delay: 3s;
}

@keyframes bounce {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-40px) scale(1.3);
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
