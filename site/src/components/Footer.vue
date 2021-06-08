<template>
  <footer class="contact">
    <address href="mailto:post@bilabonnement.app">post@bilabonnement.app</address> | 
    <a href="/om-oss">Om oss</a> | 
    <a href="/hva-er-bilabonnement">Hva er bilabonnement </a>
  </footer>
</template>

<script>

export default {
  name: 'Foot',
};
</script>

<style scoped>
.contact {
  display: flex;
  justify-content: center;
  padding: 50px;
  background: var(--main-dark);
  color: white;
  font-size: 30px;
}

a {
  color: white;
}
@media only screen and (max-width: 600px) {
  .contact {
    font-size: 20px;
  }
}

@media only screen and (max-width: 360px) {
  .contact {
    font-size: 10px;
  }
}
</style>
