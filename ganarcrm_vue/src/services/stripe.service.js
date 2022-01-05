import axios from "axios"

class StripeService {
  getStripePubKey() {
    const response = axios.get("/api/v1/stripe/get_stipe_pub_key/")

    return response
  }
  createCheckoutSession(data) {
    const response = axios.post("/api/v1/stripe/create_checkout_session/", data)

    return response
  }
  checkSession(sessionId) {
    const response = axios.post("/api/v1/stripe/check_session/", {
      sessionId: sessionId,
    })

    return response
  }
}

export default new StripeService()
