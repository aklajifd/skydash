import { defineStore } from 'pinia'

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
        const response = await fetch('http://127.0.0.1:8000/flights/')
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
        const response = await fetch('http://127.0.0.1:8000/flights/history')
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
