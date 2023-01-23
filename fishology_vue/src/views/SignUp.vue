<template>
  <div class="form-wrap">
    <form class="account-form" @submit.prevent="submitForm">
      <!-- TITLE SECTION -->
      <p>
        Already have an account?
        <router-link class="router-link" to="/sign-in">Sign In</router-link>
      </p>
      <h1 class="display-6">Start swimming your memories today!</h1>

      <div class="inputs m-3">
        <!-- USERNAME -->

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

        <!-- EMAIL -->

        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">
            <i class="fa fa-envelope" aria-hidden="true" />
          </span>
          <input
            type="text"
            class="form-control"
            placeholder="E-mail"
            v-model="email" />
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

        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">
            <i class="fa fa-lock" aria-hidden="true" />
          </span>
          <input
            type="password"
            class="form-control"
            placeholder="Repeat Password"
            v-model="password2" />
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

      <button type="submit" class="btn btn-primary">Sign Up!</button>

      <div class="angle"></div>
    </form>

    <div class="background"></div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      this.errors = [];

      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.email === "") {
        this.errors.push("The email is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }
      if (this.password !== this.password2) {
        this.errors.push("The passwords doesn't match");
      }

      if (!this.errors.length) {
        const registerInfo = {
          username: this.username,
          email: this.email,
          password: this.password,
        };

        axios
          .post("/api/v1/users/", registerInfo)
          .then((response) => {
            console.log("Account created. Please log in!");
            this.$router.push("/sign-in");
          })
          .catch((error) => {
            if (error.response) {
              console.log(error.response);
              for (const property in error.response.data) {
                this.errors.push(
                  // `${property}:${error.response.data[property]}`
                  `${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again.");
            }
          });
      }
    },
  },
};
</script>

<style lang="scss">
.form-wrap {
  overflow: hidden;
  display: flex;
  height: 80vh;
  margin: 0 auto;
  width: 100%;
  text-align: center;

  @media (min-width: 900px) {
    width: 100%;
  }
}

.account-form {
  // form {
  padding: 0 10px;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex: 1;

  @media (min-width: 900px) {
    padding: 0 50px;
  }
}

.angle {
  display: none;
  position: absolute;
  background-color: rgb(238, 249, 255) !important;
  transform: rotateZ(3deg);
  width: 60px;
  right: -30px;
  height: 101%;

  @media (min-width: 900px) {
    display: initial;
  }
}

.background {
  display: none;
  flex: 2;
  background-size: cover;
  background-image: url("https://images.unsplash.com/photo-1573350926865-cf0d512fd504?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80");
  width: 100%;
  height: 100%;

  @media (min-width: 900px) {
    display: initial;
  }
}
</style>
