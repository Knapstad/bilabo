<template>
  <footer class="footer">
    <div class="footerwrapper">
      <div class="supplyers">
        <h3>Leverandører:</h3>
        <router-link to="/volvo">Volvo</router-link>
        <router-link to="/imove">Imove</router-link>
        <router-link to="/fleks">Fleks</router-link>
        <router-link to="/kinto-flex">Kinto Flex</router-link>
        <router-link to="/swapcar">Swapcar</router-link>
        <router-link to="/flexidrive">Flexidrive</router-link>
      </div>
      <div class="contact">
        <a href="mailto:post@bilabonnement.app">post@bilabonnement.app</a>
      </div>
      <div class="internal">
        <router-link to="/om-oss">Om oss</router-link>
        <router-link to="/hva-er-bilabonnement">Hva er bilabonnement </router-link>
        <router-link to="/cookies-personvern">Cookies og personvern</router-link>
      </div>
    </div>
  </footer>
</template>

<script>

export default {
  name: 'Foot',
};
</script>

<style scoped>
h3{
  padding: 0px;
  margin: 0px;
  margin-top: .5rem;
}

.footer{
  background: var(--main-dark);
}
.footerwrapper{
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  padding-bottom: 1rem;
  padding-left: 10%;
  padding-right: 10%;
}
.internal{
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 2rem;
  font-size: 1.5rem;
}
.contact {
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 30px;
}
.supplyers{
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: white;
}

a {
  color: white;
}
@media only screen and (max-width: 600px) {
  .footerwrapper{
    padding-top: 1rem;
    flex-direction: column-reverse;
  }
  .contact , .internal, .supplyers {
    font-size: 1rem;
    justify-content: flex-start;
    margin-block-end: 10px;
  }
  .internal{
    line-height: 1.2;
  }
}

@media only screen and (max-width: 360px) {
  .contact .internal, .supplyers  {
    font-size: 10px;
  }
}
</style>
