import axios from "axios"
import store from "../store"
import TokenService from "./token.service"

const setup = (store) => {
  axios.interceptors.request.use(
    (config) => {
      const accessToken = TokenService.getLocalAccessToken()
      if (accessToken) {
        config.headers["Authorization"] = "Bearer " + accessToken // for Spring Boot back-end
        // config.headers["x-access-token"] = token // for Node.js Express back-end
      }
      return config
    },
    (error) => {
      return Promise.reject(error)
    }
  )

  axios.interceptors.response.use(
    (res) => {
      return res
    },
    async (err) => {
      const originalConfig = err.config

      if (originalConfig.url !== "/api/v1/token/" && err.response) {
        // Access Token was expired
        if (err.response.status === 401 && !originalConfig._retry) {
          originalConfig._retry = true

          try {
            const rs = await axios.post("/api/v1/token/refresh/", {
              refresh: TokenService.getLocalRefreshToken(),
            })

            const { access } = rs.data

            store.dispatch("refreshToken", access)
            TokenService.updateLocalAccessToken(access)

            return axios(originalConfig)
          } catch (_error) {
            return Promise.reject(_error)
          }
        }
      }

      return Promise.reject(err)
    }
  )
}

export default setup
