<template>
  <div class="modal fade" id="statisticsModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title" id="exampleModalLabel">Statistics</h3>
          <button
            @click="this.$store.state.modalOpened = false"
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"></button>
        </div>
        <div class="modal-body container-fluid">
          <div class="panel container-fluid">
            <!-- TAB NAVBAR -->
            <!-- <div class="tab-list dark-blue"> -->
            <ul class="nav nav-pills">
              <li class="nav-item">
                <h3
                  @click="changeSelectedTab('diaries')"
                  :class="[
                    'nav-link',
                    this.selectedTab === 'diaries' ? 'active' : '',
                  ]">
                  <i class="fa-regular fa-calendar"></i>
                  Diaries
                </h3>
              </li>
              <li class="nav-item">
                <h3
                  :class="[
                    'nav-link',
                    this.selectedTab === 'mood' ? 'active' : '',
                  ]"
                  @click="changeSelectedTab('mood')">
                  <i class="fa-regular fa-face-smile"></i>
                  Mood
                </h3>
              </li>
            </ul>
            <!-- </div> -->

            <div class="tab-content" v-show="selectedTab == 'mood'">
              <p class="text-muted mb-1">
                <small>
                  View your mood change in your diaries over the time!
                </small>
              </p>

              <div class="chart-section rounded">
                <div class="row">
                  <div class="dropdown btn-sm">
                    <select
                      v-model="moodChartRange"
                      @change="
                        this.index = 0;
                        updateMoodChart($event);
                        this.indexFreeze = false;
                      "
                      class="form-select pre-scrollables mb-1 float-end">
                      <option>
                        <p>Week</p>
                      </option>
                      <option>
                        <p>Month</p>
                      </option>
                      <option>
                        <p>Year</p>
                      </option>
                    </select>
                  </div>
                </div>

                <div class="d-flex flex-row align-items-center">
                  <i
                    v-show="!this.indexFreeze"
                    @click="this.setIndex('back')"
                    class="fa-solid fa-caret-left"></i>
                  <canvas id="moodChart"></canvas>
                  <i
                    v-show="this.index != 0"
                    @click="this.setIndex('forward')"
                    class="fa-solid fa-caret-right"></i>
                </div>
              </div>

              <div class="container-fluid mx-auto"></div>
            </div>

            <div class="tab-content" v-show="selectedTab == 'diaries'">
              <p class="text-muted mb-1">
                <small> View your diary submissions over the time! </small>
              </p>
              <div class="chart-section rounded">
                <div class="row">
                  <div class="dropdown">
                    <select
                      v-model="diariesChartRange"
                      @change="
                        this.index = 0;
                        updateDiariesChart($event);
                        this.indexFreeze = false;
                      "
                      class="form-select pre-scrollables mb-3 float-end">
                      <option>Week</option>
                      <option>Month</option>
                      <option>Year</option>
                    </select>
                  </div>
                </div>

                <div class="d-flex flex-row align-items-center m-0">
                  <i
                    v-show="!this.indexFreeze"
                    @click="this.setIndex('back')"
                    class="fa-solid fa-caret-left"></i>
                  <canvas id="diariesChart"></canvas>
                  <i
                    v-show="this.index != 0"
                    @click="this.setIndex('forward')"
                    class="fa-solid fa-caret-right"></i>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Statistics",
  data() {
    return {
      index: 0,
      indexFreeze: false,
      diaryList: [],
      months: [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ],

      // CHART.JS VARIABLES

      selectedTab: "diaries",
      moodChart: null,
      moodChartRange: "Week",
      diariesChart: null,
      diariesChartRange: "Week",
    };
  },

  async mounted() {
    ////////////////////////////////////
    // MOOD CHART
    ////////////////////////////////////

    let moodChartCanvas = document.getElementById("moodChart").getContext("2d");
    let diariesChartCanvas = document
      .getElementById("diariesChart")
      .getContext("2d");

    let moodChartObject = new Chart(moodChartCanvas, {
      type: "line",
      data: {
        labels: this.months,
        datasets: [
          {
            data: [2, 4, null, -2, 5, null, -1],
            backgroundColor: "#5BBAE8",
            spanGaps: true,
            borderWidth: 1,
            borderColor: "#5BBAE8",
            // borderColor: "#777",
            hoverBorderWidth: 3,
            hoverBorderColor: "#000",
          },
        ],
      },
      options: {
        // responsive: false,
        scales: {
          y: {
            type: "category",
            labels: ["\uf585", "\uf118", "\uf11a", "\uf119", "\uf5b4"],
            offset: true,
            position: "left",
            stack: "demo",
            stackWeight: 1,
            ticks: {
              font: {
                family: '"Font Awesome 5 Free"',
                size: 14,
              },
              color: "#4663ac",
            },
          },
        },
        plugins: {
          title: {
            display: false,
            text: "Mood Tracking",
            font: {
              size: 25,
            },
            padding: {
              top: 10,
              bottom: 30,
            },
          },
          legend: {
            display: false,
            // position: "right",
            // labels: {
            //   fontColor: "#000",
            // },
          },
          layout: {
            padding: {
              left: 50,
              right: 0,
              bottom: 0,
              top: 0,
            },
          },
        },
      },
    });

    Object.seal(moodChartObject);
    this.moodChart = moodChartObject;

    ////////////////////////////////////////////////
    // DIARY CHART
    ////////////////////////////////////////////////

    let diariesChartObject = new Chart(diariesChartCanvas, {
      type: "bar", // horizontal bar, pie, line, doughnut, radar, polarArea
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [
          {
            label: "Diaries Submitted",
            data: [617594, 181045, 153060, 106519, 105162, 95072, 2345],
            backgroundColor: "#5BBAE8",

            borderWidth: 0,
            borderColor: "#777",
            hoverBorderWidth: 3,
            hoverBorderColor: "#000",
          },
        ],
      },
      options: {
        scales: {
          y: {
            min: 0,
            suggestedMax: 5,
            ticks: {
              stepSize: 1,
            },
          },
        },
        plugins: {
          title: {
            display: false,
            text: "Custom Chart Title",
            font: {
              size: 25,
            },
            padding: {
              top: 10,
              bottom: 30,
            },
          },
          legend: {
            display: false,
            position: "bottom",
            labels: {
              fontColor: "#000",
            },
          },
          layout: {
            padding: {
              left: 50,
              right: 0,
              bottom: 0,
              top: 0,
            },
          },
        },
      },
    });

    Object.seal(diariesChartObject);
    this.diariesChart = diariesChartObject;

    this.fetchDiaryData();
    this.fetchMoodData();
  },
  methods: {
    async initStatistics() {},
    setIndex(action) {
      if (action == "back") {
        this.index++;
      } else {
        if (this.index > 0) {
          this.index--;
        }
      }

      if (this.selectedTab == "diaries") {
        this.updateDiariesChart();
      } else {
        this.updateMoodChart();
      }
      console.log("index: " + this.index);
    },
    fetchMoodData() {
      var moods = ["\uf585", "\uf118", "\uf11a", "\uf119", "\uf5b4"];
      return new Promise((resolve, reject) => {
        axios
          .get(
            `/api/v1/diary-mood-list/${this.$route.params.aquarium_id}/${this.moodChartRange}/${this.index}`
          )
          .then((response) => {
            var result = [];
            for (var value of Object.values(response.data.results)) {
              result.push(moods[moods.length - Math.round(value)]);
            }

            this.moodChart.data.datasets[0].data = result;

            // this.moodChart.data.datasets[0].data = Object.values(
            //   response.data.results
            // );

            this.moodChart.data.labels = Object.keys(response.data.results);

            // SET CHART INDEX
            if (response.data.flag) {
              this.indexFreeze = true;
            } else {
              this.indexFreeze = false;
            }

            resolve(response);
          }),
          (error) => {
            reject(error);
          };
      });
    },
    fetchDiaryData() {
      return new Promise((resolve, reject) => {
        axios
          .get(
            `/api/v1/diary-count-list/${this.$route.params.aquarium_id}/${this.diariesChartRange}/${this.index}`
          )
          .then((response) => {
            // SET CHART LABEL DATA

            this.diariesChart.data.datasets[0].data = Object.values(
              response.data.results
            );
            this.diariesChart.data.labels = Object.keys(response.data.results);

            // SET CHART INDEX
            if (response.data.flag) {
              this.indexFreeze = true;
            } else {
              this.indexFreeze = false;
            }

            resolve(response);
          }),
          (error) => {
            reject(error);
          };
      });
    },
    changeSelectedTab(tab) {
      this.indexFreeze = false;
      this.index = 0;
      this.selectedTab = tab;
      console.log(this.selectedTab);
    },

    // UPDATE CHART.JS
    async updateMoodChart() {
      this.moodChart.data.labels = [];
      this.moodChart.data.datasets[0].data = [];

      this.fetchMoodData().then(
        (response) => {
          this.moodChart.update();
        },
        (error) => {
          console.log(error);
        }
      );
    },

    async updateDiariesChart() {
      this.diariesChart.data.labels = [];
      this.diariesChart.data.datasets[0].data = [];

      this.fetchDiaryData().then(
        (response) => {
          this.diariesChart.update();
        },
        (error) => {
          console.log(error);
        }
      );
    },
  },
};
</script>
<style scoped>
#diariesChart {
  width: 100%;
  height: 100%;
}

.chart-section {
  background-color: white;
  /* padding: 1rem; */
}

.form-select {
  width: 30%;
  display: block;
}
</style>
