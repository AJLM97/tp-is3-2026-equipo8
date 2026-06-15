"use client";

import { useEffect, useState } from 'react';
import { WordCloud as IsoterikCloud } from '@isoterik/react-word-cloud';

interface WordItem {
  text: string;
  value: number;
}

interface WordCloudProps {
  words: WordItem[];
}

export default function WordCloud({ words }: WordCloudProps) {
  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    setIsClient(true);
  }, []);

  if (!isClient || !words || words.length === 0) {
    return <p className="text-center text-gray-500 py-6">No hay palabras disponibles.</p>;
  }

  const topWords = [...words]
    .sort((a, b) => b.value - a.value)
    .slice(0, 50);

  const values = topWords.map((w) => w.value);
  const minValue = Math.min(...values);
  const maxValue = Math.max(...values);
  const minFontSize = 12;
  const maxFontSize = 50;
  const fontSize = (word: WordItem) => {
    if (maxValue === minValue) {
      return minFontSize;
    }
    const normalized = (word.value - minValue) / (maxValue - minValue);
    return Math.round(minFontSize + normalized * (maxFontSize - minFontSize));
  };

  const data = topWords.map(w => ({
    text: w.text,
    value: w.value
  }));

  return (
    <div className="bg-gray-800 w-full mx-auto overflow-hidden">
      <div className="w-full flex items-center mx-auto justify-center">
        <IsoterikCloud 
          words={data} 
          width={600}
          height={300}
          fontSize={fontSize}
          padding={4}
          spiral="archimedean"
          random={() => 0.5}
        />
      </div>
    </div>
  );
}
