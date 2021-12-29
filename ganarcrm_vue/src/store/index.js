import { createStore } from "vuex"
import AuthService from "../services/auth.service"
import UserService from "../services/user.service"

export default createStore({
  state: {
    isLoading: false,
    user: {
      id: 0,
      token: "",
      isAuthenticated: false,
      username: "",
      accessToken: "",
      refreshToken: "",
    },
    team: {
      id: 0,
      name: "",
      plan: "",
      max_leads: 0,
      max_clients: 0,
    },
  },
  mutations: {
    setToken(state, { access, refresh }) {
      state.user.isAuthenticated = true
      state.user.accessToken = access
      state.user.refreshToken = refresh
    },
    removeToken(state) {
      state.user.accessToken = ""
      state.user.refreshToken = ""
      state.user.isAuthenticated = false
    },
    initializeStore(state) {
      if (localStorage.getItem("accessToken")) {
        state.user.accessToken = localStorage.getItem("accessToken")
        state.user.refreshToken = localStorage.getItem("refreshToken")
        state.user.isAuthenticated = true
        state.user.username = localStorage.getItem("username")
        state.user.id = localStorage.getItem("userid")
        state.team.name = localStorage.getItem("team_name")
        state.team.id = localStorage.getItem("team_id")
        state.team.plan = localStorage.getItem("team_plan")
        state.team.max_clients = localStorage.getItem("team_max_clients")
        state.team.max_leads = localStorage.getItem("team_max_leads")
      } else {
        // state.user = {}
        state.user.accessToken = ""
        state.user.refreshToken = ""
        state.user.isAuthenticated = false
        state.user.id = 0
        state.user.username = ""
        state.team.name = ""
        state.team.id = 0
        state.team.plan = ""
        state.team.max_clients = 0
        state.team.max_leads = 0
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },

    setTeam(state, team) {
      state.team = team

      localStorage.setItem("team_id", team.id)
      localStorage.setItem("team_name", team.name)
      localStorage.setItem("team_plan", team.plan)
      localStorage.setItem("team_max_leads", team.max_leads)
      localStorage.setItem("team_max_clients", team.max_clients)
    },
    // setToken(state, token) {
    //   state.user.token = token
    //   state.user.isAuthenticated = true
    // },
    // removeToken(state) {
    //   state.user.token = ""
    //   state.user.isAuthenticated = false
    // },
    setUser(state, user) {
      state.user = user
    },
  },
  actions: {
    login({ commit, dispatch }, user) {
      return AuthService.login(user).then(
        (response) => {
          commit("setToken", {
            accessToken: response.data.access,
            refreshToken: response.data.refresh,
          })

          return Promise.resolve(user)
        },
        (error) => {
          commit("removeToken")
          return Promise.reject(error)
        }
      )
    },
    logout({ commit }) {
      AuthService.logout()
      commit("removeToken")
    },
    register({ commit }, user) {
      return AuthService.register(user).then(
        (response) => {
          return Promise.resolve(response.data)
        },
        (error) => {
          return Promise.reject(error)
        }
      )
    },
    getMe({ commit }) {
      return UserService.getMe().then((response) => {
        commit("setUser", response.data)
        return Promise.resolve(response.data)
      })
    },
  },
  modules: {
    // auth,
  },
})
