<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home</router-link>
          </li>
          <li class="is-active">
            <router-link :to="{ name: 'AddTeam' }">Add Team</router-link>
          </li>
        </Breadcrumb>
        <h1 class="title">Add team</h1>
      </div>

      <div class="column is-half is-offset-one-quarter">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="company">Team name</label>
            <div class="control">
              <input
                placeholder="Team Name"
                type="text"
                name="company"
                class="input"
                v-model="name"
                required
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
import axios from "axios"
import { toast } from "bulma-toast"
import TeamService from "../../services/team.service"
import Breadcrumb from "../../components/dashboard/Breadcrumb.vue"

export default {
  name: "AddTeam",
  components: {
    Breadcrumb,
  },
  data() {
    return {
      name: "",
    }
  },
  mounted() {
    document.title = "GanarCRM: Add Team"
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      const team = {
        name: this.name,
      }

      try {
        const response = await TeamService.addTeam(team)
        this.$store.commit("setTeam", {
          id: response.data.id,
          name: response.data.name,
          plan: response.data.plan.name,
          max_leads: response.data.plan.max_leads,
          max_clients: response.data.plan.max_clients,
        })

        toast({
          message: "The team was added",
          type: "is-success",
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: "bottom-right",
        })

        this.$router.push({ name: "Team" })
      } catch (e) {
        console.error(e)
      }

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
