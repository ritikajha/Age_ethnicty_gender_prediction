import Vue from 'vue'
import Vuex from 'vuex'
import image from './modules/image'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        image,
    }
})