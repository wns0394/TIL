import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLunch from '@/views/TheLunch'
import TheLotto from '@/views/TheLotto'
//  @가 src 폴더를 의미한다.
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'lunch',
    component: TheLunch
  },
  {
    path: '/lotto/:lottoNum',
    name: 'lotto',
    component: TheLotto
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
