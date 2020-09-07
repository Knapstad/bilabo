module.exports = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
  },
  {
    path: '/hva-er-bilabonnement',
    name: 'Hva er Bilabonnement',
    component: () => import('@/views/Blogg.vue'),
    props: { slug: 'hva-er-bilabonnement' },
  },
  {
    path: '/*',
    name: 404,
    component: () => import('@/views/Blogg.vue'),
    props: { data: '404' },
  },
];
