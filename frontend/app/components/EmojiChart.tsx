"use client";

import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell, LabelList } from 'recharts';

interface EmojiItem {
  text: string;
  value: number;
}

interface DynamicEmojiChartProps {
  emojis: EmojiItem[];
}

export default function DynamicEmojiChart({ emojis }: DynamicEmojiChartProps) {
  if (!emojis || emojis.length === 0) {
    return <p className="text-center text-gray-500 py-6">No hay datos de emojis disponibles.</p>;
  }

  const dynamicHeight = (emojis.length * 45) + 60;

  const getDynamicColor = (index: number, total: number) => {
    const minOpacity = 0.3;
    const maxOpacity = 1.0;
    const opacity = total > 1 
      ? maxOpacity - (index / (total - 1)) * (maxOpacity - minOpacity) 
      : maxOpacity;
    return `rgba(79, 70, 229, ${opacity})`;
  };

  return (
    <div className="w-full bg-gray-800 p-4 rounded-md shadow-sm">
      
      <div className="w-full" style={{ height: `${dynamicHeight}px` }}>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart 
            data={emojis} 
            layout="vertical" 
            margin={{ top: 10, right: 35, left: 15, bottom: 5 }}
          >
            <XAxis type="number" hide />
            
            <YAxis 
              dataKey="text" 
              type="category" 
              tick={{ fontSize: 22 }} 
              axisLine={false} 
              tickLine={false} 
              width={35}
            />
            
            <Tooltip cursor={false} formatter={(value) => [`${value} usos`, 'Cantidad']} />
            
            <Bar dataKey="value" radius={[0, 4, 4, 0]} barSize={20}>
              {emojis.map((entry, index) => (
                <Cell 
                  key={`cell-${index}`} 
                  fill={getDynamicColor(index, emojis.length)} 
                />
              ))}
              
              <LabelList 
                dataKey="value" 
                position="right" 
                fill="#FFFFFF" 
                className="text-xs font-bold" 
                offset={8} 
              />
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}