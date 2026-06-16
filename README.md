# Analizador de Chats de WhatsApp

Proyecto desarrollado para la asignatura [Ingeniería de Software 3] - [2026 - Primer Cuatrimestre].
Este software permite analizar un chat grupal de WhatsApp exportado y genera visualizaciones dinámicas con estadísticas relevantes sobre la interacción entre los participantes.

## 👥 Equipo de Trabajo
- **Alejandro Javier Ledesma Miño** (@AJLM97) - Desarrollador
- **Aylén Ortiz** (@lady-coder-16) - Documentadora
- **Candela Fernández** (@candef582) - Desarrolladora
- **Thomas Vogt** (@Thomy98) - Desarrollador
- **Juan Bautista Boullon** (@JuanBa7) - Desarrollador

## 🛠️ Estructura del Proyecto
El repositorio utiliza una arquitectura de monorepositorio:
- `/backend`: Lógica de procesamiento y análisis construida sobre **FastAPI** y validada mediante **Pydantic v2**.
- `/frontend`: Interfaz de usuario desarrollada en **Next.js**, utilizando **React**. Estilizado mediante **Tailwind CSS v4**.

## 🚀 Guía de Instalación y Ejecución Local (1era vez)

Primero, clonar el repositorio (utilizando el comando de `git clone`) e ingresar a la carpeta raíz del proyecto:

### 🐍 Entorno del Backend
**Requisitos:** Python 3.10 o superior.

1. Una vez dentro de la carpeta del proyecto, navegar al directorio del backend:
```
   cd backend
```
2. Crear y activar el entorno virtual:
- **Windows**:
  ```
  python -m venv venv
  ```
  y luego
  ```
  .\venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```
  python -m venv venv
  ```
  y luego
  ```
  source venv/bin/activate
  ```

3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```
   
4. Levantar el servidor de desarrollo:
   ```
   uvicorn main:app --reload
   ```

### 📦 Entorno del Frontend
**Requisitos:** Node.js 18 o superior.

1. Navegar al directorio del frontend:
```
   cd frontend
```
2. Instalar el árbol de módulos de Node:
```
   npm install
```
3. Iniciar el servidor de desarrollo de Next.js:
```
   npm run dev
```

## 📎Links útiles para entorno local:
###  `🐍  Backend`
- API local: <http://localhost:8000/>
- Documentación interactiva de (Swagger): <http://localhost:8000/docs>

###  `📦  Frontend`
- Aplicación local en el navegador: <http://localhost:3000/>
  

## ⚡ Ejecución Rápida (2da vez en adelante)
Si ya realizó la instalación inicial y quiere volver a levantar los servidores en una nueva terminal, ejecute lo siguiente desde la raíz del proyecto:

###  `🐍  Backend`
- En **Windows**:
```
cd backend
.\venv\Scripts\activate
uvicorn main:app --reload
```
- o en **macOS/Linux**:
```
cd backend
source venv/bin/activate
uvicorn main:app --reload
```

###  `📦  Frontend`
```
cd frontend
npm run dev
```

> ⚠️ **Nota importante**: Si se realizaron cambios en las dependencias (actualizaciones en `requirements.txt` o `package.json`), antes de levantar los servidores recuerde ejecutar `pip install -r requirements.txt` en el `🐍backend` o `npm install` en el `📦frontend` según corresponda para actualizar el entorno local.

## 🚀 Estrategia de Branching
Nuestro equipo utilizó **GitHub Flow**:
1. La rama `main` siempre está lista para producción.
2. Cada nueva funcionalidad o tarea del cronograma se trabaja en una rama `feature/`.
3. Todo el código se integra mediante **Pull Requests** con revisión por pares.

---

## 🌐 Índice de Documentación Técnica (Wiki de GitHub)

Para comprender en profundidad las decisiones de diseño arquitectónico y de algoritmos implementados en el código fuente, explore las páginas de nuestra Wiki:

1. **[Home](https://github.com/AJLM97/tp-is3-2026-equipo8/wiki)**: Portal de bienvenida e índice de navegación técnica.
2. **[Arquitectura del Proyecto](https://github.com/AJLM97/tp-is3-2026-equipo8/wiki/Arquitectura-del-Proyecto)**: Desglose modular y justificación de la estrategia de procesamiento efímero en memoria RAM (*Privacy by Design*).
3. **[Módulo Parser](https://github.com/AJLM97/tp-is3-2026-equipo8/wiki/Modulo-Parser)**: Análisis técnico de las 4 expresiones regulares para el soporte multiformato y lógica multilínea.
4. **[Módulo Estadístico](https://github.com/AJLM97/tp-is3-2026-equipo8/wiki/Modulo-Estadistico)**: Algorítmica de limpieza, remoción de elementos multimedia, filtrado de *Stop Words*, sanitización Unicode de emojis y optimización horaria.
