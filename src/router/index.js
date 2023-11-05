import { createRouter, createWebHistory } from 'vue-router'
import { auth } from '../firebasefunc.js'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'



const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home, Login
    },
    {
        path:'/login',
        name:'Login',
        component:Login
    },
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
             console.log("Authenticated User")
        }
        next('/login')
    }
    next() 
})

export default router