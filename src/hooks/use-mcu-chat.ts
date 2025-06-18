import { useState } from 'react';
import { toast } from 'sonner';

export interface Movie {
  id: number;
  title: string;
  year: number;
  chronological_order: number;
  summary: string;
  connections: string[];
  post_credit?: string;
  key_characters: string[];
}

export interface ChatMessage {
  id: string;
  sender: 'user' | 'bot';
  text: string;
  timestamp: Date;
  movies?: Movie[];
  movie?: Movie;
}

const EXAMPLE_QUESTIONS = [
  "What's the correct order to watch Marvel movies?",
  "Tell me about Iron Man",
  "What movies are in Phase 1?",
  "How are Thor and Guardians of the Galaxy connected?",
  "Recommend me some Marvel movies like Captain America"
];

export const useMcuChat = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: '1',
      sender: 'bot',
      text: 'Hi! I\'m your Marvel Cinematic Universe guide. Ask me about any MCU movie, the best order to watch them, or for recommendations!',
      timestamp: new Date(),
    },
  ]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (text: string) => {
    if (!text.trim()) return;
    
    // Add user message
    const userMessage: ChatMessage = {
      id: Date.now().toString(),
      sender: 'user',
      text,
      timestamp: new Date(),
    };
    
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);
    
    try {
      // Call the Python backend
      const response = await fetch('http://127.0.0.1:5000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: text }),
      });
      
      if (!response.ok) {
        throw new Error('API response was not ok');
      }
      
      const data = await response.json();
      
      // Add bot response
      const botMessage: ChatMessage = {
        id: (Date.now() + 1).toString(),
        sender: 'bot',
        text: data.response,
        timestamp: new Date(),
        movies: data.movies,
        movie: data.movie,
      };
      
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error('Error calling chat API:', error);
      
      // Show error toast
      toast.error("Connection Error", {
        description: "Could not connect to the Marvel knowledge base. Is the backend running?",
      });
      
      // Random suggestion from examples
      const randomQuestion = EXAMPLE_QUESTIONS[Math.floor(Math.random() * EXAMPLE_QUESTIONS.length)];
      
      // Fallback response if API call fails
      const botMessage: ChatMessage = {
        id: (Date.now() + 1).toString(),
        sender: 'bot',
        text: `I'm having trouble connecting to my knowledge base right now. Make sure the Python backend is running on http://localhost:5000. Try asking something like: "${randomQuestion}"`,
        timestamp: new Date(),
      };
      
      setMessages((prev) => [...prev, botMessage]);
    } finally {
      setLoading(false);
    }
  };
  
  return {
    messages,
    loading,
    sendMessage,
  };
};
