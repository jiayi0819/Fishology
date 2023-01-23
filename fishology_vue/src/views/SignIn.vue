<template>
  <div class="form-wrap">
    <form class="account-form" @submit.prevent="submitForm">
      <!-- TITLE SECTION -->
      <p>
        Don't have an account?
        <router-link class="router-link" to="/sign-up">Sign Up</router-link>
      </p>
      <h1 class="display-6">How's your day?</h1>

      <div class="inputs m-3">
        <!-- EMAIL -->

        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">
            <i class="fa fa-user" aria-hidden="true" />
          </span>
          <input
            type="text"
            class="form-control"
            placeholder="Username"
            v-model="username" />
        </div>

        <!-- PASSWORD -->

        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">
            <i class="fa fa-lock" aria-hidden="true" />
          </span>
          <input
            type="password"
            class="form-control"
            placeholder="Password"
            v-model="password" />
        </div>

        <div v-show="errors" class="error">
          <!-- <ul>
            <li v-for="(error, index) in errors" :key="index" class="text-danger">
              <small>{{ error }}</small>z
            </li>
          </ul> -->
          <small
            v-for="(error, index) in errors"
            :key="index"
            class="text-danger">
            {{ error }}<br />
          </small>
        </div>
      </div>

      <button type="submit" class="btn btn-primary">Sign In!</button>

      <div class="angle"></div>
    </form>

    <div class="background"></div>
  </div>
</template>

<script>
import axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "SignIn",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  methods: {
    ...mapActions(["fetchAquariums", "updateEditAquarium"]),
    getUser() {
      axios
        .get(`/api/v1/users/${this.username}/`)
        .then((response) => {
          this.$store.state.user = response.data;
        })
        .catch((error) => {
          console.log("Can't fetch user info");
        });
    },
    signIn(userInfo) {
      axios
        .post("/api/v1/token/login/", userInfo)
        .then((response) => {
          const token = response.data.auth_token;

          localStorage.setItem("token", token);
          localStorage.setItem("username", this.username);
          axios.defaults.headers.common["Authorization"] = "Token " + token;

          this.$store.commit("setToken", token);
          this.$store.state.username = localStorage.getItem("username");

          this.fetchAquariums();

          this.$router.push("/aquariums");
        })
        .catch((error) => {
          console.log("motherfucker");
          this.errors.push("Wrong username or password. Please try again.");
          // if (error.response) {
          //   for (const property in error.response.data) {
          //     this.errors.push(`${error.response.data[property]}`);
          //   }
          // } else if (error.message) {
          //   this.errors.push("Something went wrong. Please try again");
          //   console.log(JSON.stringify(error));
          // }
        });
    },
    async submitForm() {
      this.errors = [];

      if (this.username === "") {
        this.errors.push("Please enter your username.");
      }
      if (this.password === "") {
        this.errors.push("Please enter your password.");
      }

      if (!this.errors.length) {
        axios.defaults.headers.common["Authorization"] = "";
        localStorage.removeItem("token");
        localStorage.removeItem("username");

        const userInfo = {
          username: this.username,
          password: this.password,
        };
        this.$store.state.loading = true;
        Promise.all([this.signIn(userInfo), this.getUser()]).then(
          (response) => {
            // this.fetchAquariums();
            if (!this.errors.length) {
              // this.$router.push("/aquariums");
            }
            this.$store.state.loading = false;
          },
          (error) => {
            console.log("Shit Happened during Sign In" + error);
          }
        );
      }
    },
  },
};
</script>
