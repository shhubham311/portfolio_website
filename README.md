# Portfolio Website

A professional AI-powered portfolio website built with Flask, featuring an interactive chatbot powered by Groq's LLaMA model and a contact form using Web3Forms. The website is ready to deploy on Vercel.

## Project Overview

This is a modern, responsive portfolio website for **Shubham Kumar**, an AI & Data Engineering Specialist. The website showcases his professional information, projects, skills, and includes interactive features like an AI-powered chatbot assistant and a contact form.

## Project Structure

```
portfolio_website/
├── app.py                 # Local Flask runner
├── api/
│   ├── __init__.py
│   └── index.py           # Vercel Flask serverless entry point
├── .python-version        # Python runtime version for Vercel
├── requirements.txt       # Python dependencies
├── vercel.json            # Vercel routing and function settings
├── .gitignore
├── .vercelignore          # Files ignored during Vercel deployment
├── public/                # Static assets served by Vercel's CDN
├── static/                # Contains images for logo, favicon and projects
├── templates/
│   └── index.html         # Main HTML template with inline CSS and JavaScript
└── README.md              # Project documentation
```

## File Descriptions

### `app.py`
The local Flask runner. Use this when running the site on your machine with `python app.py`.

### `api/index.py`
The Flask backend application used by Vercel. It handles:

- **Groq AI Integration**: Connects to Groq's API using the OpenAI SDK to power the chatbot.
- **Resume Context**: Embeds professional information about Shubham Kumar to be used by the AI assistant.
- **Environment Variables**: Passes the `WEB3FORMS_ACCESS_KEY` to the frontend for the contact form.
- **Routes**:
  - `GET /` - Serves the home page (`index.html`).
  - `POST /api/chat` - Handles chatbot queries using a Llama model via Groq.

### `requirements.txt`
Python package dependencies:
- `flask` - Web framework for building the server.
- `flask_cors` - Enables Cross-Origin Resource Sharing.
- `openai` - Client for interacting with Groq's API.
- `python-dotenv` - Loads environment variables from a `.env` file.

### `templates/index.html`
The main HTML template containing the entire frontend of the portfolio.

- **Structure**: A single-page design with sections for Hero, About, Education, Skills, Experience, Projects, Volunteering, and Contact.
- **Styling**: Inlined CSS provides a modern and responsive design, utilizing CSS variables for a consistent color scheme.
- **JavaScript Functionality**:
  - **Chatbot**: Handles user interaction with the AI assistant, sending requests to the Flask backend and displaying responses.
  - **Contact Form**: Submits form data to [Web3Forms](https://web3forms.com/) asynchronously. It retrieves the access key from the Flask backend.
  - **UI/UX**: Includes scroll animations, a responsive navigation menu, and a chat widget.

### `.env` (Not Included in Repo)
Contains sensitive environment variables:
- `GROQ_API_KEY` - Your API key for the Groq service.
- `GROQ_MODEL` - Optional Groq model override. Defaults to `llama-3.3-70b-versatile`.
- `WEB3FORMS_ACCESS_KEY` - Your access key from Web3Forms for the contact form.

## Key Features

### 1. Interactive AI Chatbot
- Powered by a Llama model hosted on Groq for fast inference.
- Uses a predefined resume context to answer questions about Shubham Kumar.
- Provides a professional and conversational interface for recruiters and visitors.

### 2. Serverless Contact Form
- Utilizes Web3Forms to handle form submissions without a dedicated backend email service.
- Includes fields for name, email, and message.
- Provides success/error feedback to the user after submission.

### 3. Responsive and Modern Design
- A clean, single-page layout that works across all devices.
- A fixed navigation bar and a mobile-friendly hamburger menu.
- Smooth animations and transitions for an enhanced user experience.

### 4. Detailed Professional Information
The site embeds and displays comprehensive professional details, including:
- Name and professional role.
- Contact information and links to social profiles.
- Education history.
- Professional experience with key achievements.
- A portfolio of featured projects with links to code and live demos.
- Technical skills and core competencies.

## Setup Instructions

### Prerequisites
- Python 3.10+
- A [Groq](https://console.groq.com/keys) API key.
- A [Web3Forms](https://web3forms.com/) access key.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/shhubham311/portfolio_website.git
    cd portfolio_website
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file and add your environment variables:**
    ```
    GROQ_API_KEY=your_groq_api_key
    WEB3FORMS_ACCESS_KEY=your_web3forms_access_key
    ```

5.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5001`.

## API Endpoints

### GET `/`
Returns the rendered HTML template for the home page.

### POST `/api/chat`
Receives and processes chat messages, returning an AI-generated response.

**Request Body:**
```json
{
  "message": "What are Shubham's skills?"
}
```

**Response:**
```json
{
  "response": "AI-generated response based on the resume context."
}
```

## Technologies Used

- **Backend**: Flask, Gunicorn
- **AI**: Groq API (Llama Model)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Contact Form**: Web3Forms
- **Deployment**: Vercel

## Deploying on Vercel

1. Push this repository to GitHub.
2. Go to [Vercel](https://vercel.com), select **Add New Project**, and import `shhubham311/portfolio_website`.
3. Keep the framework preset as **Other** if Vercel does not auto-detect Flask.
4. Add these environment variables in **Settings > Environment Variables**:
   ```text
   GROQ_API_KEY=your_groq_api_key
   GROQ_MODEL=llama-3.3-70b-versatile
   WEB3FORMS_ACCESS_KEY=your_web3forms_access_key
   ```
5. Deploy the project.

Vercel uses `api/index.py` as the Flask serverless function. Static files are also available in `public/static/` so Vercel can serve them from its CDN.

## License

This project is for personal use and is not open for commercial use.

## Contact

For questions or inquiries about this portfolio, please use the contact form on the website or reach out via:
- **Email**: shubham31103@gmail.com
- **LinkedIn**: [linkedin.com/in/shubhamkumar311](https://linkedin.com/in/shubhamkumar311/)
- **GitHub**: [github.com/shhubham311](https://github.com/shhubham311)
