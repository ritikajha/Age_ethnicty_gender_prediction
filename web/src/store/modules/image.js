import axios from 'axios'
let $http = axios.create({
    baseURL: 'http://localhost:5000'
})

const state = {
    isLoggedIn: true,

};

const mutations = {
    SET_USER_PROFILE: (state) => {

    },
};

const actions = {
 
};
const getters = {
    isLoggedIn(state) {
        return state.isLoggedIn
    },
};

export default {
    state,
    getters,
    mutations,
    actions
}