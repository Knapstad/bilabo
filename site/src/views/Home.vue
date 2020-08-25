<template>
  <div class="home">
    <div class="carcontainer">
      <div v-for="(car, index) in Object.values(cars).flat()" :key="index">
        <Car :car="car" />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Car from "@/components/Car.vue";
import cars from "../../../mycars.json";

export default {
  name: "Home",
  components: {
    Car
  },
  data() {
    return {
      cars
    };
  },
  computed: {
    flatcars: function() {
      var flatcars = [];
      for (const value in Object.entries(cars)) {
        flatcars.push(value);
      }
      return flatcars;
    }
  }
};
</script>
<style>
.carcontainer {
  display: inline-grid;
  grid-template-columns: 30% 30% 30%;
  padding: 30px;
  margin: 10px;
}
.car {
  /* background-color: rgba(255, 255, 255, 0.8); */
  border: 1px solid;
  /* padding: 20px; */
  /* font-size: 30px; */
  /* text-align: center; */
}
</style>
