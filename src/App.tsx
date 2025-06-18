
import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import MarvelChatbot from './components/MarvelChatbot'
import { ThemeProvider } from './components/ui/theme-provider'
import { Toaster } from './components/ui/sonner'

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="marvel-ui-theme">
      <Router>
        <Routes>
          <Route path="/" element={<MarvelChatbot />} />
        </Routes>
      </Router>
      <Toaster />
    </ThemeProvider>
  )
}

export default App
