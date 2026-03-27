<template>
    <div class="map-card">
        <h2 class="map-title">
            <i class="pi pi-map"></i>
            Live Flight Map
        </h2>
        <div id="flight-map" class="map-container"></div>
    </div>
</template>

<script>
import L from 'leaflet'
import { nextTick } from 'vue'

delete L.Icon.Default.prototype._getIconUrl
L.Icon.Default.mergeOptions({
    iconRetinaUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png',
    iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
    shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png'
})

export default {
    name: 'FlightMap',

    props: {
        flights: {
            type: Array,
            default: () => []
        }
    },

    data() {
        return {
            map: null,
            markers: []
        }
    },

    watch: {
        flights(newFlights) {
            this.updateMarkers(newFlights)
        }
    },

    mounted() {
        nextTick(() => {
            this.initMap()
        })
    },

    beforeUnmount() {
        if (this.map) {
            this.map.remove()
        }
    },

    methods: {
        initMap() {
            this.map = L.map('flight-map').setView([20, 0], 2)

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(this.map)

            this.updateMarkers(this.flights)
        },

        updateMarkers(flights) {
            this.markers.forEach(marker => marker.remove())
            this.markers = []

            const validFlights = flights.filter(
                f => f.latitude && f.longitude &&
                    f.latitude >= -90 && f.latitude <= 90 &&
                    f.longitude >= -180 && f.longitude <= 180
            )

            validFlights.forEach(flight => {
                const marker = L.marker([flight.latitude, flight.longitude])
                    .bindPopup(`
            <strong>${flight.callsign || 'Unknown'}</strong><br/>
            Country: ${flight.origin_country || 'N/A'}<br/>
            Altitude: ${flight.altitude ? Math.round(flight.altitude) + 'm' : 'N/A'}<br/>
            Speed: ${flight.velocity ? Math.round(flight.velocity) + ' m/s' : 'N/A'}
          `)
                    .addTo(this.map)
                this.markers.push(marker)
            })
        }
    }
}
</script>

<style scoped>
.map-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
}

.map-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.map-container {
    height: 500px;
    border-radius: 8px;
    overflow: hidden;
}
</style>