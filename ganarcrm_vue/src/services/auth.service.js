import axios from "axios"

class AuthService {
  login(user) {
    const response = axios.post("/api/v1/token/", {
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
  logout() {
    // const response = await axios.post("/api/v1/token/logout/")
    localStorage.clear()
    delete axios.defaults.headers.common["Authorization"]
  }
  register(user) {
    return axios.post("/api/v1/users/", {
      username: user.username,
      password: user.password,
    })
  }
}

export default new AuthService()
