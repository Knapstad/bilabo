<template>
    <div>
    <p><slot /></p>
    <p>{{vm}}</p>
    </div>
</template>

<script>
export default {

    name: "LinksInternal",
    props: ["_to","_type","reference","_sanityProps"],
    }

</script>