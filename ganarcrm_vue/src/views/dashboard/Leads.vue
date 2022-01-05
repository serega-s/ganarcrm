<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Dashboard' }">Dashboard</router-link>
          </li>
          <li class="is-active">
            <router-link :to="{ name: 'Leads' }">Leads</router-link>
          </li>
        </Breadcrumb>
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
              <input
                type="text"
                class="input"
                v-model="query"
                placeholder="Lead Name"
              />
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
                    {{ lead.assigned_to.first_name }}
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
import LeadService from "../../services/lead.service"
import Breadcrumb from '../../components/dashboard/Breadcrumb.vue'
export default {
  name: "Leads",
  components: {
    Breadcrumb
  },
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
    document.title = "GanarCRM: Leads"
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

      await LeadService.getLeads().then((response) => {
        this.num_leads = response.data.count
      })

      await LeadService.paginateLeads(this.currentPage, this.query).then(
        (response) => {
          this.leads = response.data.results

          if (response.data.next) {
            this.showNextButton = true
          }
          if (response.data.previous) {
            this.showPreviousButton = true
          }
        }
      )

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
