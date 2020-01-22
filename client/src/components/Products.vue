<template>
  <div class="component" v-if="productName">
    <span class="img"></span>
    <div class="product-description">
      <p class="heading">{{productName}}</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
    <button>This does nothing yet</button>
  </div>
  <div class="component" v-else>
    <span class="img"></span>
    <div class="product-description">
      <p class="heading main">Products</p>
      <p>TidyDigits specializes in producing high-quality weather-focused data products.</p>
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
.product-description {
  margin: 40px 30% 30px 30%;
  line-height: 2.5;
  font-weight: 300; 
}
.main {
  border-bottom: 1px solid;
}

.component {
  margin-bottom: 40px;
}
</style>