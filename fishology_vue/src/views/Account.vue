<template>
  <div class="form-wrap">
    <form class="account-form" @submit.prevent="submitForm">
      <h1 class="display-6 light-blue">Account Setting</h1>
      <div class="inputs m-3">
        <!-- USERNAME -->

        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">
            <i class="fa fa-user" aria-hidden="true" />
          </span>
          <input
            type="text"
            class="form-control"
            placeholder="username"
            v-model="user.username" />
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
            v-model="user.email" />
        </div>

        <!-- BIO  -->

        <div class="input-group mb-3">
          <span class="input-group-text">
            <i class="fa-regular fa-face-smile"></i>
          </span>
          <textarea
            class="form-control"
            aria-label="With textarea"
            placeholder="Introduce yourself..."
            v-model="user.bio"></textarea>
        </div>

        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1"
            ><i class="fa fa-birthday-cake" aria-hidden="true"></i
          ></span>
          <input v-model="user.birthday" class="form-control" type="date" />
        </div>

        <!-- <div class="input-group mb-3">
          <input type="file" class="form-control" id="inputGroupFile02" />
          <label class="input-group-text" for="inputGroupFile02"
            >Upload Avatar</label
          >
        </div> -->
      </div>

      <div v-show="errors" class="error text-center">
        <small
          v-for="(error, index) in errors"
          :key="index"
          class="text-danger">
          {{ error }}<br />
        </small>
      </div>

      <button type="submit" class="btn btn-primary">Submit!</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Account",
  data() {
    return {
      user: {
        username: "",
        email: "",
        bio: "",
        birthday: "",
        image: "",
      },
      errors: [],
    };
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.user.username,
        email: this.user.email,
        bio: this.user.bio,
        birthday: this.user.birthday,
        image: "",
      };

      // console.log(formData);

      axios
        .post("/api/v1/update-user/", formData)
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          // console.log(error);
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
            console.log(JSON.stringify(error.response.data));
          } else if (error.message) {
            this.errors.push("Something went wrong. Please try again");
          }
        });
    },
  },
  async mounted() {
    await axios
      .get(`/api/v1/users/${localStorage.getItem("username")}`)
      .then((response) => {
        this.user = response.data;
        console.log(this.user);
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style>
textarea {
  resize: none;
}
.input-group-text {
  background-color: #5bbae8 !important;
  color: white !important;
  border-color: #5bbae8 !important;
  /* box-shadow: inset -3px -4px 3px rgba(0, 0, 0, 0.25); */
}
</style>
