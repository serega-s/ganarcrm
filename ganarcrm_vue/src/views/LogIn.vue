<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Log in</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="email">Email</label>
            <div class="control">
              <input
                type="email"
                name="email"
                class="input"
                v-model="email"
                placeholder="Email"
              />
            </div>
          </div>

          <div class="field">
            <label for="password">Password</label>
            <div class="control">
              <input
                type="password"
                name="password"
                class="input"
                v-model="password"
                placeholder="Password"
              />
            </div>
          </div>

          <div class="field">
            <div class="control">
              <p>
                Do not have an account?
                <router-link :to="{ name: 'SignUp' }">Sign up</router-link> to
                create
              </p>
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success is-outlined">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import UserService from "../services/user.service"
import TeamService from "../services/team.service"
import AuthService from "../services/auth.service"

export default {
  name: "LogIn",
  data() {
    return {
      email: "",
      password: "",
      errors: [],
    }
  },
  mounted() {
    document.title = "GanarCRM: Log In"
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      axios.defaults.headers.common["Authorization"] = ""

      this.errors = []

      if (!this.email) {
        this.errors.push("Email field is missing!")
        this.$store.commit("setIsLoading", false)
      } else if (!this.password) {
        this.errors.push("Password field is missing!")
        this.$store.commit("setIsLoading", false)
      } else if (!this.errors.length) {
        const formData = {
          email: this.email,
          password: this.password,
        }

        await AuthService.login(formData)
          .then((response) => {
            const { access, refresh } = response.data
            if (access && refresh) {
              this.$store.commit("setToken", { access, refresh })
              axios.defaults.headers.common["Authorization"] =
                "Bearer " + access
              localStorage.setItem("accessToken", access)
              localStorage.setItem("refreshToken", refresh)
            }
          })
          .catch((error) => {
            this.$store.commit("setIsLoading", false)
            
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${error.response.data[property]}`)
              }
            } else {
              this.errors.push("Unable to sign in with bad credentials.")
            }
          })

        await UserService.getMe().then((response) => {
          this.$store.commit("setUser", {
            id: response.data.id,
            email: response.data.email,
            isAuthenticated: true,
          })
          localStorage.setItem("email", response.data.email)
          localStorage.setItem("userid", response.data.id)
        })

        await TeamService.getMyTeam()
          .then((response) => {

            this.$store.commit("setTeam", {
              id: response.data.id,
              name: response.data.name,
              plan: response.data.plan.name,
              max_leads: response.data.plan.max_leads,
              max_clients: response.data.plan.max_clients,
            })
            this.$router.push({ name: "MyAccount" })
          })
          .catch((error) => {
            this.$router.push({ name: "AddTeam" })
          })

        this.$store.commit("setIsLoading", false)
      }
    },
  },
}
</script>
