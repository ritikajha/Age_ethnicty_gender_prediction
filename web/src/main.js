import Vue from 'vue'
import vuetify from './plugins/vuetify'
import App from './App.vue'
import store from './store'
import router from './router'
import Toasted from 'vue-toasted';
Vue.config.productionTip = false

Vue.use(Toasted)
new Vue({
  vuetify,
  router,
  store,
  render: h => h(App),
}).$mount('#app')
