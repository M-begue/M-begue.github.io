import { Routes, Route, useLocation, useNavigate } from 'react-router-dom'
import { AnimatePresence } from 'framer-motion'
import menuVideo from './assets/Mainn.mp4'
import main1 from './assets/main1.mp4'
import main2 from './assets/main2.mp4'
import main3 from './assets/main3.mp4'
import P3Menu from './P3Menu'
import VideoPage from './VideoPage'
import ResumePage from './ResumePage'
import PageTransition from './PageTransition'
import Socials from './Socials'
import AboutMe from './AboutMe'
import SideProject from './SideProject'
import { useVideoPreload } from './useVideoPreload'
import './App.css'
import './loading.css'

function MenuScreen({ src }) {
  const navigate = useNavigate()
  return (
    <div id="menu-screen">
      <video src={src} autoPlay loop muted playsInline preload="auto"/>
      <P3Menu onNavigate={(page) => navigate(`/${page}`)} />
    </div>
  )
}

function AnimatedRoutes({ videos }) {
  const location = useLocation()
  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/" element={
          <PageTransition><MenuScreen src={videos.menu} /></PageTransition>
        } />
        <Route path="/about" element={
          <PageTransition variant="about"><AboutMe src={videos.main1} /></PageTransition>
        } />
        <Route path="/resume" element={
          <PageTransition><ResumePage src={videos.main2} /></PageTransition>
        } />
        <Route path="/socials" element={
          <PageTransition variant="socials"><Socials src={videos.main3} /></PageTransition>
        } />
        <Route path="/sideproj" element={
          <PageTransition variant="sideproj"><SideProject src={videos.main3} /></PageTransition>
        } />
      </Routes>
    </AnimatePresence>
  )
}

export default function App() {
  // Ajoute ici les vidéos d'AboutMe / SideProject si elles en ont (voir le message)
  const { blobs, progress } = useVideoPreload([menuVideo, main2, main3, main1])

  if (!blobs) {
    return (
      <div className="loading-screen">
        <div className="loading-title">CHARGEMENT</div>
        <div className="loading-bar">
          <div className="loading-bar-fill" style={{ transform: `scaleX(${progress})` }} />
        </div>
      </div>
    )
  }

  const videos = { menu: blobs[0], main2: blobs[1], main3: blobs[2], main1: blobs[3] }
  return <AnimatedRoutes videos={videos} />
}
