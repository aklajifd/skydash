<template>
  <nav :class="['navbar', { 'dark-mode': themeStore.isDarkMode }]">
    <div class="navbar-brand">
      <i class="pi pi-send" style="font-size: 1.5rem"></i>
      <span class="brand-name">SkyDash</span>
    </div>
    <div class="navbar-links">
      <RouterLink to="/" class="nav-link">Dashboard</RouterLink>
      <RouterLink to="/history" class="nav-link">History</RouterLink>
      <button class="theme-toggle" @click="themeStore.toggleDarkMode">
        <i :class="themeStore.isDarkMode ? 'pi pi-sun' : 'pi pi-moon'"></i>
      </button>
    </div>
  </nav>
</template>

<script>
import { useThemeStore } from '../stores/theme'

export default {
  name: 'NavBar',

  setup() {
    const themeStore = useThemeStore()
    return { themeStore }
  }
}
</script>

<style scoped>
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 2rem;
  background-color: #0f172a;
  color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.navbar-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.brand-name {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: #38bdf8;
}

.navbar-links {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-link {
  color: #cbd5e1;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
}

.nav-link:hover {
  color: #38bdf8;
}

.theme-toggle {
  background: none;
  border: 1px solid #334155;
  color: #cbd5e1;
  width: 2.25rem;
  height: 2.25rem;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.theme-toggle:hover {
  background-color: #1e293b;
  color: #38bdf8;
  border-color: #38bdf8;
}
</style>