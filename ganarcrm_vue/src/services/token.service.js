class TokenService {
  getLocalRefreshToken() {
    const refreshToken = localStorage.getItem('refreshToken')
    return refreshToken
  }

  getLocalAccessToken() {
    const accessToken = localStorage.getItem('accessToken')
    return accessToken
  }

  updateLocalAccessToken(token) {
    let accessToken = localStorage.getItem("accessToken")
    accessToken = token
    localStorage.setItem("accessToken", accessToken)
  }

  // getUser() {
  //   return JSON.parse(localStorage.getItem("user"))
  // }

  // setUser(user) {
  //   console.log(JSON.stringify(user))
  //   localStorage.setItem("user", JSON.stringify(user))
  // }

  // removeUser() {
  //   localStorage.removeItem("user")
  // }
}

export default new TokenService()
