<template>
  <button role="button" class="filter" :class="{active: isActive}" @click="active">{{item.charAt(0).toUpperCase() + item.slice(1)}}</button>
</template>

<script>
export default {
  name: "FilterItem",
  props: ["item", "type"],
  data() {
    return {
      isActive: this.$store.state[this.type].includes(this.item),
    };
  },
  methods: {
    addToUrl: function() {
      let qp = new URLSearchParams(window.location.search);
      let current = qp.get(this.type);
      let updated = ""
      if(current) {
        updated = current+decodeURIComponent("%2C")+this.item;}
      else {
        updated = this.item;
      }
      
      qp.set(this.type, updated);
      history.replaceState(null, null, `?${decodeURI(qp.toString())}`);},
    
    removeFromUrl: function() {
      let qp = new URLSearchParams(window.location.search);
      let current = qp.get(this.type);
      if(current && current.length > 0){
        let asarray = current.split(",");
        asarray.splice(asarray.indexOf(this.item),1)
        let updated = asarray.join();
        if(updated){ 
          qp.set(this.type, updated);
        }else{qp.delete(this.type)}
        if(qp.toString().length > 0){
              history.replaceState(null, null, `?${decodeURI(qp.toString())}`)
        }else{
              history.replaceState(null, null, `/`)}
        }
      },
    active: function () {
      if (this.isActive) {
        this.removeFromUrl()
        this.$store.commit("removeFilter", [this.type, this.item]);
      }
      if (!this.isActive) {
        this.addToUrl();
        this.$store.commit("addFilter", [this.type, this.item]);
      }
      this.isActive = !this.isActive;
    },
  },
};
</script>

<style scoped>
.filter-wrap {
  display: flex;
  }
.filter {
  border-radius: 2px;
  background: var(--main-medium-dark);
  color: white;
  padding: .4rem;
  margin: .2rem;
  box-shadow: 2px 2px 3px #000;
  /* cursor: pointer; */
  border: none;
  min-width: 95%;
  font-size: 1rem;
}
.active {
  background: var(--main-medium-light);
  box-shadow: inset 2px 2px 3px #000;
}
.filter:hover {
  background: var(--main-medium-light);
}
@media only screen and (max-width: 900px) {
  .filter {
    font-size: 12px;
    padding: .4rem;
    margin: 4px;
    text-align: center;
  }
}
/* @media only screen and (max-width: 600px) {
  .filter {
    font-size: 12px;
    padding: .2rem;
    margin: 4px;
    text-align: center;
  }
} */
</style>