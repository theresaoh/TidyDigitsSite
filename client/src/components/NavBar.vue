<template>
  <header id="header">
    <router-link to="/"><img id="logo" src="../../src/assets/logo.png"></router-link>
    <div class="navbar" id="navbar">
      <span class="dropbtn"><router-link to="/">Home</router-link></span>
      <div class="dropdown">
        <router-link to="/products">All Products &#x25BC;</router-link>
        <div class="dropdown-content">
          <router-link to="/product1">Product 1</router-link>
          <router-link to="/product2">Product 2</router-link>
          <router-link to="/product3">Product 3</router-link>
          <router-link to="/product4">Product 4</router-link>
          <router-link to="/product5">Product 5</router-link>
          <router-link to="/product6">Product 6</router-link>
          <router-link to="/product7">Product 7</router-link>
          <router-link to="/product8">Product 8</router-link>
          <router-link to="/product9">Product 9</router-link>
          <router-link to="/product10">Product 10</router-link>
        </div>
      </div>
    </div>
  </header>
</template>
<script>

export default {
  name: 'NavBar',
  data() {
    return {
      lastScrollPosition: 0
      }
    },
    methods: {
      onScroll () {
        const header = document.getElementById('header');
        const logo = document.getElementById('logo');
        const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop;
        if (currentScrollPosition >= 170) {
          let classList = header.classList;
          while (classList.length > 0) {
            classList.remove(classList.item(0));
          }
        // logo.style.transform = "scale(0.5)";
        header.classList.add('backtotop');
        }
        if (currentScrollPosition <= 171) {
          let classList = header.classList;
          while (classList.length > 0) {
            classList.remove(classList.item(0));
          }
        // logo.style.transform = "scale(1.0)";
        header.classList.add('scrolldown');
          }
        this.lastScrollPosition = currentScrollPosition
        }
      },
    mounted() {
      window.addEventListener('scroll', this.onScroll)
    },
    beforeDestroy() {
      window.removeEventListener('scroll', this.onScroll)
    }
  }
</script>

<style>
header {
  top: 0;
  z-index: 10;
  padding: 10px 0;
  width: 100%;
  position: fixed;
  display: block;
  background-color: rgb(44, 62, 80, 0.2);
  transition: background-color 600ms linear;
}

#logo {
  border-radius: 25px;
}

.navbar {
  overflow: hidden;
  margin: 0 20%;
  border-bottom: 1px white solid;
  transition: 0.4s;
  display: flex;
  justify-content: space-around;
  color: rgb(44, 62, 80);
}

.navbar a {
  float: left;
  font-size: 16px;
  color: #F5F5F5;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;  
  border: none;
  outline: none;
  padding: 14px 16px;
  background-color: rgb(44, 62, 80);
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: rgb(44, 62, 80);
  border-radius: 3px;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: white;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: rgb(44, 62, 80);
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: rgb(44, 62, 80);
  color: white;
}

.dropdown:hover .dropdown-content {
  display: block;
  margin-top: 50px;
  background-color: white;
  color: rgb(44, 62, 80);
}

.scrolldown {
  background-color: rgb(44, 62, 80, 0.2);
}

.backtotop {
  background-color: rgb(44, 62, 80, 0.9);
}
</style>
