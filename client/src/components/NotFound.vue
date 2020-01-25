<template>
  <div class="component">
    <span class="img">
      <div class="text-block">
        <p class="text-block heading">404 Error:<br>Whoops! We can't find what you're looking for.</p>
      </div>
    </span>
  </div>
</template>

<script>
export default {
  name: 'NotFound'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.img {
  display: block;
  z-index: 1;
  width: 100vw;
  height: 100vh;
  background-image: url("https://c.stocksy.com/a/nti700/z9/1840891.jpg?1575002095");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
}

.text-block {
  z-index: 5;
  border: 1.5px solid rgb(44, 62, 80);
  border-radius: 2px;
  background-color: rgb(125, 156, 151, 0.8);
  color: white;
  align-self: center;
}

.text-block .heading {
  font-size: 25px;
  padding: 20px;
  margin: 0;
}
</style>
