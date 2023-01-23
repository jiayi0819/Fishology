import axios from "axios";

const state = {
  scenes: [],
  props: [],
  scenesLoaded: false,
};

const getters = {
  getScenes(state) {
    return state.scenes;
  },
  getProps(state) {
    return state.props;
  },
};

const mutations = {};

const actions = {
  fetchScenes({ state }) {
    return new Promise((resolve, reject) => {
      axios.get(`/api/v1/scenes/`).then((response) => {
        response.data.forEach((item) => {
          if (
            !state.scenes.some(
              (existedScene) => existedScene.name === item.name
            )
          ) {
            const scene = {
              name: item.name,
              folder: item.folder,
              description: item.description,
              price: item.price,
              image: item.get_image,
            };
            state.scenes.push(scene);
          }
        });
        resolve(response);
        // console.log("FInish Fetching shit scenes");
      }),
        (error) => {
          reject(error);
        };
    });
  },
  resetProps({ state }) {
    state.props = [];
  },
  fetchProps({ state }, sceneName) {
    state.props = [];

    return new Promise((resolve, reject) => {
      console.log("Fetch props" + sceneName);
      axios.get(`/api/v1/props/${sceneName}`).then((response) => {
        response.data.forEach((item) => {
          const prop = {
            id: item.id,
            name: item.name,
            scene: item.scene,
            x: item.x,
            y: item.y,
            z: item.z,
            max_x: item.max_x,
            min_x: item.min_x,
            max_y: item.max_y,
            min_y: item.min_y,
            max_z: item.max_z,
            min_z: item.min_z,
            model: item.model,
            get_model: item.get_model,
          };
          state.props.push(prop);
          resolve(response);
        });
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
