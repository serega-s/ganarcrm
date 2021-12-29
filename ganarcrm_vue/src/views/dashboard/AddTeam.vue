<template>
  <div class="container">
    <div class="columns is-multiline">
      <h1 class="title">Add team</h1>
    </div>

    <div class="column is-12">
      <form @submit.prevent="submitForm">
        <div class="field">
          <label for="company">Team name</label>
          <div class="control">
            <input
              placeholder="Team Name"
              type="text"
              name="company"
              class="input"
              v-model="name"
            />
          </div>
        </div>

        <div class="field">
          <div class="control">
            <button class="button is-success">Submit</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import { toast } from "bulma-toast"
export default {
  name: "AddTeam",
  data() {
    return {
      name: "",
    }
  },
  mounted() {
    document.title = "GanarCRM: Add Team"
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      const team = {
        name: this.name,
      }

      await axios
        .post("/api/v1/teams/", team)
        .then((response) => {
          toast({
            message: "The team was added",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          })

          this.$store.commit("setTeam", {
            id: response.data.id,
            name: this.name,
          })

          this.$router.push("/dashboard/team")
        })
        .catch((error) => {
          console.log(error)
        })
      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
