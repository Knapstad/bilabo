<template>
    <div>

        <span v-for="path in breadcrumbs" :key="path.id">
            <a :href="path.href">{{ path.path }}</a><span>{{ path.seperator }}</span>
        </span>
    </div>
</template>
<script>
export default {
    name: "BreadCrumbs",
    data() {
        return {
        };
    },

    computed: {
        breadcrumbs: () => {
            let paths = window.location.href.split("/")
            let base = "https:/"
            paths = paths.slice(2, paths.length)
            let breadcrumbs = []

            for (let item in paths) {
                let path = paths[item]
                let seperator = ""
                base += "/" + paths[item]
                if (item == 0) {
                    path = "hjem"
                }
                if (item != paths.length - 1) {
                    seperator = " > "
                }
                breadcrumbs.push({ path: path, href: base, seperator: seperator })

            }
            return breadcrumbs
        },
    }
}
</script>
<style scoped>
div {
    margin-left: 1rem;
}

a {
    font-size: medium;
    text-transform: capitalize;
}
</style>