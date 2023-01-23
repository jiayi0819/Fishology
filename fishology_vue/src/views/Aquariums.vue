<template>
  <div class="page container-fluid">
    <h1 class="light-blue mt-4">My Aquariums</h1>
    <p>All of your created or shared aquariums.</p>
    <hr />
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4">
      <div class="col" v-for="aquarium in this.getAquariums" :key="aquarium.id">
        <AquariumCard
          @aquarium-changed="this.fetchAquariums"
          @set-aquarium="this.setAquarium(aquarium)"
          :aquarium="aquarium" />
      </div>
      <div class="col">
        <!-- ADD AQUARIUM -->
        <div
          class="card h-100"
          data-bs-toggle="modal"
          data-bs-target="#aquariumModal">
          <div
            class="card-body d-flex align-items-center justify-content-center">
            <i class="fa-regular fa-circle-plus m-2"></i>
            <p class="card-text">Add Aquarium</p>
          </div>
        </div>
      </div>

      <!-- MODAL! -->
      <AquariumModal @aquarium-changed="this.fetchAquariums" />

      <EditAquarium
        @aquarium-changed="this.fetchAquariums"
        :aquarium="this.editAquarium" />
    </div>
  </div>
</template>

<script type="module">
import { mapActions, mapGetters } from "vuex";

import AquariumCard from "../components/AquariumCard.vue";
import AquariumModal from "../views/AquariumModal.vue";
import EditAquarium from "../views/EditAquarium.vue";

export default {
  name: "Aquariums",
  components: {
    AquariumModal,
    AquariumCard,
    EditAquarium,
  },
  computed: {
    ...mapGetters(["getAquariums"]),
  },
  data() {
    return {
      errors: [],
      editAquarium: Object,
      aquariumModal: null,
    };
  },
  mounted() {
    // this.$store.state.loading = true;
    this.fetchAquariums();
    this.editAquariumModal = new bootstrap.Modal(
      document.getElementById("editAquariumModal")
    );
  },
  methods: {
    ...mapActions(["fetchAquariums", "updateEditAquarium"]),

    setAquarium(aquarium) {
      this.editAquarium = aquarium;
      this.editAquariumModal.toggle();
      console.log("Set aquarium!");
    },
  },
};
</script>

<style lang="scss" scoped>
.page {
  width: 80%;
  max-width: 1440px;
}
</style>
