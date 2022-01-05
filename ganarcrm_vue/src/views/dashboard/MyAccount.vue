<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home</router-link>
          </li>
          <li class="is-active">
            <router-link :to="{ name: 'MyAccount' }">My Account</router-link>
          </li>
        </Breadcrumb>
        <h1 class="title">My Account</h1>
        {{ $store.state.user.email }}
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
import Breadcrumb from "../../components/dashboard/Breadcrumb.vue"
import AuthService from "../../services/auth.service"

export default {
  name: "MyAccount",
  components: {
    Breadcrumb,
  },
  mounted() {
    document.title = "GanarCRM: Team"
  },
  methods: {
    logout() {
      this.$store.commit("setIsLoading", true)
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

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
