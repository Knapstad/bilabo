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
    path: '/volvo',
    name: 'Volvo care',
    component: () => import('@/views/Blogg.vue'),
    props: { slug: 'volvo' },
  },
  {
    path: '/imove',
    name: 'iMove',
    component: () => import('@/views/Blogg.vue'),
    props: { slug: 'imove' },
  },
  {
    path: '/om-oss',
    name: 'Om oss',
    component: () => import('@/views/Blogg.vue'),
    props: { slug: 'om-oss' },
  },
  {
    path: '/*',
    name: 404,
    component: () => import('@/views/Blogg.vue'),
    props: { slug: '404' },
  },
];
