<template>
  <div> 
    <main class="bloggcontent">
      <div v-if="this.loading" class="henterbil">
        Henter bil...
      </div>

      <div v-else-if="this.namematch">
        <div class="header">
          <img class="headerimage" :src=car.img>
          <img class="logo" :src="logo" alt="">
        </div>
        <h2>Abonner på {{car.name}} fra {{capitalize(car.site)}}</h2>
        <p>Fra {{capitalize(car.site)}} kan du abonnere på denne bilen fra {{car.make}} for {{car.price}} kroner i måneden. Da er forsikring, service og dekkbytte inkludert og du kan i tillegg kjøre {{car.kmMonth}} kilometer i måneden.<span v-if="car.site == 'imove'"> Imove tilbyr i tilegg hyttebil i 10 dager slik at du kan kjøre en liten bybil tilvanlig og bytte til en større bil om du skal på litt lengre tur.</span></p>
        <p v-if="car.extra&&car.extra.length>0">Akuratt denne bilen er utstyrt med følgende utstyr:
          <ul v-for="(item, index) in car.extra" :key="index">
            <li>{{item}}</li>
          </ul>
        </p>
        
        <div v-for="(item, index) in car.content" :key="index">
          <h3>{{item.title}}</h3>
          <p>{{item.byline}}</p>
        </div>
      <section>
        <a :href="url" target="_blank" rel="noopner nofollow">Bestill denne bilen hos {{car.site}}</a>
      </section>
    </div>

    <div v-else class="nocar">
      <p>Beklager, vi finner ikke denne bilen.</p>
      <img src="/img/logo.990de79b.png" >
      <p>
      <router-link class= "button" to="/">Gå tilbake til forsiden</router-link>
      </p>
    </div>
      
    </main>
    <Footer />
  </div>
</template>
<script>
import Footer from '../components/Footer.vue'
import axios from "axios";

export default {
  name: 'CarDetails',
  components: {Footer},
  data() {
    return {
      cars:  this.$store.state?.cars,
      id: this.$route.path.split('/')[2].split('-').reverse()[0],
      urlname: this.$route.path.split("/")[2],
      loading: true
      }
    },
    methods:{
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
                (window.sessionStorage.setItem("cars",JSON.stringify(this.$store.state.cars)))
                )
            );}
      else{this.loading = false}
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
      if (this.car.order.includes('?')) {
        return (
          this.car.order +
          '&utm_source=bilabonnemet.app&utm_medium=link&utm_campaign=bilabonnement.app'
        );
      } else if(this.car.site == "volvo"){
        return (
          this.car.order+''
        );
      } else {
        return this.car.order +
          '?utm_source=bilabonnemet.app&utm_medium=link&utm_campaign=bilabonnement.app'
        
      }
    },
      namematch: function(){
        return this.urlname.includes(this.car.name.replaceAll(" ","-"))},
      logo(){
      let logo = ""
      try{
        logo = require(`@/assets/${this.car.site}.png`);
      }catch{
        logo="";
      }
      return logo
    },
    flatCars: function () {
      this.get_cars();
      let cars = []
      try{
        cars = Object.values(this.$store.state.cars["data"]).flat();
      }catch{
        console.log("nocars")
      }
      return cars;
    },
    jsonld : function(){
      var jsondata =
      {
      "@context": "https://schema.org/",
      "@type": "Product",
      "name": this.car.name,
      "image": [
        this.car.img
      ],
      // "description": this.car?.content[0].byline,
      "brand": {
        "@type": "Brand",
        "name": this.car.make
      },
      "offers": {
        "@type": "Offer",
        "url": "https://example.com/anvil",
        "priceCurrency": "NOK",
        "price": this.car.price,
        // "priceValidUntil": "2020-11-20",
        "itemCondition": "https://schema.org/UsedCondition",
        "availability": "https://schema.org/InStock"
      }
    }
      return jsondata
    },
    car : function(){
      if(this.cars =="undefined"||this.cars==null){
      this.get_cars()
      return this.flatCars.filter(car=> car.id == this.id)[0] }
      else{
      return this.flatCars.filter(car => car.id == this.id)[0]
      }
    }
    
  },
  created() {
    (this.get_cars()),
    (this.addJsonld())
  },
  watch: {
      $route: {
        immediate: true,
        handler() {
          (this.get_cars()),
          (this.addJsonld())
        }
      }
    }
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
img.logo{
  height: auto;
  width: auto;
  max-width: 57px;
  margin-top: 10px;
  margin-right: 10px;
  align-self: center;
}
.henterbil{
  display: flex;
  font-size: xx-large;
  margin: auto;
  width: auto;
  align-self: center;
  animation: example 4s infinite;
}
.henterbil:nth-child(2){
  animation-delay: 1s;
}
@keyframes example {
  0% {color: var(--main-dark)}
  30% {color: var(--main-medium-dark)}
  60% {color: var(--main-medium-light)}
  90% {color: var(--main-medium-dark)}
  100% {color: var(--main-dark)}
}
.nocar{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

</style>