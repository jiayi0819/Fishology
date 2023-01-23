import axios from "axios";
import { vModelSelect } from "vue";

const state = {
  fishes: [],
  fishLoaded: false,
};

const getters = {
  getFishes: (state) => (totalFish) => {
    const result = state.fishes.filter((fish) => fish.price <= totalFish);
    return result;
  },

  getAllFishes(state) {
    return state.fishes;
  },

  // GET 1 FISH
  getFish: (state) => (fishID) => {
    const fish = state.fishes.find((fish) => fish.id == fishID);
    return fish;
  },
};

const actions = {
  // FETCH FISH
  fetchFishes({ state }) {
    return new Promise((resolve, reject) => {
      // state.fishes = [];
      this.fishLoaded = false;
      axios.get(`/api/v1/fishes/`).then((response) => {
        response.data.forEach((doc) => {
          if (
            !state.fishes.some((existedWeather) => existedWeather.id === doc.id)
          ) {
            const fish = {
              id: doc.id,
              name: doc.name,
              description: doc.description,
              image: doc.image,
              model: doc.model,
              price: doc.price,
              get_image: doc.get_image,
              get_lock_image: doc.get_lock_image,
              get_model: doc.get_model,
            };
            state.fishes.push(fish);
          }
        });
        this.fishLoaded = true;
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
};
