<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign up</h1>

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
            <label for="password1">Password</label>
            <div class="control">
              <input
                type="password"
                name="password1"
                class="input"
                v-model="password1"
                placeholder="Password"
              />
            </div>
          </div>

          <div class="field">
            <label for="password2">Repeat Password</label>
            <div class="control">
              <input
                type="password"
                name="password2"
                class="input"
                v-model="password2"
                placeholder="Re-password"
              />
            </div>
          </div>

          <div class="field">
            <div class="control">
              <p>
                Have an account?
                <router-link :to="{ name: 'LogIn' }">Log in</router-link> to
                continue
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
import { toast } from "bulma-toast"

export default {
  name: "SignUp",
  data() {
    return {
      email: "",
      password1: "",
      password2: "",
      errors: [],
    }
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)
      this.errors = []

      if (!this.email) {
        this.errors.push("Username field is missing!")
        this.$store.commit("setIsLoading", false)
      } else if (!this.password1 || this.password1.length < 8) {
        this.errors.push("Password must contain at least 8 characters")
        this.$store.commit("setIsLoading", false)
      } else if (this.password1 !== this.password2) {
        this.errors.push("Passwords don't match!")
        this.$store.commit("setIsLoading", false)
      } else if (!this.errors.length) {
        const formData = {
          email: this.email,
          password: this.password1,
        }

        await axios
          .post("/api/v1/users/", formData)
          .then((response) => {
            toast({
              message: "Account was created, please log in!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            })

            this.$router.push("/log-in")
          })
          .catch((error) => {
            if (error.response.data) {
              for (const property in error.response.data) {
                this.errors.push(`${error.response.data[property]}`)
              }
            } else {
              this.errors.push("Unable to sign up with bad credentials.")
            }
          })
        this.$store.commit("setIsLoading", false)
      }
    },
  },
}
</script>
