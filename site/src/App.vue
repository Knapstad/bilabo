<template>
  <div id="app">
    <div id="nav">
      <h1>Bilabonement</h1>
    </div>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: consolas, "Franklin Gothic Medium", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}
h1 {
  font-size: 40px;
  margin-bottom: 0px;
}

#nav {
  padding-top: 30px;
  padding-left: 40px;
  padding-bottom: 1px;
  margin-bottom: 0px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
}
</style>
