import re
from datetime import datetime


def transform_logs(input_text: str) -> str:
    #Hide email addresses
    input_text = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        '[HIDDEN]',
        input_text
    )

    #Normalize timestamps
    def format_timestamp(match):
        date_time = match.group()
        dt = datetime.strptime(date_time, "%d/%m/%Y %H:%M")

        day = dt.day

        # Add ordinal suffix (st, nd, rd, th)
        if 10 <= day <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

        formatted_date = f"{day}{suffix} {dt.strftime('%B %Y')}"
        formatted_time = dt.strftime("%I:%M %p").lstrip("0")

        return f"{formatted_date}, {formatted_time}"

    input_text = re.sub(
        r'\b\d{2}/\d{2}/\d{4} \d{2}:\d{2}\b',
        format_timestamp,
        input_text
    )

    #Add fun flag before errors
    input_text = re.sub(
        r'\bERROR\b',
        '🚨 ERROR',
        input_text
    )

    # Transformation 4: Clean extra spaces but preserve new lines
    input_text = re.sub(r'[ \t]+', ' ', input_text)

    # Remove trailing spaces from each line
    input_text = "\n".join(line.strip() for line in input_text.splitlines())

    return input_text


# Example usage
log = """
User john@mail.com logged in at 23/08/2025 14:05. ERROR: session timeout.
Another ERROR occurred at 24/08/2025 09:30.
"""

print(transform_logs(log))