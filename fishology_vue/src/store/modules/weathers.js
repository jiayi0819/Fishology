import axios from "axios";

const state = {
  weathers: [],
  weathersLoaded: false,
};

const getters = {
  getWeathers(state) {
    return state.weathers;
  },
};

const mutations = {};

const actions = {
  fetchWeathers({ state }) {
    state.weathers = [];

    return new Promise((resolve, reject) => {
      this.weathersLoaded = false;
      axios.get("/api/v1/weathers/").then((response) => {
        response.data.forEach((doc) => {
          if (
            !state.weathers.some(
              (existedWeather) => existedWeather.id === doc.id
            )
          ) {
            const weather = {
              id: doc.id,
              name: doc.name,
              icon: doc.icon,
            };
            state.weathers.push(weather);
          }
        });
        this.weathersLoaded = true;
        resolve(response);
      }),
        (error) => {
          reject(error);
        };
    });
  },

  setReadDiaryNo({ commit }, diaryNo) {
    commit("changeReadDiaryNo", diaryNo);
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
