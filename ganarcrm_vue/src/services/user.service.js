import axios from "axios"
import authHeader from "./auth-header"

class UserService {
  getMe() {
    return axios.get("/api/v1/users/me/", { headers: authHeader() })
    // .then((response) => {
    //   localStorage.setItem("username", response.data.username)
    //   localStorage.setItem("userid", response.data.id)
    // })
  }
  editMember() {}
}

export default new UserService()
