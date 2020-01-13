<template>
  <header id="header">
    <router-link to="/"><img id="logo" src="../../src/assets/logo.png"></router-link>
    <div class="navbar" id="navbar">
      <span class="dropbtn"><router-link to="/products">Products</router-link></span>
      <div class="dropdown">
        <router-link to="/technology">Technology &#x25BC;</router-link>
        <div class="dropdown-content">
          <a href="#">This does nothing</a>
          <a href="#">Same here</a>
          <a href="#">No links yet</a>
        </div>
      </div>
    </div>
  </header>
</template>
<script>

export default {
  name: 'NavBar',
}
</script>

<style>
header {
  top: 0;
  z-index: 10;
  padding-top: 10px;
  width: 100%;
  position: fixed;
  display: block;
  background-color: rgb(224,224,224, 0.2);
}

#logo {
  border-radius: 25px;
}

.navbar {
  overflow: hidden;
  margin: 0 20%;
  border-bottom: 1px #333 solid;
  transition: 0.4s;
  display: flex;
  justify-content: space-around;
}

.navbar a {
  float: left;
  font-size: 16px;
  color: black;
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
  color: black;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: gray;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
  margin-top: 50px;
}
</style>
