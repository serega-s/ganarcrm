<template>
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/dashboard/team" class="navbar-item">
        <strong>Ganar CRM</strong>
      </router-link>
    </div>

    <div class="navbar-menu">
      <div class="navbar-end">
        <template v-if="$store.state.user.isAuthenticated">
          <router-link :to="{ name: 'Leads' }" class="navbar-item"
            >Leads</router-link
          >
          <router-link :to="{ name: 'Clients' }" class="navbar-item"
            >Clients</router-link
          >
          <router-link to="/dashboard/team" class="navbar-item"
            >Team</router-link
          >
        </template>
        <div class="navbar-item">
          <div class="buttons">
            <template v-if="!$store.state.user.isAuthenticated">
              <router-link to="/sign-up" class="button is-success">
                <strong>Sign Up</strong>
              </router-link>
              <router-link to="/log-in" class="button is-light">
                Log In
              </router-link>
            </template>
            <template v-else>
              <router-link to="/dashboard/my-account" class="button is-info">
                My Account
              </router-link>
            </template>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
}
</script>
