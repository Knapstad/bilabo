import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Blogg from '@/views/Blogg.vue';
Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/hva-er-bilabonnement',
    name: 'Hva er Bilabonnement',
    component: Blogg,
    props: { slug: 'hva-er-bilabonnement' },
  },
  {
    path: '/*',
    name: 404,
    component: Blogg,
    props: { data: '404' },
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
