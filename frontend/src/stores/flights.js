import { defineStore } from 'pinia'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'

export const useFlightsStore = defineStore('flights', {
  state: () => ({
    liveFlights: [],
    historyFlights: [],
    loading: false,
    error: null,
  }),

  actions: {
    async fetchLiveFlights() {
      this.loading = true
      this.error = null
      try {
        const response = await fetch(`${API_BASE_URL}/flights/`)
        if (!response.ok) throw new Error('Failed to fetch flights')
        this.liveFlights = await response.json()
      } catch (err) {
        this.error = err.message
      } finally {
        this.loading = false
      }
    },

    async fetchFlightHistory() {
      this.loading = true
      this.error = null
      try {
        const response = await fetch(`${API_BASE_URL}/flights/history`)
        if (!response.ok) throw new Error('Failed to fetch history')
        this.historyFlights = await response.json()
      } catch (err) {
        this.error = err.message
      } finally {
        this.loading = false
      }
    },
  },
})
