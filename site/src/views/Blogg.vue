<template>
  <div class="bloggcontent">
    <block-content :blocks="blocks" :serializers="serializers" />
  </div>
</template>

<script>
// Import the component if not already added globally
import BlockContent from 'sanity-blocks-vue-component';
import sanityClient from '@sanity/client';
const client = sanityClient({
  projectId: 'bwpvihdh',
  dataset: 'production',
  useCdn: false,
});

// Import any components to be used as serializers
export default {
  name: 'Blogg',
  props: ['slug'],
  components: {
    BlockContent,
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
