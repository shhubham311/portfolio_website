# [Portfolio Website](https://portfolio-website-5i5g.onrender.com)

A professional AI-powered portfolio website built with Flask, featuring an interactive chatbot powered by Groq's LLaMA model and email contact functionality. The website is deployed on render.com.


## Project Overview

This is a modern, responsive portfolio website for **Shubham Kumar**, an AI & Data Engineering Specialist. The website showcases professional information, projects, skills, and includes interactive features like an AI-powered chatbot assistant and a contact form with email integration.

## Project Structure

```
portfolio_website/
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
|—— .gitignore      
├── .env                   # Environment variables (not in repo)
|—— static/                # contains images for logo, favicon and projects  
├── templates/
│   └── index.html        # Main HTML template with inline CSS and JavaScript
└── README.md             # Project documentation
```

## File Descriptions

### `app.py`
The main Flask backend application that handles:

- **Email Configuration**: Configured with Gmail SMTP to send contact form submissions
- **Groq AI Integration**: Connects to Groq's API using OpenAI SDK to power the chatbot
- **Resume Context**: Embeds professional information about Shubham Kumar
- **Routes**:
  - `GET /` - Serves the home page (index.html)
  - `POST /api/chat` - Handles chatbot queries using LLaMA-4 model
  - `POST /contact` - Processes contact form submissions and sends emails

### `requirements.txt`
Python package dependencies:
- `flask` - Web framework for building the server
- `flask_cors` - Enables Cross-Origin Resource Sharing
- `flask_mail` - Email sending functionality
- `openai` - Client for interacting with Groq's API
- `python-dotenv` - Loads environment variables from .env file

### `templates/index.html`
The main HTML template (555 lines) containing:

- **Head Section**: 
  - Meta tags for responsiveness and charset
  - Google Fonts integration (Inter font family)
  - Font Awesome icons (v6.4.0)
  - Embedded CSS styling

- **CSS Styling**:
  - CSS variables for consistent color scheme (primary: #003366, secondary: #007bff, accent: #00d4ff)
  - Responsive design with mobile-first approach
  - Fixed navigation header with hamburger menu
  - Hero section with background image
  - Professional styling for sections (About, Projects, Skills, Contact, Chat)
  - Animations and transitions for smooth UX
  - Grid/Flexbox layouts

- **JavaScript Functionality**:
  - Chatbot interaction with real-time responses from Groq API
  - Contact form validation and submission
  - Scroll reveal animations
  - Responsive navigation menu toggle
  - Dynamic message handling for chat interface

### `.env` (Not Included)
Contains sensitive environment variables:
- `GMAIL_ADDRESS` - Gmail account email
- `GMAIL_APP_PASSWORD` - 16-character Gmail App Password
- `GROQ_API_KEY` - API key for Groq service

## Key Features

### 1. Interactive AI Chatbot
- Powered by Groq's LLaMA-4 Maverick 17B model
- Uses resume context to answer questions about Shubham Kumar
- Professional tone with concise responses
- Real-time streaming responses
- Error handling with fallback messages

### 2. Contact Form
- Name, email, and message input fields
- Form validation
- Asynchronous email integration using Flask-Mail and Python Threading (non-blocking)
- Sends inquiries directly to the portfolio owner's Gmail
- Success/error feedback to users

### 3. Responsive Design
- Mobile-first approach
- Hamburger menu for mobile navigation
- Smooth scrolling and animations
- Professional color scheme and typography

### 4. Professional Information
Embedded resume context includes:
- Full name and professional role
- Contact information
- Education (B.Tech CSE from Lovely Professional University, CGPA: 8.50)
- Experience (Data Engineering & AI/ML Intern)
- Notable projects (Predictive Maintenance, Decoding Steam Success)
- Technical skills (Python, HTML/CSS, MySQL, AWS S3, etc.)

## Setup Instructions

### Prerequisites
- Python 3.12+
- Gmail account with App Password enabled
- Groq API key

### Installation

1. Clone the repository
```bash
git clone https://github.com/shhubham311/portfolio_website.git
cd portfolio_website
```

2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create `.env` file with environment variables
```
GMAIL_ADDRESS=your_email@gmail.com
GMAIL_APP_PASSWORD=your_16_char_app_password
GROQ_API_KEY=your_groq_api_key
```

5. Run the application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## API Endpoints

### GET `/`
Returns the rendered HTML template (home page)

### POST `/api/chat`
Receives and processes chat messages with AI responses

**Request Body:**
```json
{
  "message": "What is your experience?"
}
```

**Response:**
```json
{
  "response": "AI-generated response based on resume context"
}
```

### POST `/contact`
Handles contact form submissions and initiates asynchronous background email sending to prevent server timeouts.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Your message here"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Message sent successfully!"
}
```

## Technologies Used

- **Backend**: Flask, Flask-CORS, Flask-Mail
- **AI/ML**: Groq API (LLaMA-4 Model)
- **Email**: Gmail SMTP
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Google Fonts (Inter)
- **Icons**: Font Awesome 6.4.0
- **Configuration**: python-dotenv

## Configuration Details

### Email Configuration
- Server: smtp.gmail.com
- Port: 587
- TLS: Enabled
- Authentication: Gmail credentials

### Groq Configuration
- Base URL: https://api.groq.com/openai/v1
- Model: meta-llama/llama-4-maverick-17b-128e-instruct
- Temperature: 0.5
- Max Tokens: 300

### Color Scheme
- Primary: #003366 (Dark Blue)
- Secondary: #007bff (Bright Blue)
- Accent: #00d4ff (Cyan)
- Text Dark: #1e293b
- Text Light: #64748b
- Background Light: #f8fafc

## Error Handling

- Groq API errors return: "I am currently unavailable" message
- Email errors return: "Failed to send email" message with HTTP 500
- Missing contact form fields return: HTTP 400 with error message
- All errors are logged to console for debugging

## Future Enhancements

- Add database to store contact messages
- Implement rate limiting for API endpoints
- Add authentication for admin panel
- Expand chatbot capabilities with more context
- Add project portfolio images and details
- Implement analytics tracking
- Add download resume functionality

## License

This project is personal and not open for commercial use.

## Contact

For questions or inquiries about this portfolio:
- Email: shubham31103@gmail.com
- Phone: +91 6204992324
- LinkedIn: linkedin.com/in/shubhamkumar311/
- GitHub: github.com/shhubham311