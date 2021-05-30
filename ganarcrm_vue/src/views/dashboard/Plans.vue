<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Plans</h1>
      </div>

      <div class="column is-4">
        <div class="box">
          <h2 class="subtitle">Free</h2>
          <h4 class="is-size-4">$0</h4>

          <p>Max 5 clients</p>
          <p>Max 5 leads</p>

          <button @click="subscribe('free')" class="button is-primary">
            Subscribe
          </button>
        </div>
      </div>

      <div class="column is-4">
        <div class="box">
          <h2 class="subtitle">Small team</h2>
          <h4 class="is-size-4">$10</h4>

          <p>Max 15 clients</p>
          <p>Max 15 leads</p>

          <button @click="subscribe('smallteam')" class="button is-primary">
            Subscribe
          </button>
        </div>
      </div>

      <div class="column is-4">
        <div class="box">
          <h2 class="subtitle">Big team</h2>
          <h4 class="is-size-4">$25</h4>

          <p>Max 50 clients</p>
          <p>Max 50 leads</p>

          <button @click="subscribe('bigteam')" class="button is-primary">
            Subscribe
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { toast } from "bulma-toast"
import axios from "axios"
export default {
  name: "Plans",
  data() {
    return {
      pub_key: "",
      stipe: null,
    }
  },
  async mounted() {
    await this.getPubKey()
    this.stripe = Stripe(this.pub_key)
  },
  methods: {
    async getPubKey() {
      this.$store.commit("setIsLoading", true)

      await axios
        .get("/api/v1/stripe/get_stipe_pub_key/")
        .then((response) => {
          console.log(response.data)

          this.pub_key = response.data.pub_key
        })
        .catch((error) => {
          console.log(error)
        })

      this.$store.commit("setIsLoading", false)
    },
    async subscribe(plan) {
      this.$store.commit("setIsLoading", true)

      const data = {
        plan: plan,
      }

      await axios
        .post(`/api/v1/teams/upgrade_plan/`, data)
        .then((response) => {
          this.$store.commit("setTeam", {
            id: response.data.id,
            name: response.data.name,
            plan: response.data.plan.name,
            max_leads: response.data.plan.max_leads,
            max_clients: response.data.plan.max_clients,
          })

          toast({
            message: "The plan was updated",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          })
          this.$router.push({ name: "Team" })
        })
        .catch((error) => {
          console.log(error)
        })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
