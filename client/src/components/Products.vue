<template>
  <div class="component">
    <span class="img"></span>
    <div class="product-description">
      <p class="heading">{{productName}}</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Products',
  props: {
    productName: String,
    productDescription: String,
    imgSrc: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.img {
  display: block;
  z-index: 1;
  width: 100vw;
  height: 300px;
  background-image: url("https://previews.123rf.com/images/gar1984/gar19841802/gar1984180200015/102371713-moscow-russia-february-2018-traffic-jam-on-the-mkad-circle-moscow-road-during-blizzard-snowstorm.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}
.heading {
  font-size: 50px;
  letter-spacing: 3px;
  font-family: 'Montserrat', Helvetica, Arial, sans-serif;
  margin: 0 0 20px 0;
}
.product-description {
  margin: 40px 30% 0 30%;
  line-height: 2.5;
  font-weight: 300; 
}
</style>