<template>
  <div>
    <BreadCrumb :key="$route.path"></BreadCrumb>
    <main>
      <div v-if="loading" class="loading">
        <div class="loading__letter">H</div>
        <div class="loading__letter">e</div>
        <div class="loading__letter">n</div>
        <div class="loading__letter">t</div>
        <div class="loading__letter">e</div>
        <div class="loading__letter">r</div>
        <div class="loading__letter">-</div>
        <div class="loading__letter">b</div>
        <div class="loading__letter">i</div>
        <div class="loading__letter">l</div>
        <div class="loading__letter">.</div>
        <div class="loading__letter">.</div>
        <div class="loading__letter">.</div>
      </div>

      <div v-if="this.idmatch && car" class="bloggcontent">

        <div class="header">

          <img v-if="car && car.img" class="headerimage" :src="headerImageTransformation" :alt="car.name">
          <img class="logo" :src="logo" :alt='"logo for " + car.site'>
        </div>
        <h2>Abonner på {{ car.name }} fra {{ $capitalize(car.site == "volvo" ? "Care by Volvo" : car.site) }}</h2>
        <p>Fra {{ $capitalize(car.site == "volvo" ? "Care by Volvo" : car.site) }} kan du abonnere på denne bilen fra
          {{ car.make }} for {{ car.price }} kroner i måneden. Da er forsikring, service og dekkbytte inkludert og du
          kan i
          tillegg kjøre {{ car.kmMonth }} kilometer i måneden.<span v-if="car.site == 'imove'"> Imove tilbyr i tilegg
            hyttebil i 10 dager slik at du kan kjøre en liten bybil tilvanlig og bytte til en større bil om du skal på
            litt lengre tur.</span></p>
        <p v-if="car.description">{{ car.description }}</p>

        <p v-if="car.extra && car.extra.length > 0">Akuratt denne bilen er utstyrt med følgende utstyr:
        <ul v-for="(item, index) in car.extra" :key="index">
          <li>{{ item }}</li>
        </ul>
        </p>
        <details v-for="(item, index) in car.details" :key="index">
          <summary>{{ index }}</summary>
          {{ item }}
        </details>


        <div v-if="car.site == 'volvo'" class="">
          <p>Her kan du abonnere på en flott bil i fargen {{ car.color }} fra Volvo.
            <span v-if="car.cargoVolume"> Bilen er utstyrt med {{ car.cargoVolume }} bagasjerom. </span>
            <span v-if="car.co2">Den har et lavt utslipp på ca {{ car.co2 }}. </span>
            <span v-if="car.fuelconsumption">Forbruket ligger på rundt {{ car.fuelconsumption }}. </span>
            <span v-if="car.engine">Bilen er utstyrt med en {{ car.engine }} motor.</span>

            <span v-if="car.towbar">Bilen er også utstyrt med hengerfeste. </span>
            <span v-if="car.delivery">Det er omtrent {{ car.delivery }} leveringstid på bilen.</span>
            <span v-if="car.towbar">Bilen er i tillegg utstyrt med hengerfeste</span>


          </p>
          <section>
            <a :href="url" target="_blank" rel="noopner nofollow">Bestill denne bilen hos {{
              $capitalize(car.site == "volvo"
                ? "Care by Volvo" : car.site)
            }}</a>
          </section>
          <section v-for="(category, index) in car.categories" :key="index">
            <h3>{{ category.displayName }}</h3>
            <p>{{ category.description }}</p>
            <div v-for="(sub, index) in category.subCategories" :key="index">
              <h4>{{ sub.displayName }}</h4>
              <p>{{ sub.description }}</p>
              <div v-for="(item, key) in sub.items" :key="key">
                <details>
                  <summary>{{ item.displayName }}</summary>
                  {{ item.description }}
                </details>
              </div>
            </div>
          </section>
        </div>


        <div v-for="(item, index) in car.content" :key="index">
          <h3>{{ item.title }}</h3>
          <p>{{ item.byline }}</p>
        </div>
        <section>
          <a :href="url" target="_blank" rel="noopner nofollow">Bestill denne bilen hos {{
            $capitalize(car.site == "volvo" ?
              "Care by Volvo" : car.site)
          }}</a>
        </section>
        <section class="table">
          <table>
            <tr v-for="(item, key, index) in     car    " :key="index">
              <td
                v-if="item && !['details', 'id', 'img', 'order', 'site', 'description', 'carid', 'content', 'extra', 'from', 'to'].includes(key)">
                {{
                  $capitalize(key) }}:</td>
              <td
                v-if="item && !['details', 'id', 'img', 'order', 'site', 'description', 'carid', 'content', 'extra', 'from', 'to'].includes(key)">
                {{
                  $capitalize(item) }}</td>
            </tr>
          </table>

        </section>

      </div>

      <div v-if="!car" class="nocar">
        <div class="bloggcontent nocar">
          <p>Beklager, vi finner ikke denne bilen.</p>
          <img src="/img/logo.990de79b.png">
          <p>

            <router-link class="button" to="/">Gå tilbake til forsiden</router-link>
          </p>
          <p>Eller ta en titt på disse bilene fra {{ $capitalize(this.$route.params.site) }} eller
            {{ this.$route.params.carname.split("-")[0] }}:</p>
        </div>


      </div>
      <section class="">
        <h3 v-if="car && similarCars.length >= 1" class="bloggcontent">Det er for øyeblikket {{ similarCars.length }} {{
          (similarCars.length
            >
            1) ? "tilgengelige biler" : "tilgengelig bil" }} fra {{ $capitalize(this.$route.params.site) }} og
          {{ $capitalize(this.$route.params.carname.split("-")[0]) }}</h3>
        <div class="carcontainer">
          <article class="car" v-for="(    car, index    ) in     similarCars.sort(this.compare)    " :key="index">
            <Car class :car="car" :id="index" />
          </article>
        </div>
      </section>
    </main>
    <Footer />
  </div>
