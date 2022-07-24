//import Vue from 'vue'
//import Vuex from 'vuex'
//Vue.use(Vuex)

export const state = () => ({
  loggedin: false,
  api_token: '',
})

export const mutations = {
  set (state, [variable, value]) {
    state[variable] = value
  }
}

