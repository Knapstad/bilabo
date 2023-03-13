import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueMeta from 'vue-meta';
import Tracking from './services/Tracking';
import * as Sentry from "@sentry/vue";
import { BrowserTracing } from "@sentry/tracing";

Vue.config.productionTip = false;
Vue.use(VueMeta, {
  refreshOnceOnNavigation: true
});
Sentry.init({
  Vue,
  dsn: "https://ad160e55dd9d4d45a89ef3295ef332c2@o4504831113691136.ingest.sentry.io/4504831115001856",
  replaysSessionSampleRate: 0.1,
  // If the entire session is not sampled, use the below sample rate to sample
  // sessions when an error occurs.
  replaysOnErrorSampleRate: 1.0,
  integrations: [
    new BrowserTracing({
      routingInstrumentation: Sentry.vueRouterInstrumentation(router),
      tracePropagationTargets: ["localhost", "my-site-url.com", /^\//],
    }),
    new Sentry.Replay(),
  ],
  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for performance monitoring.
  // We recommend adjusting this value in production
  tracesSampleRate: 1.0,
});
Vue.use(Tracking);
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
