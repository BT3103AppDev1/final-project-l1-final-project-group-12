import { createRouter, createWebHistory } from 'vue-router'

import Portfolio from '@/views/Portfolio.vue'
import NotFound from '@/views/NotFound.vue'
import LogIn from '@/components/Portfolio/Login.vue'

const routes = [
    {
        path: '/',
        name: 'Login',
        component: LogIn
    },

    {
        path: '/portfolio',
        name: 'Portfolio',
        component: Portfolio
    },
    {
        path: '/:catchAll(.*)',
        name: 'NotFound',
        component: NotFound
      }

]

const router = createRouter ({
    history: createWebHistory(),
    routes
})

export default router