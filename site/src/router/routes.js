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
    
  
  return {test}
}


module.exports = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
  },
  // {
  //   path: '/hva-er-bilabonnement',
  //   name: 'Hva er Bilabonnement',
  //   component: () => import('@/views/Blogg.vue'),
  //   props: { slug: 'hva-er-bilabonnement' },
  // },
  // {
  //   path: '/volvo',
  //   name: 'Volvo care',
  //   component: () => import('@/views/Blogg.vue'),
  //   props: { slug: 'volvo' },
  // },
  {
    path: '/:slug',
    meta: {
      sitemap: {
       // Slugs can also be provided asynchronously
       // The callback must always return an array
        slugs: getSlugs(),
      }
    },
    name: ':slug',
    component: () => import('@/views/Blogg.vue'),
  },
  // {
  //   path: '/imove',
  //   name: 'iMove',
  //   component: () => import('@/views/Blogg.vue'),
  //   props: { slug: 'imove' },
  // },
  // {
  //   path: '/om-oss',
  //   name: 'Om oss',
  //   component: () => import('@/views/Blogg.vue'),
  //   props: { slug: 'om-oss' },
  // },
  {
    path: '/*',
    name: 404,
    component: () => import('@/views/Blogg.vue'),
    props: { slug: '404' },
  },
];
