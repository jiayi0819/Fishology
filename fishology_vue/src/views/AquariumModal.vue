<template>
  <!-- Modal -->
  <div
    class="modal fade"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    id="aquariumModal"
    tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title" id="exampleModalLabel">Add Aquarium</h3>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"></button>
        </div>
        <form @submit.prevent="createAquarium">
          <div class="modal-body">
            <div class="inputs m-3">
              <div class="form-floating mb-3">
                <input
                  type="text"
                  v-model="aquarium.name"
                  class="form-control"
                  id="floatingInput"
                  placeholder="A Wonderful Aquarium" />
                <label for="floatingInput">Aquairum Name</label>
              </div>

              <div class="form-floating mb-3">
                <textarea
                  v-model="aquarium.description"
                  class="form-control"
                  placeholder="Introduce your aquarium!"
                  id="floatingTextarea2"
                  style="height: 100px"></textarea>
                <label for="floatingTextarea2">Aquarium Description</label>
              </div>

              <div class="form-text mb-1">
                Invite your friends to share the aquarium!
              </div>
              <ul class="list-group mb-3">
                <li
                  class="list-group-item d-flex flex-row justify-content-between align-items-center"
                  v-for="(participant, index) in this.aquarium.participants"
                  :key="index">
                  <p>{{ this.aquarium.participants[index] }}</p>
                  <i
                    @click="removeParticipant(index)"
                    class="fa-regular fa-circle-xmark text-danger"></i>
                </li>
                <li class="list-group-item" v-if="this.showInput">
                  <input
                    @blur="this.validateParticipant()"
                    v-model="this.newParticipant"
                    class="form-control no-border"
                    type="text" />
                </li>
                <li class="list-group-item text-center">
                  <i
                    @click="addParticipant"
                    class="fa-regular fa-circle-plus light-blue"></i>
                </li>
              </ul>

              <div
                class="form-check form-switch px-0 d-flex align-items-center">
                <input
                  class="form-check-input me-3"
                  type="checkbox"
                  id="flexSwitchCheckDefault" />
                <span>
                  <label class="form-check-label" for="flexSwitchCheckDefault"
                    >Private Aquarium
                  </label>
                  <div class="form-text mt-0">
                    Private aquarium will not be discovered by other users.
                  </div>
                </span>
              </div>
              <div v-show="errors" class="error text-center">
                <small
                  v-for="(error, index) in errors"
                  :key="index"
                  class="text-danger">
                  {{ error }}<br />
                </small>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal">
              Close
            </button>
            <button type="submit" class="btn btn-primary">Save Changes</button>
            <button
              type="button"
              id="close-modal"
              data-bs-dismiss="modal"
              style="display: none">
              Close
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "AquariumModal",
  data() {
    return {
      aquarium: {
        name: "",
        participants: [],
        description: "",
        image: "",
        isPrivate: false,
      },
      errors: [],
      newParticipant: "",
      showInput: false,
      aquariumModal: {},
    };
  },
  methods: {
    addParticipant() {
      this.showInput = true;
    },
    validateParticipant() {
      this.errors = [];
      if (this.newParticipant == "") {
        this.showInput = false;
      } else {
        axios
          .post(`/api/v1/search-user/${this.newParticipant}/`)
          .then((response) => {
            this.searchResults = response.data;
            console.log(this.searchResults);

            if (this.searchResults.length == 0) {
              this.errors.push("Username doesn't exist.");
            } else {
              this.aquarium.participants.push(this.newParticipant);
            }
            this.newParticipant = "";
            this.showInput = false;
          })
          .catch((error) => this.errors.push(error));
      }
    },
    createAquarium() {
      this.errors = [];
      if (this.aquarium.name === "") {
        this.errors.push("Please enter aquarium name.");
      }
      if (this.aquarium.description === "") {
        this.errors.push("Please enter aquarium description.");
      }
      if (!this.errors.length) {
        axios
          .post("/api/v1/create-aquarium/", this.aquarium)
          .then((response) => {
            console.log("Successfully added aquarium!");

            document.getElementById("close-modal").click();

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
<style scoped>
label {
  font-family: "Open Sans";
}
</style>
