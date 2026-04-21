"use client";
import { useState, useEffect, useCallback } from "react";

export default function FileUploader() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  const handleUpload = useCallback(async (selectedFile: File) => {
    setLoading(true);
    setResult(null);
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("http://localhost:8000/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error("Error en la subida");

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Error al conectar con el backend");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    if (file) {
      handleUpload(file);
    }
  }, [file, handleUpload]);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-6 bg-gray-50 text-gray-800">
      <div className="w-full max-w-md bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
        
        <div className="p-8">
          <h1 className="text-2xl font-bold mb-6 text-center text-gray-900">
            Analizador de WhatsApp
          </h1>

          <div
            onDragOver={(e) => e.preventDefault()}
            onDrop={(e) => {
              e.preventDefault();
              if (e.dataTransfer.files?.[0]) {
                setFile(e.dataTransfer.files[0]);
              }
            }}
            className="relative border-2 border-dashed border-blue-400 rounded-lg p-10 text-center hover:bg-blue-50 transition-colors group"
          >
            <input
              type="file"
              accept=".zip,.txt"
              onChange={(e) => setFile(e.target.files?.[0] || null)}
              className="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-10"
              id="fileInput"
            />

            <div className="flex flex-col items-center justify-center space-y-2">
              <span className="text-gray-600 group-hover:text-blue-600 transition-colors">
                {file ? (
                  <strong className="text-blue-600">{file.name}</strong>
                ) : (
                  "Arrastra o selecciona tu archivo .zip o .txt"
                )}
              </span>
              {loading && (
                <p className="text-sm text-blue-500 animate-pulse font-medium">
                  Analizando archivo...
                </p>
              )}
            </div>
          </div>

          {result && (
            <div className="mt-6 p-4 bg-gray-900 rounded-lg animate-in fade-in slide-in-from-bottom-2 duration-300">
              <div className="flex justify-between items-center mb-2">
                <span className="text-green-400 text-xs font-mono">Análisis listo:</span>
                <button onClick={() => setResult(null)} className="text-gray-500 hover:text-white text-xs">Ocultar</button>
              </div>
              <pre className="text-white text-[10px] overflow-auto max-h-48 custom-scrollbar">
                {JSON.stringify(result, null, 2)}
              </pre>
            </div>
          )}
        </div>

        <div className="bg-gray-100 p-6 border-t border-gray-200">
          <h2 className="text-sm font-bold text-gray-700 mb-3 uppercase tracking-wider">
            ¿Cómo obtener el archivo?
          </h2>
          <ul className="space-y-3 text-sm text-gray-600">
            <li className="flex gap-3">
              <span className="flex-none flex items-center justify-center w-5 h-5 bg-blue-100 text-blue-600 rounded-full text-xs font-bold">1</span>
              <span>Abre el chat de <strong>WhatsApp</strong> que deseas analizar.</span>
            </li>
            <li className="flex gap-3">
              <span className="flex-none flex items-center justify-center w-5 h-5 bg-blue-100 text-blue-600 rounded-full text-xs font-bold">2</span>
              <span>Presiona el botón de opciones <strong>"⋮"</strong>.</span>
            </li>
            <li className="flex gap-3">
              <span className="flex-none flex items-center justify-center w-5 h-5 bg-blue-100 text-blue-600 rounded-full text-xs font-bold">3</span>
              <span>Selecciona <strong>"Más"</strong> y luego presiona <strong>"Exportar chat"</strong>.</span>
            </li>
            <li className="flex gap-3">
              <span className="flex-none flex items-center justify-center w-5 h-5 bg-blue-100 text-blue-600 rounded-full text-xs font-bold">4</span>
              <span>Elige <strong>"Sin archivos"</strong> para generar el <strong>.txt</strong> o <strong>"Incluir archivos"</strong> para generar el <strong>.zip</strong>.</span>
            </li>
          </ul>
        </div>
      </div>
    </main>
  );
}
