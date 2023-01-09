<template>
  <div>
    <BreadCrumb></BreadCrumb>
    <div v-if="this.blocks == 0" class="notfound bloggcontent">
      <p>Beklager vi finner ikke siden du leter etter</p>
    </div>
    <div class="bloggcontent">
      <div>
        <img v-if="mainImage.url" class="headerimage" :src='mainImage.url + "?w=675&h=345&fit=crop&hotspot=true"'
          :alt="mainImage.alt">
      </div>
      <block-content :blocks="blocks" :serializers="serializers" :imageOptions="{ h: 300, w: 1000, fit: 'crop' }" />
    </div>
    <section class="">
      <h3 v-if="flatCars.lengt >= 1" class="bloggcontent">Det er for øyeblikket {{ flatCars.length }} {{(flatCars.length
      >
      1) ? "tilgengelige biler" : "tilgengelig bil"}} fra {{ title }}</h3>
      <div class="carcontainer">
        <article class="car" v-for="(car, index) in flatCars.sort(this.compare)" :key="index">
          <Car class :car="car" />
        </article>
      </div>
    </section>
    <Footer />
  </div>

</template>

<script>
import BlockContent from 'sanity-blocks-vue-component';
import BlockImage from '@/components/BlockImage.vue';
import DataRef from '@/components/DataRef.vue';
import Links from '@/components/Links.vue';
import Footer from '@/components/Footer.vue';
import BreadCrumb from '@/components/BreadCrumb.vue'
import sanityClient from '@sanity/client';
import Car from "@/components/Car.vue";
import axios from "axios";


const client = sanityClient({
  projectId: 'bwpvihdh',
  dataset: 'production',
  useCdn: false,
});
const serializers = {
  types: {
    image: BlockImage,
    dataref: DataRef
  },
  marks: {
    link: Links
  }
}

