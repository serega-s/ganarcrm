<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'Leads' }">Leads</router-link>
          </li>
          <li class="is-active">
            <router-link :to="{ name: 'Lead' }">{{ lead.id }}</router-link>
          </li>
        </Breadcrumb>
        <h1 class="title">{{ lead.company }}</h1>

        <div class="buttons">
          <button
            @click="convertToClient"
            class="button is-info is-rounded is-outlined"
          >
            Convert to client
          </button>
          <button @click="deleteLead" class="button is-danger">Delete</button>
        </div>

        <router-link :to="{ name: 'EditLead', params: { id: lead.id } }"
          >Edit</router-link
        >
      </div>

      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Details</h2>
          <template v-if="lead.assigned_to">
            <p>
              <strong>Assigned To: </strong>{{ lead.assigned_to.first_name }}
              {{ lead.assigned_to.last_name }}
            </p>
          </template>
          <p><strong>Status: </strong>{{ lead.status }}</p>
          <p><strong>Priority: </strong>{{ lead.priority }}</p>
          <p><strong>Confidence: </strong>{{ lead.confidence }}</p>
          <p><strong>Estimated value: </strong>{{ lead.estimated_value }}</p>
          <p><strong>Created at: </strong>{{ lead.created_at }}</p>
          <p><strong>Modified at: </strong>{{ lead.modified_at }}</p>
        </div>
      </div>

      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Contact information</h2>

          <p><strong>Contact person: </strong>{{ lead.contact_person }}</p>
          <p><strong>Email: </strong>{{ lead.email }}</p>
          <p><strong>Phone: </strong>{{ lead.phone }}</p>
          <template v-if="lead.website">
            <p><strong>Website: </strong>{{ lead.website }}</p>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LeadService from '../../services/lead.service'
import Breadcrumb from '../../components/dashboard/Breadcrumb.vue'
export default {
  name: "Lead",
  components: {
    Breadcrumb
  },
  data() {
    return {
      lead: {},
    }
  },
  mounted() {
    document.title = "GanarCRM: Lead"
    this.getLead()
  },
  methods: {
    async deleteLead() {
      this.$store.commit("setIsLoading", true)

      const leadID = this.$route.params.id

      await LeadService.deleteLead(leadID)
        .then((response) => {
          console.log(response.data)

          this.$router.push({ name: "Leads" })
        })

      this.$store.commit("setIsLoading", false)
    },
    async getLead() {
      this.$store.commit("setIsLoading", true)

      const leadID = this.$route.params.id

      await LeadService.getLead(leadID)
        .then((response) => {
          this.lead = response.data
        })
        .catch((error) => {
          console.log(error)
        })

      this.$store.commit("setIsLoading", false)
    },
    async convertToClient() {
      this.$store.commit("setIsLoading", true)
      const leadID = this.$route.params.id
      const data = {
        lead_id: leadID,
      }
      await LeadService.convertLeadToClient(data)
        .then((response) => {
          console.log("converted to client")
          this.$router.push("/dashboard/clients")
        })
        
      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
