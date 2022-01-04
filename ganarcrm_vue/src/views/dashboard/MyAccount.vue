<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My Account</h1>
        {{ $store.state.user.username }}
      </div>

      <div class="column is-12">
        <div class="buttons">
          <button @click="logout()" class="button is-danger">Logout</button>
          <router-link
            :to="{ name: 'EditMember', params: { id: $store.state.user.id } }"
            class="mx-5"
            >Edit</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import AuthService from "../../services/auth.service"

export default {
  name: "MyAccount",
  mounted() {
    document.title = "GanarCRM: Team"
  },
  methods: {
    logout() {
      AuthService.logout()
      this.$store.commit("removeToken")
      this.$router.push({ name: "LogIn" })
      //   this.$store.dispatch("logout").then(
      //     () => {
      //       this.$router.push({ name: "LogIn" })
      //     },
      //     (error) => {
      //       console.log(error.response)
      //     }
      //   )
    },
  },
}
</script>
