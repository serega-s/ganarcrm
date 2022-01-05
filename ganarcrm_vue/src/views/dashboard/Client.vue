<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home
            </router-link>
          </li>
          <li>
            <router-link :to="{ name: 'Clients' }">Clients</router-link>
          </li>
          <li class="is-active">
            <router-link :to="{ name: 'Client', params: { id: client.id } }">{{
              client.id
            }}</router-link>
          </li>
        </Breadcrumb>
        <h1 class="title">{{ client.name }}</h1>
        <div class="buttons">
          <button @click="deleteClient" class="button is-danger">
            Delete client
          </button>
          <router-link
            :to="{ name: 'EditClient', params: { id: client.id } }"
            class="mx-5"
            >Edit</router-link
          >
        </div>
      </div>

      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Details</h2>
          <p><strong>Created at: </strong>{{ client.created_at }}</p>
          <p><strong>Modified at: </strong>{{ client.modified_at }}</p>
        </div>
      </div>

      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Contact information</h2>

          <p><strong>Contact person: </strong>{{ client.contact_person }}</p>
          <p><strong>Email: </strong>{{ client.email }}</p>
          <p><strong>Phone: </strong>{{ client.phone }}</p>
          <p><strong>Website: </strong>{{ client.website }}</p>
        </div>
      </div>

      <div class="column is-12">
        <h2 class="subtitle">Notes</h2>

        <router-link
          :to="{ name: 'AddNote', params: { id: client.id } }"
          class="button is-info is-light is-outlined mb-6"
          >Add note</router-link
        >

        <div class="box" v-for="note in notes" :key="note.id">
          <h3 class="is-size-4">{{ note.name }}</h3>

          <p>{{ note.body }}</p>

          <router-link
            :to="{
              name: 'EditNote',
              params: { id: client.id, note_id: note.id },
            }"
            class="button is-light is-info mt-6"
            >Edit note</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Breadcrumb from "@/components/dashboard/Breadcrumb.vue"
import ClientService from "../../services/client.service"
import NoteService from "../../services/note.service"

export default {
  name: "Client",
  components: {
    Breadcrumb,
  },
  data() {
    return {
      client: {},
      notes: [],
    }
  },
  mounted() {
    document.title = "GanarCRM: Client"
    this.getClient()
  },
  methods: {
    async deleteClient() {
      this.$store.commit("setIsLoading", true)

      const clientID = this.$route.params.id

      await ClientService.deleteClient(clientID)
        .then((response) => {

          this.$router.push({ name: "Clients" })
        })

      this.$store.commit("setIsLoading", false)
    },
    async getClient() {
      this.$store.commit("setIsLoading", true)

      const clientID = this.$route.params.id

      await ClientService.getClient(clientID)
        .then((response) => {
          this.client = response.data
        })

      await NoteService.getClientNotes(clientID)
        .then((response) => {
          this.notes = response.data
        })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
