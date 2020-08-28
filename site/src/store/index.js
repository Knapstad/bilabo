import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    locations: [],
    sites: [],
  },
  mutations: {
    addLocation(state, location) {
      state.locations.push(location);
    },
    removeLocation(state, location) {
      let index = state.locations.indexOf(location);
      if (index > -1) {
        state.locations.splice(index, 1);
      }
    },
  },
  actions: {},
  modules: {},
});
