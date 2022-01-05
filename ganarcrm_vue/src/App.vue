<template>
  <div>
    <Navbar />
    <PWAPrompt />
    <div
      class="is-loading-bar has-text-centered"
      :class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>
    <section class="section">
      <router-view />
    </section>

    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/layout/Navbar"
import Footer from "@/components/layout/Footer"
import PWAPrompt from './components/pwa/PWAPrompt'
import axios from "axios"
import EventBus from "./common/EventBus"
export default {
  name: "App",
  components: {
    Navbar,
    Footer,
    PWAPrompt
  },
  beforeCreate() {
    this.$store.commit("initializeStore")
    const accessToken = this.$store.state.user.accessToken

    if (accessToken) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + accessToken
    } else {
      axios.defaults.headers.common["Authorization"] = ""
    }

    if (!this.$store.state.team.id) {
      this.$router.push("/dashboard/add-team")
    }
  },
  // methods: {
  //   logout() {
  //     AuthService.logout()
  //     this.$store.commit("removeToken")
  //     this.$router.push({ name: "LogIn" })
  //   },
  // },
  // mounted() {
  //   EventBus.on("logout", () => {
  //     this.logout()
  //   })
  // },
  // beforeUnmount() {
  //   EventBus.remove("logout")
  // },
}
</script>

<style lang="scss">
@import "../node_modules/bulma";

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
