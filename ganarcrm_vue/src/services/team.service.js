import axios from "axios"
import authHeader from "./auth-header"

class TeamService {
  getMyTeam() {
    const response = axios.get("/api/v1/teams/get_my_team/", {
      headers: authHeader(),
    })

    return response
  }

  addTeam(team) {
    const response = axios.post("/api/v1/teams/", team)

    return response
  }
  cancelPlan() {
    const response = axios.post("/api/v1/teams/cancel_plan/")

    return response
  }
}

export default new TeamService()
