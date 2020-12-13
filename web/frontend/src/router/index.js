import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/LogIn.vue'
import store from '../store'
Vue.use(VueRouter)

const routes = [{
    path: '/login',
    name: 'login',
    component: Login
},

// {
//     path: '*',
//     name: 'Error',
//     component: () =>
//         import('../pages/Error.vue'),


// }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

// router.beforeEach((to, _from, next) => {
//     if (to.matched.some(record => record.meta.requiresAuth)) {
//         if (store.getters.userToken) {
//             next();
//         } else {
//             next('/')
//         }
//     } else {
//         next();
//     }
//   });


export default router