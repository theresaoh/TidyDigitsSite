<template>
  <v-footer absolute class="footer">
    <div class="contact-container">
      <div class="contact-info">
        <a href=mailto:support@tidydigits.com target="_blank" rel="noopener noreferrer">support@tidydigits.com</a>
      </div>
      <div class="copy-container">
        <div class="copy">
          <p class="copy-text">COPYRIGHT &copy; 2020 TidyDigits</p>
        </div>
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
a {
  color: white;
}

.footer {
  display: flex;
  background-color: rgb(44, 62, 80);
  width: 100%;
  height: 75px;
  bottom: 0;
  color: white;
  flex-direction: column;
  padding-bottom: 10px;
}
.contact-container {
  padding: 20px 10% 20px 10%;
}
.contact-info {
  height: 85%;
  width: 100%;
}
.copy-container {
  display: flex;
  height: 25px;
  width: 100%;
  height: 15%;
  justify-content: flex-start;
}
</style>