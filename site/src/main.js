import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueMeta from 'vue-meta';
import Tracking from './services/Tracking';

Vue.config.productionTip = false;
Vue.use(VueMeta,{
  refreshOnceOnNavigation: true
});
Vue.use(Tracking);
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
