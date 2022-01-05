import axios from "axios"

class LeadService {
  addLead(lead) {
    const response = axios.post("/api/v1/leads/", lead)

    return response
  }

  getLead(leadID) {
    const response = axios.get(`/api/v1/leads/${leadID}/`)

    return response
  }

  getLeads() {
    const response = axios.get(`/api/v1/leads/`)

    return response
  }

  editLead(leadID, lead) {
    const response = axios.patch(`/api/v1/leads/${leadID}/`, lead)

    return response
  }

  deleteLead(leadID) {
    const response = axios.post(`/api/v1/leads/delete_lead/${leadID}/`)

    return response
  }
  convertLeadToClient(data) {
    const response = axios.post(`/api/v1/convert_lead_to_client/`, data)

    return response
  }
  paginateLeads(currentPage, query) {
    const response = axios.get(
      `/api/v1/leads/?page=${currentPage}&search=${query}`
    )

    return response
  }
}

export default new LeadService()
