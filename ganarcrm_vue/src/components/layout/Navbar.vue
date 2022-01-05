<template>
  <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link :to="{ name: 'Home' }" class="navbar-item">
        <strong>Ganar CRM</strong>
      </router-link>

      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbar-menu"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div class="navbar-menu" id="navbar-menu">
      <div class="navbar-end">
        <template v-if="$store.state.user.isAuthenticated">
          <router-link :to="{ name: 'Leads' }" class="navbar-item"
            >Leads</router-link
          >
          <router-link :to="{ name: 'Clients' }" class="navbar-item"
            >Clients</router-link
          >
          <router-link :to="{ name: 'Team' }" class="navbar-item"
            >Team</router-link
          >
        </template>
        <div class="navbar-item">
          <div class="buttons">
            <template v-if="!$store.state.user.isAuthenticated">
              <router-link to="/sign-up" class="button is-success">
                <strong>Sign Up</strong>
              </router-link>
              <router-link to="/log-in" class="button is-info is-outlined">
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
