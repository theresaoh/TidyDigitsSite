<template>
  <div id="app">
    <NavBar></NavBar>
    <ContactForm></ContactForm>
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>
<script>
import NavBar from './components/NavBar.vue'
import ContactForm from './components/ContactForm.vue'
import Footer from './components/Footer.vue'
export default {
  name: 'app',
  components: {
    NavBar,
    ContactForm,
    Footer
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

.heading {
  font-size: 50px;
  letter-spacing: 3px;
  font-family: 'Montserrat', Helvetica, Arial, sans-serif;
  margin: 0 0 20px 0;
}
</style>
