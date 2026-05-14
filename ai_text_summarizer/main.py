import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))

# Text to summarize
text = """
Python automation is useful for APIs,
data processing, reporting, AI workflows,
and business automation.
"""

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": f"Summarize this text in one sentence:\n\n{text}"
            }
        ]
    )

    summary = response.choices[0].message.content

    print("\n=== AI SUMMARY ===")
    print(summary)

    # Save output
    with open("summary.txt", "w") as file:
        file.write(summary)

    print("\n✓ Saved summary.txt")

except Exception as error:
    print(f"Error: {error}")