"use client";
import { useState, useEffect, useCallback } from "react";

export default function FileUploader() {

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-6 bg-gray-50 text-gray-800">
      <div className="w-full max-w-md bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">

        <div className="p-8">
          <h1 className="text-2xl font-bold mb-6 text-center text-gray-900">
            Analizador de WhatsApp
          </h1>

          <div className="relative border-2 border-dashed border-blue-400 rounded-lg p-10 text-center hover:bg-blue-50 transition-colors group">
            <div className="flex flex-col items-center justify-center space-y-2">
                <span className="text-gray-600 group-hover:text-blue-600 transition-colors">
                    Arrastra o selecciona tu archivo .zip o .txt
                </span>
            </div>
          </div>
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
