import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Portfolio from '@/views/Portfolio.vue'
import Equities from '@/views/Equities.vue'
import User from '@/views/User.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },

    {
        path: '/portfolio',
        name: 'Portfolio',
        component: Portfolio
    },

    {
        path: '/equities',
        name: 'Equities',
        component: Equities
    },

    {
        path: '/user',
        name: 'User',
        component: User
    }
]

const router = createRouter ({
    history: createWebHistory(),
    routes
})

export default router