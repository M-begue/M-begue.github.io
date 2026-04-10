import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

import char1 from "./assets/char1.png"; 
import char2 from "./assets/char2.png";
import bgVideo from "./assets/main3.mp4";
import icon1 from "./assets/icon1.png";
import icon2 from "./assets/icon2.png";
import imgLatice from "./assets/latice_1.png";
import imgMorpion from "./assets/morpion.png";
import imgAllumettes from "./assets/allumettes.png";
import imgDevinette from "./assets/devinette.png";

const ROLES = [
  { text: "LEADER", color: "#e8c100", bg: "rgba(232,193,0,0.12)", border: "rgba(232,193,0,0.5)" },
  { text: "PARTY",  color: "#4a8fff", bg: "rgba(74,143,255,0.12)", border: "rgba(74,143,255,0.5)" },
  { text: "PARTY",  color: "#4a8fff", bg: "rgba(74,143,255,0.12)", border: "rgba(74,143,255,0.5)" },
];

const PROJECTS = [
  {
    id: "latice",
    label: "LATICE",
    desc: "Projet de groupe — JavaFX",
    icon: icon1,
    char: char1,
    color: "#ffd43b",
    skills: ["POO", "JavaFX", "MVC", "Git"],
    subItems: [
      { 
        name: "LATICE BOARD", 
        img: imgLatice, 
        info: "STRATÉGIE", 
        count: "04 PERS", 
        details: "Développement d'un jeu de plateau avec interface graphique complète." 
      }
    ]
  },
  {
    id: "python-bundle",
    label: "PYTHON GAMES",
    desc: "Apprentissage des bases",
    icon: icon2,
    char: char2,
    color: "#3ce2ff",
    skills: ["Python", "Logique", "Algorithmes"],
    subItems: [
      { 
        name: "MORPION", 
        img: imgMorpion, 
        info: "STRATÉGIE", 
        count: "PVP", 
        isLarge: true,
        details: "Un classique du 3x3. Gestion des conditions de victoire et d'égalité."
      },
      { 
        name: "JEU DES ALLUMETTES", 
        img: imgAllumettes, 
        info: "LOGIQUE", 
        count: "NIM", 
        isLarge: false,
        details: "Variante du jeu de Nim. Réflexion sur les algorithmes de retrait optimaux."
      },
      { 
        name: "DEVINETTE", 
        img: imgDevinette, 
        info: "BOUCLES", 
        count: "V1.2", 
        isLarge: false,
        details: "Manipulation des nombres aléatoires et des entrées utilisateurs."
      }
    ]
  }
];