</template>
<script>
import BreadCrumb from '../components/BreadCrumb.vue'
import Footer from '../components/Footer.vue'
import Car from '../components/Car.vue'
import axios from "axios";

export default {
  name: 'CarDetails',
  components: {
    Footer,
    Car,
    BreadCrumb
  },

  data() {
    return {
      cars: this.$store.state?.cars,
      urlname: this.$route.path.split("/")[2],
      loading: true
    }
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
    get_cars: function () {
      if (this.cars == "undefined" || this.cars == null) {
        axios
          .get(" https://data.bilabonnement.app/cars")
          .then((response) => (this.$store.commit("addData", ["cars", response])),
          )
          .finally(
            () => (
              (this.loading = false),
              (this.cars = this.$store.state.cars),
              (this.$track("loadingDone"))
              // (window.sessionStorage.setItem("cars",JSON.stringify(this.$store.state.cars))),
              // window.dataLayer=window.dataLayer||[],
              // window.dataLayer.push({
              //   event: 'loadingDone',
              // })
            )
          );
      }
      else {
        this.loading = false
        this.$track("loadingDone")
        // window.dataLayer=window.dataLayer||[],
        // window.dataLayer.push({
        //   event: 'loadingDone',
        // })
      }
    },
    addJsonld: function () {
      try {
        var Jsoninterval = setInterval(() => {
          if (this.loading === false) {
            if (!document.querySelector("#articledata")) {
              // console.log("article script not found")
              var jsonldScript = document.createElement("script")
              // console.log("article script created")
              jsonldScript.setAttribute("type", "application/ld+json")
              // console.log("set type")
              jsonldScript.setAttribute("id", "articledata")
              // console.log("set id")

            } else {
              jsonldScript = document.querySelector("#articledata")
              if (jsonldScript.innerText === JSON.stringify(this.jsonld)) {
                clearInterval(Jsoninterval)
                return;
              }
            }
            jsonldScript.textContent = JSON.stringify(this.jsonld);
            // console.log("setting data")
            document.head.appendChild(jsonldScript)
            // console.log("appending script")
            clearInterval(Jsoninterval)
          }
        }
          , 1000);
      } catch {
        console.log("error addjsonld")
      }

    }
  },
  computed: {
    url() {
      try {
        if (this.car.site == "volvo") {
          return (
            this.car.order
          );
        } else if (this.car.order.includes('?')) {
          return (
            this.car.order +
            '&utm_source=bilabonnemet.app&utm_medium=link&utm_campaign=bilabonnement.app'
          );

        } else {
          return this.car.order +
            '?utm_source=bilabonnemet.app&utm_medium=link&utm_campaign=bilabonnement.app'

        }
      } catch {
        console.log("error url")
        return ""
      }

    },
    id() { return this.$route.path.split('/')[2].split('-').reverse()[0] },
    idmatch: function () {
      return decodeURI(this.urlname).includes(decodeURI(this.car?.id))
    },
    logo() {
      let logo = ""
      try {
        logo = require(`@/assets/${this.car?.site}.png`);
      } catch {
        logo = "";
      }
      return logo
    },
    flatCars: function () {
      let cars = []
      try {
        cars = Object.values(this.$store.state.cars["data"]).flat();
      } catch {
        console.log("nocars")
      }
      return cars;
    },
    similarCars: function () {
      let cars = []
      try {
        cars = Object.values(this.$store.state.cars["data"]).flat();
        cars = cars.filter(car => car.make.includes(this.$route.params.carname.split("-")[0]) || car.site.includes(this.$route.params.site));
      } catch {
        console.log("nocars")
      }
      return cars;
    },
    breadcrumbs: function () {
      let paths = window.location.href.split("/")
      let base = "https:/"
      paths = paths.slice(2, paths.length)
      let breadcrumbs = []

      for (let item in paths) {
        let name = paths[item]
        let position = parseInt(item) + 1
        base += "/" + paths[item]
        if (item == 0) {
          name = "Hjem"
        }
        breadcrumbs.push({ "@type": "ListItem", name: name, position: position, item: base })

      }
      return breadcrumbs
    },
    jsonld: function () {
      var jsondata = {}
      if (this.car) {
        jsondata = [

          {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": this.car?.name,
            "sku": this.car?.id,
            "image": [
              this.car?.img
            ],
            "brand": {
              "@type": "Brand",
              "name": this.car?.make
            },
            "offers": {
              "@type": "Offer",
              "availability": "https://schema.org/InStock",
              "areaServed": this.car?.location.join(" "),
              "seller": this.car?.site,
              "offeredBy": this.car?.site,
              "deliveryLeadTime": this.car?.deliveryTime,
              "priceValidUntil": `${new Date(new Date().setDate(new Date().getDate() + 7))}`,
              "priceSpecification": {
                "@type": "UnitPriceSpecification",
                "priceCurrency": "NOK",
                "price": this.car?.price,
                "validThrough": `${new Date(new Date().setDate(new Date().getDate() + 7))}`,
              },
              "itemOffered": {
                "@type": "Car",
                "name": this.car?.name,
                "description": `Fra ${this.$capitalize(this.car?.site)} kan du abonnere på denne bilen fra ${this.car?.make} for ${this.car?.price} kroner i måneden.`,
                "image": this.car?.image,
                "color": this.car?.color,
                "vehicleEngine": {
                  "@type": "EngineSpecification",
                  "name": this.car?.enginDescription || this.car?.engine,
                },
                "vehicleTransmission": this.car?.transmissionType || this.car?.transmission,
                "driveWheelConfiguration": this.car?.driveWheel,
                "emissionsCO2": this.car?.co2,
                "fuelConsumption": this.car?.fuelConsumption,
                "fuelType": this.car?.fuelType,
                "numberOfDoors": this.car?.doors,
                "bodyType": this.car?.modelType,
                "modelDate": this.car?.modelYear || this.car?.year,
                "seatingCapacity": this.car?.seats,
                "cargoVolume": this.car?.cargoCapacity || this.car?.cargoVolume,

              }
            },
            "gtin": this.car?.pno12,
            "category": "Car",
            "itemCondition": "New",



          },
          {
            "@context": "https://schema.org/",
            "@type": "BreadcrumbList",
            "itemListElement": this.breadcrumbs
          }]
      }
      return jsondata
    },
    car: function () {
      return this.flatCars.filter(car => car.id == this.id)[0]
    },
    imageTransformation: function () {

      if (window.innerWidth < 1101) {
        let imgWidth = window.innerWidth * 0.475
        return this.car?.img.replace("/upload/", `/upload/c_lfill,w_${imgWidth},ar_1.77/q_auto/f_auto/e_trim/`)
      }
      else if (window.innerWidth < 2401) {
        let imgWidth = window.innerWidth * 0.2958
        return this.car?.img.replace("/upload/", `/upload/c_lfill,w_${imgWidth},ar_1.77/q_auto/f_auto/e_trim/`)
      }
      else if (window.innerWidth > 2401) {
        let imgWidth = window.innerWidth * 0.2264
        return this.car?.img.replace("/upload/", `/upload/c_lfill,w_${imgWidth},ar_1.77/q_auto/f_auto/e_trim/`)
      }
      else {
        return this.car?.img.replace("/upload/", `/upload/c_lfill,w_500,ar_1.77/q_auto/f_auto/e_trim/`)
      }

    },
    headerImageTransformation: function () {
      if (window.innerWidth < 901) {
        let imgWidth = window.innerWidth * 0.95
        return this.car?.img.replace("/upload/", `/upload/c_lfill,w_${imgWidth},ar_1.77/q_auto/f_auto/e_trim/`)
      }
      else if (window.innerWidth < 1301) {
        let imgWidth = window.innerWidth * 0.60
        return this.car?.img.replace("/upload/", `/upload/c_lfill,w_${imgWidth},ar_1.77/q_auto/f_auto/e_trim/`)
      }
      else if (window.innerWidth > 1399) {
        let imgWidth = window.innerWidth * 0.50
        return this.car?.img.replace("/upload/", `/upload/c_lfill,w_${imgWidth},ar_1.77/q_auto/f_auto/e_trim/`)
      }
      else {
        return this.car?.img.replace("/upload/", `/upload/c_lfill,w_500,ar_1.77/q_auto/f_auto/e_trim/`)
      }
    }


  },
  created() {
  },
  watch: {
    $route: {
      immediate: true,
      handler() {
        (this.get_cars()),
          (this.addJsonld())
      }
    }
  },
  metaInfo() {
    try {
      return {
        title: `${this.car?.name} fra ${this.$capitalize(this.car?.site)} | `,
        titleTemplate: `%s Bilabonnement.app`,
        meta: [
          { charset: 'utf-8' },
          { property: 'og:description ', content: `Fra ${this.$capitalize(this.car?.site)} kan du abonnere på denne bilen fra ${this.car?.make} for ${this.car?.price} kroner i måneden.` },
          { name: 'twitter:description ', content: `Fra ${this.$capitalize(this.car?.site)} kan du abonnere på denne bilen fra ${this.car?.make} for ${this.car?.price} kroner i måneden.` },
          { name: 'twitter:creator ', content: "@bknapstad" },
          { property: 'og:title ', content: `${this.car?.name} fra ${this.$capitalize(this.car?.site)}` },
          { property: 'og:url ', content: `${window.location.href}` },
          { property: 'og:image ', content: this.car?.img },
          { name: 'twitter:title ', content: `${this.car?.name} fra ${this.$capitalize(this.car?.site)}` },
          { property: 'og:type ', content: "product" },
          { property: 'article:published_time', content: "" },
          { property: 'article:modified_time', content: "" },
          { name: 'description', content: `Fra ${this.$capitalize(this.car?.site)} kan du abonnere på denne bilen fra ${this.car?.make} for ${this.car?.price} kroner i måneden.` },
          { property: 'og:site_name', content: "Bilabonnement.app" },
          { property: 'og:locale', content: "no" },
          { property: "fb:app_id", content: "381160890208041" },

        ],
        link: [
          { rel: 'canonical', href: `${window.location.href}` }
        ]
      };
    } catch {
      console.log("error metadata")
    }
  },
}

