// 1. Define route components.
// These can be imported from other files
//const About = { template: "<div>About</div>" };
import Home from "../src/views/Home.vue";
import About from "../src/views/About.vue";
import { createRouter, createWebHistory } from "vue-router";
// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
  { path: "/", component: Home },
  { path: "/about", component: About },
];

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
export default createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHistory(),
  routes, // short for `routes: routes`
});
