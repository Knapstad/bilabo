<template>
  <div id="app">
    <header id="header">
      <router-link to="/">
        <img src="@/assets/logo.png" class="logo" alt="Til forsiden" /></router-link>
      <p class="tagline"><router-link to="/">
          <h1>Bilabonnement</h1>
        </router-link> - vi samler bilabonnement på en side</p>
    </header>
    <router-view />
    <Footer />
  </div>
</template>
<script>
export default {
};
</script>

<style>
:root {
  --main-dark: #040F1C;
  --main-medium-dark: #0c2342;
  --main-medium-light: #10366a;
  --main-light: #0c2342;
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

.tagline {
  color: whitesmoke;
}

h1 {
  font-size: 40px;
  margin-bottom: 0px;
  color: #whitesmoke;
}

#header {
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

.bloggcontent {
  display: flex;
  flex-direction: column;
  width: 50%;
  margin: auto;
  line-height: 1.5;
}

.bloggcontent h2 {
  color: whitesmoke;
  font-size: 33px;
}

.bloggcontent h3 {
  color: whitesmoke;
  font-size: 1.5rem;
  font-weight: bolder;
}

.bloggcontent p {
  font-size: 22px;
  margin-bottom: 17px;
}

.bloggcontent section {
  font-size: 22px;
  margin-bottom: 50px;
}

img.headerimage {
  width: 100%;
}

img.fullwidth {
  width: 100%;
  margin-top: 1rem;
}

@media screen and (max-width: 1500px) {
  .bloggcontent {
    width: 50%;
  }
}

@media screen and (max-width: 1400px) {
  .bloggcontent {
    width: 50%;
  }
}

@media screen and (max-width: 1300px) {
  .bloggcontent {
    width: 60%;
  }
}

@media only screen and (max-width: 900px) {
  .bloggcontent {
    width: 95%;
  }

  #nav {
    padding: 0px;
  }
}
</style>
