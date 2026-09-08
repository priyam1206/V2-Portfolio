from pathlib import Path
import textwrap

path = Path('docs/index.html')
text = path.read_text(encoding='utf-8')

css = r'''
/* --- MailMate Project Showcase --- */
#mailmate-project-row {
    position: relative;
    isolation: isolate;
    min-height: 760px;
    align-items: center;
    gap: clamp(54px, 7vw, 110px);
    overflow: visible;
}

#mailmate-project-row::before {
    content: "";
    position: absolute;
    z-index: -2;
    top: 7%;
    left: 50%;
    width: 100vw;
    height: 86%;
    transform: translateX(-50%);
    pointer-events: none;
    background:
        radial-gradient(circle at 24% 48%, rgba(168, 85, 247, 0.11), transparent 26%),
        radial-gradient(circle at 33% 61%, rgba(216, 132, 162, 0.07), transparent 29%),
        radial-gradient(circle at 73% 36%, rgba(59, 130, 246, 0.055), transparent 27%);
    opacity: 0;
    transition: opacity 1.2s ease;
}

#mailmate-project-row.is-visible::before { opacity: 1; }

#mailmate-project-row .project-info {
    order: 2 !important;
    position: relative;
    z-index: 4;
    justify-content: center;
    padding-right: clamp(0px, 2vw, 32px);
}

.mm-visual {
    order: 1 !important;
    position: relative;
    z-index: 3;
    min-height: 610px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 36px 28px;
    box-sizing: border-box;
    perspective: 1000px;
}

.mm-visual::before {
    content: "";
    position: absolute;
    inset: 10% 4% 6%;
    border: 1px solid rgba(255,255,255,0.055);
    border-radius: 38px;
    background: linear-gradient(145deg, rgba(255,255,255,0.018), rgba(255,255,255,0.005));
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.025);
    opacity: 0;
    transform: scale(.96);
    transition: opacity .9s ease .1s, transform 1s cubic-bezier(.16,1,.3,1) .1s;
}

#mailmate-project-row.is-visible .mm-visual::before {
    opacity: 1;
    transform: scale(1);
}

.mm-event {
    position: absolute;
    top: 12%;
    left: 9%;
    z-index: 6;
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 9px 13px 9px 10px;
    border: 1px solid rgba(216,132,162,.17);
    border-radius: 999px;
    background: rgba(8,8,8,.68);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    opacity: 0;
    transform: translateY(18px);
    transition: opacity .7s ease .2s, transform .8s cubic-bezier(.16,1,.3,1) .2s;
}

#mailmate-project-row.is-visible .mm-event {
    opacity: 1;
    transform: translateY(0);
}

.mm-event img {
    width: 29px;
    height: 32px;
    object-fit: contain;
}

.mm-event-copy span,
.mm-event-copy strong { display: block; }
.mm-event-copy span {
    margin-bottom: 2px;
    color: #616161;
    font-size: 8px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}
.mm-event-copy strong {
    color: #cfcfcf;
    font-size: 10px;
    font-weight: 500;
    letter-spacing: .15px;
}

.mm-stage {
    position: relative;
    z-index: 4;
    width: min(340px, 76%);
    aspect-ratio: 1;
    display: grid;
    place-items: center;
    opacity: 0;
    transform: translateY(40px) scale(.92);
    filter: blur(8px);
    transition:
        opacity .8s ease .12s,
        transform 1.05s cubic-bezier(.16,1,.3,1) .12s,
        filter .9s ease .12s;
}

#mailmate-project-row.is-visible .mm-stage {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
}

.mm-stage-float {
    position: relative;
    width: 72%;
    aspect-ratio: 1;
    display: grid;
    place-items: center;
    animation: mmFloat 5.4s ease-in-out infinite;
    will-change: transform;
}

.mm-stage-tilt {
    position: relative;
    width: 100%;
    height: 100%;
    display: grid;
    place-items: center;
    transform-style: preserve-3d;
    transition: transform .42s cubic-bezier(.16,1,.3,1);
    will-change: transform;
}

.mm-stage-tilt::before {
    content: "";
    position: absolute;
    inset: 9%;
    z-index: -1;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(168,85,247,.27), rgba(168,85,247,.08) 38%, transparent 69%);
    filter: blur(28px);
    transform: translateZ(-30px) scale(1.25);
    animation: mmPulse 3.8s ease-in-out infinite;
}

.mm-logo {
    width: 82%;
    height: 82%;
    display: block;
    object-fit: contain;
    border-radius: 26%;
    transform: translateZ(35px);
    filter: drop-shadow(0 28px 42px rgba(0,0,0,.48));
    user-select: none;
    -webkit-user-drag: none;
}

.mm-ring {
    position: absolute;
    inset: 0;
    border: 1px solid rgba(168,85,247,.13);
    border-radius: 50%;
    animation: mmSpin 19s linear infinite;
}
.mm-ring::before,
.mm-ring::after {
    content: "";
    position: absolute;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #d884a2;
    box-shadow: 0 0 16px rgba(216,132,162,.8);
}
.mm-ring::before { top: 12%; left: 17%; }
.mm-ring::after { right: 7%; bottom: 28%; width: 3px; height: 3px; background: #a855f7; }
.mm-ring.secondary {
    inset: 11%;
    border-color: rgba(255,255,255,.055);
    animation-duration: 13s;
    animation-direction: reverse;
}

.mm-petal {
    position: absolute;
    z-index: 2;
    left: var(--x);
    top: var(--y);
    width: var(--s);
    height: calc(var(--s) * .55);
    border-radius: 70% 15% 70% 15%;
    background: rgba(216,132,162,.55);
    opacity: 0;
    transform: rotate(var(--r));
    animation: mmPetal var(--d) ease-in-out var(--delay) infinite;
}

.mm-caption {
    position: relative;
    z-index: 5;
    margin: -14px 0 0;
    color: #575757;
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 2.2px;
    text-transform: uppercase;
    opacity: 0;
    transform: translateY(12px);
    transition: opacity .7s ease .58s, transform .7s ease .58s;
}
#mailmate-project-row.is-visible .mm-caption { opacity: 1; transform: translateY(0); }

.mm-team {
    position: absolute;
    z-index: 8;
    left: 9%;
    bottom: 10%;
    display: flex;
    align-items: center;
    gap: 18px;
    opacity: 0;
    transform: translateY(20px);
    transition: opacity .75s ease .72s, transform .8s cubic-bezier(.16,1,.3,1) .72s;
}
#mailmate-project-row.is-visible .mm-team { opacity: 1; transform: translateY(0); }
.mm-team-copy span,
.mm-team-copy strong { display: block; }
.mm-team-copy span {
    margin-bottom: 4px;
    color: #555;
    font-size: 8px;
    font-weight: 600;
    letter-spacing: 1.7px;
    text-transform: uppercase;
}
.mm-team-copy strong { color: #bdbdbd; font-size: 11px; font-weight: 500; }

.mm-people { display: flex; align-items: center; padding-left: 9px; }
.mm-person {
    position: relative;
    width: 38px;
    height: 38px;
    margin-left: -9px;
    border-radius: 50%;
    border: 2px solid #080808;
    background: #111;
    text-decoration: none;
    opacity: 0;
    transform: translateX(-14px) scale(.8);
    transition:
        opacity .5s ease calc(.8s + var(--i) * 90ms),
        transform .6s cubic-bezier(.16,1,.3,1) calc(.8s + var(--i) * 90ms),
        margin .28s ease,
        box-shadow .28s ease;
}
#mailmate-project-row.is-visible .mm-person { opacity: 1; transform: translateX(0) scale(1); }
.mm-person:hover,
.mm-person:focus-visible {
    z-index: 20;
    transform: translateY(-5px) scale(1.08) !important;
    box-shadow: 0 10px 25px rgba(0,0,0,.5), 0 0 0 1px rgba(168,85,247,.35);
    outline: none;
}
.mm-person img { width: 100%; height: 100%; display: block; object-fit: cover; border-radius: inherit; }
.mm-person-card {
    position: absolute;
    left: 50%;
    bottom: calc(100% + 14px);
    width: max-content;
    max-width: 210px;
    padding: 10px 12px;
    border: 1px solid rgba(255,255,255,.09);
    border-radius: 11px;
    background: rgba(10,10,10,.96);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 16px 40px rgba(0,0,0,.42);
    opacity: 0;
    visibility: hidden;
    transform: translate(-50%, 8px) scale(.96);
    pointer-events: none;
    transition: opacity .2s ease, visibility .2s ease, transform .25s cubic-bezier(.16,1,.3,1);
}
.mm-person:hover .mm-person-card,
.mm-person:focus-visible .mm-person-card { opacity: 1; visibility: visible; transform: translate(-50%, 0) scale(1); }
.mm-person-card strong,
.mm-person-card small,
.mm-person-card em { display: block; }
.mm-person-card strong { color: #efefef; font-size: 11px; font-weight: 600; margin-bottom: 3px; }
.mm-person-card small { color: #777; font-size: 9px; line-height: 1.35; }
.mm-person-card em { margin-top: 7px; color: #a855f7; font-size: 9px; font-style: normal; }

.mm-kicker {
    display: flex;
    align-items: center;
    gap: 9px;
    margin-bottom: 15px;
    color: #777;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 1.7px;
    text-transform: uppercase;
    opacity: 0;
    transform: translateY(16px);
    transition: opacity .65s ease .18s, transform .75s cubic-bezier(.16,1,.3,1) .18s;
}
.mm-kicker-dot { width: 6px; height: 6px; border-radius: 50%; background: #d884a2; box-shadow: 0 0 14px rgba(216,132,162,.58); }
#mailmate-project-row.is-visible .mm-kicker,
#mailmate-project-row.is-visible .mm-title,
#mailmate-project-row.is-visible .mm-lede,
#mailmate-project-row.is-visible .mm-role,
#mailmate-project-row.is-visible .mm-actions,
#mailmate-project-row.is-visible .mm-tech { opacity: 1; transform: translateY(0); }

.mm-title {
    margin: 0 0 20px;
    font-size: clamp(54px, 5vw, 82px);
    font-weight: 400;
    letter-spacing: -3.8px;
    line-height: .98;
    color: #fff;
    opacity: 0;
    transform: translateY(22px);
    transition: opacity .72s ease .25s, transform .9s cubic-bezier(.16,1,.3,1) .25s;
}
.mm-lede {
    max-width: 560px;
    margin: 0;
    color: #9b9b9b;
    font-size: clamp(16px,1.18vw,18px);
    font-weight: 300;
    line-height: 1.72;
    opacity: 0;
    transform: translateY(20px);
    transition: opacity .7s ease .34s, transform .9s cubic-bezier(.16,1,.3,1) .34s;
}
.mm-role {
    display: grid;
    grid-template-columns: 54px 1fr;
    gap: 15px;
    max-width: 560px;
    margin: 25px 0 0;
    padding-top: 18px;
    border-top: 1px solid rgba(255,255,255,.065);
    color: #737373;
    font-size: 12px;
    line-height: 1.6;
    opacity: 0;
    transform: translateY(18px);
    transition: opacity .7s ease .43s, transform .9s cubic-bezier(.16,1,.3,1) .43s;
}
.mm-role span { color: #4f4f4f; font-size: 8px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; }
.mm-role strong { font-weight: 400; }
.mm-actions {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 25px;
    opacity: 0;
    transform: translateY(16px);
    transition: opacity .7s ease .5s, transform .9s cubic-bezier(.16,1,.3,1) .5s;
}
.mm-action {
    min-height: 42px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 9px;
    padding: 0 17px;
    box-sizing: border-box;
    border: 1px solid rgba(255,255,255,.105);
    border-radius: 999px;
    background: transparent;
    color: #cfcfcf;
    font-family: 'Inter',sans-serif;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: .8px;
    text-decoration: none;
    cursor: pointer;
    transition: color .24s ease, border-color .24s ease, background .24s ease, transform .24s ease;
}
.mm-action:hover,
.mm-action:focus-visible { color: #fff; border-color: rgba(168,85,247,.45); background: rgba(168,85,247,.07); transform: translateY(-2px); outline: none; }
.mm-action.primary { border-color: rgba(255,255,255,.17); background: #f1f1f1; color: #080808; }
.mm-action.primary:hover,
.mm-action.primary:focus-visible { background: #fff; color: #050505; border-color: #fff; }
.mm-action svg { width: 15px; height: 15px; fill: currentColor; }
.mm-action .mm-plus { font-size: 17px; font-weight: 300; line-height: 1; transition: transform .45s cubic-bezier(.16,1,.3,1); }
.mm-action[aria-expanded="true"] .mm-plus { transform: rotate(45deg); }
.mm-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    max-width: 560px;
    margin-top: 22px;
    opacity: 0;
    transform: translateY(14px);
    transition: opacity .7s ease .58s, transform .9s cubic-bezier(.16,1,.3,1) .58s;
}
.mm-tech span {
    padding: 7px 11px;
    border: 1px solid rgba(168,85,247,.18);
    border-radius: 999px;
    color: #777;
    font-size: 9px;
    font-weight: 500;
    letter-spacing: .2px;
    background: rgba(168,85,247,.02);
    transition: border-color .25s ease, color .25s ease, transform .25s ease;
}
.mm-tech span:hover { color: #cfcfcf; border-color: rgba(168,85,247,.38); transform: translateY(-2px); }
.mm-contrib {
    display: grid;
    grid-template-rows: 0fr;
    max-width: 570px;
    opacity: 0;
    transition: grid-template-rows .62s cubic-bezier(.16,1,.3,1), opacity .34s ease;
}
.mm-contrib.is-open { grid-template-rows: 1fr; opacity: 1; }
.mm-contrib-clip { overflow: hidden; }
.mm-contrib-inner {
    margin-top: 22px;
    padding: 20px 0 2px;
    border-top: 1px solid rgba(255,255,255,.075);
    transform: translateY(-8px);
    transition: transform .55s cubic-bezier(.16,1,.3,1);
}
.mm-contrib.is-open .mm-contrib-inner { transform: translateY(0); }
.mm-contrib-row {
    display: grid;
    grid-template-columns: minmax(105px, .55fr) 1.45fr;
    gap: 16px;
    padding: 9px 0;
    border-bottom: 1px solid rgba(255,255,255,.035);
}
.mm-contrib-row strong { color: #cfcfcf; font-size: 10px; font-weight: 600; }
.mm-contrib-row span { color: #696969; font-size: 10px; line-height: 1.55; }
.mm-attribution-note { margin: 13px 0 0; color: #444; font-size: 9px; line-height: 1.6; }

@keyframes mmFloat { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-12px); } }
@keyframes mmPulse { 0%,100% { opacity: .65; transform: translateZ(-30px) scale(1.18); } 50% { opacity: 1; transform: translateZ(-30px) scale(1.34); } }
@keyframes mmSpin { to { transform: rotate(360deg); } }
@keyframes mmPetal {
    0%,100% { opacity: 0; transform: translate3d(0,10px,0) rotate(var(--r)); }
    18% { opacity: .65; }
    72% { opacity: .28; }
    88% { opacity: 0; transform: translate3d(32px,-86px,0) rotate(calc(var(--r) + 140deg)); }
}

@media (max-width: 1024px) {
    #mailmate-project-row { min-height: auto; gap: 22px; }
    #mailmate-project-row .project-info,
    .mm-visual { order: unset !important; }
    .mm-visual { min-height: 560px; width: 100%; }
    .mm-event { left: 5%; }
    .mm-team { left: 5%; }
    .mm-lede,
    .mm-role,
    .mm-contrib,
    .mm-tech { max-width: 100%; }
}

@media (max-width: 620px) {
    #mailmate-project-row { padding-top: 75px; padding-bottom: 75px; }
    .mm-visual { min-height: 490px; padding: 26px 10px; }
    .mm-visual::before { inset: 8% 0 5%; border-radius: 28px; }
    .mm-event { top: 10%; left: 3%; }
    .mm-stage { width: min(300px, 88%); }
    .mm-team { left: 3%; right: 3%; bottom: 8%; justify-content: space-between; gap: 12px; }
    .mm-team-copy strong { font-size: 10px; }
    .mm-person { width: 34px; height: 34px; margin-left: -10px; }
    .mm-person-card { display: none; }
    .mm-title { font-size: 48px; letter-spacing: -2.6px; }
    .mm-role { grid-template-columns: 45px 1fr; }
    .mm-actions { gap: 8px; }
    .mm-action { min-height: 40px; padding: 0 14px; }
    .mm-contrib-row { grid-template-columns: 1fr; gap: 4px; padding: 10px 0; }
}

@media (prefers-reduced-motion: reduce) {
    .mm-stage-float,
    .mm-ring,
    .mm-stage-tilt::before,
    .mm-petal { animation: none !important; }
    #mailmate-project-row *,
    #mailmate-project-row::before { transition-duration: .01ms !important; }
}
'''

