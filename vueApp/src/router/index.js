import { createRouter, createWebHistory } from 'vue-router'
import { auth } from './../firebasefunc.js'
import Home from '@/views/Home.vue'
import Portfolio from '@/views/Portfolio.vue'
import Equities from '@/views/Equities.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Profile from '@/views/Profile.vue'



const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },

    {
        path:'/login',
        name:'Login',
        component:Login
    },

    {
        path:'/user',
        name:'User',
        component:Portfolio,
        meta: { auth:true }
    },

    {
        path: '/portfolio',
        name: 'Portfolio',
        component: Portfolio,
        meta: { auth:true }
    },

    {
        path: '/equities',
        name: 'Equities',
        component: Equities,
        meta: { auth:true }
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile,
        meta: { auth:true }
    }
]

const router = createRouter ({
    history: createWebHistory(),
    routes
})

router.beforeEach(async (to, from, next)=>{
    if (to.matched.some(record => record.meta.auth)){
        // Auth check 
        if (auth.currentUser) {
            //check if token is valid 
             next()
        }
        next('/login')
    }
    next() 
})

export default router