import chainlit as cl
import os
from dotenv import load_dotenv
import json
import requests
from datetime import datetime, timedelta
import random

# Load environment variables
load_dotenv()

# Travel agent system prompt
TRAVEL_AGENT_PROMPT = """You are an expert travel agent with extensive knowledge of destinations worldwide. Your role is to help users plan their perfect trip by:

1. Understanding their preferences (budget, interests, travel style, dates)
2. Suggesting suitable destinations
3. Creating detailed itineraries
4. Providing practical travel advice
5. Recommending accommodations, activities, and dining options

Always be friendly, professional, and thorough in your responses. Ask clarifying questions when needed to provide the best recommendations."""

# Sample travel data (in a real app, this would come from APIs)
DESTINATIONS = {
    "beach": ["Maldives", "Bali", "Hawaii", "Santorini", "Maui", "Phuket", "Cancun", "Fiji"],
    "mountain": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes", "Alps", "Canadian Rockies"],
    "city": ["Paris", "Tokyo", "New York", "London", "Rome", "Barcelona", "Amsterdam", "Prague"],
    "adventure": ["New Zealand", "Costa Rica", "Nepal", "Iceland", "Patagonia", "Alaska"],
    "cultural": ["Kyoto", "Varanasi", "Marrakech", "Istanbul", "Petra", "Machu Picchu"],
    "relaxation": ["Bora Bora", "Seychelles", "Mauritius", "Tahiti", "St. Lucia", "Antigua"]
}

ACTIVITIES = {
    "beach": ["Snorkeling", "Scuba diving", "Beach volleyball", "Sunset cruises", "Water sports"],
    "mountain": ["Hiking", "Skiing", "Rock climbing", "Mountain biking", "Camping"],
    "city": ["Museum visits", "Shopping", "Food tours", "Architecture tours", "Nightlife"],
    "adventure": ["Zip lining", "White water rafting", "Bungee jumping", "Hiking", "Wildlife safaris"],
    "cultural": ["Temple visits", "Local markets", "Traditional cooking classes", "Historical tours"],
    "relaxation": ["Spa treatments", "Yoga classes", "Meditation retreats", "Beach walks", "Sunset watching"]
}

