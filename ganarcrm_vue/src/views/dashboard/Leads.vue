<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Leads</h1>

        <router-link
          v-if="$store.state.team.max_leads > num_leads"
          :to="{ name: 'AddLead' }"
          >Add lead</router-link
        >

        <div class="notification is-danger" v-else>
          You have reached the top of your limitations. Please upgrade a plan!
        </div>

        <hr />

        <form @submit.prevent="getLeads">
          <div class="field has-addons">
            <div class="control">
              <input type="text" class="input" v-model="query" />
            </div>
            <div class="control">
              <button class="button is-success">Search</button>
            </div>
          </div>
        </form>
      </div>

      <div class="column is-12">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <td>Company</td>
              <th>Contact person</th>
              <th>Assigned to</th>
              <th>Status</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="lead in leads" :key="lead.id">
              <td>{{ lead.company }}</td>
              <td>{{ lead.contact_person }}</td>
              <td>
                <template v-if="lead.assigned_to">
                  <p>
                    <strong>Assigned to: </strong
                    >{{ lead.assigned_to.first_name }}
                    {{ lead.assigned_to.last_name }}
                  </p>
                </template>
              </td>
              <td>{{ lead.status }}</td>
              <td>
                <router-link :to="{ name: 'Lead', params: { id: lead.id } }"
                  >Details</router-link
                >
              </td>
            </tr>
          </tbody>
        </table>

        <div class="buttons">
          <button
            class="button is-light"
            @click="goToPreviousPage()"
            v-if="showPreviousButton"
          >
            Previous
          </button>
          <button
            class="button is-light"
            @click="goToNextPage()"
            v-if="showNextButton"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "Leads",
  data() {
    return {
      leads: [],
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
      query: "",
      num_leads: 0,
    }
  },
  mounted() {
    this.getLeads()
  },
  methods: {
    goToNextPage() {
      this.currentPage += 1
      this.getLeads()
    },
    goToPreviousPage() {
      this.currentPage -= 1
      this.getLeads()
    },
    async getLeads() {
      this.$store.commit("setIsLoading", true)

      this.showNextButton = false
      this.showPreviousButton = false

      await axios
        .get(`/api/v1/leads/`)
        .then((response) => {
          this.num_leads = response.data.count
        })
        .catch((error) => {
          console.log(error)
        })

      await axios
        .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
        .then((response) => {
          this.leads = response.data.results

          if (response.data.next) {
            this.showNextButton = true
          }
          if (response.data.previous) {
            this.showPreviousButton = true
          }
        })
        .catch((error) => {
          console.log(error)
        })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
