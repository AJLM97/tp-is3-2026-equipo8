"use client"
import { Bar } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

type Props = {
  buckets: number[]
}

export default function BarHours({ buckets }: Props) {
  const labels = Array.from({ length: 24 }, (_, i) => `${i}:00`)

  const data = {
    labels,
    datasets: [
      {
        // dataset label removed to avoid duplicating the title
        label: '',
        data: buckets || Array.from({ length: 24 }, () => 0),
        backgroundColor: 'rgba(59,130,246,0.9)',
      },
    ],
  }

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      // hide legend so the title is the single descriptor
      legend: { display: false as const },
      title: { display: false },
    },
    scales: {
      x: { ticks: { maxRotation: 0, autoSkip: true, color: 'rgba(255,255,255,0.85)' }, grid: { color: 'rgba(255,255,255,0.06)' } },
      y: { ticks: { color: 'rgba(255,255,255,0.85)' }, grid: { color: 'rgba(255,255,255,0.06)' } },
    },
  }

  return (
    <div className="bg-gray-800 p-4 rounded-md shadow-sm">
      <h3 className="text-green-400 font-bold mb-2" style={{ textShadow: '0 1px 4px rgba(0,0,0,0.8)' }}>
        Mensajes por hora
      </h3>
      <div className="h-56 md:h-72">
        <Bar data={data} options={options} />
      </div>
    </div>
  )
}
