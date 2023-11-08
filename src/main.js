import './style/App.css'

import { createApp } from 'vue'
import App from './App.vue'
// import equityRouter from './router/equity_router/index.js'
import router from './router/index.js'

import VueChartkick from 'vue-chartkick'
import 'chartkick/chart.js'

createApp(App)
  .use(router)
//   .use(equityRouter)
  .use(VueChartkick)
  .mount('#app');