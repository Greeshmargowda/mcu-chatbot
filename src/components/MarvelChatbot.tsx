
import React, { useState, useRef, useEffect } from 'react';
import { useMcuChat, ChatMessage } from '@/hooks/use-mcu-chat';
import { Input } from './ui/input';
import { Button } from './ui/button';
import { Card } from './ui/card';
import { Separator } from './ui/separator';
import { Send, Film, Info, Clock, Search, Star, Calendar, List } from 'lucide-react';
import { toast } from 'sonner';

const MarvelChatbot: React.FC = () => {
  const { messages, loading, sendMessage } = useMcuChat();
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      sendMessage(input);
      setInput('');
    }
  };

  // Show welcome toast when component mounts
  useEffect(() => {
    toast.success("Marvel Chatbot Ready!", {
      description: "Ask me about MCU movies, viewing orders, and more!",
      duration: 5000,
    });
  }, []);

  // Scroll to bottom of chat on new message
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleQuickQuestion = (question: string) => {
    sendMessage(question);
  };

  return (
    <div className="flex flex-col h-screen max-w-4xl mx-auto">
      {/* Header */}
      <div className="bg-gradient-to-r from-red-600 to-purple-800 p-4 text-white rounded-b-lg shadow-lg">
        <h1 className="text-3xl font-bold text-center">Marvel Cinematic Universe Guide</h1>
        <p className="text-center opacity-90">Your AI assistant for all things MCU</p>
      </div>
      
      {/* Quick Action Buttons */}
      <div className="p-2 bg-gray-900">
        <div className="flex justify-center gap-2 flex-wrap">
          <QuickActionButton 
            icon={<List size={16} />} 
            text="Release Order"
            onClick={() => handleQuickQuestion("What is the release order of Marvel movies?")}
          />
          <QuickActionButton 
            icon={<Calendar size={16} />} 
            text="Chronological"
            onClick={() => handleQuickQuestion("What is the chronological order of Marvel movies?")}
          />
          <QuickActionButton 
            icon={<Film size={16} />} 
            text="Phases"
            onClick={() => handleQuickQuestion("What movies are in Phase 1?")}
          />
          <QuickActionButton 
            icon={<Star size={16} />} 
            text="Recommendations"
            onClick={() => handleQuickQuestion("Can you recommend some Marvel movies?")}
          />
        </div>
      </div>
      
      {/* Chat Messages */}
      <div className="flex-1 overflow-y-auto p-4 bg-slate-100 dark:bg-gray-800">
        {messages.map((message) => (
          <MessageBubble key={message.id} message={message} />
        ))}
        <div ref={messagesEndRef} />
      </div>
      
      {/* Input Area */}
      <form onSubmit={handleSubmit} className="p-4 border-t bg-white dark:bg-gray-900">
        <div className="flex gap-2">
          <Input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask about MCU movies or recommendations..."
            className="flex-1"
            disabled={loading}
          />
          <Button type="submit" disabled={loading} className="bg-red-600 hover:bg-red-700">
            <Send size={18} />
            <span className="ml-2 hidden sm:inline">Send</span>
          </Button>
        </div>
        <div className="mt-2 text-xs text-gray-500 dark:text-gray-400">
          Try asking: "What's the best order to watch Marvel movies?" or "Tell me about Iron Man"
        </div>
      </form>
    </div>
  );
};

const QuickActionButton: React.FC<{ 
  icon: React.ReactNode;
  text: string;
  onClick: () => void;
}> = ({ icon, text, onClick }) => {
  return (
    <button 
      onClick={onClick}
      className="px-3 py-1 flex items-center gap-1 bg-gray-800 hover:bg-gray-700 text-white rounded-full text-xs"
    >
      {icon}
      <span>{text}</span>
    </button>
  );
};

const MessageBubble: React.FC<{ message: ChatMessage }> = ({ message }) => {
  const isBot = message.sender === 'bot';
  
  return (
    <div className={`flex ${isBot ? 'justify-start' : 'justify-end'} mb-4`}>
      <div
        className={`max-w-[80%] p-4 rounded-lg ${
          isBot
            ? 'bg-gradient-to-r from-blue-600 to-purple-700 text-white'
            : 'bg-gray-200 text-gray-800 dark:bg-gray-700 dark:text-white'
        }`}
      >
        <div className="text-sm">{message.text}</div>
        
        {/* Movie List */}
        {message.movies && message.movies.length > 0 && (
          <div className="mt-3 space-y-2">
            <Separator className="bg-white/20" />
            <div className="text-sm font-semibold">
              {message.movies.length === 1 ? 'Movie Information:' : 'Movie Suggestions:'}
            </div>
            <div className="grid grid-cols-1 gap-2 max-h-[300px] overflow-y-auto">
              {message.movies.map((movie) => (
                <MovieCard key={movie.id} movie={movie} />
              ))}
            </div>
          </div>
        )}
        
        {/* Single Movie */}
        {message.movie && <MovieCard movie={message.movie} detailed />}
      </div>
    </div>
  );
};

const MovieCard: React.FC<{ movie: any; detailed?: boolean }> = ({ movie, detailed = false }) => {
  return (
    <Card className="bg-black/20 p-3 rounded-md text-white text-sm">
      <div className="flex items-start gap-2">
        <Film size={16} className="mt-1 flex-shrink-0" />
        <div>
          <div className="font-semibold">{movie.title} ({movie.year})</div>
          {detailed ? (
            <>
              <p className="text-xs mt-1 text-white/90">{movie.summary}</p>
              <div className="mt-2 flex items-center text-xs">
                <Clock size={12} className="mr-1" />
                <span className="text-white/80">
                  Chronological order: #{movie.chronological_order}, Release order: #{movie.id}
                </span>
              </div>
              {movie.connections.length > 0 && (
                <div className="mt-2">
                  <div className="text-xs font-semibold mb-1 flex items-center">
                    <Info size={12} className="mr-1" /> Connected movies:
                  </div>
                  <div className="flex flex-wrap gap-1">
                    {movie.connections.map((connection: string) => (
                      <span key={connection} className="bg-purple-900/50 px-2 py-1 rounded-full text-xs">
                        {connection}
                      </span>
                    ))}
                  </div>
                </div>
              )}
              {movie.post_credit && (
                <div className="mt-2 text-xs text-white/80">
                  <span className="font-semibold text-amber-300">Post-credit scene: </span>
                  {movie.post_credit}
                </div>
              )}
            </>
          ) : (
            <p className="text-xs mt-1 text-white/80 line-clamp-2">
              {movie.summary}
            </p>
          )}
        </div>
      </div>
    </Card>
  );
};

export default MarvelChatbot;
