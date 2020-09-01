<template>
  <div class="contact">
    Contact: <a href="mailto:post@bilabonnement.app">post@bilabonnement.app</a>
  </div>
</template>

<script>
// import FilterItem from "@/components/FilterItem.vue";

export default {
  name: "Foot"
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

</style>