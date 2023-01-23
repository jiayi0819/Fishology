<template>
  <div class="card h-100">
    <img
      :src="
        this.getTotalDiary >= fish.price ? fish.get_image : fish.get_lock_image
      "
      class="card-img-top"
      alt="" />
    <div class="card-body">
      <h5 class="card-title light-blue f-primary">{{ fish.name }}</h5>
      <h6 class="card-text text-muted small">
        {{ fish.description }}
      </h6>
    </div>
    <div class="card-footer">
      <div class="progress">
        <div
          :class="[
            this.getTotalDiary >= fish.price ? 'bg-info' : 'bg-warning',
            'progress-bar',
            'progress-bar-striped',
          ]"
          role="progressbar"
          :style="`width: ${
            this.getTotalDiary >= fish.price
              ? 100
              : this.getProgress(fish.price)
          }%`"
          aria-valuenow="75"
          aria-valuemin="0"
          aria-valuemax="100"></div>
      </div>
      <h3 class="small mt-2 text-center dark-blue">
        {{
          this.getTotalDiary >= fish.price
            ? fish.price
            : this.getTotalDiary + " / " + fish.price
        }}
        <i class="fas fa-fish"></i>
      </h3>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "CatalogueCard",
  computed: {
    ...mapGetters(["getTotalDiary"]),
  },
  methods: {
    getProgress(fishPrice) {
      //   console.log(this.getTotalDiary / fishPrice);
      return ((this.getTotalDiary / fishPrice) * 100).toFixed(2);
      //   return 50;
    },
  },
  props: {
    fish: Object,
  },
};
</script>
<style scoped>
.card {
  background: rgba(254, 254, 250, 0.7);
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.card-body {
  max-height: 100%;
  overflow-y: auto;
}

.card-img-top {
  width: 100%;
  height: 15vw;
  object-fit: cover;
}
</style>
