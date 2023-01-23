<template>
  <!-- Modal -->
  <div class="modal fade" id="filterModal">
    <div class="modal-dialog modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title text-center">Filter</h3>
          <button
            @click="this.$store.state.modalOpened = false"
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body container-fluid">
          <form action="">
            <div class="row mb-3 d-flex align-items-center">
              <label for="inputEmail3" class="col-sm-2 col-form-label">
                Date
              </label>
              <div class="col d-flex align-items-center">
                <input
                  v-model="this.filter.dateFrom"
                  class="form-control"
                  type="date" />
                <span class="mx-1"> to </span>
                <input
                  v-model="this.filter.dateTo"
                  class="form-control"
                  type="date" />
              </div>
            </div>
            <div class="row mb-3">
              <label for="inputEmail3" class="col-sm-2 col-form-label">
                Mood
              </label>
              <div class="col-sm-10 d-flex align-items-center">
                <i
                  v-for="mood in this.getMoods"
                  :key="mood.id"
                  :class="[
                    'me-1',
                    `${mood.icon} `,
                    this.filter.mood == mood.id ? 'dark-blue' : 'light-blue',
                  ]"
                  @click="
                    this.filter.mood == mood.id
                      ? (this.filter.mood = '')
                      : (this.filter.mood = mood.id)
                  "
                  data-toggle="tooltip"
                  data-placement="bottom"
                  :title="mood.name"></i>
              </div>
            </div>
            <div class="row mb-3">
              <label for="inputEmail3" class="col-sm-2 col-form-label">
                Weather
              </label>
              <div class="col-sm-10 d-flex align-items-center">
                <i
                  v-for="weather in this.getWeathers"
                  :key="weather.id"
                  :class="[
                    'me-1',
                    `${weather.icon} `,
                    this.filter.weather == weather.id
                      ? 'dark-blue'
                      : 'light-blue',
                  ]"
                  @click="
                    this.filter.weather == weather.id
                      ? (this.filter.weather = '')
                      : (this.filter.weather = weather.id)
                  "
                  data-toggle="tooltip"
                  data-placement="bottom"
                  :title="weather.id"></i>
              </div>
            </div>
            <div class="row mb-3">
              <label for="inputEmail3" class="col-sm-2 col-form-label">
                Fish
              </label>
              <div class="col-sm-10 d-flex align-items-center">
                <select
                  :key="this.$store.state.fishLoaded"
                  id="inputState"
                  class="form-select"
                  v-model="this.filter.fish">
                  <option value="" selected></option>
                  <option
                    v-for="fish in this.getFishes(this.getTotalDiary)"
                    :key="fish.id"
                    v-bind:value="fish.id">
                    {{ fish.name }}
                  </option>
                </select>
              </div>
            </div>
            <div class="row mb-3">
              <label for="inputEmail3" class="col-sm-2 col-form-label">
                Author
              </label>
              <div class="col-sm-10 d-flex align-items-center">
                <select
                  :key="this.$store.state.currentAquarium"
                  id="inputState"
                  class="form-select"
                  v-model="this.filter.author">
                  <option value="" selected></option>
                  <option
                    v-for="(author, index) in this.authors"
                    :key="index"
                    v-bind:value="author">
                    {{ author }}
                  </option>
                </select>
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
            <a
              @click="
                this.resetFilter();
                this.$store.state.modalOpened = false;
              "
              type="button"
              class="btn btn-link float-end">
              Reset Filter
            </a>
          </form>
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
            @click="this.setFilter()"
            type="button"
            class="btn btn-primary">
            Filter
          </button>
          <button
            type="button"
            id="close-modal"
            data-bs-dismiss="modal"
            style="display: none">
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Filter",
  computed: {
    ...mapGetters([
      "getCurrentAquarium",
      "getAquarium",
      "getFishes",
      "getMoods",
      "getTotalDiary",
      "getWeathers",
    ]),
  },
  data() {
    return {
      filter: {
        mood: "",
        weather: "",
        fish: "",
        author: "",
        dateFrom: "",
        dateTo: "",
      },
      authors: [],
      errors: [],
    };
  },
  watch: {
    async $route() {
      if (this.$route.name === "aquarium") {
        await new Promise((resolve) => setTimeout(resolve, 300));
        this.fetchAquarium(this.$route.params.aquarium_id).then((resolve) => {
          // this.filter.authors = resolve;
          this.filter.authors = resolve.participants;
        });
      }
    },
  },
  mounted() {
    this.fetchAquarium(this.$route.params.aquarium_id).then((resolve) => {
      this.authors = resolve.participants;
      // this.authors = resolve;
    });
  },
  methods: {
    ...mapActions(["fetchAquarium", "filterDiaries", "fetchDiaries"]),
    resetFilter() {
      this.fetchDiaries(this.$route.params.aquarium_id).then((resolve) => {
        this.$emit("filter-diary");
        document.getElementById("close-modal").click();
      });
    },
    setFilter() {
      const payload = {
        id: this.$route.params.aquarium_id,
        filter: this.filter,
      };
      this.filterDiaries(payload).then((resolve) => {
        this.$emit("filter-diary");
        document.getElementById("close-modal").click();
        this.$store.state.modalOpened = false;
      });
    },
  },
};
</script>
<style scoped>
label {
  font-family: "Readex Pro";
  /* font-weight: 600 !important; */
  color: #4663ac !important;
}
</style>
