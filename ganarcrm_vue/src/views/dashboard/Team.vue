<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home</router-link>
          </li>
          <li class="is-active">
            <router-link :to="{ name: 'Team' }">Team</router-link>
          </li>
        </Breadcrumb>
        <h1 class="title">Team</h1>

        <hr />
        <template v-if="team.created_by">
          <p><strong>Plan: </strong>{{ $store.state.team.plan }}</p>
          <p>
            <strong>Max clients: </strong>{{ $store.state.team.max_clients }}
          </p>
          <p><strong>Max leads: </strong>{{ $store.state.team.max_leads }}</p>
          <p v-if="$store.state.team.plan !== 'Free'">
            <strong>Plan end date: </strong>{{ team.plan_end_date }}
          </p>

          <p>
            <router-link :to="{ name: 'Plans' }">Change plan</router-link>
          </p>

          <hr />

          <template
            v-if="team.created_by.id === parseInt($store.state.user.id)"
          >
            <router-link
              :to="{ name: 'AddMember' }"
              class="button is-primary is-light is-outlined"
              >Add Member</router-link
            >
          </template>
        </template>
        <template v-else>
          <router-link
            :to="{ name: 'AddTeam' }"
            class="button is-info is-light is-outlined"
            >Add Team</router-link
          >
        </template>
      </div>

      <div class="column is-12">
        <h2 class="subtitle">Members</h2>

        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Email</th>
              <th>Full name</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="member in team.members" :key="member.id">
              <td>{{ member.email }}</td>
              <td>{{ member.first_name }} {{ member.last_name }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Breadcrumb from "../../components/dashboard/Breadcrumb.vue"
import TeamService from "../../services/team.service"

export default {
  name: "Team",
  components: {
    Breadcrumb,
  },
  data() {
    return {
      team: {
        members: [],
        created_by: {},
      },
    }
  },
  mounted() {
    document.title = "GanarCRM: Team"
    this.getTeam()
  },
  methods: {
    async getTeam() {
      this.$store.commit("setIsLoading", true)
      try {
        const response = await TeamService.getMyTeam()
        this.team = response.data
      } catch (e) {
        console.error(e)
      }

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
