# Gemini AI Integration Web Application

## Overview
This project is a Flask web application developed for the **NTU SCTP Data Science and AI (DSAI) Module 6** assignment. It demonstrates the integration of Google's Gemini AI API into a web application, along with additional features including user management, price prediction, Web3 PayNow, and Telegram bot backend integration.

## Features

### 🤖 **Gemini AI Integration**
- Interactive chat interface with Google's Gemini 2.0 Flash model
- Real-time AI responses to user prompts
- Clean and intuitive web interface for AI interactions

### 📊 **Simple User Management System**
- User login with timestamp tracking
- SQLite database storage for user data
- Database viewing and management interface
- User data clearing functionality

### 💰 **Price Prediction Model**
- Simple linear regression model for price prediction
- Input: USD/SGD exchange rate
- Formula: `Predicted Price = 90.23 + (-50.6 × USD/SGD rate)`
- Input validation and error handling

### 💳 **Web3 Integration**
- Web3 transaction interface
- Transaction details display

### 🤖 **Telegram Bot Integration**
- Webhook setup for Telegram bot
- Start/stop bot functionality
- Integration with external domain for webhook handling

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite3
- **AI Service**: Google Gemini API
- **Frontend**: HTML templates with CSS styling
- **Deployment**: Render.com
- **External APIs**: Telegram Bot API

## Prerequisites

- Python 3.7+
- Google Gemini API key
- Telegram Bot API key (optional, for Telegram features)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ntu_dsai_mod6
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   TELEGRAM_API_KEY=your_telegram_bot_token_here
   TELEGRAM_DOMAIN_URL=your_webhook_domain_url_here
   ```

4. **Initialize the database**
   The SQLite database will be created automatically when the application runs.

## Usage

### Running the Application

**Development Mode:**
```bash
python app.py
```

**Production Mode:**
```bash
gunicorn app:app
```

The application will be available at `http://localhost:5000`

### Application Routes

- **`/`** - Home page
- **`/main`** - Main application interface with user registration
- **`/database`** - View all users login history
- **`/gemini/`** - Gemini AI chat interface
- **`/prediction`** - Price prediction tool
- **`/paynow`** - Web3 PayNow interface
- **`/start_telegram`** - Start Telegram bot webhook
- **`/stop_telegram`** - Stop Telegram bot webhook

## File Structure

```
gemini_tryout/
├── app.py                 # Main Flask application
├── config.py             # Configuration and environment variables
├── requirements.txt      # Python dependencies
├── user.db              # SQLite database (auto-generated)
├── templates/           # HTML templates
│   ├── index.html       # Home page
│   ├── main.html        # Main interface
│   ├── gemini.html      # AI chat interface
│   ├── gemini_reply.html # AI response display
│   ├── prediction.html   # Price prediction interface
│   ├── database.html    # User database view
│   ├── paynow.html      # Web3 PayNow interface
│   ├── start_telegram.html # Telegram bot start
│   └── stop_telegram.html  # Telegram bot stop
├── static/
│   └── styles.css       # Application styling
└── README.md           # This file
```

## API Integration Details

### Google Gemini API
- **Model**: `gemini-2.0-flash`
- **Function**: `get_gemini_response(prompt)`
- **Purpose**: Generate AI responses to user queries

### Telegram Bot API
- **Webhook Setup**: Automated webhook configuration
- **Base URL**: `https://api.telegram.org/bot{token}/`
- **Methods**: `setWebhook`, `deleteWebhook`

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    timestamp TEXT NOT NULL
);
```

## Assignment Context

This project demonstrates key concepts from the DSAI Module 6 curriculum:

1. **API Integration**: Working with external AI services (Gemini API)
2. **Web Development**: Building interactive web applications with Flask
3. **Database Management**: Implementing CRUD operations with SQLite
4. **Machine Learning**: Simple predictive modeling
5. **Bot Development**: Integration with messaging platforms

## Security Considerations

- Environment variables are used for sensitive API keys
- Input validation is implemented for user inputs
- Error handling for API failures and invalid data

## Future Enhancements

- [ ] User authentication and session management
- [ ] More sophisticated ML models for price prediction
- [ ] Enhanced Telegram bot functionality
- [ ] Data visualization features
- [ ] API rate limiting and caching

## Contributing

This is an educational project for the NTU SCTP DSAI course. For academic purposes only.