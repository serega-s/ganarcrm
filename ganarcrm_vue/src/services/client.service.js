import axios from "axios"

class ClientService {
  addClient(client) {
    const response = axios.post("/api/v1/clients/", client)

    return response
  }

  getClient(clientID) {
    const response = axios.get(`/api/v1/clients/${clientID}/`)

    return response
  }

  getClients() {
    const response = axios.get(`/api/v1/clients/`)

    return response
  }

  paginateClients(currentPage, query) {
    const response = axios.get(
      `/api/v1/clients/?page=${currentPage}&search=${query}`
    )

    return response
  }

  deleteClient(clientID) {
    const response = axios.post(`/api/v1/clients/delete_client/${clientID}/`)
    return response
  }

  editClient(clientID, client) {
    const response = axios.patch(`/api/v1/clients/${clientID}/`, client)

    return response
  }
}

export default new ClientService()
