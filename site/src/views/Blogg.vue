<template>
  
  <div>
    <div v-if="this.blocks==0" class="notfound bloggcontent">
      <p>Beklager vi finner ikke siden du leter etter</p>
    </div>
    <div class="bloggcontent">
      <div>
        <img v-if="mainImage" class="headerimage" :src="mainImage.url" :alt="mainImage.alt">
      </div>
      <block-content :blocks="blocks" :serializers="serializers" :imageOptions="{h: 300, w: 1000 ,fit : 'crop'}"/>
    
    </div>
    <Footer />
  </div>

</template>

<script>
import BlockContent from 'sanity-blocks-vue-component';
import sanityClient from '@sanity/client';
import Footer from '@/components/Footer.vue'
import BlockImage from '@/components/BlockImage.vue'


const client = sanityClient({
  projectId: 'bwpvihdh',
  dataset: 'production',
  useCdn: false,
});
export default {
  name: 'Blogg',
  props: [],
  components: {
    BlockContent,
    Footer,
  },
  data() {
    return {
      loading: true,
      blocks: [],
      response: undefined,
      updated: "",
      created: "",
      title: "",
      description: "",
      mainImage: undefined,
      serializers: {
        types: {
          image: BlockImage
          }
      },
    };
  },
  computed: {
   },
  methods:{
    loadData: function() {
      this.loading= true,
      this.blocks= [],
      this.response= undefined,
      this.updated= "",
      this.create= "",
      this.title= "",
      this.description= "",
      this.mainImage= undefined,
      this.serializers= {
        types: {
          image: BlockImage
          }
      }

      client
        .fetch(`*[_type=='post' && slug.current == "${this.$route.params.slug}"]{..., body[]{..., "asset": asset->}, mainImage{..., "asset": asset->}}`)
        .then((response) => {
          this.response=response,
            this.blocks=this.response[0].body,
            this.created=this.response[0]._createdAt,
            this.updated=this.response[0]._updatedAt,
            this.title=this.response[0].title,
            this.description=this.response[0].description,
            this.mainImage={ url: this.response[0].mainImage.asset.url+"?w=1000&h=300&fit=crop&hotspot=true&fp-y=0.58"||"", alt: response[0].mainImage.alt||"" };
        })
      .finally(
        () => (
          (this.loading=false),
          window.dataLayer=window.dataLayer||[],
          window.dataLayer.push({
            event: 'loadingDone',
          })
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
        { property: 'og:description ', content: this.description},
        { name: 'twitter:description ', content: this.description},
        { name: 'twitter:creator ', content: "@bknapstad"},
        { property: 'og:title ', content: this.title},
        { name: 'twitter:title ', content: this.title},
        { property: 'og:type ', content: "article"},
        { property: 'article:published_time', content: this.created},
        { property: 'article:modified_time', content: this.updated},
        { name: 'description', content: this.description}
      ],
      link: [
      {rel: 'canonical', href: `https://bilabonnement.app/${this.$route.params.slug}`}
  ]
      };
  },
  mounted() {
    // this.loadData();
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
.bloggcontent h1 {
  color: black;
  font-size: 33px;
}
.bloggcontent p {
  font-size: 22px;
  margin-bottom: 50px;
}
img.headerimage {
  width: 100%;
}
img.fullwidth{
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
  .bloggcontent{
    width: 95%;
  }
}
</style>
