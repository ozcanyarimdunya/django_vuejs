import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/dist/logger';

import auth from './auth';
import todo from './todo'

const debug = process.env.NODE_ENV !== 'production';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    todo
  },
  state: {
    menuCollapsed: false,
  },
  actions: {},
  mutations: {},
  strict: debug,
  plugins: debug ? [createLogger()] : [],
})