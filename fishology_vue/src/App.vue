<template>
  <div class="wrapper">
    <Loading v-show="isLoading" />
    <nav class="navbar navbar-expand-lg sticky-top navbar-light bg-light">
      <div class="content container-fluid">
        <!-- LOGO -->
        <router-link to="/" class="navbar-brand light-blue">
          <i class="fas fa-fish"></i><b class="ms-3 d-sm-inline">Fishology</b>
        </router-link>
        <!-- NAVBAR BUTTON -->

        <div>
          <div v-if="this.$store.state.isAuthenticated">
            <!-- <button
              :key="this.$store.state.username"
              class="btn btn-outline-success me-2">
              <img
                class="avatar"
                src="https://assets.petco.com/petco/image/upload/f_auto,q_auto/rabbit-care-sheet"
                alt="" />
              {{ this.getUsername }}
            </button> -->
            <button
              class="btn"
              type="button"
              data-bs-toggle="offcanvas"
              data-bs-target="#offcanvasExample"
              aria-controls="offcanvasExample">
              <span class="navbar-toggler-icon"></span>
            </button>
          </div>
          <div v-else>
            <router-link to="/sign-in" class="btn btn-primary">
              <i class="fas fa-user me-1"></i>
              Sign In / Up
            </router-link>
          </div>
        </div>
      </div>
    </nav>
    <Navigation :key="this.$route.params.aquarium_id" />
    <!-- <Navigation :key="this.$route.fullPath" /> -->
    <!-- <body> -->
    <router-view />
    <!-- </body> -->
  </div>
</template>

<script>
import axios from "axios";

import Navigation from "./components/Navigation.vue";
import Loading from "./components/Loading.vue";

import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["isLoading", "getUsername"]),
  },
  components: {
    Navigation,
    Loading,
  },

  beforeCreate() {
    this.$store.state.loading = true;
    this.$store.commit("initializeStore");

    const token = localStorage.getItem("token");
    console.log(token);

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
    this.$store.state.loading = false;
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;600;700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");

html,
body {
  margin: 0;
  padding: 0;
}

body {
  background-color: rgb(238, 249, 255) !important;
  height: 100%;
}

#three {
  position: fixed;
  top: 0;
  left: 0;
  outline: none;
}

.content {
  width: 100%;
}

.navbar {
  // opacity: 85%;
}

.avatar {
  object-fit: cover;
  width: 25px;
  height: 25px;
  border-radius: 50%;
}

///////////////////////////////////////////////
// ROOT STYLE
///////////////////////////////////////////////

b,
h1,
h2,
h3,
.f-primary {
  font-family: "Readex Pro";
  font-weight: 600 !important;
}

p,
a,
input {
  font-family: "Open Sans";
  color: #212325;
  margin: 0 !important;
}

textarea {
  resize: none !important;
}

// FONT COLOUR

.light {
  color: white;
}

.light-blue {
  color: #5bbae8 !important;
}

.dark-blue {
  color: #4663ac !important;
}

// BACKGROUND COLOUR

.bg-white {
  background-color: white;
}

.form-check-input:checked {
  background-color: #5bbae8 !important;
  border-color: #5bbae8 !important;
}

// BUTTONS
.btn,
a {
  text-decoration: none !important;
}

.btn-primary,
.btn-light,
.btn-red {
  font-family: "Readex Pro" !important;
  font-style: normal;
  font-weight: 400;
  font-size: 0.85rem !important;
  text-transform: uppercase;
  padding-top: 0.75rem !important;
  padding-bottom: 0.75rem !important;
  box-shadow: inset -3px -4px 3px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  border: none !important;
}

.btn-primary {
  background: #5bbae8 !important;
  transition: all 1s;

  &:hover {
    background: #71cffe !important;
  }

  &:active {
    background: #56a2c8 !important;
  }
}

.btn-light {
  background: rgba(225, 241, 253, 1) !important;
  color: #9b9b9b !important;
}

.btn-red {
  background: #eb5757 !important;
  color: rgba(238, 249, 255, 0.85) !important;
}

// PANEL

.modal-content {
  background-color: rgba(238, 249, 255, 0.9) !important;
  box-shadow: inset -3px -4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  padding: 1rem;

  .modal-title {
    color: #5bbae8;
  }

  .modal-body {
    // padding: 0 2rem 2rem;
  }
}

/* SCROLLBAR */

/* width */
::-webkit-scrollbar {
  width: 6px;
}

/* Track */
::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px white;
  border-radius: 10px;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #c8d9ed;
  /* box-shadow: inset 0 0 5px grey; */
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #4663ac;
}
</style>
