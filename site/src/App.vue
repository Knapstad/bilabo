<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">
        <img src="@/assets/logo.png" class="logo"
      /></router-link>
      <router-link to="/"> <h1>Bilabonnement</h1> </router-link>
    </div>
    <router-view />
  </div>
</template>
<script>
export default {};
</script>

<style>
:root {
  --main-dark: #204051;
  --main-medium-dark: #3b6978;
  --main-medium-light: #84a9ac;
  --main-light: #cae8d5;
}
/* *,
*:before,
*:after {
  box-sizing: inherit;
} */
body {
  box-sizing: border-box;
  margin: 0;
}

body,
html,
#app {
  background: var(--main-light);
  font-family: consolas, 'Franklin Gothic Medium', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: auto;
  overflow-x: hidden;
}

h1 {
  font-size: 40px;
  margin-bottom: 0px;
  color: #cae8d5;
}

#nav {
  display: flex;
  padding-top: 40px;
  padding-left: 40px;
  padding-bottom: 40px;
  margin-bottom: px;
  background: var(--main-dark);
  width: 100%;
  align-items: center;
}

.logo {
  width: 60px;
  height: 60px;
  padding-right: 10px;
}
.router-link {
  text-decoration: none;
}
.router-link-active {
  text-decoration: none;
}
@media only screen and (max-width: 900px) {
  #nav {
    padding: 0px;
  }
}
</style>
