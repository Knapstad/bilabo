export default {

    install(Vue) {
        Vue.prototype.$capitalize = function (str) {
            if (str) {
                return str.charAt(0).toUpperCase() + str.slice(1);
            }
        }
    }
}

