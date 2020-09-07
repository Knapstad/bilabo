const routes = require('./src/router/routes.js');

module.exports = {
  pluginOptions: {
    sitemap: {
      baseURL: 'https://bilabonnement.app',
      routes,
    },
  },
};
