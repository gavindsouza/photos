import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import("./views/Login.vue"),
    meta: {
      isLoginPage: true,
    },
    props: true,
  },
]

let router = createRouter({
  history: createWebHistory('/gallery'),
  routes,
})

export default router