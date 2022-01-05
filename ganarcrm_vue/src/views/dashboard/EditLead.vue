<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Dashboard' }">Dashboard</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'Leads' }">Leads</router-link>
          </li>
          <li>
            <router-link
              :to="{ name: 'Lead', params: { id: $route.params.id } }"
              >{{ lead.id }}</router-link
            >
          </li>
          <li class="is-active">
            <router-link
              :to="{ name: 'EditLead', params: { id: $route.params.id } }"
              >Edit Lead</router-link
            >
          </li>
        </Breadcrumb>
        <h1 class="title">Edit {{ lead.company }}</h1>
      </div>

      <div class="column is-half is-offset-one-quarter">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Company</label>
            <div class="control">
              <input type="text" class="input" v-model="lead.company" />
            </div>
          </div>

          <div class="field">
            <label>Contact person</label>
            <div class="control">
              <input type="text" class="input" v-model="lead.contact_person" />
            </div>
          </div>

          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" class="input" v-model="lead.email" />
            </div>
          </div>

          <div class="field">
            <label>Phone</label>
            <div class="control">
              <input type="text" class="input" v-model="lead.phone" />
            </div>
          </div>

          <div class="field">
            <label>Website</label>
            <div class="control">
              <input type="text" class="input" v-model="lead.website" />
            </div>
          </div>

          <div class="field">
            <label>Confidence</label>
            <div class="control">
              <input type="number" class="input" v-model="lead.confidence" />
            </div>
          </div>

          <div class="field">
            <label>Estimated value</label>
            <div class="control">
              <input
                type="number"
                class="input"
                v-model="lead.estimated_value"
              />
            </div>
          </div>

          <div class="field">
            <label>Status</label>
            <div class="control">
              <div class="select">
                <select v-model="lead.status">
                  <option value="new">New</option>
                  <option value="contacted">Contacted</option>
                  <option value="inprogress">In progress</option>
                  <option value="lost">Lost</option>
                  <option value="won">Won</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label>Priority</label>
            <div class="control">
              <div class="select">
                <select v-model="lead.priority">
                  <option value="low">Low</option>
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label>Assigned to</label>
            <div class="control">
              <div class="select">
                <select v-model="lead.assigned_to">
                  <option value="" selected>Select member</option>
                  <option
                    v-for="member in team.members"
                    :key="member.id"
                    :value="member"
                    >{{ member.email }}</option
                  >
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success is-outlined">Update</button>
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

import LeadService from "../../services/lead.service"
import TeamService from "../../services/team.service"
import Breadcrumb from "../../components/dashboard/Breadcrumb.vue"

export default {
  name: "EditLead",
  components: {
    Breadcrumb,
  },
  data() {
    return {
      lead: {},
      team: {
        members: [],
      },
    }
  },
  mounted() {
    document.title = "GanarCRM: Edit Lead"
    this.getLead()
    this.getTeam()
  },
  methods: {
    async getLead() {
      this.$store.commit("setIsLoading", true)

      const leadID = this.$route.params.id

      await LeadService.getLead(leadID).then((response) => {
        this.lead = response.data
      })

      this.$store.commit("setIsLoading", false)
    },
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      const leadID = this.$route.params.id

      await LeadService.editLead(leadID, this.lead).then((response) => {
        toast({
          message: "The lead was updated",
          type: "is-success",
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: "bottom-right",
        })

        this.$router.push(`/dashboard/leads/${leadID}`)
      })

      this.$store.commit("setIsLoading", false)
    },
    async getTeam() {
      this.$store.commit("setIsLoading", true)
      await TeamService.getMyTeam().then((response) => {
        this.team = response.data
      })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
