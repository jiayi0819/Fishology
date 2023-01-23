<template>
  <!-- Modal -->
  <div class="modal fade" id="readDiaryModal" tabindex="-1">
    <div class="modal-dialog modal-lg modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <!-- <h5 class="modal-title" id="exampleModalLabel">
            {{ this.formatDate(diary.created) }}
          </h5> -->
          <button
            @click="this.$store.state.modalOpened = false"
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"></button>
        </div>
        <div class="modal-body container-fluid">
          <div class="row g-2">
            <div class="col-md-4 col-12">
              <h3 class="dark-blue">{{ this.formatDate(diary.created) }}</h3>
              <h6 class="label">
                <i class="fa-regular fa-calendar"></i>
                {{ this.getDay(diary.created) }}
              </h6>
              <h6 class="label">
                <i class="fa-regular fa-clock"></i>
                {{ this.getTime(diary.created) }}
              </h6>
              <h6 class="label">
                <i class="fa-regular fa-pen-nib"></i>
                {{ diary.author }}
              </h6>

              <p class="dark-blue">Weather</p>
              <div class="icon-group">
                <i
                  v-for="weather in this.getWeathers"
                  :key="weather.id"
                  :class="[
                    'me-1',
                    `${weather.icon} `,
                    diary.weather == weather.name ? 'dark-blue' : 'light-blue',
                  ]"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  :title="diary.weather"></i>
              </div>

              <p class="dark-blue">Feeling:</p>
              <div class="icon-group">
                <i
                  v-for="mood in this.getMoods"
                  :key="mood.id"
                  :class="[
                    'me-1',
                    `${mood.icon} `,
                    diary.mood == mood.name ? 'dark-blue' : 'light-blue',
                  ]"
                  data-toggle="tooltip"
                  data-placement="bottom"
                  :title="mood.name"></i>
              </div>
            </div>

            <div class="col-md-8 bg-white rounded col-12">
              <div class="diary-content ql-editor" v-html="diary.body"></div>
              <div class="mb-3"></div>
            </div>
          </div>
        </div>
        <!-- <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal">
            Close
          </button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import moment from "moment";

export default {
  name: "ReadDiary",
  data() {
    return {
      // mood: getMood(diary.mood),
      fish: {},
      date: null,
    };
  },
  props: {
    diary: Function,
  },
  methods: {
    printMood(array) {
      for (attribute of array) {
        console.log(attribute);
      }
    },
  },
  computed: {
    ...mapGetters(["getFish", "getMoods", "getWeathers"]),
    getMoodName(mood) {
      return mood.name;
    },
    getDate() {
      return moment(diary.created).format("Do MMMM YYYY");
    },
  },
  methods: {
    formatDate(date) {
      return moment(date).format("Do MMMM YYYY");
    },
    getDay(date) {
      return moment(date).format("dddd");
    },
    getTime(date) {
      return moment(date).format("h:mm a");
    },
  },
};
</script>

<style lang="scss" scoped>
.ql-editor {
  // overflow-y: auto;
}
.col-8 {
  overflow-y: auto;
  padding: 1rem;
}
.label {
  color: #4663ac !important;
  font-family: "Readex Pro";
  font-weight: 600 !important;
}
.bg-white {
  background-color: white;
  opacity: 0.8;
}
</style>
