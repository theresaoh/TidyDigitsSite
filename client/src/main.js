import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Home from './components/Home.vue'
import Products from './components/Products.vue'
import Technology from './components/Technology.vue'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: "/", component: Home },
    { path: "/products", component: Products},
    { path: "/technology", component: Technology}
  ]
});

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
