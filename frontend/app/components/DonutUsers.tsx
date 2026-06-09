"use client"
import { Doughnut } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js'

ChartJS.register(ArcElement, Tooltip, Legend)

type UserCount = { user: string; count: number }

type Props = {
  topUsers: UserCount[]
}

export default function DonutUsers({ topUsers }: Props) {
  const labels = (topUsers || []).map((u) => u.user)
  const dataValues = (topUsers || []).map((u) => u.count)

  const data = {
    labels,
    datasets: [
      {
        // no dataset label (title will be the single descriptor)
        label: '',
        data: dataValues,
        backgroundColor: [
          '#ef4444',
          '#f59e0b',
          '#f97316',
          '#facc15',
          '#34d399',
          '#60a5fa',
          '#a78bfa',
          '#fb7185',
          '#94a3b8',
          '#c084fc',
        ],
      },
    ],
  }

  const options = {
    maintainAspectRatio: false,
    responsive: true,
    plugins: { legend: { position: 'right' as const, labels: { color: 'rgba(255,255,255,0.9)' } } },
  }

  return (
    <div className="bg-gray-800 p-4 rounded-md shadow-sm">
      <h3 className="text-green-400 font-bold mb-2" style={{ textShadow: '0 1px 4px rgba(0,0,0,0.8)' }}>
        Usuarios más activos
      </h3>
      <div className="h-56 md:h-72 flex items-center justify-center">
        <Doughnut data={data} options={options} />
      </div>
    </div>
  )
}
