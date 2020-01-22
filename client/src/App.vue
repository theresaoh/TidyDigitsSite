<template>
  <div id="app">
    <NavBar></NavBar>
    <ContactForm></ContactForm>
    <router-view></router-view>
  </div>
</template>
<script>
import NavBar from './components/NavBar.vue'
import Home from './components/Home.vue'
import Technology from './components/Technology.vue'
import Products from './components/Products.vue'
import ContactForm from './components/ContactForm.vue'
export default {
  name: 'app',
  components: {
    NavBar,
    Home,
    Technology,
    Products,
    ContactForm
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100vw;
  height: 100vh;
  position: relative;
}

button {  
  font-size: 16px;  
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: #532d9d;
  opacity: 0.8;
  font-family: inherit;
  margin: 0;
  }

button:hover {
  opacity: 1;
}

</style>
