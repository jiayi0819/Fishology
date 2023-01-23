import axios from "axios";

const state = {
  skies: [],
};

const getters = {
  getSkies(state) {
    return state.skies;
  },
};

const mutations = {};

const actions = {
  fetchSkies({ state }) {
    return new Promise((resolve, reject) => {
      axios.get(`/api/v1/skies/`).then((response) => {
        response.data.forEach((item) => {
          if (
            !state.skies.some((existedSky) => existedSky.name === item.name)
          ) {
            const sky = {
              name: item.name,
              description: item.description,
              price: item.price,
              folder: item.folder,
              image: item.get_image,
              maps: item.get_maps,
            };
            state.skies.push(sky);
          }
        });
        resolve(response);
      }),
        (error) => {
          reject(error);
        };
    });
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
