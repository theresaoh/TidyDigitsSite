<template>
  <v-footer absolute class="footer">
    <div class="container">
      <div class="site-map">
      </div>
      <div class="copy">
        <p class="copy-text">COPYRIGHT &copy; 2020 TidyDigits</p>
      </div>
    </div>
  </v-footer>
</template>

<script>
export default {
  name: 'Footer',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.footer {
  display: flex;
  background-color: rgb(44, 62, 80);
  width: 100%;
  height: 75px;
  bottom: 0;
  color: white;
}
.container {
  padding: 20px 10% 20px 10%;
  flex-direction: column;
  display: flex;
}
.site-map {
  height: 85%;
  display: flex;
  flex-direction: row;
  align-content: space-around;
}
.copy {
  align-content: flex-end;
  display: flex;
  height: 25px;
  width: 100%;
  height: 15%;
}
</style>