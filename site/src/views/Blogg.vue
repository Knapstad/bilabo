<template>
  <div>
    <div class="bloggcontent">
      <block-content :blocks="blocks" :serializers="serializers" />
    
    </div>
    <Footer />
  </div>

</template>

<script>
import BlockContent from 'sanity-blocks-vue-component';
import sanityClient from '@sanity/client';
import Footer from '@/components/Footer.vue'


const client = sanityClient({
  projectId: 'bwpvihdh',
  dataset: 'production',
  useCdn: false,
});
export default {
  name: 'Blogg',
  props: ['slug'],
  components: {
    BlockContent,
    Footer,
  },
  data() {
    return {
      loading: true,
      blocks: [],
      updates: "",
      created: "",
      title: "",
      description: "",
      serializers: {
        types: {},
      },
    };
  },
  computed: {
    query() {
      return `*[_type=='post' && slug.current == ${this.slug}]`;
    },
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
      ]};
  },
  mounted() {
    client
      .fetch(`*[_type=='post' && slug.current == "${this.slug}"]`)
      .then((response) => (
        this.response = response,
        this.blocks = this.response[0].body,
        this.created = this.response[0]._createdAt,
        this.created = this.response[0]._updatedAt,
        this.updated = this.response[0]._updatedAt,
        this.title = response[0].title,
        this.description = response[0].description))
      .finally(
        () => (
          (this.loading = false),
          window.dataLayer.push({
            event: 'loadingDone',
          })
        )
      );
  },
};
</script>
<style scoped>
.bloggcontent {
  display: flex;
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
</style>
