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
  mounted() {
    client
      .fetch(`*[_type=='post' && slug.current == "${this.slug}"]`)
      .then((response) => (this.blocks = response[0].body))
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
