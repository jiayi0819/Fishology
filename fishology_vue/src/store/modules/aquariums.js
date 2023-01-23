import axios from "axios";

const state = {
  aquariums: [],
  currentAquarium: {},
  editAquarium: null,
};

const getters = {
  getAquariums(state) {
    return state.aquariums;
  },
  getAquarium: (state) => (id) => {
    console.log("THe id is " + id);
    console.log();
    return state.aquariums.find((aquarium) => aquarium.id == id);
  },
  getCurrentAquarium(state) {
    console.log("Current Aquarium: ");
    console.log(state.currentAquarium);
    return state.currentAquarium;
  },
};

const mutations = {};

const actions = {
  fetchAquariums({ state }) {
    state.aquariums = [];

    return new Promise((resolve, reject) => {
      axios.get("/api/v1/aquariums").then((response) => {
        response.data.forEach((item) => {
          if (
            !state.aquariums.some(
              (existedAquarium) => existedAquarium.id === item.id
            )
          ) {
            const aquarium = {
              id: item.id,
              host: item.host,
              participants: item.participants,
              name: item.name,
              description: item.description,
              image: item.image,
              sky: item.sky,
              scene: item.scene,
              isPrivate: item.isPrivate,
              created: item.created,
              updated: item.updated,
              get_absolute_url: item.get_absolute_url,
              get_total_fish: item.get_total_fish,
              get_image: item.get_image,
            };
            state.aquariums.push(aquarium);
          }
        });
        console.log(state.aquariums);
        resolve(response);
      }),
        (error) => {
          reject(error);
        };
    });
  },
  fetchAquarium({ state }, id) {
    return new Promise((resolve, reject) => {
      axios.get(`/api/v1/aquarium/${id}/`).then((response) => {
        state.currentAquarium = response.data;
        resolve(response.data);
        // resolve(response.data.participants);
      }),
        (error) => {
          reject(error);
        };
    });
  },
  setCurrentAquarium({ state, getters }, id) {
    state.currentAquarium = getters.getAquarium(id);
    // console.log("Currrent Aquarium " + state.currentAquarium);
  },

  updateAquariumSky({ state, getters }, payload) {
    console.log("sky name - " + payload.mapName + " id - " + payload.id);
    return new Promise((resolve, reject) => {
      axios
        .post(`/api/v1/update-aquarium-sky/${payload.id}/${payload.mapName}/`)
        .then((response) => {
          state.currentAquarium = response.data;
          resolve(response.data);
        }),
        (error) => {
          reject(error);
        };
    });
  },
  updateAquariumScene({ state, getters }, payload) {
    console.log("scene name - " + payload.sceneName + " id - " + payload.id);
    return new Promise((resolve, reject) => {
      axios
        .post(
          `/api/v1/update-aquarium-scene/${payload.id}/${payload.sceneName}/`
        )
        .then((response) => {
          state.currentAquarium = response.data;
          resolve(response.data);
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
