<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Thank you</h1>

        <router-link :to="{ name: 'Team' }" class="button is-primary">
          Back to Team
        </router-link>
      </div>

      <div class="column is-4">
        <p>Thank you for subscribing to a plan!</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import { toast } from "bulma-toast"
export default {
  name: "PlansThankYou",
  mounted() {
    document.title = "GanarCRM: Thank You"
    axios
      .post("/api/v1/stripe/check_session/", {
        sessionId: this.$route.params.session_id,
      })
      .then((response) => {
        toast({
          message: "The plan was updated",
          type: "is-success",
          dismissible: true,
          pauseOnHover: true,
          duration: 200,
          position: "bottom-right",
        })

        this.$store.commit("setTeam", {
          id: response.data.id,
          name: response.data.name,
          plan: response.data.plan.name,
          max_leads: response.data.plan.max_leads,
          max_clients: response.data.plan.max_clients,
        })
      })
      .catch((error) => {
        toast({
          message: "Something went wrong ...",
          type: "is-danger",
          dismissible: true,
          pauseOnHover: true,
          duration: 200,
          position: "bottom-right",
        })
        console.log("Error:", error.response)
      })
  },
}
</script>
