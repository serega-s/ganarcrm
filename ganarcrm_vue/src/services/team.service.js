import axios from "axios"
import authHeader from "./auth-header"

class TeamService {
  getMyTeam() {
    return axios.get("/api/v1/teams/get_my_team", {
      headers: authHeader(),
    })
  }
}

export default new TeamService()
