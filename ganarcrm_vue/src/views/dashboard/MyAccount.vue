<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My Account</h1>
        {{ $store.state.user.username }}
      </div>

      <div class="column is-12">
        <div class="buttons">
          <router-link
            :to="{ name: 'EditMember', params: { id: $store.state.user.id } }"
            class="button is-light"
            >Edit</router-link
          >
          <button @click="logout()" class="button is-danger">Logout</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "MyAccount",
  mounted(){
    document.title = "GanarCRM: Team"
  },
  methods: {
    logout() {
      this.$store.dispatch("logout").then(
        () => {
          this.$router.push({ name: "LogIn" })
        },
        (error) => {
          console.log(error.response)
        }
      )
    },
  },
}
</script>
