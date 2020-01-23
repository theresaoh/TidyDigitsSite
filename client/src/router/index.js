import Vue from 'vue'
import Router from 'vue-router'
// import VueAnalytics from 'vue-analytics';

// Vue.use(VueAnalytics, {
//   id: "",
//   router
// });

const routerOptions = [
    { path: "/", component: 'Home' },
    { path: "/products", component: 'Products'},
    { path: "/product1", 
      component: 'Products', 
    props: {productName: "Product 1", content: false} },
    { path: "/product2", 
      component: 'Products', 
    props: {productName: "Product 2", content: false} },
    { path: "/product3", 
      component: 'Products', 
    props: {productName: "Product 3", content: false} },
    { path: "/product4", 
      component: 'Products', 
    props: {productName: "Product 4", content: false} },
    { path: "/product5", 
      component: 'Products', 
    props: {productName: "Product 5", content: false} },
    { path: "/product6", 
      component: 'Products', 
    props: {productName: "Product 6", content: false} },
    { path: "/product7", 
      component: 'Products', 
    props: {productName: "Product 7", content: false} },
    { path: "/product8", 
      component: 'Products', 
    props: {productName: "Product 8", content: false} },
    { path: "/product9", 
      component: 'Products', 
    props: {productName: "Product 9", content: false} },
    { path: "/product10", 
      component: 'Products', 
    props: {productName: "Product 10", content: false} },
  ];

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

const router = new Router({
  routes,
  mode: 'history'
})

export default router;