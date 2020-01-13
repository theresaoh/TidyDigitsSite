<template>
  <div id="app">
    <NavBar></NavBar>
    <ContactForm></ContactForm>
    <span class="img"></span>
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
.img {
  display: block;
  z-index: 1;
  width: 100vw;
  height: 100vh;
  background-image: url("https://img.wallpapersafari.com/desktop/1920/1080/57/70/gKDlOv.jpg");
  background-repeat: no-repeat;
  background-size: 100vw 100vh
}

.component {
  margin: 0 20%;
}

</style>
