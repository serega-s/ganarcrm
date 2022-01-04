<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit "{{ client.name }}"</h1>
      </div>
      <div class="column is-half is-offset-one-quarter">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="name">Name</label>
            <div class="control">
              <input
                type="text"
                name="name"
                class="input"
                v-model="client.name"
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
                v-model="client.contact_person"
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
                v-model="client.email"
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
                v-model="client.phone"
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
                v-model="client.website"
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
export default {
  name: "AddClient",
  data() {
    return {
      client: {},
    }
  },
  mounted() {
    document.title = "GanarCRM: Edit Client"
    this.getClient()
  },
  methods: {
    async getClient() {
      this.$store.commit("setIsLoading", true)

      const clientID = this.$route.params.id

      axios
        .get(`/api/v1/clients/${clientID}/`)
        .then((response) => {
          this.client = response.data
        })
        .catch((error) => {
          console.log(error)
        })

      this.$store.commit("setIsLoading", false)
    },
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      const clientID = this.$route.params.id

      axios
        .patch(`/api/v1/clients/${clientID}/`, this.client)
        .then((response) => {
          toast({
            message: "The client was updated",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          })

          this.$router.push({ name: "Clients" })
        })
        .catch((error) => {
          console.log(error)
        })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
