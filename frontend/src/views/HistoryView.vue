<template>
  <div class="history">
    <div class="page-header">
      <h1 class="page-title">
        <i class="pi pi-history"></i>
        Flight History
      </h1>
      <PrimeButton
        label="Refresh History"
        icon="pi pi-refresh"
        :loading="store.loading"
        @click="loadHistory"
      />
    </div>

    <div v-if="store.error" class="error-message">
      {{ store.error }}
    </div>

    <div v-if="store.loading" class="loading-message">
      <i class="pi pi-spin pi-spinner"></i>
      Loading flight history...
    </div>

    <DataTable
      v-else
      :value="store.historyFlights"
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
      <Column field="recorded_at" header="Recorded At">
        <template #body="{ data }">
          {{ formatDate(data.recorded_at) }}
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
  name: 'HistoryView',
  components: { DataTable, Column, PrimeButton },

  setup() {
    const store = useFlightsStore()
    return { store }
  },

  mounted() {
    this.loadHistory()
  },

  methods: {
    async loadHistory() {
      await this.store.fetchFlightHistory()
    },

    formatDate(dateString) {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleString()
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
