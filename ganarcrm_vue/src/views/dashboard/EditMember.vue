<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'MyAccount' }">MyAccount</router-link>
          </li>
          <li class="is-active">
            <router-link
              :to="{ name: 'EditMember', params: { id: $route.params.id } }"
              >Edit</router-link
            >
          </li>
        </Breadcrumb>
        <h1 class="title">Edit member</h1>
      </div>
      <div class="column is-half is-offset-one-quarter">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="name">First name</label>
            <div class="control">
              <input
                type="text"
                name="name"
                class="input"
                placeholder="First Name"
                v-model="user.first_name"
              />
            </div>
          </div>

          <div class="field">
            <label for="name">Last name</label>
            <div class="control">
              <input
                type="text"
                name="name"
                class="input"
                placeholder="Last Name"
                v-model="user.last_name"
              />
            </div>
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
import { toast } from "bulma-toast"
import UserService from "../../services/user.service"
import Breadcrumb from "../../components/dashboard/Breadcrumb.vue"
export default {
  name: "EditMember",
  components: {
    Breadcrumb,
  },
  data() {
    return {
      user: {},
    }
  },
  mounted() {
    document.title = "GanarCRM: Edit Member"
    this.getUser()
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      const userID = this.$route.params.id

      try {
        const response = await UserService.editMember(userID, this.user)
        toast({
          message: "The user was updated",
          type: "is-success",
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: "bottom-right",
        })
        this.$router.push({ name: "MyAccount" })
      } catch (e) {
        console.error(e)
      }

      this.$store.commit("setIsLoading", false)
    },
    async getUser() {
      this.$store.commit("setIsLoading", true)

      const userID = this.$route.params.id

      try {
        const response = await UserService.getUser(userID)
        this.user = response.data
      } catch (e) {
        console.error(e)
      }

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
