<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <Breadcrumb>
          <li>
            <router-link :to="{ name: 'Home' }">Home</router-link>
          </li>
          <li class="is-active">
            <router-link :to="{ name: 'Dashboard' }">Dashboard</router-link>
          </li>
        </Breadcrumb>
        <h1 class="title">Dashboard</h1>
      </div>
    </div>
  </div>
</template>

<script>
import Breadcrumb from "../../components/dashboard/Breadcrumb.vue"
export default {
  name: "Dashboard",
  components: {
    Breadcrumb,
  },
  mounted() {
    document.title = "GanarCRM: Dashboard"
  },
}
</script>
