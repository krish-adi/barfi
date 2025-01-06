import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import StreamlitAppComponent from './App.tsx'
import './index.css'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <StreamlitAppComponent />
  </StrictMode>,
)
