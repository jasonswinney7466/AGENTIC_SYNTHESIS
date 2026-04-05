import asyncio
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import socket
import random
import re

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# [ AGENTIC_SYNTHESIS // AMBER_SIGNAL v8.4 ]
# [ NODE: PC1 // 2070 S // STAINLESS ]
# [ PATCH: VOICE_DIVERSITY_v2 // GENDER_SYNC_FIX ]
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

OLLAMA_URL = "http://127.0.0.1:11434"

HTML_CONTENT = r"""
<!DOCTYPE html>
<html>
<head>
    <title>AGENTIC_SYNTHESIS // AMBER_SIGNAL</title>
    <style>
        html, body { background: #000; color: #FFF; font-family: 'Courier New', monospace; margin: 0; padding: 0; overflow: hidden; height: 100%; width: 100%; }
        #header { height: 40px; border-bottom: 2px solid #FFB000; color: #FFB000; display: flex; justify-content: center; align-items: center; font-weight: bold; background: #080808; box-sizing: border-box; letter-spacing: 2px; position: relative; z-index: 10; }
        .header-side { position: absolute; left: 20px; font-size: 10px; color: #444; letter-spacing: 1px; }
        #state-ui { position: absolute; right: 20px; font-size: 10px; transition: color 0.3s; }
        .state-active { color: #00FFFF !important; text-shadow: 0 0 10px #00FFFF; animation: blink 1s infinite; }
        
        #arena { display: flex; height: calc(100vh - 230px); padding: 15px; gap: 15px; box-sizing: border-box; align-items: stretch; }
        .node-box { width: 22%; display: flex; flex-direction: column; align-items: center; border: 1px solid #222; padding: 15px; background: #030303; position: relative; box-sizing: border-box; }
        #feed { flex-grow: 1; width: 56%; display: flex; flex-direction: column; border: 2px solid #1a1a1a; background: #020202; overflow: hidden; position: relative; }
        #log { flex-grow: 1; overflow-y: auto; padding: 20px; scroll-behavior: smooth; }
        
        #splash, #recap { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.98); z-index: 100; display: none; flex-direction: column; align-items: center; justify-content: center; text-align: center; border: 2px solid #FFB000; box-sizing: border-box; padding: 40px; }
        .splash-logo { color: #FFB000; font-size: 11px; margin-bottom: 20px; line-height: 1.1; }
        .splash-intel, .recap-txt { color: #FFF; font-size: 14px; max-width: 85%; margin-bottom: 30px; border-top: 1px solid #222; padding-top: 20px; line-height: 1.6; }
        #splash-bar-container { width: 300px; height: 4px; background: #111; border: 1px solid #222; }
        #splash-bar { width: 0%; height: 100%; background: #FFB000; box-shadow: 0 0 10px #FFB000; transition: width 6s linear; }

        pre.pixel-art { font-size: 18px; line-height: 1.1; color: #FFF; margin: 15px auto; background: #000; border: 1px solid #111; width: 100%; height: 130px; white-space: pre; display: flex; align-items: center; justify-content: center; text-align: center; flex-shrink: 0; }
        .amber-txt { color: #FFB000; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 5px; font-size: 14px; }
        .trait-tag { font-size: 10px; color: #FFB000; border: 1px solid #333; padding: 2px 6px; margin-bottom: 10px; text-transform: uppercase; background: #080808; }
        .timer-container { width: 100%; height: 8px; background: #111; margin-top: 15px; border: 1px solid #222; flex-shrink: 0; }
        .timer-bar { width: 0%; height: 100%; background: linear-gradient(90deg, #FFB000 0%, #FFD700 100%); transition: width 0.1s linear; }
        .vitals { font-size: 9px; color: #FF00FF; width: 100%; border-top: 1px solid #111; padding-top: 10px; margin-top: auto; opacity: 0.8; text-align: center; }
        .msg { margin-bottom: 40px; border-bottom: 1px solid #333; padding-bottom: 25px; font-size: 15px; line-height: 1.7; color: #ddd; width: 100%; }
        .node-name { color: #FFB000; font-weight: bold; display: block; border-left: 4px solid #FFB000; padding-left: 12px; margin-bottom: 10px; font-size: 13px; }
        
        #control-deck { height: 190px; background: #000; border-top: 2px solid #FFB000; padding: 10px 15px; display: grid; grid-template-columns: 1.2fr 1.5fr 1.2fr; gap: 15px; box-sizing: border-box; }
        .deck-section { display: flex; flex-direction: column; gap: 4px; }
        input, textarea, select { background: #000; color: #FFB000; border: 1px solid #222; padding: 4px; font-family: monospace; font-size: 11px; }
        button { background: #FFB000; color: #000; border: none; padding: 10px; font-weight: bold; cursor: pointer; text-transform: uppercase; }
        #reset-btn { background: #330000; color: #FFF; padding: 5px; font-size: 10px; margin-top: 4px; }
        .thinking { color: #FF0000; font-weight: bold; animation: blink 1.5s infinite; display: none; font-size: 10px; text-align:center; }
        @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    </style>
</head>
<body onload="init()">
    <div id="header">
        <span class="header-side">PC1 // NOBLE_24.04 // v8.4.0</span>
        <span>[ AGENTIC SYNTHESIS ]</span>
        <span id="state-ui">[ STANDBY ]</span>
    </div>
    
    <div id="arena">
        <div class="node-box" id="pod-1"><div class="amber-txt" id="display-n1">AGENT_01</div><div class="trait-tag" id="trait-1">OFFLINE</div><pre class="pixel-art" id="art-1"></pre><div class="timer-container"><div id="bar-1" class="timer-bar"></div></div><div id="think-1" class="thinking">>> [ SIMULATING ]</div><div class="vitals">NODE: <span id="load-1">0%</span> | PULSE: <span id="pulse-1">0ms</span></div></div>
        
        <div id="feed">
            <div id="splash">
                <pre class="splash-logo">
   ___   ___________ _  ____________   _____  __  ___  __________  __________ ____
  / _ | / ___/ __/ |/ |/_  __/  _/ /  / __/ |/ / / / /_  __/ / / / __/ __//  _/
 / __ |/ (_ / _//    /  / / _/ // /__/ _//    / / / / / / / / /_/ /\ \/ _/ _/ // 
/_/ |_|\___/___/_/|_/  /_/ /___/____/___/_/|_/ /_/ /_/  \____/___/___/___/   
                </pre>
                <div class="splash-roster" id="splash-roster-txt">AGENT_01 VS AGENT_02</div>
                <div class="splash-intel" id="splash-topic-txt">TOPIC: WAITING FOR SIGNAL...</div>
                <div id="splash-bar-container"><div id="splash-bar"></div></div>
            </div>
            
            <div id="recap">
                <pre class="splash-logo">
   ___   ___________ _  ____________   _____  __  ___  __________  __________ ____
  / _ | / ___/ __/ |/ |/_  __/  __/ /  / __/ |/ / / / /_  __/ / / / __/ __//  _/
 / __ |/ (_ / _//    /  / / _/ // /__/ _//    / / / / / / / / /_/ /\ \/ _/ _/ // 
/_/ |_|\___/___/_/|_/  /_/ /___/____/___/_/|_/ /_/ /_/  \____/___/___/___/   
                </pre>
                <div class="amber-txt">SYNTHESIS COMPLETE // POST-LOG ANALYSIS</div>
                <div class="recap-txt" id="recap-content">ARCHIVING DATA VECTORS...</div>
                <button onclick="downloadSession()">DOWNLOAD HARD-COPY (.TXT)</button>
                <button id="reset-btn" onclick="stopAndReset()">CLEAR RECAP</button>
            </div>
            <div id="log"></div>
        </div>
        
        <div class="node-box" id="pod-2"><div class="amber-txt" id="display-n2">AGENT_02</div><div class="trait-tag" id="trait-2">OFFLINE</div><pre class="pixel-art" id="art-2"></pre><div class="timer-container"><div id="bar-2" class="timer-bar"></div></div><div id="think-2" class="thinking">>> [ SIMULATING ]</div><div class="vitals">NODE: <span id="load-2">0%</span> | PULSE: <span id="pulse-2">0ms</span></div></div>
    </div>

    <div id="control-deck">
        <div class="deck-section">
            <div style="display:flex; gap:4px;"><select id="silo-1-1" onchange="applySilo(1, 1)"><option value="">- ACADEMIC -</option></select><select id="silo-1-2" onchange="applySilo(1, 2)"><option value="">- CIVILIAN -</option></select><select id="silo-1-3" onchange="applySilo(1, 3)"><option value="">- FRINGE -</option></select></div>
            <input type="text" id="name-1" placeholder="NAME"><select id="model-1"></select><textarea id="persona-1" rows="2"></textarea>
        </div>
        <div class="deck-section">
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px; margin-bottom:5px;"><span>ROUND: <span id="round-display">00/--</span></span><span>LIMIT: <input type="number" id="rounds-limit" value="10" min="1" max="20" style="width:40px;"></span></div>
            <div style="display:flex; gap:5px; margin-bottom:5px;">
                <select id="spark-cat" style="width:100px;"><option value="societal matters">SOCIETAL</option><option value="the future of AI safety">AI_SAFETY</option><option value="theoretical science">SCIENCE</option><option value="comparative history">HISTORY</option></select>
                <input type="text" id="topic" placeholder="TOPIC" style="flex-grow:1;"><button style="width:40px;" onclick="sparkAI()">⚡</button>
            </div>
            <button id="start-btn" onclick="runSynthesis()">IGNITE SYNTHESIS</button>
            <button id="reset-btn" onclick="stopAndReset()">RESET NODE</button>
        </div>
        <div class="deck-section">
            <div style="display:flex; gap:4px;"><select id="silo-2-1" onchange="applySilo(2, 1)"><option value="">- ACADEMIC -</option></select><select id="silo-2-2" onchange="applySilo(2, 2)"><option value="">- CIVILIAN -</option></select><select id="silo-2-3" onchange="applySilo(2, 3)"><option value="">- FRINGE -</option></select></div>
            <input type="text" id="name-2" placeholder="NAME"><select id="model-2"></select><textarea id="persona-2" rows="2"></textarea></div>
        </div>
    </div>

    <script>
        let abortSignal = false; let synth = window.speechSynthesis; let sessionBuffer = [];
        let voicesUsed = { "1": null, "2": null };

        const ART = { physicist: "  .---.\n / o o \\\\\n(  <  )\n \\\\---/ \n  [|||]", lawyer: "  _____\n |     |\n |⚖️ |\n |_____|\n  /___\\", neuro: "  _---_\n ( BRAIN )\n  \\---/\n   | |", dean: "  _--_\n /|  |\\\n |----|\n |____|", archivist: "  .---.\n |#####|\n |#####|\n '-----'", ceo: "  .---.\n / $$$ \\\\\n |  _  |\n '-----'", diplomat: "  .---.\n /WORLD \\\\\n |  _  |\n '-----'", ethicist: "  .---.\n | DNA |\n |#####|\n '-----'", architect: "  .---.\n |CITY |\n |#####|\n '-----'", math: "  .---.\n |1+1=2|\n |#####|\n '-----'", trucker: "  _____\n | RIG |\n |_____|\n O---O ", clerk: "  .---.\n |SCAN |\n |_____|\n   | |", foreman: "  .---.\n | HARD|\n | HAT |\n '-----'", farmer: "  .---.\n |GRAIN|\n |#####|\n   | |", teacher: "  .---.\n | ABC |\n |#####|\n '-----'", mechanic: "  _   _\n \\\\ / /\n  \\ V /\n  / _ \\", nurse: "  .---.\n |  +  |\n |_____|\n   | |", cook: "  .---.\n ( CHEF)\n |_____|\n   | |", electric: "  .---.\n |BOLT |\n |#####|\n '-----'", social: "  .---.\n |HELP |\n |#####|\n '-----'", anarchist: "  .---.\n (  A  )\n  \\---/ ", conspiracy: "  .---.\n / TIN \\\\\n | FOIL|\n '-----'", transhuman: "  .---.\n (CYBER)\n |#####|\n '-----'", hacker: "  .---.\n | GLCH|\n |#####|\n '-----'", hermit: "  .---.\n ( SHHH)\n |_____|\n   | |", cult: "  .---.\n ( EYE )\n |_____|\n   | |", colonist: "  .---.\n ( MARS)\n |_____|\n   | |", artist: "  .---.\n (PAINT)\n |_____|\n   | |", prepper: "  .---.\n (SAFE )\n |_____|\n   | |", oracle: "  .---.\n ( AI  )\n |_____|\n   | |" };
        const VAULT = {
            academic: { "Physicist": {g:"male", t:"ACADEMIC", p:"Theoretical physicist. Logic metaphors.", a:ART.physicist}, "Lawyer": {g:"male", t:"LEGAL", p:"Constitutional lawyer. Precise.", a:ART.lawyer}, "Neurosurgeon": {g:"male", t:"MEDICAL", p:"Neurosurgeon. Clinical.", a:ART.neuro}, "Dean": {g:"male", t:"INSTITUTIONAL", p:"University Dean. Bureaucratic.", a:ART.dean}, "Archivist": {g:"female", t:"HISTORY", p:"Historical archivist. Obsessed with truth.", a:ART.archivist}, "CEO": {g:"male", t:"CORPORATE", p:"CEO. Strategic.", a:ART.ceo}, "Diplomat": {g:"male", t:"GEOPOLITICS", p:"Diplomat. Nuanced.", a:ART.diplomat}, "Ethicist": {g:"female", t:"BIO-ETHICS", p:"Bio-ethicist. Philosophical.", a:ART.ethicist}, "Architect": {g:"female", t:"URBANISM", p:"City architect. Structural.", a:ART.architect}, "Mathematician": {g:"male", t:"PURE LOGIC", p:"Mathematician. Abstract.", a:ART.math} },
            civilian: { "Trucker": {g:"male", t:"LOGISTICS", p:"Trucker. Practical grit.", a:ART.trucker}, "Clerk": {g:"female", t:"RETAIL", p:"Retail worker. Observant.", a:ART.clerk}, "Foreman": {g:"male", t:"CONSTRUCTION", p:"Foreman. Direct.", a:ART.foreman}, "Farmer": {g:"male", t:"AGRARIAN", p:"Farmer. Grounded.", a:ART.farmer}, "Teacher": {g:"female", t:"EDUCATION", p:"Teacher. Patient.", a:ART.teacher}, "Mechanic": {g:"male", t:"REPAIR", p:"Mechanic. Problem solver.", a:ART.mechanic}, "Nurse": {g:"female", t:"HEALTHCARE", p:"Nurse. Biological empathy.", a:ART.nurse}, "Cook": {g:"male", t:"CULINARY", p:"Line cook. Fast-paced.", a:ART.cook}, "Electrician": {g:"male", t:"UTILITY", p:"Electrician. Power focused.", a:ART.electric}, "Social Worker": {g:"female", t:"SOCIETAL", p:"Social worker. Weary of systems.", a:ART.social} },
            fringe: { "Anarchist": {g:"male", t:"SUBVERSIVE", p:"Anarchist. Anti-system.", a:ART.anarchist}, "Conspiracist": {g:"male", t:"REVELATION", p:"Conspiracy theorist.", a:ART.conspiracy}, "Transhuman": {g:"female", t:"POST-HUMAN", p:"Transhumanist.", a:ART.transhuman}, "Hacker": {g:"male", t:"DIGITAL", p:"Cyber-hacker. Digital subversion.", a:ART.hacker}, "Hermit": {g:"male", t:"ISOLATION", p:"Hermit. Minimalist.", a:ART.hermit}, "Cult Leader": {g:"male", t:"CHARISMA", p:"Cult leader. Ethereal.", a:ART.cult}, "Colonist": {g:"female", t:"OFF-WORLD", p:"Space colonist.", a:ART.colonist}, "Artist": {g:"female", t:"EPHEMERAL", p:"Street artist. Creative.", a:ART.artist}, "Prepper": {g:"male", t:"SURVIVAL", p:"Doomsday prepper. survivalist.", a:ART.prepper}, "AI Oracle": {g:"female", t:"SYNTHETIC", p:"Machine voice. eerie.", a:ART.oracle} }
        };

        function getVoice(gender, otherVoice) {
            let voices = synth.getVoices().filter(v => v.lang.startsWith('en'));
            let filtered = voices.filter(v => {
                let n = v.name.toLowerCase();
                return (gender === 'male') ? (n.includes('david') || n.includes('mark') || n.includes('male')) : (n.includes('zira') || n.includes('zira') || n.includes('female'));
            });
            if (filtered.length === 0) filtered = voices; 
            let choice = filtered.find(v => v !== otherVoice) || filtered[0];
            return choice;
        }

        function init() { fetchModels(); for (let i = 1; i <= 2; i++) { populate(document.getElementById(`silo-${i}-1`), VAULT.academic); populate(document.getElementById(`silo-${i}-2`), VAULT.civilian); populate(document.getElementById(`silo-${i}-3`), VAULT.fringe); } setInterval(() => { for(let i=1; i<=2; i++){ document.getElementById(`load-${i}`).innerText = Math.floor(Math.random()*15+30)+"%"; document.getElementById(`pulse-${i}`).innerText = Math.floor(Math.random()*40+80)+"ms"; } }, 1000); }
        function populate(sel, data) { Object.keys(data).sort().forEach(k => { let o = document.createElement('option'); o.value = k; o.innerText = k.toUpperCase(); sel.appendChild(o); }); }
        
        function applySilo(agent, siloNum) { 
            const keys = ["academic", "civilian", "fringe"]; 
            const val = document.getElementById(`silo-${agent}-${siloNum}`).value; 
            if (!val) return; 
            for(let s=1; s<=3; s++) { if(s !== siloNum) document.getElementById(`silo-${agent}-${s}`).value = ""; } 
            const data = VAULT[keys[siloNum-1]][val]; 
            document.getElementById(`name-${agent}`).value = val; 
            document.getElementById(`persona-${agent}`).value = data.p; 
            document.getElementById(`trait-${agent}`).innerText = data.t; 
            document.getElementById(`display-n${agent}`).innerText = val; 
            document.getElementById(`art-${agent}`).textContent = data.a;
            document.getElementById(`pod-${agent}`).dataset.gender = data.g; 
        }

        async function fetchModels() { try { const res = await fetch('/models'); const json = await res.json(); [document.getElementById('model-1'), document.getElementById('model-2')].forEach(s => { s.innerHTML = ""; json.forEach(m => { let o = document.createElement('option'); o.value = m.name; o.innerText = m.name.toUpperCase(); if(m.name.includes("3.2:3b")) o.selected = true; s.appendChild(o); }); }); } catch (e) {} }
        async function sparkAI() { const m = document.getElementById('model-1').value; const c = document.getElementById('spark-cat').value; try { const res = await fetch('/spark', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({model:m, category:c})}); const d = await res.json(); document.getElementById('topic').value = d.prompt; } catch (e) {} }
        async function stopAndReset() { abortSignal = true; synth.cancel(); document.getElementById('log').innerHTML = ""; document.getElementById('round-display').innerText = "00/--"; document.getElementById('start-btn').style.display = 'block'; document.getElementById('splash').style.display = 'none'; document.getElementById('recap').style.display = 'none'; document.getElementById('state-ui').innerText = "[ STANDBY ]"; document.getElementById('state-ui').classList.remove('state-active'); sessionBuffer = []; await fetch('/purge', {method:'POST'}); }
        function downloadSession() { const content = sessionBuffer.join("\n\n"); const blob = new Blob([content], { type: 'text/plain' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = `Synthesis_Take_${Date.now()}.txt`; a.click(); }

        async function runSynthesis() {
            abortSignal = false; sessionBuffer = [];
            const rounds = parseInt(document.getElementById('rounds-limit').value) || 10;
            const topic = document.getElementById('topic').value;
            const n1 = document.getElementById('name-1').value; const n2 = document.getElementById('name-2').value;
            
            document.getElementById('state-ui').innerText = "[ ACTIVE ]";
            document.getElementById('state-ui').classList.add('state-active');
            
            const g1 = document.getElementById('pod-1').dataset.gender;
            const g2 = document.getElementById('pod-2').dataset.gender;
            voicesUsed["1"] = getVoice(g1, null);
            voicesUsed["2"] = getVoice(g2, voicesUsed["1"]);

            sessionBuffer.push(`TOPIC: ${topic}\nROSTER: ${n1} vs ${n2}\n---`);
            document.getElementById('splash').style.display = 'flex';
            document.getElementById('splash-topic-txt').innerText = `TOPIC: ${topic}`;
            document.getElementById('splash-roster-txt').innerText = `${n1} VS ${n2}`;
            setTimeout(() => { document.getElementById('splash-bar').style.width = '100%'; }, 50);
            await new Promise(r => setTimeout(r, 6500)); 
            if(abortSignal) return;
            document.getElementById('splash').style.display = 'none';
            document.getElementById('splash-bar').style.width = '0%';
            document.getElementById('start-btn').style.display = 'none';
            
            let last = topic;
            for (let i = 1; i <= rounds; i++) {
                if (abortSignal) break;
                document.getElementById('round-display').innerText = `${i.toString().padStart(2,'0')}/${rounds}`;
                const agents = [{id:"1", n:n1, m:document.getElementById('model-1').value, p:document.getElementById('persona-1').value}, {id:"2", n:n2, m:document.getElementById('model-2').value, p:document.getElementById('persona-2').value}];
                for (const a of agents) {
                    if (abortSignal) break;
                    document.getElementById(`think-${a.id}`).style.display = 'block';
                    try {
                        const r = await fetch('/generate', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({prompt:last, system:`Role: ${a.n}. Persona: ${a.p}. Under 100 words. Speak directly.`, model:a.m})});
                        const j = await r.json(); last = j.response;
                        sessionBuffer.push(`${a.n}: ${last}`);
                    } catch (e) { last = "NODE_ERROR"; }
                    document.getElementById(`think-${a.id}`).style.display = 'none';
                    const msg = document.createElement('div'); msg.className = 'msg';
                    msg.innerHTML = `<span class="node-name">${a.n}</span><span class="txt"></span>`;
                    document.getElementById('log').appendChild(msg);
                    const span = msg.querySelector('.txt');
                    const ut = new SpeechSynthesisUtterance(last);
                    ut.voice = voicesUsed[a.id];
                    let charIdx = 0; const bar = document.getElementById(`bar-${a.id}`);
                    await new Promise(res => {
                        ut.onend = async () => { await new Promise(ok => setTimeout(ok, 3000)); res(); };
                        synth.speak(ut);
                        const ty = setInterval(() => {
                            if (charIdx < last.length && !abortSignal) {
                                span.innerHTML += last[charIdx];
                                document.getElementById('log').scrollTop = document.getElementById('log').scrollHeight;
                                charIdx++; bar.style.width = ((charIdx/last.length)*100)+"%";
                            } else { clearInterval(ty); bar.style.width = "100%"; }
                        }, 60);
                    });
                }
            }
            if(!abortSignal) {
                document.getElementById('recap').style.display = 'flex';
                document.getElementById('recap-content').innerText = "SYSTEM ANALYZING CONVERSATION...";
                document.getElementById('state-ui').innerText = "[ ANALYZING ]";
                const res = await fetch('/analyze', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({log: sessionBuffer.join("\n"), model: document.getElementById('model-1').value})});
                const data = await res.json();
                document.getElementById('recap-content').innerText = data.analysis;
                document.getElementById('state-ui').innerText = "[ STANDBY ]";
                document.getElementById('state-ui').classList.remove('state-active');
            }
        }
    </script>
</body>
</html>
"""

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        payload = {"model":data['model'], "stream":False, "prompt":f"Provide a 3-sentence executive summary of the intellectual core of this transcript. TRANSCRIPT: {data['log']}"}
        res = await client.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=60.0)
        return {"analysis": re.sub(r'<think>.*?</think>', '', res.json()['response'], flags=re.DOTALL).strip()}

@app.post("/spark")
async def spark(request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{OLLAMA_URL}/api/generate", json={"model":data['model'], "stream":False, "prompt":f"Scenario for conversation about {data.get('category')}. One sentence."}, timeout=60.0)
        return {"prompt": re.sub(r'<think>.*?</think>', '', res.json()['response'], flags=re.DOTALL).strip()}

@app.get("/", response_class=HTMLResponse)
async def home(): return HTMLResponse(content=HTML_CONTENT)

@app.get("/models")
async def models():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{OLLAMA_URL}/api/tags")
        return res.json()['models']

@app.post("/purge")
async def purge():
    async with httpx.AsyncClient() as client:
        await client.post(f"{OLLAMA_URL}/api/generate", json={"model":"", "keep_alive":0})
    return {"status":"OK"}

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{OLLAMA_URL}/api/generate", json={"model":data['model'], "prompt":data['prompt'], "system":data['system'], "stream":False}, timeout=120.0)
        raw = res.json()['response']
        clean = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL)
        clean = re.sub(r'^As [a-zA-Z0-9_ ]+[,:]', '', clean, flags=re.IGNORECASE)
        clean = re.sub(r'^[a-zA-Z0-9_ ]+:', '', clean)
        return {"response": clean.strip()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=18789)