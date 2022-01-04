<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add note</h1>
      </div>
      <div class="column is-half is-offset-one-quarter">
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
import NoteService from "../../services/note.service"
export default {
  name: "AddNote",
  data() {
    return {
      name: "",
      body: "",
      client_id: this.$route.params.id,
    }
  },
  mounted() {
    document.title = "GanarCRM: Add Note"
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      const note = {
        name: this.name,
        body: this.body,
        client_id: this.client_id,
      }

      await NoteService.addNote(note)
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

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
