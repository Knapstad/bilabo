<template>
    <img :class=clss :src="imgUrl" :alt=alt >
</template>

<script>
export default {

    props: [ "_key", "_type", "alt", "asset", "caption", "clss", "_sanityProps" ],
    computed: {
        imgUrl() {
            if(!this._sanityProps.options){
                return this.asset.url
            }
            let test=this.asset.url+"?"
            Object.entries(this._sanityProps.options.imageOptions).forEach(function(e)  {try{test+=e.join("=")+"&"}catch{/*comment*/}})
            return test
        }
},
}
</script>