html = r'''
<!-- MAILMATE / CIPHERSQUAD -->
<div class="project-row" id="mailmate-project-row">
    <div class="mm-visual" id="mailmateVisual" aria-label="MailMate project identity and CipherSquad team">
        <div class="mm-event">
            <img src="./images/code2create.svg" alt="Code2Create logo">
            <div class="mm-event-copy"><span>Built at</span><strong>Code2Create 7.0 · ACM-VIT</strong></div>
        </div>

        <span class="mm-petal" style="--x:18%;--y:72%;--s:6px;--r:18deg;--d:6.8s;--delay:.4s"></span>
        <span class="mm-petal" style="--x:74%;--y:70%;--s:5px;--r:70deg;--d:7.9s;--delay:1.1s"></span>
        <span class="mm-petal" style="--x:82%;--y:43%;--s:4px;--r:120deg;--d:6.4s;--delay:2.3s"></span>
        <span class="mm-petal" style="--x:25%;--y:48%;--s:4px;--r:40deg;--d:8.6s;--delay:3s"></span>
        <span class="mm-petal" style="--x:61%;--y:80%;--s:5px;--r:95deg;--d:7.2s;--delay:1.8s"></span>

        <div class="mm-stage">
            <div class="mm-stage-float">
                <div class="mm-stage-tilt" id="mailmateTilt">
                    <span class="mm-ring"></span>
                    <span class="mm-ring secondary"></span>
                    <img class="mm-logo" src="https://raw.githubusercontent.com/sphereofrupayan/CipherSquad/main/assets/images/cs_logo.png" alt="MailMate logo" loading="lazy" decoding="async">
                </div>
            </div>
        </div>
        <p class="mm-caption">MailMate · CipherSquad</p>

        <div class="mm-team">
            <div class="mm-team-copy"><span>Built with</span><strong>Team CipherSquad</strong></div>
            <div class="mm-people" aria-label="CipherSquad GitHub profiles">
                <a class="mm-person" style="--i:0" href="https://github.com/Priyam-06" target="_blank" rel="noopener noreferrer" aria-label="Priyam Trivedi on GitHub"><img src="https://avatars.githubusercontent.com/u/193306497?v=4" alt="Priyam Trivedi" loading="lazy"><span class="mm-person-card"><strong>Priyam Trivedi</strong><small>System architecture · integration · current application</small><em>@Priyam-06 ↗</em></span></a>
                <a class="mm-person" style="--i:1" href="https://github.com/Sreyanko" target="_blank" rel="noopener noreferrer" aria-label="Sreyanko on GitHub"><img src="https://avatars.githubusercontent.com/u/231457860?v=4" alt="Sreyanko" loading="lazy"><span class="mm-person-card"><strong>Sreyanko</strong><small>Original dashboard · Overview frontend</small><em>@Sreyanko ↗</em></span></a>
                <a class="mm-person" style="--i:2" href="https://github.com/kartikay633" target="_blank" rel="noopener noreferrer" aria-label="Kartikay on GitHub"><img src="https://avatars.githubusercontent.com/u/143950873?v=4" alt="Kartikay" loading="lazy"><span class="mm-person-card"><strong>Kartikay</strong><small>Early Supabase · Node integration</small><em>@kartikay633 ↗</em></span></a>
                <a class="mm-person" style="--i:3" href="https://github.com/asminsinha" target="_blank" rel="noopener noreferrer" aria-label="Asmin Sinha on GitHub"><img src="https://avatars.githubusercontent.com/u/283420706?v=4" alt="Asmin Sinha" loading="lazy"><span class="mm-person-card"><strong>Asmin Sinha</strong><small>Express · Gmail OAuth · Gemini foundation</small><em>@asminsinha ↗</em></span></a>
                <a class="mm-person" style="--i:4" href="https://github.com/sphereofrupayan" target="_blank" rel="noopener noreferrer" aria-label="Rupayan on GitHub"><img src="https://avatars.githubusercontent.com/u/232069471?v=4" alt="Rupayan" loading="lazy"><span class="mm-person-card"><strong>Rupayan</strong><small>Repository setup · isolated local-time UI</small><em>@sphereofrupayan ↗</em></span></a>
            </div>
        </div>
    </div>

    <div class="project-info">
        <div class="mm-kicker"><span class="mm-kicker-dot"></span><span>AI Mail Workspace</span><span>·</span><span>Code2Create 7.0</span></div>
        <h3 class="mm-title">MailMate</h3>
        <p class="mm-lede">A Gmail-first intelligent workspace built with team CipherSquad. MailMate combines authenticated mail workflows, calendar and deadline intelligence, Kyle, local Whisper voice input, background Work agents and Tailscale-connected compute in one focused workspace.</p>
        <p class="mm-role"><span>Role</span><strong>System architecture, integration and final application engineering — including the Flask migration, Gmail workspace, calendar intelligence, Kyle, voice, privacy controls and runtime stabilization.</strong></p>

        <div class="mm-actions">
            <a class="mm-action primary" href="https://github.com/sphereofrupayan/CipherSquad" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.44 9.8 8.21 11.39.6.11.82-.26.82-.58v-2.23c-3.34.72-4.04-1.42-4.04-1.42-.55-1.38-1.33-1.75-1.33-1.75-1.09-.75.08-.73.08-.73 1.2.09 1.84 1.24 1.84 1.24 1.07 1.83 2.81 1.3 3.49 1 .11-.78.42-1.3.76-1.6-2.67-.31-5.47-1.34-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.18 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.29-1.55 3.3-1.23 3.3-1.23.65 1.66.24 2.88.12 3.18.77.84 1.23 1.91 1.23 3.22 0 4.61-2.81 5.62-5.48 5.92.43.37.82 1.1.82 2.22v3.29c0 .32.22.69.82.58A12 12 0 0 0 24 12C24 5.37 18.63 0 12 0z"/></svg>Open repository</a>
            <button class="mm-action" id="mailmateContribToggle" type="button" aria-expanded="false" aria-controls="mailmateContrib">Contribution map <span class="mm-plus" aria-hidden="true">+</span></button>
        </div>

        <div class="mm-tech" aria-label="MailMate technologies"><span>Python</span><span>Flask</span><span>Gmail API</span><span>Google Calendar</span><span>Whisper</span><span>Agentic Systems</span><span>Tailscale</span><span>Voice AI</span></div>

        <div class="mm-contrib" id="mailmateContrib" aria-hidden="true">
            <div class="mm-contrib-clip"><div class="mm-contrib-inner">
                <div class="mm-contrib-row"><strong>Priyam Trivedi</strong><span>Primary integration and current-system architecture: Flask migration, Gmail workspace, calendar intelligence, Kyle, Whisper, Tailscale compute, Work Agent, voice, privacy controls and runtime/UI stabilization.</span></div>
                <div class="mm-contrib-row"><strong>Sreyanko</strong><span>Substantial original dashboard shell and Overview frontend work.</span></div>
                <div class="mm-contrib-row"><strong>Kartikay</strong><span>Early Supabase / Node dashboard and service integration.</span></div>
                <div class="mm-contrib-row"><strong>Asmin Sinha</strong><span>Initial Express, Gmail OAuth and Gemini backend foundation.</span></div>
                <div class="mm-contrib-row"><strong>Rupayan</strong><span>Initial repository setup and isolated local-time UI work.</span></div>
                <p class="mm-attribution-note">Attribution follows original branch history, not only the author of later main-branch integration commits. Merge-only commits, lockfiles and disconnected snapshot diffs are not treated as proof of authorship.</p>
            </div></div>
        </div>
    </div>
</div>
'''

