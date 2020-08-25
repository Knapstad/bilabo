<template>
  <div class="hello">
    <div class="column">
      <p>{{ car.name }}</p>
      <p>{{ car.site }}</p>
      <p>{{ car.price }}</p>
    </div>
    <div class="column">
      <img :src="car.img.replace(' ','-')" />
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    car: Object,
    site: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  width: 100%;
  margin: auto;
}
.column {
  float: right;
  width: 50%;
  margin: auto;
  min-height: 160px;
}
img {
  width: 100%;
}
</style>
