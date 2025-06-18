
# Marvel Cinematic Universe Chatbot

This application is a Marvel-themed chatbot that provides information about MCU movies, their connections, viewing orders, and recommendations.

## Features

- Chat interface with Marvel-themed UI
- Information about all MCU movies
- Details on chronological and release order
- Movie connections and relationships
- Movie recommendations based on user preferences

## Tech Stack

- **Frontend**: React with TypeScript, Tailwind CSS, shadcn/ui components
- **Backend**: Python with Flask 

## Running the Application

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd src/backend
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Start the Flask server:
   ```
   python api.py
   ```

### Frontend Setup

1. In a new terminal, start the React development server:
   ```
   npm run dev
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5173
   ```

## Note

This application uses a simulated backend with a limited dataset of Marvel movies. For a production application, you would want to use a more complete database and improve the language processing capabilities.
