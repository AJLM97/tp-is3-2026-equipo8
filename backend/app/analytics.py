from collections import Counter

# 1.2.1 Cantidad de mensajes
def obtener_cantidad_mensajes(mensajes: list) -> int:
    return len(mensajes)

# 1.2.2 Usuario que envió más mensajes
def usuario_mas_activo(mensajes: list) -> dict:
    usuarios = [m["user"] for m in mensajes if m.get("user") != "Sistema"]
    
    if not usuarios: 
        return {"user": "N/A", "messages_total": 0}
    
    conteo = Counter(usuarios)
    nombre, cantidad = conteo.most_common(1)[0]
    
    return {"user": nombre, "messages_total": cantidad}

# 1.2.3 Franja horaria con mayor actividad
def franja_horaria_pico(mensajes: list) -> dict:
    horas = [m["hour"].split(":")[0] for m in mensajes if "hour" in m]
    
    if not horas:
        return {"peak_time": "N/A", "messages_total": 0}
    
    conteo = Counter(horas)
    hora_pico, cantidad = conteo.most_common(1)[0]
    
    return {
        "peak_time": f"{hora_pico}:00 - {hora_pico}:59",
        "messages_total": cantidad
    }

# 1.2.4 Tres días con mayor cantidad de mensajes
def dias_mas_activos(mensajes: list) -> list:
    fechas = [m["date"] for m in mensajes if "date" in m]
    
    if not fechas:
        return []
    
    conteo = Counter(fechas)
    top_dias = conteo.most_common(3)
    
    return [{"date": fecha, "messages_total": cantidad} for fecha, cantidad in top_dias]


# ---- Nuevas funciones para gráficos ----
def hour_buckets(mensajes: list) -> list:
    """Devuelve una lista de 24 enteros con el conteo de mensajes por hora (0..23)."""
    buckets = [0] * 24
    for m in mensajes:
        h = None
        # soporte tanto 'hour' como 'hour' string 'HH:MM' o entero
        if "hour" in m and m["hour"] is not None:
            hour_val = m["hour"]
            try:
                if isinstance(hour_val, int):
                    h = hour_val
                else:
                    # si viene como '07:15' o '7:15'
                    h = int(str(hour_val).split(":")[0])
            except Exception:
                h = None

        if h is not None and 0 <= h < 24:
            buckets[h] += 1

    return buckets


def top_users(mensajes: list, n: int = 10) -> list:
    """Devuelve una lista de dicts {user, count} con los n usuarios más activos."""
    usuarios = [m.get("user") or "Unknown" for m in mensajes if m.get("user") != "Sistema"]
    conteo = Counter(usuarios)
    return [{"user": u, "count": c} for u, c in conteo.most_common(n)]

