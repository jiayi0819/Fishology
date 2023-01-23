import axios from "axios";

const state = {
  readDiaryNo: 0,
  diaries: [],
  diary: {
    mood: "",
    weather: "",
    fish: "",
    body: "",
  },
};

const getters = {
  getDiaries(state) {
    return state.diaries;
  },

  // GET DIARY TOTAL COUNT
  getTotalDiary(state) {
    return state.diaries.length;
  },

  getDiary(state) {
    return state.diary;
  },

  // getDiary: (state) => (diaryID) => {
  //   return state.diaries.find((diary) => diary.id == diaryID);
  // },
};

const mutations = {};

const actions = {
  filterDiaries({ state }, payload) {
    state.diaries = [];
    return new Promise((resolve, reject) => {
      console.log(payload);
      axios
        .post(`/api/v1/diaries/filter/${payload.id}/`, payload.filter)
        .then((response) => {
          response.data.forEach((doc) => {
            //CHECK IF DIARY EXISTED ADY
            if (
              !state.diaries.some((existedDiary) => existedDiary.id === doc.id)
            ) {
              const diary = {
                id: doc.id,
                aquarium: doc.aquarium,
                author: doc.author,
                fish: doc.fish,
                body: doc.body,
                created: doc.created,
                mood: doc.mood,
                weather: doc.weather,
              };
              state.diaries.push(diary);
            }
          });
          // console.log(state.diaries);
          resolve(response);
        }),
        (error) => {
          reject(error);
        };
    });
  },
  //FETCH DIARIES
  fetchDiaries({ state }, aquarium_id) {
    state.diaries = []; //RESET
    return new Promise((resolve, reject) => {
      axios.get(`/api/v1/diaries/${aquarium_id}/`).then((response) => {
        response.data.forEach((doc) => {
          //CHECK IF DIARY EXISTED ADY
          if (
            !state.diaries.some((existedDiary) => existedDiary.id === doc.id)
          ) {
            const diary = {
              id: doc.id,
              aquarium: doc.aquarium,
              author: doc.author,
              fish: doc.fish,
              body: doc.body,
              created: doc.created,
              mood: doc.mood,
              weather: doc.weather,
            };
            // console.log(diary)
            state.diaries.push(diary);
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
