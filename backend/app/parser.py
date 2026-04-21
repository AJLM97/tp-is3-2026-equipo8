import re

REGEX_INICIO = r"^(\d{1,2}/\d{1,2}/\d{2,4})\s(\d{1,2}:\d{2})\s-\s"

def process_chat(chat_text: str):
    lines = chat_text.splitlines()
    parsed_messages = []
    current_message = None

    for line in lines:
        match_inicio = re.match(REGEX_INICIO, line)
        if match_inicio:
            if current_message:
                parsed_messages.append(current_message)
            
            date, hour = match_inicio.group(1), match_inicio.group(2)
            resto = line[match_inicio.end():]
            
            user, message = resto.split(": ", 1) if ": " in resto else ("Sistema", resto)
            current_message = {"date": date, "hour": hour, "user": user.strip(), "message": message.strip()}
        else:
            if current_message:
                current_message["message"] += " " + line.strip()

    if current_message:
        parsed_messages.append(current_message)
    return parsed_messages
