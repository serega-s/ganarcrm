import axios from "axios"

class NoteService {
  addNote(note) {
    const response = axios.post("/api/v1/notes/", note)

    return response
  }

  getClientNotes(clientID) {
    const response = axios.get(`/api/v1/notes/?client_id=${clientID}`)

    return response
  }

  getNote(noteID, clientID) {
    const response = axios.get(`/api/v1/notes/${noteID}/?client_id=${clientID}`)

    return response
  }

  editNote(clientID, note) {
    const response = axios.patch(
      `/api/v1/notes/${note.id}/?client_id=${clientID}`,
      note
    )

    return response
  }
}

export default new NoteService()
