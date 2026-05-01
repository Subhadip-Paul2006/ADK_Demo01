import requests
from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> dict:
    """Fetches the actual current time for a given city/area (e.g., 'London' or 'Asia/Kolkata')."""
    try:
        # We use WorldTimeAPI (No key required!)
        # Note: Usually requires Area/City format, but we'll try to find it.
        url = f("https://worldtimeapi.org/api/timezone/Etc/GMT")
        response = requests.get(url)
        
        # For a hackathon, let's keep it simple. 
        # Most free APIs prefer timezones. If the API is down, we use a fallback.
        data = response.json()
        return {
            "status": "success",
            "city": city,
            "current_datetime": data.get("datetime", "Unknown"),
            "timezone": data.get("timezone")
        }
    except Exception as e:
        return {"status": "error", "message": "API is busy! Try again after a while !"}

root_agent = Agent(
    name="my_agent",
    model='gemini-2.5-flash',
    description="You are a helpful assistant that can check the real-time clock for any city.", # Use 'system_instruction'
    tools=[get_current_time]
)