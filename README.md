# AI Travel Agent with Chainlit 🌍✈️

A comprehensive AI-powered travel planning assistant built with Chainlit that helps users plan their perfect trips.

## Features

### 🎯 Core Capabilities
- **Destination Recommendations** - Get personalized suggestions based on travel preferences
- **Itinerary Planning** - Create detailed day-by-day travel plans
- **Budget Planning** - Receive cost estimates and money-saving tips
- **Accommodation Advice** - From luxury hotels to budget-friendly options
- **Local Cuisine Guidance** - Discover authentic dining experiences
- **Weather & Timing** - Know the best time to visit any destination
- **Transportation Tips** - Comprehensive travel logistics advice

### 🏖️ Destination Categories
- **Beach Destinations** - Tropical paradises and coastal getaways
- **Mountain Adventures** - Hiking, skiing, and alpine experiences
- **Urban Exploration** - City breaks and metropolitan adventures
- **Cultural Immersion** - Heritage sites and traditional experiences
- **Adventure Travel** - Thrilling outdoor activities and expeditions
- **Relaxation & Wellness** - Spa retreats and peaceful escapes

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd travel-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional)
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   chainlit run travel_agent.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8000` to start chatting with your AI travel agent!

## Usage

### Getting Started
1. Open the application in your browser
2. The AI travel agent will greet you and ask about your travel preferences
3. Tell the agent what type of trip you're interested in
4. Answer follow-up questions about budget, dates, and preferences
5. Receive personalized recommendations and detailed itineraries

### Example Conversations

**User:** "I want a beach vacation"
**Agent:** Provides beach destination recommendations with activities, best times to visit, and budget estimates

**User:** "What's the best time to visit Bali?"
**Agent:** Gives detailed weather information and seasonal advice

**User:** "I need budget travel tips"
**Agent:** Offers comprehensive money-saving strategies for accommodation, transportation, and activities

## Project Structure

```
travel-agent/
├── travel_agent.py      # Main Chainlit application
├── requirements.txt     # Python dependencies
├── chainlit.md         # Chainlit configuration and welcome message
├── README.md           # Project documentation
└── .env               # Environment variables (create this file)
```

## Dependencies

- **chainlit** - Chat interface framework
- **openai** - AI language model integration
- **python-dotenv** - Environment variable management
- **requests** - HTTP requests for external APIs
- **beautifulsoup4** - Web scraping capabilities
- **pandas** - Data manipulation
- **numpy** - Numerical computing

## Customization

### Adding New Destinations
Edit the `DESTINATIONS` dictionary in `travel_agent.py` to add new locations:

```python
DESTINATIONS = {
    "beach": ["Maldives", "Bali", "Hawaii", "Your New Destination"],
    # ... other categories
}
```

### Adding New Activities
Update the `ACTIVITIES` dictionary to include new activities:

```python
ACTIVITIES = {
    "beach": ["Snorkeling", "Scuba diving", "Your New Activity"],
    # ... other categories
}
```

### Extending Functionality
- Add new recommendation functions following the existing pattern
- Integrate with external APIs for real-time data
- Add image generation capabilities for destination previews
- Implement booking integration features

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions:
1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed information

## Future Enhancements

- [ ] Real-time flight and hotel booking integration
- [ ] Weather API integration for current conditions
- [ ] Currency conversion and budget tracking
- [ ] Photo gallery of destinations
- [ ] Multi-language support
- [ ] Voice interaction capabilities
- [ ] Travel insurance recommendations
- [ ] Local guide and tour booking

---

**Happy Traveling! 🌍✈️**

*Built with ❤️ using Chainlit*
