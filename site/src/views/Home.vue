<template>
  <div class="home">
    <div class="carcontainer">
      <div class="car" v-for="(car, index) in Object.values(cars).flat()" :key="index">
        <Car class :car="car" />
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
.home {
  /* align-items: center; */
  /* margin: auto; */
}
.carcontainer {
  display: inline-grid;
  grid-template-columns: 30% 30% 30%;
  padding: 30px;
  margin: auto;
  /* align-: center; */
}
.car {
  /* background-color: rgba(255, 255, 255, 0.8); */
  /* border: 1px solid; */
  /* padding: 20px; */
  /* font-size: 30px; */
  /* text-align: center; */
  box-shadow: 2px 2px 3px #000;
  border-radius: 2px;
  margin: 5px;
}
</style>
