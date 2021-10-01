<template>
  <div> 
    <main>

      <div v-if="this.loading" class="loading">
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

      <div v-else-if="this.namematch" class="bloggcontent"> 
        <div class="header">
          <img class="headerimage" :src="car.img.replace(' ', '-').replace('/upload/','/upload/c_crop,f_auto,g_center,q_auto/')"  :alt="car.name">
          <img class="logo" :src="logo" :alt='"logo for " + car.site'>
        </div>
        <h2>Abonner på {{car.name}} fra {{capitalize(car.site=="volvo" ? "Care by Volvo": car.site)}}</h2>
        <p>Fra {{capitalize(car.site=="volvo" ? "Care by Volvo": car.site)}} kan du abonnere på denne bilen fra {{car.make}} for {{car.price}} kroner i måneden. Da er forsikring, service og dekkbytte inkludert og du kan i tillegg kjøre {{car.kmMonth}} kilometer i måneden.<span v-if="car.site == 'imove'"> Imove tilbyr i tilegg hyttebil i 10 dager slik at du kan kjøre en liten bybil tilvanlig og bytte til en større bil om du skal på litt lengre tur.</span></p>
        <p v-if="car.description">{{car.description}}</p>

        <p v-if="car.extra&&car.extra.length>0">Akuratt denne bilen er utstyrt med følgende utstyr:
          <ul v-for="(item, index) in car.extra" :key="index">
            <li>{{item}}</li>
          </ul>
        </p>
        <details v-for="(item, index) in car.details" :key="index">
            <summary>{{index}}</summary>
            {{item}}
        </details>
          
        <div v-if="car.site == 'volvo'" class="">
          <p>Her kan  du abonnere på en flott {{car.color}} bil fra Volvo. <span v-if="car.cargoVolume"> Bilen er utstyrt med {{car.cargoVolume}} bagasjerom. </span><span v-if="car.co2">Bilen har et lavt utslipp på ca {{car.co2}}. </span><span v-if="car.fuelconsumption">Forbruket ligger på rundt {{car.fuelconsumption}}. </span><span v-if="car.engine">Bilen er utstyrt med en {{car.engine}} motor, nærmere bestemt {{car.enginDescription}}</span></p>
          <section>
            <a :href="url" target="_blank" rel="noopner nofollow">Bestill denne bilen hos {{capitalize(car.site=="volvo" ? "Care by Volvo": car.site)}}</a>
          </section>
          <section v-for="(category, index) in car.categories" :key="index">
            <h3>{{category.displayName}}</h3> 
            <p>{{category.description}}</p>
            <div v-for="(sub, index) in category.subCategories" :key="index">
              <h4>{{sub.displayName}}</h4>
              <p>{{sub.description}}</p>
              <div v-for="(item,key) in sub.items" :key="key">
                <details>
                  <summary>{{item.displayName}}</summary>
                  {{item.description}}
                </details>
              </div>
            </div>
          </section>
        </div>


          <div v-for="(item, index) in car.content" :key="index">
            <h3>{{item.title}}</h3>
            <p>{{item.byline}}</p>
          </div>
        <section>
          <a :href="url" target="_blank" rel="noopner nofollow">Bestill denne bilen hos {{capitalize(car.site=="volvo" ? "Care by Volvo": car.site)}}</a>
        </section>
      </div>
    
      <div v-else class="nocar">
        <div class="bloggcontent nocar">
        <p>Beklager, vi finner ikke denne bilen.</p>
        <img src="/img/logo.990de79b.png" >
        <p>
        
        <router-link class= "button" to="/">Gå tilbake til forsiden</router-link>
        </p>
        <p>Eller ta en titt på disse bilene fra {{capitalize(this.$route.params.site)}} eller {{this.$route.params.carname.split("-")[0]}}:</p>
        </div>
        
        <div class="carcontainer">
          <article class="car" v-for="(car, index) in similarCars.sort(this.compare)" :key="index">
            <Car class :car="car" />
          </article>
        </div>
      </div>
      
    </main>
    <Footer />
  </div>
</template>
<script>
import Footer from '../components/Footer.vue'
import Car from '../components/Car.vue'
import axios from "axios";

