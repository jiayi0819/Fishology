<template>
  <div class="card h-100">
    <!-- <img :src="aquarium.get_image" class="card-img-top" alt="" /> -->
    <div class="card-header">
      <h5
        @click="this.openAquarium(aquarium.get_absolute_url)"
        class="card-title light-blue f-primary text-center">
        {{ aquarium.name }}
      </h5>
    </div>
    <div class="card-body">
      <!-- AQUARIUM LINK -->

      <div>
        <span class="d-flex justify-content-between align-items-center">
          <!-- <i
            data-bs-toggle="collapse"
            href="#aquariumInfo"
            class="fa-regular fa-circle-caret-down light-blue"></i> -->
        </span>
        <div class="collapse" id="aquariumInfo"></div>

        <h6 class="f-primary text-center card-text dark-blue">
          {{ aquarium.get_total_fish }} <i class="fas fa-fish"></i>
        </h6>

        <p class="card-text text-center">
          <small>
            {{ aquarium.description }}
          </small>
        </p>
        <hr />
        <div class="mb-0">
          <p class="card-text">
            <small>
              <i class="fa-fw fa-duotone fa-cake-candles me-1 light-blue"></i>
              Created:
              {{ this.formatDateFull(aquarium.created) }}
            </small>
          </p>
          <p class="card-text">
            <small>
              <i class="fa-fw fa-duotone fa-users me-1 light-blue"></i>
              Participants:
              {{ aquarium.participants.length + 1 }}
            </small>
          </p>
        </div>
      </div>
    </div>
    <div class="card-footer">
      <div class="row">
        <small class="col-9 text-muted ps-2"
          >Last updated {{ this.formatDate(aquarium.updated) }} ago</small
        >
        <div class="col-3 icons align-items-center pe-2">
          <div
            class="icon dark-blue me-1"
            @click="$emit('set-aquarium', aquarium)">
            <i class="fa fa-pencil" aria-hidden="true"></i>
          </div>
          <div class="icon dark-blue" @click="deleteAquarium">
            <i class="fa fa-trash" aria-hidden="true"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import { mapActions } from "vuex";

export default {
  name: "AquariumCard",
  props: {
    aquarium: Object,
  },
  methods: {
    ...mapActions(["setCurrentAquarium"]),
    formatDate(value) {
      if (value) {
        return moment(String(value)).fromNow();
      }
    },
    formatDateFull(value) {
      return moment(value).format("DD/MM/YYYY");
    },
    openAquarium(url) {
      this.$router.push(url);
    },
    deleteAquarium() {
      let message = "Are you sure you want to delete this aquarium?";

      if (confirm(message)) {
        axios
          .delete(`/api/v1/update-aquarium/${this.aquarium.id}/`, this.aquarium)
          .then((response) => {
            console.log("Successfully deleted aquarium!");
            this.$emit("aquarium-changed");
          })
          .catch((error) => {
            // console.log(error);
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
    },
  },
};
</script>

<style lang="scss" scoped>
.card-header {
  // background-color: #5bbae8
}

.icons {
  display: flex;
  flex-direction: row;
  justify-content: right;
}
.card {
  background: rgba(254, 254, 250, 0.7);
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.fa-pencil,
.fa-trash,
.fa-circle-caret-down {
  transition: all 0.5s;
  padding: 0.4rem;
  border-radius: 50%;

  &:hover {
    background-color: rgb(213, 213, 213);
  }
}
</style>
