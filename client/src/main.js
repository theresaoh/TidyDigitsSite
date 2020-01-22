import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Home from './components/Home.vue'
import Products from './components/Products.vue'
import ProductOverview from './components/ProductOverview.vue'
// import VueAnalytics from 'vue-analytics';

// Vue.use(VueAnalytics, {
//   id: "",
//   router
// });

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: "/", component: Home },
    { path: "/products", component: Products},
    { path: "/product-overview", component: ProductOverview},
    { path: "/product1", 
      component: Products, 
    props: {productName: "Product 1", content: false} },
    { path: "/product2", 
      component: Products, 
    props: {productName: "Product 2", content: false} },
    { path: "/product3", 
      component: Products, 
    props: {productName: "Product 3", content: false} },
    { path: "/product4", 
      component: Products, 
    props: {productName: "Product 4", content: false} },
    { path: "/product5", 
      component: Products, 
    props: {productName: "Product 5", content: false} },
    { path: "/product6", 
      component: Products, 
    props: {productName: "Product 6", content: false} },
    { path: "/product7", 
      component: Products, 
    props: {productName: "Product 7", content: false} },
    { path: "/product8", 
      component: Products, 
    props: {productName: "Product 8", content: false} },
    { path: "/product9", 
      component: Products, 
    props: {productName: "Product 9", content: false} },
    { path: "/product10", 
      component: Products, 
    props: {productName: "Product 10", content: false} },
  ]
});

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
