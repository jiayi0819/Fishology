<template>
  <div
    class="offcanvas offcanvas-start"
    tabindex="-1"
    id="offcanvasExample"
    aria-labelledby="offcanvasExampleLabel">
    <div class="offcanvas-header">
      <h3 class="light-blue" v-if="this.isAquarium">
        {{ this.aquarium.name }}
      </h3>
      <!-- <i class="fa-solid fa-water"></i> -->
      <button
        type="button"
        class="btn-close text-reset flex-end"
        data-bs-dismiss="offcanvas"
        aria-label="Close"></button>
    </div>
    <div class="offcanvas-body">
      <div class="light-blue m-2" v-if="this.isAquarium">
        <p class="light-blue">Total Fish <i class="fas fa-fish"></i></p>
        <h3 class="f-primary">{{ this.aquarium.get_total_fish }}</h3>
      </div>
      <!-- <ul class="nav flex-column"> -->
      <ul class="nav flex-column">
        <li class="nav-item">
          <span class="d-flex flex-row align-items-center">
            <i class="fa-solid fa-grid-2-plus"></i>
            <a
              @click="this.navigateTo('aquariums')"
              data-bs-dismiss="offcanvas"
              class="nav-link active">
              My Aquariums
            </a>
          </span>
        </li>
        <li class="nav-item" v-if="this.isAquarium">
          <span class="d-flex flex-row align-items-center">
            <i class="fas fa-book-open"></i>
            <a
              class="nav-link"
              @click="this.openModal('catalogueModal')"
              data-bs-dismiss="offcanvas">
              Catalogue
            </a>
          </span>
        </li>
        <li class="nav-item" v-if="this.isAquarium">
          <span class="d-flex flex-row align-items-center">
            <i class="fas fa-chart-area"></i>
            <a
              class="nav-link"
              @click="this.openModal('statisticsModal')"
              data-bs-dismiss="offcanvas">
              Statistics
            </a>
          </span>
        </li>
        <li class="nav-item" v-if="this.isAquarium">
          <span class="d-flex flex-row align-items-center">
            <i class="fas fa-filter"></i>
            <a
              class="nav-link"
              @click="this.openModal('filterModal')"
              data-bs-dismiss="offcanvas">
              Filter
            </a>
          </span>
        </li>
        <li class="nav-item" v-if="this.isAquarium">
          <span class="d-flex flex-row align-items-center">
            <i class="fas fa-gear"></i>
            <a
              class="nav-link"
              @click="this.openModal('editAquariumModal')"
              data-bs-dismiss="offcanvas">
              Aquarium Setting
            </a>
          </span>
        </li>
        <li class="nav-item">
          <span class="d-flex flex-row align-items-center">
            <i class="fa-solid fa-user-gear"></i>
            <a
              data-bs-dismiss="offcanvas"
              @click="this.navigateTo('account')"
              class="nav-link">
              Account Setting
            </a>
          </span>
        </li>
        <li class="nav-item" v-if="this.isAquarium">
          <span class="d-flex flex-row align-items-center">
            <i class="fa-solid fa-music"></i>
            <a class="form-check-label nav-link" for="flexSwitchCheckDefault"
              >Background Music
            </a>
            <div class="form-check form-switch">
              <input
                @change="this.musicControl(event)"
                v-model="this.bgm"
                class="form-check-input"
                type="checkbox"
                role="switch"
                id="flexSwitchCheckDefault" />
            </div>
          </span>
        </li>
      </ul>
    </div>
    <div class="offcanvas-footer" :key="this.$store.state.username">
      <div class="d-flex align-items-center">
        <!-- <template @click="signOut()" v-if="$store.state.isAuthenticated"> -->
        <span class="me-auto d-flex flex-row align-items-center">
          <i class="fa-solid fa-user fa-lg light me-3"></i>
          <span>
            <h6 class="light f-primary mb-0">{{ this.getUser.username }}</h6>
            <p class="light small">{{ this.getUser.email }}</p>
            <!-- <p class="light" v-if="this.isAquarium">
              <i class="fa-solid fa-water"></i> {{ this.aquarium.name }}
            </p> -->
          </span>
        </span>
        <button
          @click="signOut()"
          data-bs-dismiss="offcanvas"
          class="btn btn-light flex-end">
          Logout
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { mapGetters, mapActions, mapState } from "vuex";

export default {
  name: Navigation,
  computed: {
    ...mapGetters([
      "getCurrentAquarium",
      "getAquarium",
      "getUsername",
      "getUser",
    ]),
    isAquarium() {
      return this.$route.name === "aquarium";
    },
  },
  data() {
    return {
      aquarium: Object,
      bgm: false,
      radio: null,
    };
  },
  methods: {
    ...mapActions(["openModal", "fetchAquarium"]),
    musicControl() {
      if (this.bgm) {
        this.radio.play();
      } else {
        this.radio.pause();
        this.radio.currentTime = 0;
      }
    },
    navigateTo(destination) {
      this.$router.push(`/${destination}`);
    },

    signOut() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");

      this.$store.commit("removeToken");

      this.$router.push("/");
    },
  },
  async mounted() {
    this.fetchAquarium(this.$route.params.aquarium_id).then((resolve) => {
      this.aquarium = resolve;
    });

    this.radio = new Audio("http://127.0.0.1:8000/media/bgm/TheFish.mp3");
    this.radio.loop = true;
  },
};
</script>
<style lang="scss" scoped>
.offcanvas {
  background: rgba(238, 249, 255, 1);
  box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.25);
}

.offcanvas-footer {
  padding: 24px;
  background: #5bbae8;
  color: white;
}

.offcanvas-body,
.body-header {
  padding: 0;
}

a,
a:link,
a:visited {
  // text-decoration: none !important;
  color: #5bbae8;

  &:hover {
    color: white;
  }
}

.nav-item {
  padding: 1rem 1rem;
  border-top: 1px solid #5ab8e780;
  color: #5bbae8 !important;
  font-family: Readex Pro;
  transition: 0.25s all ease-in-out;

  &:hover {
    color: white !important;
    background-color: #9edfff !important;
  }

  @media (min-width: 768px) {
    // padding: 1rem 0.5rem;
  }

  // &:hover {
  //   // color: rgb(238, 249, 255);
  //   // background-color: #5ab8e780;
  //   background-color: rgb(238, 249, 255);
  //   border-color: #5ab8e780;
  // }

  &:last-child {
    border-bottom: 1px solid #5ab8e780;
  }
}
</style>
