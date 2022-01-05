<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add lead</h1>
      </div>
      <div class="column is-half is-offset-one-quarter">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="company">Company</label>
            <div class="control">
              <input
                type="text"
                name="company"
                class="input"
                placeholder="Company Name"
                v-model="company"
                required
              />
            </div>
          </div>

          <div class="field">
            <label for="contact_person">Contact person</label>
            <div class="control">
              <input
                type="text"
                name="contact_person"
                class="input"
                placeholder="Contact person"
                v-model="contact_person"
                required
              />
            </div>
          </div>

          <div class="field">
            <label for="email">Email</label>
            <div class="control">
              <input
                type="email"
                name="email"
                class="input"
                v-model="email"
                placeholder="Email"
                required
              />
            </div>
          </div>

          <div class="field">
            <label for="phone">Phone</label>
            <div class="control">
              <input
                type="number"
                name="phone"
                class="input"
                v-model="phone"
                placeholder="Phone"
                required
              />
            </div>
          </div>

          <div class="field">
            <label for="website">Website</label>
            <div class="control">
              <input
                type="text"
                name="website"
                class="input"
                v-model="website"
                placeholder="Website"
              />
            </div>
          </div>

          <div class="field">
            <label for="confidence">Confidence</label>
            <div class="control">
              <input
                type="number"
                name="confidence"
                class="input"
                v-model="confidence"
                placeholder="Confidence"
                required
              />
            </div>
          </div>

          <div class="field">
            <label for="estimated_value">Estimated value</label>
            <div class="control">
              <input
                type="number"
                name="estimated_value"
                class="input"
                v-model="estimated_value"
              />
            </div>
          </div>

          <div class="field">
            <label for="status">Status</label>
            <div class="control">
              <div class="select">
                <select name="status" v-model="status" required>
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
            <label for="priority">Priority</label>
            <div class="control">
              <div class="select">
                <select name="priority" v-model="priority" required>
                  <option value="low">Low</option>
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                </select>
              </div>
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
import LeadService from "../../services/lead.service"
export default {
  name: "AddLead",
  data() {
    return {
      company: "",
      contact_person: "",
      email: "",
      phone: "",
      website: "",
      confidence: "",
      estimated_value: 0,
      status: "",
      priority: "",
    }
  },
  mounted() {
    document.title = "GanarCRM: Add Lead"
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      const lead = {
        company: this.company,
        contact_person: this.contact_person,
        email: this.email,
        phone: this.phone,
        website: this.website,
        confidence: this.confidence,
        estimated_value: this.estimated_value,
        status: this.status,
        priority: this.priority,
      }

      await LeadService.addLead(lead)
        .then((response) => {
          toast({
            message: "The lead was created",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          })
          this.$router.push({ name: "Leads" })
        })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
