<template>
  <div class="buttons">
    <button @click="back" id="btn1" class="btn btn-secondary">
      Go Back
    </button>
    <button @click="forward" id="btn2" class="btn btn-secondary">
      Go Forward
    </button>
  </div>
  <br><br>
  <div id="nav">
    <router-link id="nav-element" to="/">Home</router-link> |
    <router-link id="nav-element" :to="{ name: 'About' }">About</router-link> |
    <router-link id="nav-element" :to="{ name: 'Jobs' }">Jobs</router-link>
    <br><br><br>
  </div>
  <router-view />
</template>

<script>
export default {
  methods: {
    back() {
      this.$router.go(-1);
    },
    forward() {
      this.$router.go(1);
    },
    //this.$router.push({name:'Home'});//redirect
  },
};
</script>

<style>
#app {
  font-family: sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #ddf1fd;
  padding-top: 50px;
  padding-left: 7%;
  padding-right: 7%;
  font-size: larger;
}

#nav {
  text-align: center;
}

#nav-element {
  color: #ce96fb;
  font-weight: bolder;
  font-size: x-large;
}

#nav a.router-link-exact-active {
  color: rgb(26, 32, 41);
  background: #ff8fcf;
  padding: 7px;
  border-radius: 5px;
}
.buttons {
  display: flex;
  justify-content: space-between;
}
.btn {
  background: rgb(26, 32, 41);
  color: rgb(132, 250, 230);
  border-color: #ddf1fd;
}
</style>