js = r'''
<script>
    // --- MAILMATE SHOWCASE INTERACTIONS ---
    (() => {
        const row = document.getElementById('mailmate-project-row');
        if (!row) return;

        const reveal = () => row.classList.add('is-visible');
        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        reveal();
                        observer.disconnect();
                    }
                });
            }, { threshold: 0.18, rootMargin: '0px 0px -7% 0px' });
            observer.observe(row);
        } else {
            reveal();
        }

        const toggle = document.getElementById('mailmateContribToggle');
        const panel = document.getElementById('mailmateContrib');
        if (toggle && panel) {
            toggle.addEventListener('click', () => {
                const open = !panel.classList.contains('is-open');
                panel.classList.toggle('is-open', open);
                panel.setAttribute('aria-hidden', String(!open));
                toggle.setAttribute('aria-expanded', String(open));
            });
        }

        const visual = document.getElementById('mailmateVisual');
        const tilt = document.getElementById('mailmateTilt');
        const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (visual && tilt && !reduced && window.matchMedia('(pointer:fine)').matches) {
            visual.addEventListener('pointermove', (event) => {
                const rect = visual.getBoundingClientRect();
                const px = (event.clientX - rect.left) / rect.width - .5;
                const py = (event.clientY - rect.top) / rect.height - .5;
                tilt.style.transform = `rotateX(${py * -7}deg) rotateY(${px * 9}deg)`;
            });
            visual.addEventListener('pointerleave', () => {
                tilt.style.transform = 'rotateX(0deg) rotateY(0deg)';
            });
        }
    })();
</script>
'''

