<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home</router-link>
          </li>
          <li class="is-active">
            <router-link :to="{ name: 'Clients' }">Clients</router-link>
          </li>
        </Breadcrumb>
        <h1 class="title">Clients</h1>

        <router-link
          :to="{ name: 'AddClient' }"
          v-if="$store.state.team.max_leads > num_clients"
          >Add client</router-link
        >
        <div class="notification is-danger" v-else>
          You have reached the top of your limitations. Please upgrade!
        </div>

        <hr />

        <form @submit.prevent="getClients">
          <div class="field has-addons">
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="query"
                placeholder="Client Name"
              />
            </div>
            <div class="control">
              <button class="button is-success">Search</button>
            </div>
          </div>
        </form>
      </div>

      <div class="column is-12">
        <template v-if="clients.length">
          <table class="table is-fullwidth">
            <thead>
              <tr>
                <td>Name</td>
                <th>Contact person</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="client in clients" :key="client.id">
                <td>{{ client.name }}</td>
                <td>{{ client.contact_person }}</td>
                <td>
                  <router-link
                    :to="{ name: 'Client', params: { id: client.id } }"
                    >Details</router-link
                  >
                  <!-- <a href="#">Details</a> -->
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
        </template>
        <template v-else>
          <p>You don't have any clients yet...</p>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import ClientService from "../../services/client.service"
import Breadcrumb from '../../components/dashboard/Breadcrumb.vue'

export default {
  name: "Clients",
  components: {
    Breadcrumb
  },
  data() {
    return {
      clients: [],
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
      query: "",
      num_clients: 0,
    }
  },
  mounted() {
    document.title = "GanarCRM: Clients"
    this.getClients()
  },
  methods: {
    goToNextPage() {
      this.currentPage += 1
      this.getClients()
    },
    goToPreviousPage() {
      this.currentPage -= 1
      this.getСlients()
    },
    async getClients() {
      this.$store.commit("setIsLoading", true)

      this.showNextButton = false
      this.showPreviousButton = false

      await ClientService.getClients()
        .then((response) => {
          this.num_clients = response.data.count
        })
        .catch((error) => {
          console.log(error)
        })
      await ClientService.paginateClients(this.currentPage, this.query).then(
        (response) => {
          this.clients = response.data.results

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
