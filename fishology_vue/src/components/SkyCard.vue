<template>
  <div class="card h-100">
    <img :src="sky.image" class="card-img-top" alt="" />
    <div class="card-body">
      <h5 class="card-title">{{ sky.name }}</h5>
      <h6 class="card-text text-muted small">
        {{ sky.description }}
      </h6>
    </div>
    <div class="card-footer">
      <div class="progress">
        <div
          :class="[
            this.getTotalDiary >= sky.price ? 'bg-info' : 'bg-warning',
            'progress-bar',
            'progress-bar-striped',
          ]"
          role="progressbar"
          :style="`width: ${
            this.getTotalDiary >= sky.price ? 100 : this.getProgress(sky.price)
          }%`"
          aria-valuenow="75"
          aria-valuemin="0"
          aria-valuemax="100"></div>
      </div>
      <h6 class="small mt-2 text-muted text-center">
        {{
          this.getTotalDiary >= sky.price
            ? sky.price
            : this.getTotalDiary + " / " + sky.price
        }}
        <i class="fas fa-fish"></i>
      </h6>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "SkyCard",
  computed: {
    ...mapGetters(["getTotalDiary"]),
  },
  methods: {
    getProgress(fishPrice) {
      return ((this.getTotalDiary / fishPrice) * 100).toFixed(2);
    },
  },
  props: {
    sky: Object,
  },
  mounted() {
    console.log(this.sky);
  },
};
</script>
<style scoped>
.card {
  background: rgba(254, 254, 250, 0.7);
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
</style>
