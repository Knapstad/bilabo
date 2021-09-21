export default{

    install(Vue) {
        Vue.prototype.$track = function(eventName, data){
            setTimeout(()=>{
            window.dataLayer=window.dataLayer||[],
            window.dataLayer.push({
                event: eventName,
                data
            })
            console.log("send tracking")},500)
        }
    }
}