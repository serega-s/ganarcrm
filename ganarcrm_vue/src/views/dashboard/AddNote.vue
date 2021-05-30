<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="columns is-12">
        <h1 class="title">Add note</h1>
      </div>
      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="name">Name</label>
            <div class="control">
              <input type="text" name="name" class="input" v-model="name" />
            </div>
          </div>

          <div class="field">
            <label for="body">Body</label>
            <div class="control">
              <textarea class="textarea" v-model="body" />
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
  </div>
</template>

<script>
import axios from "axios"
import { toast } from "bulma-toast"
export default {
  name: "AddNote",
  data() {
    return {
      name: "",
      body: "",
      client_id: this.$route.params.id,
    }
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      const note = {
        name: this.name,
        body: this.body,
        client_id: this.client_id,
      }

      await axios
        .post("/api/v1/notes/", note)
        .then((response) => {
          toast({
            message: "The note was added",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          })
          this.$router.push({
            name: "Client",
            params: { id: this.$route.params.id },
          })
        })
        .catch((error) => {
          console.log(error.response)
        })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