export default {
  name: 'Blogg',
  props: [],
  components: {
    BlockContent,
    BreadCrumb,
    Footer,
    Car,
  },
  data() {
    return {
      cars: this.$store.state.cars,
      loading: true,
      blocks: [],
      response: undefined,
      updated: "",
      created: "",
      title: "",
      description: "",
      mainImage: undefined,
      serializers: serializers
    }
  },
  computed: {
    jsonld: function () {
      var jsondata =
      {
        "@context": "http://schema.org",
        "@type": "Article",
        "name": this.blocks[0].children[0].text,
        "headline": this.blocks[0].children[0].text,
        "image": this.mainImage?.url,
        "articleBody": this.blocks.slice(1).map((block) => block.children[0].text).join(),
        "publisher": {
          "@type": "Organization",
          "name": "Bilabonnement"
        }
      }
      return jsondata
    },
    flatCars: function () {
      this.get_cars();
      let cars = []
      try {
        cars = Object.values(this.$store.state.cars["data"]).flat();
        cars = cars.filter((car) => this.$route.params.slug.includes(car.site));
      } catch {
        console.log("nocars")
      }
      return cars;
    },
  },
  methods: {
    addJsonld: function () {
      if (this.loading === false) {
        if (!document.querySelector("#articledata")) {
          var jsonldScript = document.createElement("script")
          jsonldScript.setAttribute("type", "application/ld+json")
          jsonldScript.setAttribute("id", "articledata")
        }
        else {
          jsonldScript = document.querySelector("#articledata")
        }
        jsonldScript.textContent = JSON.stringify(this.jsonld);
        document.head.appendChild(jsonldScript)
      }
    },
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
          .get("https://europe-west1-bilabo.cloudfunctions.net/give_car")
          .then((response) => (this.$store.commit("addData", ["cars", response])),
          )
          .finally(
            () => (
              (this.loading = false),
              (this.cars = this.$store.state.cars),
              (window.sessionStorage.setItem("cars", JSON.stringify(this.$store.state.cars)))
            )
          );
      }
      else { this.loading = false }
    },

    loadData: function () {
      this.loading = true,
        this.blocks = [],
        this.response = undefined,
        this.updated = "",
        this.create = "",
        this.title = "",
        this.description = "",
        this.mainImage = undefined,
        client
          .fetch(`*[_type=='post' && slug.current == "${this.$route.params.slug}"]{..., body[]{..., "asset": asset->}, mainImage{..., "asset": asset->}}`)
          .then((response) => {
            this.response = response,
              this.blocks = this.response[0].body,
              this.created = this.response[0]._createdAt,
              this.updated = this.response[0]._updatedAt,
              this.title = this.response[0].title,
              this.description = this.response[0].description,
              this.mainImage = { url: this.response[0].mainImage?.asset.url || "", alt: response[0].mainImage?.alt || "" };
          })
          .finally(
            () => (
              (this.loading = false),
              window.dataLayer = window.dataLayer || [],
              window.dataLayer.push({
                event: 'loadingDone',
              }),
              (this.addJsonld()),
              (this.get_cars())
            )
          );
    }
  },
  metaInfo() {
    return {
      title: `${this.title} | `,
      titleTemplate: `%s Bilabonnement.app`,
      meta: [
        { charset: 'utf-8' },
        { property: 'og:description ', content: this.description },
        { name: 'twitter:description ', content: this.description },
        { name: 'twitter:creator ', content: "@bknapstad" },
        { property: 'og:title ', content: this.title },
        { property: 'og:url ', content: `https://bilabonnement.app/${this.$route.params.slug}` },
        { property: 'og:image ', content: `https://res.cloudinary.com/db0kzjtgs/image/upload/v1624966021/${this.$route.params.slug}-site.png` },
        { name: 'twitter:title ', content: this.title },
        { property: 'og:type ', content: "article" },
        { property: 'article:published_time', content: this.created },
        { property: 'article:modified_time', content: this.updated },
        { name: 'description', content: this.description },
        { property: 'og:site_name', content: "Bilabonnement.app" },
        { property: 'og:locale', content: "no" },
        { property: "fb:app_id", content: "381160890208041" },
      ],
      link: [
        { rel: 'canonical', href: `https://bilabonnement.app/${this.$route.params.slug}` }
      ]
    };
  },
  mounted() {
    this.loadData();
  },
  watch: {
    $route: {
      immediate: true,
      handler() {
        this.loadData()

      }
    }
  }
};
</script>
<style scoped>
.carcontainer {
  justify-content: center;
  display: inline-grid;
  grid-template-columns: 23% 23% 23% 23%;
  padding-top: 30px;
  padding-bottom: 30px;
  width: 100%;
}

.results {
  padding-left: 6px;
  font-size: 1.3rem;
  grid-column: 1 / -1;
}

.car {
  background: #fff;
  box-shadow: 2px 2px 3px #000;
  border-radius: 2px;
  margin: 5px;
  position: relative;
}

.notfound {
  height: 70vh;
  justify-content: center;
  align-items: center;
}

.bloggcontent {
  display: flex;
  flex-direction: column;
  width: 33%;
  margin: auto;
  line-height: 1.5;
}

.bloggcontent h2 {
  color: black;
  font-size: 33px;
}

.bloggcontent h3 {
  color: black;
  font-size: 1.5rem;
  font-weight: bolder;
}

.bloggcontent p {
  font-size: 22px;
  margin-bottom: 50px;
}

img.headerimage {
  width: 100%;
}

img.fullwidth {
  width: 100%;
  margin-top: 1rem;
}

@media screen and (max-width: 1500px) {
  .bloggcontent {
    width: 40%;
  }
}

@media screen and (max-width: 1400px) {
  .bloggcontent {
    width: 50%;
  }
}

@media screen and (max-width: 1300px) {
  .bloggcontent {
    width: 60%;
  }
}

@media only screen and (max-width: 900px) {
  .bloggcontent {
    width: 95%;
  }

  .carcontainer {
    grid-template-columns: 49% 49%;
    padding: 0;
  }

}
</style>
