<template>
  <div class="component">
    <div class="button-container">
      <button class="contactButton" @click="$refs.modal.style.display='flex'">Contact Us</button>
    </div>
    <div class="modal" ref="modal">
      <div class="modal-content" ref="modalContent">
        <div class="modal-body">
          <span @click="$refs.modal.style.display='none'" class="close">&times;</span>
          <p class="label">Name:</p>
          <div class="info-container">
            <span>
              <input v-model="firstName" type="text" @keyup.enter="checkValidity()"/>
              <p class="sub-label">First</p>
            </span>
            <span>
              <input v-model="lastName" type="text" @keyup.enter="checkValidity()"/>
              <p class="sub-label">Last</p>
            </span>
          </div>
          <p class="label">Contact Info:</p>
          <div class="info-container">
            <span>
              <input v-model="email" type="email" @keyup.enter="checkValidity()"/>
              <p class="sub-label">Email</p>
            </span>
            <span>
              <input v-model="phone" type="text" @keyup.enter="checkValidity()"/>
              <p class="sub-label">Phone</p>
            </span>
          </div>
          <div class="message-container">
            <p class="label">Message:</p>
            <textarea></textarea>
          </div>
          <button @click="checkValidity()">SUBMIT</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactForm',
  data(){
    return {
      firstName: '',
      lastName: '',
      email: '',
      phone: '',
      textBody: ''
    }
  },
  methods:{
    submitContact() {
      console.log("contact form submitted");
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.label {
  text-align: left;
  font-weight: bold;
}

.sub-label {
  text-align: left;
  font-weight: normal;
}

.button-container {
  position: absolute;
  right: 0;
  top: 50%;
}
.info-container {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  margin: 15px 0;
}

textarea {
  width: 100%;
  height: 80px;
  resize: none;
}

.modal-body {
  padding: 15px 0;
  width: 50%;
  height: 100%;
}

button {
  font-size: 18px;  
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: #532d9d;
  font-family: inherit;
}

.contactButton {
  margin: 0;
  position: fixed;
  z-index: 100;
  transform: rotate(90deg);
  right: -45px;
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
  border-radius: 10px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fefefe;
  margin: auto;
  padding: 2px 16px;  
  border: 1px solid #888;
  width: 40%;
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