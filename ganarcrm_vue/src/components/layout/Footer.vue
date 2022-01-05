<template>
  <footer class="footer">
    <div class="content has-text-centered">
      <p>
        <strong>GanarCRM</strong>: All Rights Reserved © Copyright
        {{ getDateYear() }}
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  methods: {
    getDateYear() {
      const dateYear = new Date()
      return dateYear.getUTCFullYear()
    },
  },
}
</script>
