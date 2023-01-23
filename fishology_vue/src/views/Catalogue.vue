<template>
  <!-- Modal -->
  <div class="modal fade" id="catalogueModal">
    <div class="modal-dialog modal-xl modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title">Catalogue</h3>
          <button
            @click="this.$store.state.modalOpened = false"
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body container-fluid">
          <ul class="nav nav-pills mb-3">
            <li class="nav-item">
              <h3
                :class="['nav-link', this.catalogue == 'fish' ? 'active' : '']"
                @click="this.catalogue = 'fish'">
                <i class="fas fa-fish"></i>
                Fish
              </h3>
            </li>
            <li class="nav-item">
              <h3
                :class="['nav-link', this.catalogue == 'theme' ? 'active' : '']"
                @click="this.catalogue = 'theme'">
                <i class="fa-regular fa-crystal-ball"></i>
                Theme
              </h3>
            </li>
            <li class="nav-item">
              <h3
                :class="['nav-link', this.catalogue == 'sky' ? 'active' : '']"
                @click="this.catalogue = 'sky'">
                <i class="fa-regular fa-clouds-sun"></i>
                Sky
              </h3>
            </li>
          </ul>
          <div class="container-fluid">
            <!-- FISH CATALOGUE -->
            <div
              v-if="this.catalogue == 'fish'"
              class="row row-cols-sm-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-4">
              <div class="col" v-for="fish in this.fishes" :key="fish.id">
                <FishCard :fish="fish" />
              </div>
            </div>

            <!-- CORAL CATALOGUE -->
            <div
              v-if="this.catalogue == 'theme'"
              class="row row-cols-sm-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-4">
              <div class="col" v-for="scene in this.scenes" :key="scene.name">
                <SceneCard
                  @click="this.$emit('change-scene', scene.folder)"
                  :scene="scene" />
              </div>
            </div>

            <!-- SKY CATALOGUE -->
            <div
              v-if="this.catalogue == 'sky'"
              class="row row-cols-sm-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-4">
              <div class="col" v-for="sky in this.skies" :key="sky.name">
                <!-- sky -->
                <SkyCard
                  @click="this.$emit('change-sky', sky.folder)"
                  :sky="sky" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import FishCard from "../components/FishCard.vue";
import SceneCard from "../components/SceneCard.vue";
import SkyCard from "../components/SkyCard.vue";

export default {
  name: "Catalogue",
  components: {
    FishCard,
    SceneCard,
    SkyCard,
  },
  computed: {
    ...mapGetters(["getAllFishes", "getScenes", "getSkies"]),
  },
  data() {
    return {
      fishes: [],
      scenes: [],
      skies: [],
      catalogue: "fish",
    };
  },
  mounted() {
    this.fishes = this.getAllFishes;
    this.scenes = this.getScenes;
    this.skies = this.getSkies;

    console.log("The skies are");
    console.log(this.skies);
  },
  methods: {},
};
</script>

<style lang="scss">
.nav-pills {
  .active {
    background-color: #5bbae8 !important;
    color: white;
  }
  .nav-link {
    text-decoration: none !important;
    color: #5bbae8;

    &:hover {
      color: rgb(59, 138, 192);
    }
  }
}
</style>
