<template>
    <p>

        {{ bendik }}
    </p>
</template>

<script>
export default {

    name: "DataRef",
    props: ["_key", "_type", "text", "data", "_sanityProps"],
    computed: {

        bendik: function () {

            return 'Hei bendik' + this.text
        }
    }
}

</script>