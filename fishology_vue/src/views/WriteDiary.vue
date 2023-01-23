<template>
  <!-- Modal -->
  <div class="modal fade" id="writeDiaryModal" tabindex="-1">
    <div class="modal-dialog modal-lg modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title dark-blue">
            {{ this.getDate() }}
          </h3>
          <button
            @click="this.$store.state.modalOpened = false"
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="container-fluid">
            <div class="row g-2">
              <div class="col-md-4 col-12">
                <h6 class="label">
                  <i class="fa-regular fa-calendar"></i>
                  {{ this.getDay() }}
                </h6>
                <h6 class="label">
                  <i class="fa-regular fa-clock"></i>
                  {{ this.getTime() }}
                </h6>
                <h6 class="label">
                  <i class="fa-regular fa-pen-nib"></i>
                  {{ this.getUsername }}
                </h6>

                <!-- MOOD -->
                <div class="icon-group">
                  <p class="mb-0 dark-blue label">Mood</p>
                  <i
                    v-for="mood in this.getMoods"
                    :key="mood.id"
                    :class="[
                      'me-1',
                      `${mood.icon} `,
                      this.diary.mood == mood.name ? 'dark-blue' : 'light-blue',
                    ]"
                    @click="
                      this.diary.mood == mood.name
                        ? (this.diary.mood = '')
                        : (this.diary.mood = mood.name)
                    "
                    data-toggle="tooltip"
                    data-placement="bottom"
                    :title="mood.name"></i>
                </div>

                <!-- WEATHER -->

                <div class="icon-group">
                  <h6 class="mb-0 dark-blue label">Weather</h6>
                  <i
                    v-for="weather in this.getWeathers"
                    :key="weather.id"
                    :class="[
                      'me-1',
                      `${weather.icon} `,
                      this.diary.weather == weather.name
                        ? 'dark-blue'
                        : 'light-blue',
                    ]"
                    @click="
                      this.diary.weather == weather.name
                        ? (this.diary.weather = '')
                        : (this.diary.weather = weather.name)
                    "
                    data-toggle="tooltip"
                    data-placement="bottom"
                    :title="weather.id"></i>
                </div>

                <!-- FISH -->

                <label for="inputState" class="form-label">
                  <h6 class="label">Fish</h6>
                </label>
                <select
                  :key="this.$store.state.fishLoaded"
                  id="inputState"
                  class="form-select"
                  v-model="this.diary.fish">
                  <option
                    v-for="fish in this.getFishes(this.getTotalDiary)"
                    :key="fish.id"
                    v-bind:value="fish.id">
                    {{ fish.name }}
                  </option>
                </select>
              </div>

              <div class="col-md-8 col-12 bg-white rounded">
                <div id="editor"></div>
              </div>
            </div>
          </div>
        </div>
        <div v-show="errors" class="error text-center">
          <small
            v-for="(error, index) in errors"
            :key="index"
            class="text-danger">
            {{ error }}<br />
          </small>
        </div>
        <div class="modal-footer">
          <button
            @click="this.$store.state.modalOpened = false"
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal">
            Close
          </button>
          <button
            type="button"
            id="close-edit-modal"
            data-bs-dismiss="modal"
            style="display: none">
            Close
          </button>
          <button
            type="button"
            class="btn btn-primary"
            @click="this.submitDiary()">
            Swim!
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import { mapGetters } from "vuex";
import { QuillEditor, Quill } from "vue3-quill";
import "quill/dist/quill.snow.css";
import moment from "moment";

export default {
  name: "WriteDiary",
  computed: {
    ...mapGetters([
      "getFishes",
      "getMoods",
      "getWeathers",
      "getTotalDiary",
      "getUsername",
    ]),
    fishes() {
      return this.getFishes;
    },
  },
  components: {},
  data() {
    return {
      diary: {
        mood: "",
        weather: "",
        fish: "",
        body: "",
      },
      errors: [],
      fishes: [],
    };
  },
  methods: {
    getDate() {
      return moment(new Date()).format("Do MMMM YYYY");
    },
    getDay() {
      return moment(new Date()).format("dddd");
    },
    getTime(date) {
      return moment(new Date()).format("h:mm a");
    },
    updateDiary(editorText) {
      this.diary.body = editorText;
    },
    submitDiary() {
      this.errors = [];
      console.log(this.diary);

      if (
        this.diary.mood == "" ||
        this.diary.weather == "" ||
        this.diary.fish == "" ||
        this.diary.body == ""
      ) {
        this.errors.push("Please fill in all fields before submit.");
      } else {
        if (this.diary.body.length !== 0) {
          this.loading = true;

          const diary = {
            mood: this.diary.mood,
            weather: this.diary.weather,
            fish: this.diary.fish,
            body: this.diary.body,
            aquarium: this.$route.params.aquarium_id,
          };

          axios
            .post("/api/v1/submit-diary/", diary)
            .then((response) => {
              console.log("Diary Added!");
              document.getElementById("close-edit-modal").click();
              this.$store.state.modalOpened = false;
              this.$emit("diary-added");
            })
            .catch((error) => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(
                    `${property}: ${error.response.data[property]}`
                  );
                }
                console.log(JSON.stringify(error.response.data));
              } else if (error.message) {
                this.errors.push("Something went wrong. Please try again");
              }
            });
        }
      }
    },
  },
  mounted() {
    var quill = new Quill("#editor", {
      theme: "snow",
      placeholder: "Dear Diary...",
      modules: {
        toolbar: [
          ["bold", "italic", "underline", "strike"],
          // ["blockquote", "code-block"],
          [{ list: "ordered" }, { list: "bullet" }],
          [{ indent: "-1" }, { indent: "+1" }],
          // [{ direction: "rtl" }],
          // [{ size: ["small", false, "large", "huge"] }],
          [{ header: [1, 2, 3, 4, 5, 6, false] }],
          // [{ color: [] }, { background: [] }],
          [{ font: [] }],
          [{ align: [] }],
          // ["clean"],
          // ["link", "image", "video"],
        ],
      },
    });
    const that = this;
    quill.on("text-change", function () {
      that.updateDiary(quill.root.innerHTML);
    });
  },
};
</script>

<style scoped>
.modal-dialog {
  height: 80vh;
}
.modal-body {
  height: 70vh;
}

.modal-title {
  color: #4663ac;
}

#editor {
  height: 55vh;
  /* height: 100%;
  border: none; */
}
.ql-editor {
}
.col-md-8 {
  /* overflow-y: auto; */
  height: 100%;
  padding: 1rem;
}
.label {
  color: #4663ac !important;
  font-family: "Readex Pro";
  font-weight: 600 !important;
}
</style>
