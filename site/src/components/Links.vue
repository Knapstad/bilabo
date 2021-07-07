<template>
    <pre>{{JSON.stringify(_sanityProps)}}</pre>
</template>

<script>
export default {

    name: "Links",
    props: [ "_key", "_type", "href", "newtab", "_sanityProps" ],
    computed: {
        }
}

</script>