export default function SideProject() {
  const [active, setActive] = useState(0);
  const [mounted, setMounted] = useState(false);
  const [activeSub, setActiveSub] = useState(0);
  const [focus, setFocus] = useState("left"); // "left" ou "right"
  const [showPreview, setShowPreview] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const t = setTimeout(() => setMounted(true), 60);
    return () => clearTimeout(t);
  }, []);

  useEffect(() => {
    const onKey = (e) => {
      if (showPreview) {
        if (["Escape", "Backspace", "Enter"].includes(e.key)) setShowPreview(false);
        return;
      }

      if (focus === "left") {
        if (e.key === "ArrowUp") setActive(i => Math.max(0, i - 1));
        if (e.key === "ArrowDown") setActive(i => Math.min(PROJECTS.length - 1, i + 1));
        if (e.key === "ArrowRight") { setFocus("right"); setActiveSub(0); }
        if (e.key === "Escape") navigate("/");
        if (e.key === "ArrowLeft") navigate("/");
      } else {
        if (e.key === "ArrowUp") setActiveSub(i => Math.max(0, i - 1));
        if (e.key === "ArrowDown") setActiveSub(i => Math.min(PROJECTS[active].subItems.length - 1, i + 1));
        if (e.key === "ArrowLeft") setFocus("left");
        if (e.key === "Enter") setShowPreview(true);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [active, focus, showPreview, navigate]);

  const currentProj = PROJECTS[active];

  return (
    <div id="menu-screen" style={{ position: 'relative', width: '100vw', height: '100vh', overflow: 'hidden', background: '#000' }}>
      <video src={bgVideo} autoPlay loop muted playsInline preload="auto"
        style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', opacity: 0.5 }} 
      />

      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Anton&family=Barlow+Condensed:wght@400;700&display=swap');

        /* --- CONTENEUR DES BARRES GAUCHE --- */
        .proj-root {
          position: absolute;
          inset: 0;
          z-index: 10;
          pointer-events: none;
          display: flex;
          flex-direction: column;
          justify-content: center;
          gap: 8px;
        }

        .proj-bar-outer {
          position: relative;
          transform: translateX(-100%);
          transition: transform 0.55s cubic-bezier(0.22, 1, 0.36, 1);
        }
        .proj-bar-outer.mounted { transform: translateX(0); }

        .proj-bar {
          position: relative;
          width: 45vw;
          height: 64px;
          background: #111;
          cursor: pointer;
          pointer-events: all;
          clip-path: polygon(0 0, 100% 0, calc(100% - 14px) 100%, 0 100%);
          transition: height 0.3s cubic-bezier(0.22,1,0.36,1);
          z-index: 2;
        }
        .proj-bar-outer.active .proj-bar { height: 90px; }

        /* Effet rouge de Socials */
        .proj-red {
          position: absolute;
          top: 0; left: 0;
          width: 45vw;
          height: 64px;
          background: #c4001a;
          clip-path: polygon(50% 0, 100% 0, 100% 100%, calc(50% - 10px) 100%);
          transform: translateY(-7px);
          opacity: 0;
          transition: opacity 0.2s, height 0.3s;
          z-index: 1;
        }
        .proj-bar-outer.active .proj-red { opacity: 1; height: 90px; }

        /* Effet blanc incliné */
        .proj-fill {
          position: absolute;
          inset: 0;
          background: #fff;
          clip-path: polygon(100% 0, 100% 0, calc(100% - 32px) 100%, calc(100% - 32px) 100%);
          transition: clip-path 0.35s cubic-bezier(0.22, 1, 0.36, 1);
          z-index: 1;
        }
        .proj-bar-outer.active .proj-fill {
          clip-path: polygon(22% 0, 100% 0, calc(100% - 14px) 100%, calc(22% + 138px) 100%);
        }

        /* Personnage (Alignement Socials) */
        .proj-char {
          position: absolute;
          top: 0;
          left: 110px;
          height: 100%;
          z-index: 5;
          pointer-events: none;
          clip-path: polygon(20px 0%, 100% 0%, calc(100% - 20px) 100%, 0% 100%);
        }

        .proj-label {
          position: absolute;
          left: 340px;
          top: 50%;
          transform: translateY(-50%);
          font-family: 'Bebas Neue', sans-serif;
          font-size: 32px;
          letter-spacing: 4px;
          color: rgba(255,255,255,0.8);
          z-index: 6;
          transition: color 0.3s;
        }
        .proj-bar-outer.active .proj-label { color: #111; }

        .proj-role {
          position: absolute;
          left: 20px;
          top: 50%;
          transform: translateY(-50%) rotate(-15deg);
          z-index: 10;
          font-family: 'Anton', sans-serif;
          font-size: 38px;
          line-height: 1;
          color: var(--color);
          background: var(--bg);
          border: 1px solid var(--border);
          padding: 2px 12px;
          user-select: none;
          pointer-events: none;
          transition: all 0.3s ease;
          opacity: 0.6;
        }
        .proj-bar-outer.active .proj-role {
          opacity: 1;
          transform: translateY(-50%) rotate(-10deg) scale(1.1);
        }
        

        /* --- LISTE DE DROITE --- */
        .sub-list {
          position: absolute;
          right: 80px;
          top: 50%;
          transform: translateY(-50%);
          z-index: 20;
          display: flex;
          flex-direction: column;
          gap: 12px;
          pointer-events: all;
        }

        .sub-item {
          width: 380px;
          height: 50px;
          background: rgba(0,0,0,0.8);
          border-radius: 4px;
          display: flex;
          align-items: center;
          padding: 0 20px;
          cursor: pointer;
          font-family: 'Bebas Neue', sans-serif;
          font-size: 22px;
          color: #fff;
          letter-spacing: 1px;
          transition: all 0.2s;
          border: 1px solid rgba(255,255,255,0.1);
        }

        .sub-item.selected {
          background: #fff;
          color: #000;
          transform: translateX(-15px);
          border-left: 8px solid #c4001a;
        }

        /* --- FOOTER SKILLS --- */
        .proj-footer {
          position: absolute;
          bottom: 30px;
          left: 50px;
          z-index: 30;
          opacity: 0;
          transition: opacity 0.5s 0.5s;
        }
        .proj-footer.mounted { opacity: 1; }

        /* --- PREVIEW OVERLAY --- */
        .proj-preview-overlay {
          position: fixed;
          inset: 0;
          background: rgba(0, 0, 0, 0.95);
          display: flex;
          align-items: center;
          justify-content: center;
          z-index: 1000;
        }
        .proj-fullscreen-wrap {
          position: relative;
          width: 80vw;
          height: 75vh;
          border: 6px solid #fff;
          background: #000;
          box-shadow: 20px 20px 0px #c4001a;
        }
      `}</style>

      {/* Rendu des Projets (Gauche) */}
      <div className="proj-root">
        {PROJECTS.map((p, i) => (
          <div 
            key={p.id} 
            className={`proj-bar-outer ${active === i ? "active" : ""} ${mounted ? "mounted" : ""}`}
            style={{ 
              transitionDelay: `${i * 80}ms`,
              '--color': ROLES[i]?.color || '#fff',
              '--bg': ROLES[i]?.bg || 'transparent',
              '--border': ROLES[i]?.border || 'transparent'
            }}
            onMouseEnter={() => { setActive(i); setFocus("left"); }}
          >
            <div className="proj-red" />
            <div className="proj-bar">
              <div className="proj-fill" />
              <img src={p.char} className="proj-char" alt="" />
              <div className="proj-role">{ROLES[i]?.text}</div>
              <span className="proj-label">{p.label}</span>
            </div>
          </div>
        ))}
      </div>

      {/* Rendu des Sous-Items (Droite) */}
      <div className="sub-list">
        <div style={{ color: currentProj.color, fontFamily: 'Anton', fontSize: '12px', letterSpacing: '2px', marginBottom: '5px' }}>
          PROJET SELECTIONNÉ — {currentProj.label}
        </div>
        {currentProj.subItems.map((sub, idx) => (
          <div 
            key={idx}
            className={`sub-item ${focus === "right" && activeSub === idx ? "selected" : ""}`}
            onMouseEnter={() => { setFocus("right"); setActiveSub(idx); }}
            onClick={() => setShowPreview(true)}
          >
            <span style={{ flex: 1 }}>{sub.name}</span>
            <span style={{ fontSize: '14px', opacity: 0.6 }}>{sub.info}</span>
          </div>
        ))}
      </div>

      {/* Footer Skills */}
      <div className={`proj-footer ${mounted ? "mounted" : ""}`}>
        <div style={{ color: currentProj.color, fontSize: '24px', fontFamily: 'Anton' }}>{currentProj.desc}</div>
        <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
          {currentProj.skills.map(s => (
            <span key={s} style={{ background: '#fff', color: '#000', padding: '2px 12px', fontWeight: 'bold', fontFamily: 'Bebas Neue' }}>
              {s}
            </span>
          ))}
        </div>
      </div>

      {/* Overlay de Visualisation */}
      {showPreview && (
        <div className="proj-preview-overlay" onClick={() => setShowPreview(false)}>
          <div className="proj-fullscreen-wrap" onClick={(e) => e.stopPropagation()}>
            <div style={{ position: 'absolute', top: '-40px', background: '#fff', color: '#000', padding: '5px 20px', fontFamily: 'Anton', fontSize: '20px' }}>
              {currentProj.subItems[activeSub].name}
            </div>
            <img 
              src={currentProj.subItems[activeSub].img} 
              alt=""
              style={{ width: '100%', height: '100%', objectFit: 'contain', padding: '20px' }} 
            />
            <div style={{ position: 'absolute', bottom: '10px', right: '15px', color: '#fff', fontFamily: 'Bebas Neue', opacity: 0.5 }}>
              [ ESC ] POUR QUITTER
            </div>
          </div>
        </div>
      )}
    </div>
  );
}