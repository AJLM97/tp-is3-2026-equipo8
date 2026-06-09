"use client";
import { useEffect, useState, useMemo, useCallback } from 'react';
// @ts-ignore
import CloudRenderer from 'react-d3-cloud';

export default function WordCloud({ words }: any) {
  const [isClient, setIsClient] = useState(false);
  useEffect(() => setIsClient(true), []);

  const [min, max] = useMemo(() => {
    if (!words || words.length === 0) return [0, 0];
    const vals = words.map((w: any) => w.value);
    return [Math.min(...vals), Math.max(...vals)];
  }, [words]);

  const fontSize = useCallback((word: any) => {
    if (max === min) return 20;
    return 14 + ((word.value - min) / (max - min)) * (65 - 14);
  }, [min, max]);

  if (!isClient || !words) return null;

  return (
    <div className="bg-gray-800 p-4 rounded-md shadow-sm w-full">
      <CloudRenderer
        data={words}
        width={600}
        height={340}
        font="sans-serif"
        fontSize={fontSize}
        padding={3}
      />
    </div>
  );
}
