import axios from "axios";

const state = {
  moods: [],
  moodsLoaded: false,
};

const getters = {
  getMoods(state) {
    return state.moods;
  },
  getMood: (state) => (moodID) => {
    const mood = state.moods.find((mood) => mood.id == moodID);
    return mood;
  },
};

const mutations = {};

const actions = {
  fetchMoods({ state }) {
    state.moods = [];

    return new Promise((resolve, reject) => {
      this.moodsLoaded = false;
      axios.get("/api/v1/moods/").then((response) => {
        response.data.forEach((doc) => {
          if (!state.moods.some((existedMood) => existedMood.id === doc.id)) {
            const mood = {
              id: doc.id,
              name: doc.name,
              icon: doc.icon,
              value: doc.value,
            };
            state.moods.push(mood);
          }
        });
        this.moodsLoaded = true;
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
