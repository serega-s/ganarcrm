<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home</router-link>
          </li>
          <li><router-link :to="{ name: 'Team' }">Team</router-link></li>
          <li class="is-active">
            <router-link :to="{ name: 'AddMember' }">Add Member</router-link>
          </li>
        </Breadcrumb>
        <h1 class="title">Add member</h1>
      </div>

      <div class="column is-half is-offset-one-quarter">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="email">Email</label>
            <div class="control">
              <input
                type="email"
                name="email"
                class="input"
                placeholder="Email"
                v-model="email"
                required
              />
            </div>
          </div>

          <div class="field">
            <label for="password1">Password</label>
            <div class="control">
              <input
                type="password"
                name="password1"
                placeholder="Password"
                class="input"
                v-model="password1"
                required
              />
            </div>
          </div>

          <div class="field">
            <label for="password2">Repeat Password</label>
            <div class="control">
              <input
                type="password"
                name="password2"
                placeholder="Repeat Password"
                class="input"
                v-model="password2"
                required
              />
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
import AuthService from "../../services/auth.service"
import UserService from "../../services/user.service"
import Breadcrumb from "@/components/dashboard/Breadcrumb.vue"

export default {
  name: "AddMember",
  components: {
    Breadcrumb,
  },
  data() {
    return {
      email: "",
      password1: "",
      password2: "",
      errors: [],
    }
  },
  mounted() {
    document.title = "GanarCRM: Add Member"
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)
      this.errors = []

      if (!this.email) {
        this.$store.commit("setIsLoading", false)
        this.errors.push("The email is missing!")
      }
      if (!this.password1) {
        this.$store.commit("setIsLoading", false)
        this.errors.push("The password is too short!")
      }
      if (this.password1 !== this.password2) {
        this.$store.commit("setIsLoading", false)
        this.errors.push("The passwords are not matching!")
      }

      if (!this.errors.length) {
        this.$store.commit("setIsLoading", true)
        const formData = {
          email: this.email,
          password: this.password1,
        }

        await AuthService.register(formData)
          .then((response) => {
            const emailData = {
              email: this.email,
            }

            UserService.addMember(emailData).then((response) => {
              toast({
                message: "The member was added!",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: "bottom-right",
              })
              this.$router.push({ name: "Team" })
            })
          })
          .catch((error) => {
            this.errors.push(error.response.data)
          })

        this.$store.commit("setIsLoading", false)
      }
    },
  },
}
</script>
