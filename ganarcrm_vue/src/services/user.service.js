import axios from "axios"
import authHeader from "./auth-header"

class UserService {
  getMe() {
    const response = axios.get("/api/v1/users/me/", { headers: authHeader() })

    return response
  }
  editMember(userID, user) {
    const response = axios.put(`/api/v1/teams/member/${userID}/`, user)

    return response
  }
  getUser(userID) {
    const response = axios.get(`/api/v1/teams/member/${userID}/`)

    return response
  }
}

export default new UserService()
