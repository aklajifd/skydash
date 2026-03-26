<template>
  <div class="home">
    <div class="page-header">
      <h1 class="page-title">
        <i class="pi pi-globe"></i>
        Live Flight Dashboard
      </h1>
      <PrimeButton
        label="Refresh Flights"
        icon="pi pi-refresh"
        :loading="store.loading"
        @click="loadFlights"
      />
    </div>

    <div class="stats-row">
      <div class="stat-card">
        <span class="stat-label">Total Flights</span>
        <span class="stat-value">{{ store.liveFlights.length }}</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">Countries</span>
        <span class="stat-value">{{ uniqueCountries }}</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">Airborne</span>
        <span class="stat-value">{{ airborneCount }}</span>
      </div>
    </div>

    <div v-if="store.error" class="error-message">
      {{ store.error }}
    </div>

    <div v-if="store.loading" class="loading-message">
      <i class="pi pi-spin pi-spinner"></i>
      Fetching live flight data...
    </div>

    <DataTable
      v-else
      :value="store.liveFlights"
      :paginator="true"
      :rows="20"
      stripedRows
      class="flights-table"
    >
      <Column field="icao24" header="ICAO24" />
      <Column field="callsign" header="Callsign" />
      <Column field="origin_country" header="Country" />
      <Column field="altitude" header="Altitude (m)">
        <template #body="{ data }">
          {{ data.altitude ? Math.round(data.altitude) + 'm' : 'N/A' }}
        </template>
      </Column>
      <Column field="velocity" header="Speed (m/s)">
        <template #body="{ data }">
          {{ data.velocity ? Math.round(data.velocity) + ' m/s' : 'N/A' }}
        </template>
      </Column>
      <Column field="heading" header="Heading">
        <template #body="{ data }">
          {{ data.heading ? Math.round(data.heading) + '°' : 'N/A' }}
        </template>
      </Column>
    </DataTable>
  </div>
</template>

<script>
import { useFlightsStore } from '../stores/flights'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import PrimeButton from 'primevue/button'

export default {
  name: 'HomeView',
  components: { DataTable, Column, PrimeButton },

  setup() {
    const store = useFlightsStore()
    return { store }
  },

  computed: {
    uniqueCountries() {
      const countries = this.store.liveFlights.map((f) => f.origin_country).filter(Boolean)
      return new Set(countries).size
    },
    airborneCount() {
      return this.store.liveFlights.filter((f) => f.altitude && f.altitude > 0).length
    },
  },

  mounted() {
    this.loadFlights()
  },

  methods: {
    async loadFlights() {
      await this.store.fetchLiveFlights()
    },
  },
}
</script>

<style scoped>
.page-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2rem;
}

.page-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #0f172a;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.stats-row {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  flex: 1;
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
}

.stat-label {
  font-size: 0.875rem;
  color: #64748b;
  font-weight: 500;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: #0f172a;
}

.error-message {
  background: #fee2e2;
  color: #dc2626;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.loading-message {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: #64748b;
  font-size: 1rem;
  padding: 2rem;
}

.flights-table {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
}
</style>
