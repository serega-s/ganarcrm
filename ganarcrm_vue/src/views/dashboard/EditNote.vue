<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit note</h1>
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
                v-model="note.name"
              />
            </div>
          </div>

          <div class="field">
            <label for="body">Body</label>
            <div class="control">
              <textarea class="textarea" v-model="note.body" />
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
import { toast } from "bulma-toast"
import NoteService from '../../services/note.service'
export default {
  name: "EditNote",
  data() {
    return {
      note: {},
    }
  },
  mounted() {
    document.title = "GanarCRM: Edit Note"
    this.getNote()
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      const clientID = this.$route.params.id

      await NoteService.editNote(clientID, this.note)
        .then((response) => {
          toast({
            message: "The note was updated",
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
    async getNote() {
      this.$store.commit("setIsLoading", true)

      const noteID = this.$route.params.note_id
      const clientID = this.$route.params.id

      await NoteService.getNote(noteID, clientID)
        .then((response) => {
          this.note = response.data
        })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
