import { createRouter, createWebHistory } from "vue-router"
import store from "../store"
import routes from "./routes"

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.user.isAuthenticated
  ) {
    next("/log-in")
  } else {
    next()
  }
})

export default router