</script>
<style scoped>
* {
  color: whitesmoke;
}

table {

  border-collapse: collapse;
  width: 100%;
  color: #333;
  font-size: 14px;
  text-align: left;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  margin: auto;
  margin-top: 50px;
  margin-bottom: 50px;

}

td {
  border-bottom: 1px solid var(--main-medium-light);
}

.header {
  position: relative;
}

.headerimage {
  display: block;
  width: 100%;
  z-index: 9;
}

.logo {
  position: absolute;
  z-index: 10;
  top: 5px;
  right: 5%;
}

ul li {
  line-height: 0.1;
}

.car {
  background: var(--main-medium-light);
  box-shadow: 2px 2px 3px #000;
  border-radius: 12px;
  margin: 5px;
  overflow: hidden;
}

details {
  margin-bottom: 10px;
  background: var(--main-medium-dark);
  width: 100%;
  border-radius: 3px;
  margin: auto;
  margin-bottom: 5px;
  box-shadow: 2px 2px 3px #000;
  color: whitesmoke;
  padding: 6px;
  padding-left: 10px;
  font-size: medium;
}

summary {
  font-size: 20px;
  cursor: pointer;
}

img.logo {
  height: auto;
  width: auto;
  max-width: 57px;
  margin-top: 10px;
  margin-right: 10px;
  align-self: center;
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
  animation-duration: 5s;
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
  color: var(--main-light);
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

.loading__letter:nth-child(11) {
  animation-delay: 3.3s;
}

.loading__letter:nth-child(12) {
  animation-delay: 3.6s;
}

.loading__letter:nth-child(13) {
  animation-delay: 3.9s;
}

@keyframes bounce {
  0% {
    transform: translateY(0px);
  }

  20% {
    transform: translateY(-40px) scale(1.3);
  }

  40% {
    transform: translateY(0px) scale(1);
  }
}

.nocar {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.carcontainer {
  justify-content: center;
  display: inline-grid;
  grid-template-columns: 23% 23% 23% 23%;
  padding-top: 30px;
  padding-bottom: 30px;
  width: 100%;
}

@media only screen and (min-width: 1100px) {
  table {
    font-size: 1rem;

  }
}
</style>