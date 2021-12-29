import axios from "axios"

class AuthService {
  async login(user) {
    const response = await axios.post("/api/v1/token/", {
      username: user.username,
      password: user.password,
    })
    // const { access, refresh } = response.data
    // if (access && refresh) {
    //   axios.defaults.headers.common["Authorization"] = "Bearer " + access
    //   localStorage.setItem("accessToken", access)
    //   localStorage.setItem("accessToken", refresh)
    // }
    return response
  }
  async logout() {
    // const response = await axios.post("/api/v1/token/logout/")
    delete axios.defaults.headers.common["Authorization"]
    localStorage.clear()
  }
  register(user) {
    return axios.post("/api/v1/users/", {
      username: user.username,
      password: user.password,
    })
  }
}

export default new AuthService()
