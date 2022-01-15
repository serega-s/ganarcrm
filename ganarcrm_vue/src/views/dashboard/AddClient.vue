<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home</router-link>
          </li>
          <li><router-link :to="{ name: 'Clients' }">Clients</router-link></li>
          <li class="is-active">
            <router-link :to="{ name: 'AddClient' }">Add Client</router-link>
          </li>
        </Breadcrumb>
        <h1 class="title">Add client</h1>
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
                v-model="name"
                placeholder="Client Name"
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
                v-model="contact_person"
                placeholder="Contact Person"
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
                placeholder="Website"
                v-model="website"
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
import Breadcrumb from "@/components/dashboard/Breadcrumb.vue"
import { toast } from "bulma-toast"
import ClientService from "../../services/client.service"
export default {
  name: "AddClient",
  components: {
    Breadcrumb,
  },
  data() {
    return {
      name: "",
      contact_person: "",
      email: "",
      phone: "",
      website: "",
    }
  },
  mounted() {
    document.title = "GanarCRM: Add Client"
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      const client = {
        name: this.name,
        contact_person: this.contact_person,
        email: this.email,
        phone: this.phone,
        website: this.website,
      }

      try {
        const response = await ClientService.addClient(client)
        toast({
          message: "The client was created",
          type: "is-success",
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: "bottom-right",
        })
        this.$router.push({ name: "Clients" })
      } catch (e) {
        console.error(e)
      }

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
