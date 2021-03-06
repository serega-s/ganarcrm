<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'Team' }">Team</router-link>
          </li>
          <li class="is-active">
            <router-link :to="{ name: 'Plans' }">Plans</router-link>
          </li>
        </Breadcrumb>
        <h1 class="title">Plans</h1>
      </div>

      <div class="column is-4 has-text-centered">
        <div class="box">
          <h2 class="subtitle">Free</h2>
          <h4 class="is-size-4">$0</h4>

          <p>Max 5 clients</p>
          <p>Max 5 leads</p>
          <hr />
          <template v-if="$store.state.team.plan === 'Free'">
            <button class="button is-info is-rounded is-medium" disabled>
              Subscribed
            </button>
          </template>
          <template v-else>
            <button
              @click="cancelPlan"
              class="button is-success is-rounded is-medium is-outlined"
            >
              Subscribe
            </button>
          </template>
        </div>
      </div>

      <div class="column is-4 has-text-centered">
        <div class="box">
          <h2 class="subtitle">Small team</h2>
          <h4 class="is-size-4">$10</h4>

          <p>Max 15 clients</p>
          <p>Max 15 leads</p>
          <hr />
          <template v-if="$store.state.team.plan === 'Small team'">
            <button class="button is-info is-rounded is-medium" disabled>
              Subscribed
            </button>
            <button
              class="button is-medium is-rounded is-light is-danger"
              @click="cancelPlan"
            >
              Cancel
            </button>
          </template>
          <template v-else>
            <button
              @click="subscribe('smallteam')"
              class="button is-success is-rounded is-medium is-outlined"
            >
              Subscribe
            </button>
          </template>
        </div>
      </div>

      <div class="column is-4 has-text-centered">
        <div class="box">
          <h2 class="subtitle">Big team</h2>
          <h4 class="is-size-4">$25</h4>

          <p>Max 50 clients</p>
          <p>Max 50 leads</p>
          <hr />
          <template v-if="$store.state.team.plan === 'Big team'">
            <button class="button is-info is-rounded is-medium" disabled>
              Subscribed
            </button>
            <button
              class="button is-medium is-rounded is-light is-danger"
              @click="cancelPlan"
            >
              Cancel
            </button>
          </template>
          <template v-else>
            <button
              @click="subscribe('bigteam')"
              class="button is-success is-rounded is-medium is-outlined"
            >
              Subscribe
            </button>
          </template>
        </div>
      </div>

      <hr />
    </div>
  </div>
</template>

<script>
import { toast } from "bulma-toast"

import StripeService from "../../services/stripe.service"
import TeamService from "../../services/team.service"
import Breadcrumb from "../../components/dashboard/Breadcrumb.vue"

export default {
  name: "Plans",
  components: {
    Breadcrumb,
  },
  data() {
    return {
      pub_key: "",
      stripe: null,
      team: {
        plan: {},
      },
    }
  },
  async mounted() {
    document.title = "GanarCRM: Plans"
    await this.getPubKey()
    this.stripe = Stripe(this.pub_key)
  },
  methods: {
    async getPubKey() {
      this.$store.commit("setIsLoading", true)

      try {
        const response = await StripeService.getStripePubKey()
        this.pub_key = response.data.pub_key
      } catch (e) {
        console.error(e)
      }

      this.$store.commit("setIsLoading", false)
    },
    async cancelPlan() {
      this.$store.commit("setIsLoading", true)
      try {
        const response = await TeamService.cancelPlan()
        this.$store.commit("setTeam", {
          id: response.data.id,
          name: response.data.name,
          plan: response.data.plan.name,
          max_leads: response.data.plan.max_leads,
          max_clients: response.data.plan.max_clients,
        })
        toast({
          message: "The plan was cancelled!",
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
    async subscribe(plan) {
      this.$store.commit("setIsLoading", true)

      const data = {
        plan: plan,
      }

      try {
        const response = await StripeService.createCheckoutSession(data)
        return this.stripe.redirectToCheckout({
          sessionId: response.data.sessionId,
        })
      } catch (e) {
        console.error(e)
      }

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
