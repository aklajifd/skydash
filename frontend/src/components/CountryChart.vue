<template>
    <div class="chart-card">
        <h2 class="chart-title">
            <i class="pi pi-chart-bar"></i>
            Top 10 Countries by Flight Count
        </h2>
        <Bar :data="chartData" :options="chartOptions" />
    </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
    name: 'CountryChart',
    components: { Bar },

    props: {
        flights: {
            type: Array,
            default: () => []
        }
    },

    computed: {
        countryCounts() {
            const counts = {}
            this.flights.forEach(f => {
                if (f.origin_country) {
                    counts[f.origin_country] = (counts[f.origin_country] || 0) + 1
                }
            })
            return Object.entries(counts)
                .sort((a, b) => b[1] - a[1])
                .slice(0, 10)
        },

        chartData() {
            return {
                labels: this.countryCounts.map(([country]) => country),
                datasets: [
                    {
                        label: 'Flights',
                        data: this.countryCounts.map(([, count]) => count),
                        backgroundColor: '#38bdf8',
                        borderColor: '#0284c7',
                        borderWidth: 1,
                        borderRadius: 6
                    }
                ]
            }
        },

        chartOptions() {
            const isDark = document.documentElement.classList.contains('dark-mode')
            return {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    title: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: { color: isDark ? '#334155' : '#f1f5f9' },
                        ticks: { color: isDark ? '#94a3b8' : '#64748b' }
                    },
                    x: {
                        grid: { display: false },
                        ticks: { color: isDark ? '#94a3b8' : '#64748b' }
                    }
                }
            }
        }
    }
}
</script>

<style scoped>
.chart-card {
    background: var(--card-bg, white);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
}

.chart-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--title-color, #0f172a);
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

:global(.dark-mode) {
    --card-bg: #1e293b;
    --title-color: #e2e8f0;
}
</style>