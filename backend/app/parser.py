import re

# Formato viejo: 31/3/2026 18:11 - Usuario:
REGEX_VIEJO = r"^(\d{1,2}/\d{1,2}/\d{2,4})\s(\d{1,2}:\d{2})\s-\s"

# Formato nuevo entre corchetes: [31/3/26, 18:11:22] Usuario:
REGEX_NUEVO = r"^\[(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2}):\d{2}\]\s"

# Formato nuevo con coma y p.m./a.m.: 31/3/2026, 6:11 p. m. - Usuario:
# Nota: \s? soporta espacios normales y espacios invisibles de no ruptura (\u202f)
REGEX_NUEVO_COMA = r"^(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2})\s?([ap]\.\s?m\.)\s-\s"

def process_chat(chat_text: str):
    lines = chat_text.splitlines()
    parsed_messages = []
    current_message = None

    for line in lines:
        # Buscamos coincidencias en los tres formatos
        match_viejo = re.match(REGEX_VIEJO, line)
        match_nuevo = re.match(REGEX_NUEVO, line)
        match_nuevo_coma = re.match(REGEX_NUEVO_COMA, line)

        match_inicio = match_viejo or match_nuevo or match_nuevo_coma

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
