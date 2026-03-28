<template>
  <div id="app" :class="{ 'dark-mode': themeStore.isDarkMode }">
    <NavBar />
    <main class="main-content">
      <RouterView />
    </main>
  </div>
</template>

<script>
import { onMounted } from 'vue'
import NavBar from './components/NavBar.vue'
import { useThemeStore } from './stores/theme'

export default {
  components: { NavBar },

  setup() {
    const themeStore = useThemeStore()
    onMounted(() => {
      themeStore.initTheme()
    })
    return { themeStore }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', sans-serif;
  background-color: #f8fafc;
  color: #1e293b;
  transition: background-color 0.3s, color 0.3s;
}

.main-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

/* Dark mode global styles */
.dark-mode body {
  background-color: #0f172a;
  color: #e2e8f0;
}

.dark-mode .main-content {
  color: #e2e8f0;
}

.dark-mode .stat-card {
  background-color: #1e293b;
  color: #e2e8f0;
}

.dark-mode .stat-label {
  color: #94a3b8;
}

.dark-mode .stat-value {
  color: #e2e8f0;
}

.dark-mode .chart-card {
  background-color: #1e293b;
  color: #e2e8f0;
}

.dark-mode .chart-title {
  color: #e2e8f0;
}

.dark-mode .map-card {
  background-color: #1e293b;
  color: #e2e8f0;
}

.dark-mode .map-title {
  color: #e2e8f0;
}

.dark-mode .page-title {
  color: #e2e8f0;
}

.dark-mode .flights-table {
  background-color: #1e293b;
  color: #e2e8f0;
}
</style>