export default {
  name: 'CarDetails',
  components: {Footer, Car},
  data() {
    return {
      cars:  this.$store.state?.cars,
      urlname: this.$route.path.split("/")[2],
      loading: true
      }
    },
    methods:{
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
      get_cars: function(){
        if(this.cars=="undefined" || this.cars==null)
          {axios
            .get("https://europe-west1-bilabo.cloudfunctions.net/give_car")
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
            );}
      else{
        this.loading = false
        this.$track("loadingDone")
          // window.dataLayer=window.dataLayer||[],
          // window.dataLayer.push({
          //   event: 'loadingDone',
          // })
        }
      },
      capitalize(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
      },
      addJsonld : function(){
      var Jsoninterval = setInterval(() => {
        if(this.loading === false){
          if(!document.querySelector("#articledata")){
              console.log("article script not found")
              var jsonldScript = document.createElement("script")
              console.log("article script created")
              jsonldScript.setAttribute("type", "application/ld+json")
              console.log("set type")
              jsonldScript.setAttribute("id", "articledata")
              console.log("set id")

            }else{
              jsonldScript=document.querySelector("#articledata")
              if (jsonldScript.innerText === JSON.stringify(this.jsonld)){
                clearInterval(Jsoninterval)
                return;}
            }
          jsonldScript.textContent=JSON.stringify(this.jsonld);
          console.log("setting data")
          document.head.appendChild(jsonldScript)
          console.log("appending script")
          clearInterval(Jsoninterval)
            }}
              , 1000);}
      },
    computed: {
      url() {
      if (this.car?.order.includes('?')) {
        return (
          this.car?.order +
          '&utm_source=bilabonnemet.app&utm_medium=link&utm_campaign=bilabonnement.app'
        );
      } else if(this.car?.site == "volvo"){
        return (
          this.car?.order+''
        );
      } else {
        return this.car?.order +
          '?utm_source=bilabonnemet.app&utm_medium=link&utm_campaign=bilabonnement.app'
        
      }
    },
      id () { return this.$route.path.split('/')[2].split('-').reverse()[0]},
      namematch: function(){
        return decodeURI(this.urlname).includes(decodeURI(this.car?.name.replaceAll(" ","-")))},
      logo(){
      let logo = ""
      try{
        logo = require(`@/assets/${this.car?.site}.png`);
      }catch{
        logo="";
      }
      return logo
    },
    flatCars: function () {
      let cars = []
      try{
        cars = Object.values(this.$store.state.cars["data"]).flat();
      }catch{
        console.log("nocars")
      }
      return cars;
    },
    similarCars: function () {
      let cars = []
      try{
        cars = Object.values(this.$store.state.cars["data"]).flat();
        cars = cars.filter(car => car.make.includes(this.$route.params.carname.split("-")[0]) || car.site.includes(this.$route.params.site));
      }catch{
        console.log("nocars")
      }
      return cars;
    },
    jsonld : function(){
      var jsondata = {}
      if (this.car){
        jsondata =
      
      {
      "@context": "https://schema.org/",
      "@type": "Product",
      "name": this.car?.name,
      "sku": this.car?.id,
      "image": [
        this.car?.img
      ],
      "description": `Fra ${this.capitalize(this.car?.site)} kan du abonnere på denne bilen fra ${this.car?.make} for ${this.car?.price} kroner i måneden.`,
      "brand": {
        "@type": "Brand",
        "name": this.car?.make
      },
      "offers": {
        "@type": "Offer",
        "url": "https://example.com/anvil",
        "priceCurrency": "NOK",
        "price": this.car?.price,
        "priceValidUntil": `${new Date( new Date().setDate(new Date().getDate()+2))}`,
        "itemCondition": "https://schema.org/UsedCondition",
        "availability": "https://schema.org/InStock"
      }
    }
     }
      return jsondata
    },
    car : function(){
      return this.flatCars.filter(car=> car.id == this.id)[0] }
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
    return {
      title: `${this.car?.name} fra ${this.capitalize(this.car?.site)} | `,
      titleTemplate: `%s Bilabonnement.app`,
      meta: [
        { charset: 'utf-8' },
        { property: 'og:description ', content: `Fra ${this.capitalize(this.car?.site)} kan du abonnere på denne bilen fra ${this.car?.make} for ${this.car?.price} kroner i måneden.`},
        { name: 'twitter:description ', content: `Fra ${this.capitalize(this.car?.site)} kan du abonnere på denne bilen fra ${this.car?.make} for ${this.car?.price} kroner i måneden.`},
        { name: 'twitter:creator ', content: "@bknapstad"},
        { property: 'og:title ', content: `${this.car?.name} fra ${this.capitalize(this.car?.site)}`},
        { property: 'og:url ', content:  `${window.location.href}`},
        { property: 'og:image ', content:  this.car?.img},
        { name: 'twitter:title ', content:`${this.car?.name} fra ${this.capitalize(this.car?.site)}`},
        { property: 'og:type ', content: "product"},
        { property: 'article:published_time', content: ""},
        { property: 'article:modified_time', content: ""},
        { name: 'description', content: `Fra ${this.capitalize(this.car?.site)} kan du abonnere på denne bilen fra ${this.car?.make} for ${this.car?.price} kroner i måneden.`},
        { property: 'og:site_name', content: "Bilabonnement.app"},
        { property: 'og:locale', content: "no"},
        { property: "fb:app_id", content: "381160890208041"},
      ],
      link: [
          {rel: 'canonical', href: `${window.location.href}`}
      ]
          };
      },
}

</script>
<style scoped>
.header{
  position: relative;
}
.headerimage{
  display:block;
  width: 100%;
  z-index: 9;
}
.logo{
  position: absolute;
  z-index: 10;
  top: 5px;
  right: 5%;
  }
ul li{
  line-height: 0.1;
}
details{
    margin-bottom: 10px;
    background: var(--main-medium-dark);
    width: 100%;
    border-radius: 3px;
    margin: auto;
    margin-bottom: 5px;
    box-shadow: 2px 2px 3px #000;
    color: white;
    padding: 6px;
    padding-left: 10px;
    font-size: medium;
}
summary{
  font-size: 20px;
  cursor: pointer;
}

img.logo{
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
    transform: translateY(0px)  scale(1);
  }
}
.nocar{
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
.car {
  background: #fff;
  box-shadow: 2px 2px 3px #000;
  border-radius: 2px;
  margin: 5px;
  position: relative;
}

</style>