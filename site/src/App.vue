<template>
  <div id="app">
    <div id="nav">
      <img src="@/assets/logo.png" class="logo" />
      <h1>Bilabonnement</h1>
    </div>
    <router-view />
  </div>
</template>
<script>
(function(w, d, s, l, i) {
  w[l] = w[l] || [];
  w[l].push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
  var f = d.getElementsByTagName(s)[0],
    j = d.createElement(s),
    dl = l != 'dataLayer' ? '&l=' + l : '';
  j.async = true;
  j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
  f.parentNode.insertBefore(j, f);
})(window, document, 'script', 'dataLayer', 'GTM-M9LVHZT');

export default {};
</script>

<style>
:root {
  --main-dark: #204051;
  --main-medium-dark: #3b6978;
  --main-medium-light: #84a9ac;
  --main-light: #cae8d5;
}

body,
html,
#app {
  background: var(--main-light);
  font-family: consolas, 'Franklin Gothic Medium', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 100%;
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
</style>
