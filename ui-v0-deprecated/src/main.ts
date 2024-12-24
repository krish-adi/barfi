import Vue from "vue";
import App from "./App.vue";

import { BaklavaVuePlugin } from "@baklavajs/plugin-renderer-vue";
import "./assets/styles.css";

Vue.use(BaklavaVuePlugin);

Vue.config.productionTip = false;
Vue.config.devtools = false;

Vue.prototype.log = console.log;

new Vue({
  render: (h) => h(App),
}).$mount("#app");
