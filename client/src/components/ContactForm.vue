<template>
  <div class="component">
    <div class="button-container">
      <button class="contactButton" @click="$refs.modal.style.display='flex'">Contact Us</button>
    </div>
    <div class="modal" ref="modal">
      <div class="modal-content" ref="modalContent">
        <div class="modal-body">
          <span @click="$refs.modal.style.display='none'" class="close">&times;</span>
          <p>Some text! Neat! </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactForm',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.button-container {
  width: 100%;
  height: 100%;
  position: absolute;
  display: flex;
}

.contactButton {
  font-size: 18px;  
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: #532d9d;
  font-family: inherit;
  margin: 0;
  position: fixed;
  z-index: 100;
  transform: rotate(90deg);
  right: 0;
  align-self: center;
  opacity: 0.7;
}

button:hover {
  opacity: 1;
}

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

.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 100; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%;
  height: 100%; 
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content/Box */
.modal-content {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fefefe;
  margin: auto;
  padding: 2px 16px;  
  border: 1px solid #888;
  width: 20%;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19);
  animation-name: animatedown;
  animation-duration: 0.5s
}

/* The Close Button */
.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.animate-up {
  animation-name: animateup;
  animation-duration: 0.5s;
}

.fade-out {
  animation-name: fadeout;
  animation-duration: 0.5s;
}

@keyframes animatedown {
  from {top: -300px; opacity: 0}
  to {top: 0; opacity: 1}
}

@keyframes animateup {
  from {top: 0; opacity: 1}
  to {top: -300px; opacity: 0}
}

@keyframes fadeout {
  from {opacity: 1}
  to {opacity: 0}
}

</style>