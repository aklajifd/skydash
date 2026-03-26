<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <i class="pi pi-send" style="font-size: 1.5rem"></i>
      <span class="brand-name">SkyDash</span>
    </div>
    <div class="navbar-links">
      <RouterLink to="/" class="nav-link">Dashboard</RouterLink>
      <RouterLink to="/history" class="nav-link">History</RouterLink>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar'
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
</style>