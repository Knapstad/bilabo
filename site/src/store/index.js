import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    locations: [],
    sites: [],
    makes: [],
    data: [],
  },
  mutations: {
    addFilter(state, value) {
      let arr = state[value[0]];
      arr.push(value[1]);
    },
    removeFilter(state, value) {
      let index = state[value[0]].indexOf(value[1]);
      if (index > -1) {
        state[value[0]].splice(index, 1);
      }
    },
  },
  actions: {},
  modules: {},
});
