def filter_alerts(alerts, minimum_severity):
    severity_levels = ["ADVISORY", "WATCH", "WARNING"]
    minimum_index = severity_levels.index(minimum_severity)
    filtered_alerts = []

    for alert in alerts:
        if alert.strip() == "":
            continue
        parts = alert.split(" - ")
        if len(parts) != 3:
            continue
        severity_and_location = parts[0]
        description = parts[2]

        if "] " not in severity_and_location:
            continue
        severity_part, location = severity_and_location.split("] ")
        severity = severity_part.replace("[", "")

        if severity not in severity_levels:
            continue
        if severity_levels.index(severity) >= minimum_index:
            summary = f"{severity} ({location}): {description}"
            filtered_alerts.append(summary)

    return filtered_alerts
weather_data = [
    "[ADVISORY] Austin - 11/05 08:00 - Dense fog reported.",
    "[ADVISORY] Dallas - 11/05 08:15 - Light rain expected.",
    "[WATCH] Houston - 11/05 12:00 - Conditions favorable for tornadoes.",
    "",
    "[WARNING] Galveston - 11/05 14:30 - Hurricane making landfall.",
    "[WARNING] Miami - 11/05 15:00 - Flash flooding imminent.",
    "[ADVISORY] Seattle - 11/05 16:00 - Light drizzle."
]
print(filter_alerts(weather_data, "WATCH"))
print(filter_alerts(weather_data, "WARNING"))


