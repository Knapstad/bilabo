import Vue from 'vue';
import VueRouter from 'vue-router';
const routes = require('./routes');
Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  routes,
  scrollBehavior() {
    document.getElementById('app').scrollIntoView();
}
});

export default router;
