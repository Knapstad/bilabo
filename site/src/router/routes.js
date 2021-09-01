var sanityClient = require('@sanity/client');


const client = sanityClient({
  projectId: 'bwpvihdh',
  dataset: 'production',
  useCdn: false,
});



async function getSlugs() {
  var test=""
  await client.fetch(`*[_type=='post'].slug.current`)
    .then((response) => {
      test=response
    }
    )
  return test
}

module.exports = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
  },
  {
    path: '/:slug',
    meta: {
      sitemap: {
       // Slugs can also be provided asynchronously
       // The callback must always return an array
        slugs:  async () => await getSlugs(),
      }
    },

    component: () => import('@/views/Blogg.vue'),
  },
  {
    path: '/:site/:carname',
    name: 'cardetails',
    component: () => import('@/views/CarDetails.vue'),
    meta: {
      sitemap: {
        ignoreRoute: true,
      },
    }
  },
  {
    path: '/*',
    name: 404,
    component: () => import('@/views/Blogg.vue'),
    props: { slug: '404' },
  },
];
