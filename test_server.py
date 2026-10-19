import asyncio
from server import fetch_weather, CROP_GUIDE

async def main():
    print("--- Testing Weather API ---")
    # Madurai Coordinates
    lat, lon = 9.9252, 78.1198
    weather = await fetch_weather(lat, lon)
    print("Weather Response:")
    print(weather)

    print("\n--- Testing Crop Guidance ---")
    print("Tomato Soil Info:", CROP_GUIDE.get("tomato", {}).get("soil"))
    print("Tomato Advice:", CROP_GUIDE.get("tomato", {}).get("guidance"))

if __name__ == "__main__":
    asyncio.run(main())