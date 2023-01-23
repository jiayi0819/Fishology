import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Account from "../views/Account.vue";
import Aquarium from "../views/Aquarium.vue";
import Aquariums from "../views/Aquariums.vue";
import SignUp from "../views/SignUp.vue";
import SignIn from "../views/SignIn.vue";

import store from "../store/index";

console.log("The store is ");
console.log(store.state.isAuthenticated);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
    meta: {
      title: "Home",
      requiresAuth: false,
    },
  },
  {
    path: "/account",
    name: "account",
    component: Account,
    meta: {
      title: "Account",
      requiresAuth: true,
    },
  },
  {
    path: "/aquariums",
    name: "aquariums",
    component: Aquariums,
    meta: {
      title: "Aquariums",
      requiresAuth: true,
    },
  },
  {
    path: "/:aquarium_id/",
    name: "aquarium",
    component: Aquarium,
    meta: {
      title: "Aquarium",
      requiresAuth: true,
    },
  },
  {
    path: "/sign-up",
    name: "sign-up",
    component: SignUp,
    meta: {
      title: "Sign Up",
      requiresAuth: false,
    },
  },
  {
    path: "/sign-in",
    name: "sign-in",
    component: SignIn,
    meta: {
      title: "Sign In",
      requiresAuth: false,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !store.state.isAuthenticated) {
    console.log("motherfucker!!!");

    next("sign-in");
    // router.push({
    //   path: "/sign-in",
    //   name: "aquariums",
    //   component: Aquariums,
    // });
  } else {
    document.title = `${to.meta.title} | Fishology 🐟`;
    next();
  }

  // if (to.meta.requiresAuth && !auth.isLoggedIn()) {
  //   console.log("motherfucker!!!");
  //   // return {
  //   //   path: "/sign-in",
  //   //   // save the location we were at to come back later
  //   //   query: { redirect: to.fullPath },
  //   // };
  // }
});

export default router;