@cl.on_chat_start
async def start():
    """Initialize the travel agent chat"""
    await cl.Message(
        content="🌍 Welcome to your AI Travel Agent! I'm here to help you plan your perfect trip. Let me know what kind of adventure you're looking for!",
        author="Travel Agent"
    ).send()
    
    # Send initial questions
    await cl.Message(
        content="To get started, could you tell me:\n\n1. What type of trip are you interested in? (beach, mountain, city, adventure, cultural, relaxation)\n2. What's your budget range?\n3. How many people are traveling?\n4. When are you planning to travel?",
        author="Travel Agent"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    """Handle user messages and provide travel recommendations"""
    
    user_input = message.content.lower()
    
    # Analyze user input and provide appropriate response
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        response = "Hello! I'm excited to help you plan your next adventure. What type of trip are you dreaming of?"
    
    elif any(word in user_input for word in ["beach", "ocean", "sea", "coastal"]):
        response = await generate_beach_recommendations()
    
    elif any(word in user_input for word in ["mountain", "hiking", "skiing", "alpine"]):
        response = await generate_mountain_recommendations()
    
    elif any(word in user_input for word in ["city", "urban", "metropolitan"]):
        response = await generate_city_recommendations()
    
    elif any(word in user_input for word in ["adventure", "thrilling", "exciting"]):
        response = await generate_adventure_recommendations()
    
    elif any(word in user_input for word in ["cultural", "heritage", "traditional"]):
        response = await generate_cultural_recommendations()
    
    elif any(word in user_input for word in ["relaxation", "spa", "peaceful", "calm"]):
        response = await generate_relaxation_recommendations()
    
    elif any(word in user_input for word in ["budget", "cost", "price", "expensive", "cheap"]):
        response = await generate_budget_advice()
    
    elif any(word in user_input for word in ["itinerary", "schedule", "plan", "day by day"]):
        response = await generate_sample_itinerary()
    
    elif any(word in user_input for word in ["accommodation", "hotel", "stay", "lodging"]):
        response = await generate_accommodation_recommendations()
    
    elif any(word in user_input for word in ["food", "dining", "restaurant", "cuisine"]):
        response = await generate_food_recommendations()
    
    elif any(word in user_input for word in ["weather", "climate", "season"]):
        response = await generate_weather_advice()
    
    elif any(word in user_input for word in ["transport", "flight", "getting there"]):
        response = await generate_transport_advice()
    
    else:
        response = "I'd love to help you plan your trip! Could you tell me more about what you're looking for? For example:\n\n• What type of destination interests you? (beach, mountain, city, adventure, cultural, relaxation)\n• What's your budget?\n• When do you want to travel?\n• Any specific interests or activities you'd like to include?"
    
    await cl.Message(content=response, author="Travel Agent").send()

async def generate_beach_recommendations():
    """Generate beach destination recommendations"""
    destinations = DESTINATIONS["beach"]
    activities = ACTIVITIES["beach"]
    
    selected_destinations = random.sample(destinations, 3)
    
    response = f"🏖️ **Beach Paradise Recommendations**\n\n"
    response += "Here are some amazing beach destinations:\n\n"
    
    for i, dest in enumerate(selected_destinations, 1):
        response += f"**{i}. {dest}**\n"
        response += f"   • Perfect for: {', '.join(random.sample(activities, 3))}\n"
        response += f"   • Best time to visit: {get_best_time(dest)}\n"
        response += f"   • Estimated budget: ${random.randint(1500, 5000)} per person\n\n"
    
    response += "Would you like me to create a detailed itinerary for any of these destinations?"
    return response

async def generate_mountain_recommendations():
    """Generate mountain destination recommendations"""
    destinations = DESTINATIONS["mountain"]
    activities = ACTIVITIES["mountain"]
    
    selected_destinations = random.sample(destinations, 3)
    
    response = f"⛰️ **Mountain Adventure Recommendations**\n\n"
    response += "Here are some breathtaking mountain destinations:\n\n"
    
    for i, dest in enumerate(selected_destinations, 1):
        response += f"**{i}. {dest}**\n"
        response += f"   • Perfect for: {', '.join(random.sample(activities, 3))}\n"
        response += f"   • Best time to visit: {get_best_time(dest)}\n"
        response += f"   • Estimated budget: ${random.randint(2000, 6000)} per person\n\n"
    
    response += "Would you like me to create a detailed itinerary for any of these destinations?"
    return response

async def generate_city_recommendations():
    """Generate city destination recommendations"""
    destinations = DESTINATIONS["city"]
    activities = ACTIVITIES["city"]
    
    selected_destinations = random.sample(destinations, 3)
    
    response = f"🏙️ **Urban Adventure Recommendations**\n\n"
    response += "Here are some vibrant city destinations:\n\n"
    
    for i, dest in enumerate(selected_destinations, 1):
        response += f"**{i}. {dest}**\n"
        response += f"   • Perfect for: {', '.join(random.sample(activities, 3))}\n"
        response += f"   • Best time to visit: {get_best_time(dest)}\n"
        response += f"   • Estimated budget: ${random.randint(1800, 4500)} per person\n\n"
    
    response += "Would you like me to create a detailed itinerary for any of these destinations?"
    return response

async def generate_adventure_recommendations():
    """Generate adventure destination recommendations"""
    destinations = DESTINATIONS["adventure"]
    activities = ACTIVITIES["adventure"]
    
    selected_destinations = random.sample(destinations, 3)
    
    response = f"🏔️ **Adventure Seeker Recommendations**\n\n"
    response += "Here are some thrilling adventure destinations:\n\n"
    
    for i, dest in enumerate(selected_destinations, 1):
        response += f"**{i}. {dest}**\n"
        response += f"   • Perfect for: {', '.join(random.sample(activities, 3))}\n"
        response += f"   • Best time to visit: {get_best_time(dest)}\n"
        response += f"   • Estimated budget: ${random.randint(2500, 7000)} per person\n\n"
    
    response += "Would you like me to create a detailed itinerary for any of these destinations?"
    return response

async def generate_cultural_recommendations():
    """Generate cultural destination recommendations"""
    destinations = DESTINATIONS["cultural"]
    activities = ACTIVITIES["cultural"]
    
    selected_destinations = random.sample(destinations, 3)
    
    response = f"🏛️ **Cultural Immersion Recommendations**\n\n"
    response += "Here are some culturally rich destinations:\n\n"
    
    for i, dest in enumerate(selected_destinations, 1):
        response += f"**{i}. {dest}**\n"
        response += f"   • Perfect for: {', '.join(random.sample(activities, 3))}\n"
        response += f"   • Best time to visit: {get_best_time(dest)}\n"
        response += f"   • Estimated budget: ${random.randint(1200, 4000)} per person\n\n"
    
    response += "Would you like me to create a detailed itinerary for any of these destinations?"
    return response

async def generate_relaxation_recommendations():
    """Generate relaxation destination recommendations"""
    destinations = DESTINATIONS["relaxation"]
    activities = ACTIVITIES["relaxation"]
    
    selected_destinations = random.sample(destinations, 3)
    
    response = f"🧘 **Relaxation & Wellness Recommendations**\n\n"
    response += "Here are some peaceful destinations:\n\n"
    
    for i, dest in enumerate(selected_destinations, 1):
        response += f"**{i}. {dest}**\n"
        response += f"   • Perfect for: {', '.join(random.sample(activities, 3))}\n"
        response += f"   • Best time to visit: {get_best_time(dest)}\n"
        response += f"   • Estimated budget: ${random.randint(2000, 8000)} per person\n\n"
    
    response += "Would you like me to create a detailed itinerary for any of these destinations?"
    return response

async def generate_budget_advice():
    """Generate budget travel advice"""
    response = "💰 **Budget Travel Tips**\n\n"
    response += "Here are some ways to make your trip more affordable:\n\n"
    response += "**Accommodation Savings:**\n"
    response += "• Consider hostels, guesthouses, or vacation rentals\n"
    response += "• Book in advance for better rates\n"
    response += "• Look for package deals\n\n"
    response += "**Transportation Savings:**\n"
    response += "• Use public transportation\n"
    response += "• Book flights during off-peak seasons\n"
    return response

async def generate_sample_itinerary():
    """Generate a sample travel itinerary"""
    response = "📅 **Sample 7-Day Itinerary: Bali Adventure**\n\n"
    response += "**Day 1: Arrival & Relaxation**\n"
    response += "• Arrive in Denpasar\n"
    response += "• Check into hotel in Seminyak\n"
    response += "• Sunset at Tanah Lot Temple\n"
    response += "• Welcome dinner at local restaurant\n\n"
    response += "**Day 2: Cultural Immersion**\n"
    response += "• Morning yoga session\n"
    response += "• Visit Ubud Palace and Sacred Monkey Forest\n"
    response += "• Traditional Balinese cooking class\n"
    response += "• Evening traditional dance performance\n\n"
    response += "**Day 3: Nature & Adventure**\n"
    response += "• Sunrise hike at Mount Batur\n"
    response += "• Hot springs relaxation\n"
    response += "• Rice terrace visit in Tegalalang\n"
    response += "• Optional: White water rafting\n\n"
    response += "**Day 4: Beach Day**\n"
    response += "• Transfer to Nusa Penida\n"
    response += "• Visit Kelingking Beach and Angel's Billabong\n"
    response += "• Snorkeling at Crystal Bay\n"
    response += "• Sunset at Broken Beach\n\n"
    response += "**Day 5: Island Hopping**\n"
    response += "• Day trip to Gili Islands\n"
    response += "• Snorkeling with sea turtles\n"
    response += "• Beach relaxation\n"

    response += "**Day 6: Wellness & Shopping**\n"
    response += "• Spa treatment at luxury resort\n"
    response += "• Shopping at Ubud Art Market\n"
    response += "• Visit Tegenungan Waterfall\n"
    response += "• Farewell dinner\n\n"
    response += "**Day 7: Departure**\n"
    response += "• Morning beach walk\n"
    response += "• Last-minute shopping\n"
    response += "• Transfer to airport\n\n"
    response += "Would you like me to customize this itinerary for a different destination?"
    return response

async def generate_accommodation_recommendations():
    """Generate accommodation recommendations"""
    response = "🏨 **Accommodation Recommendations**\n\n"
    response += "**Luxury Hotels ($$$):**\n"
    response += "• Four Seasons, Ritz-Carlton, Aman Resorts\n"
    response += "• Perfect for: Honeymoons, special occasions\n"
    response += "• Price range: $300-1000+ per night\n\n"
    response += "**Boutique Hotels ($$):**\n"
    response += "• Unique, personalized experiences\n"
    response += "• Perfect for: Couples, small groups\n"

    return response

async def generate_food_recommendations():
    """Generate food and dining recommendations"""
    response += "• Rooftop dining with city views\n"
    response += "• Chef's table experiences\n"
    response += "• Wine pairing dinners\n\n"
    response += "**Dietary Considerations:**\n"
    response += "• Research local cuisine for dietary restrictions\n"
    response += "• Learn key phrases in local language\n"
    response += "• Use translation apps for menus\n"
    response += "• Consider food tours for safe sampling\n\n"
    response += "What type of cuisine are you most excited to try?"
    return response

async def generate_weather_advice():
    """Generate weather and climate advice"""
    response = "🌤️ **Weather & Best Time to Travel**\n\n"
    response += "**General Guidelines:**\n"
    response += "• Research seasonal weather patterns\n"
    response += "• Consider peak vs. off-peak seasons\n"
    response += "• Check for monsoon/rainy seasons\n"
    response += "• Look into hurricane/typhoon seasons\n\n"
    response += "**Seasonal Travel Tips:**\n"
    response += "**Spring (Mar-May):** Cherry blossoms, mild weather\n"
    response += "**Summer (Jun-Aug):** Peak season, higher prices\n"
    response += "**Fall (Sep-Nov):** Shoulder season, good deals\n"
    response += "**Winter (Dec-Feb):** Ski season, holiday crowds\n\n"
    response += "**Weather Preparation:**\n"
    response += "• Pack layers for variable weather\n"
    response += "• Bring appropriate footwear\n"
    response += "• Consider travel insurance for weather delays\n"
    response += "• Check weather forecasts before departure\n\n"
    response += "What destination are you considering? I can give you specific weather advice!"
    return response

async def generate_transport_advice():
    """Generate transportation advice"""
    response = "✈️ **Transportation Tips**\n\n"
    response += "**Flight Booking:**\n"
    response += "• Book 2-3 months in advance for best prices\n"
    response += "• Use flight comparison websites\n"
    response += "• Consider alternative airports\n"
    response += "• Sign up for fare alerts\n\n"

    return response

def get_best_time(destination):
    """Get the best time to visit a destination"""
    best_times = {
        "Maldives": "November to April (dry season)",
        "Bali": "April to October (dry season)",
        "Hawaii": "April to October (avoid hurricane season)",
        "Santorini": "May to October (avoid winter rains)",
        "Paris": "April to June, September to October",

    }
    return best_times.get(destination, "Year-round (check specific weather patterns)")

if __name__ == "__main__":
    # This will be handled by Chainlit
    pass 