import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

// import { quillEditor, Quill } from "vue3-quill";
window.bootstrap = require("bootstrap/dist/js/bootstrap.bundle.js");

axios.defaults.baseURL = "http://127.0.1:8000";

createApp(App).use(store).use(router, axios).mount("#app");
