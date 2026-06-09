import re

# Formato viejo: 31/3/2026 18:11 - Usuario:
REGEX_VIEJO = r"^(\d{1,2}/\d{1,2}/\d{2,4})\s(\d{1,2}:\d{2})\s-\s"

# Formato nuevo entre corchetes: [31/3/26, 18:11:22] Usuario:
REGEX_NUEVO = r"^\[(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2}):\d{2}\]\s"

# Formato nuevo con coma y p.m./a.m.: 31/3/2026, 6:11 p. m. - Usuario:
# Nota: \s? soporta espacios normales y espacios invisibles de no ruptura (\u202f)
REGEX_NUEVO_COMA = r"^(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2})\s?([ap]\.\s?m\.)\s-\s"

# Formato nuevo con coma pero sin a.m./p.m. (24 horas): 9/6/2026, 04:21 - Usuario:
REGEX_NUEVO_24H = r"^(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2})\s-\s"

def process_chat(chat_text: str):
    lines = chat_text.splitlines()
    parsed_messages = []
    current_message = None

    for line in lines:
        # Buscamos coincidencias en los tres formatos
        match_viejo = re.match(REGEX_VIEJO, line)
        match_nuevo = re.match(REGEX_NUEVO, line)
        match_nuevo_coma = re.match(REGEX_NUEVO_COMA, line)
        match_nuevo_24h = re.match(REGEX_NUEVO_24H, line)

        match_inicio = match_viejo or match_nuevo or match_nuevo_coma or match_nuevo_24h

        if match_inicio:
            if current_message:
                parsed_messages.append(current_message)
            
            date = match_inicio.group(1)
            
            # Si coincide con el formato de coma y AM/PM, unificamos la hora
            if match_nuevo_coma:
                hour = f"{match_inicio.group(2)} {match_inicio.group(3)}".replace("\u202f", " ")
            else:
                hour = match_inicio.group(2)

            resto = line[match_inicio.end():]
            
            if ": " in resto:
                user, message = resto.split(": ", 1)
            else:
                user, message = "Sistema", resto

            current_message = {
                "date": date,
                "hour": hour,
                "user": user.strip(),
                "message": message.strip()
            }

        else:
            if current_message:
                current_message["message"] += " " + line.strip()

    if current_message:
        parsed_messages.append(current_message)

    return parsed_messages

STOP_WORDS = {"el", "la", "los", "las", "un", "una",
              "con", "para", "por", "en", "a",
              "y", "o", "pero", "que",
              "yo", "tú", "él", "ella", "usted", "vos", "nosotros", "vosotros", "me", "te", "se", "nos", "os",
              "mi", "tu", "su", "nuestro", "vuestro",
              "es", "son", "fue", "han", "está", "están", "era", "eran", "será", "serán",
              "sí", "no", "si", "este", "esta", "estos", "estas", "eso", "esa", "esos", "esas",
              "aquí", "allí", "allá", "ahí",
              "del", "al", "lo", "le", "les",}

def limpiar_texto_mensaje(texto_original: str) -> list:
    """Limpia un texto individual y devuelve una lista de palabras filtradas válidas."""
    if not texto_original or not isinstance(texto_original, str):
        return []
        
    texto = texto_original.lower()
    
    texto = re.sub(r'http\S+|www\S+', '', texto)
    
    palabras = re.findall(r'\b[a-záéíóúüñ]+\b', texto)
    
    return [w for w in palabras if w not in STOP_WORDS and len(w) > 2]