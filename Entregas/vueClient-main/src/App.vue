<template>
  <header>
    <router-view></router-view>
  </header>
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

@media (max-width: 768px) {
  header {
    height: auto;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 1rem;
  }

  nav {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  nav a {
    margin: 0.5rem 0;
  }
}
</style>
