import axios from "axios";
import Vuex from "vuex";

import aquariums from "./modules/aquariums.js";
import diaries from "./modules/diaries.js";
import fishes from "./modules/fishes.js";
import moods from "./modules/moods.js";
import panels from "./modules/panels.js";
import scenes from "./modules/scenes.js";
import skies from "./modules/skies.js";
import weathers from "./modules/weathers.js";

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    token: "",
    username: "",
    modalOpened: false,
    loading: false,
    user: Object,
  },
  getters: {
    getUsername(state) {
      console.log("youre calling get username: " + state.username);
      return state.username;
    },
    getAuthenticated(state) {
      return state.isAuthenticated;
    },
    getUser(state) {
      return state.user;
    },
    isLoading(state) {
      return state.loading;
    },
  },
  mutations: {
    initializeStore(state) {
      console.log("Try to initialize store");

      if (localStorage.getItem("token")) {
        state.isAuthenticated = true;
        state.token = localStorage.getItem("token");
        state.username = localStorage.getItem("username");
        console.log("Store initialized " + state.username);

        axios
          .get(`/api/v1/users/${state.username}/`)
          .then((response) => {
            state.user = response.data;
            console.log(state.user);
          })
          .catch((error) => {
            console.log("Can't fetch user info");
          });
      } else {
        state.token = "";
        state.isAuthenticated = false;
        console.log("Nothing in the local Storage : (");
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {
    aquariums,
    diaries,
    fishes,
    moods,
    panels,
    scenes,
    skies,
    weathers,
  },
});
