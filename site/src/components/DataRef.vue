<template>
    <p>{{_sanityProps}}</p>
</template>

<script>
export default {

    name: "DataRef",
    props: [ "_key", "_type", "data", "_sanityProps" ],
    computed: {
        }
}

</script>