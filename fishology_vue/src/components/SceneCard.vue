<template>
  <div class="card h-100">
    <img :src="scene.image" class="card-img-top" alt="" />
    <div class="card-body">
      <h5 class="card-title">{{ scene.name }}</h5>
      <h6 class="card-text text-muted small">
        {{ scene.description }}
      </h6>
    </div>
    <div class="card-footer">
      <div class="progress">
        <div
          :class="[
            this.getTotalDiary >= scene.price ? 'bg-info' : 'bg-warning',
            'progress-bar',
            'progress-bar-striped',
          ]"
          role="progressbar"
          :style="`width: ${
            this.getTotalDiary >= scene.price
              ? 100
              : this.getProgress(scene.price)
          }%`"
          aria-valuenow="75"
          aria-valuemin="0"
          aria-valuemax="100"></div>
      </div>
      <h6 class="small mt-2 text-muted text-center">
        {{
          this.getTotalDiary >= scene.price
            ? scene.price
            : this.getTotalDiary + " / " + scene.price
        }}
        <i class="fas fa-fish"></i>
      </h6>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "SceneCard",
  computed: {
    ...mapGetters(["getTotalDiary"]),
  },
  methods: {
    getProgress(fishPrice) {
      return ((this.getTotalDiary / fishPrice) * 100).toFixed(2);
    },
  },
  props: {
    scene: Object,
  },
};
</script>
<style scoped>
.card {
  background: rgba(254, 254, 250, 0.7);
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
</style>