css = textwrap.indent(textwrap.dedent(css).strip(), '        ')
html = textwrap.indent(textwrap.dedent(html).strip(), '            ')
js = textwrap.indent(textwrap.dedent(js).strip(), '    ')

css_start_marker = '        /* --- MailMate Project --- */'
css_end_marker = '        /* --- Testimonials Section (Sticky & Overlap Logic) --- */'
css_start = text.index(css_start_marker)
css_end = text.index(css_end_marker)
text = text[:css_start] + css + '\n\n' + text[css_end:]

html_start_marker = '            <!-- MAILMATE / CIPHERSQUAD -->'
html_end_marker = '            <div class="project-row" id="priyn-project-row"'
html_start = text.index(html_start_marker)
html_end = text.index(html_end_marker)
text = text[:html_start] + html + '\n\n' + text[html_end:]

script_marker = '    <!-- YouTube Background Video Logic (Direct IFrame) -->'
if 'MAILMATE SHOWCASE INTERACTIONS' not in text:
    text = text.replace(script_marker, js + '\n\n' + script_marker, 1)

text = text.replace(
    '<span>★</span><span>★</span><span>★</span><span class="half-star">★</span><span class="half-star">★</span>\n                            <span class="testi-rating-label">Learning and execution</span>',
    '<span>★</span><span>★</span><span>★</span><span>★</span><span class="half-star">★</span>\n                            <span class="testi-rating-label">Learning and execution</span>'
)

path.write_text(text, encoding='utf-8')
print('MailMate showcase patched:', path)
