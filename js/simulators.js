/**
 * CYBERNEXUS - Interactive Labs & Attack Simulators Engine
 * Pure Vanilla JavaScript & Canvas visualizers
 */

const SimulatorsEngine = {
  // Current active simulator id
  activeLabId: null,

  // Initialize and render a lab inside #lab-workspace-content
  loadLab(labId) {
    this.activeLabId = labId;
    const container = document.getElementById('lab-workspace-content');
    if (!container) return;

    switch (labId) {
      case 'tor':
        this.renderTorLab(container);
        break;
      case 'password':
        this.renderPasswordLab(container);
        break;
      case 'killchain':
        this.renderKillChainLab(container);
        break;
      case 'phishing':
        this.renderPhishingLab(container);
        break;
      case 'eviltwin':
        this.renderEvilTwinLab(container);
        break;
      case 'malware':
        this.renderMalwareLab(container);
        break;
      case 'ddos':
        this.renderDDoSAttackLab(container);
        break;
      case 'mobile-mdm':
        this.renderMobileMDMLab(container);
        break;
      default:
        container.innerHTML = `<p class="text-muted">Select a cyber lab to launch the interactive simulator.</p>`;
    }
  },

  /* =========================================================================
     LAB 1: TOR ONION ROUTING SIMULATOR
     ========================================================================= */
  renderTorLab(container) {
    container.innerHTML = `
      <div class="lab-header">
        <div>
          <span class="sim-badge">Privacy & Network Layer</span>
          <h3>🧅 Tor Onion Routing & 3-Hop Encryption Visualizer</h3>
          <p class="text-secondary" style="font-size:0.85rem;">Observe how Onion Routing encrypts packet payloads in 3 distinct layers and strips them step-by-step across Guard, Middle, and Exit relays.</p>
        </div>
        <button class="btn-cyber-outline" onclick="SimulatorsEngine.resetTorLab()">Reset Circuit</button>
      </div>

      <div class="lab-interactive-canvas-wrap" id="tor-canvas-wrap" style="padding: 2rem 1rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; position: relative; gap: 1rem; flex-wrap: wrap;">
          <!-- Client Node -->
          <div class="sim-node" id="tor-client" style="flex:1; min-width:130px;">
            <div style="font-size:1.5rem;">💻</div>
            <strong style="color:var(--text-primary); font-size:0.85rem;">Client (Source)</strong>
            <div style="font-size:0.7rem; color:var(--text-muted); font-family:var(--font-mono);">IP: 198.51.100.24</div>
            <div style="margin-top:0.4rem; font-size:0.65rem; color:var(--cyber-cyan); background:rgba(0,242,254,0.1); padding:2px 4px; border-radius:3px;">Holds Keys: K1, K2, K3</div>
          </div>

          <div style="color:var(--text-muted); font-size:1.2rem;">➔</div>

          <!-- Guard Node -->
          <div class="sim-node" id="tor-guard" style="flex:1; min-width:130px;">
            <div style="font-size:1.5rem;">🛡️</div>
            <strong style="color:var(--text-primary); font-size:0.85rem;">Entry / Guard</strong>
            <div style="font-size:0.7rem; color:var(--text-muted); font-family:var(--font-mono);">IP: 104.244.72.11</div>
            <div style="margin-top:0.4rem; font-size:0.65rem; color:var(--cyber-cyan); background:rgba(0,242,254,0.1); padding:2px 4px; border-radius:3px;">Peels Layer 1 (K1)</div>
          </div>

          <div style="color:var(--text-muted); font-size:1.2rem;">➔</div>

          <!-- Middle Node -->
          <div class="sim-node" id="tor-middle" style="flex:1; min-width:130px;">
            <div style="font-size:1.5rem;">🔄</div>
            <strong style="color:var(--text-primary); font-size:0.85rem;">Middle Relay</strong>
            <div style="font-size:0.7rem; color:var(--text-muted); font-family:var(--font-mono);">IP: 185.220.101.5</div>
            <div style="margin-top:0.4rem; font-size:0.65rem; color:var(--cyber-green); background:rgba(0,255,135,0.1); padding:2px 4px; border-radius:3px;">Peels Layer 2 (K2)</div>
          </div>

          <div style="color:var(--text-muted); font-size:1.2rem;">➔</div>

          <!-- Exit Node -->
          <div class="sim-node" id="tor-exit" style="flex:1; min-width:130px;">
            <div style="font-size:1.5rem;">🚪</div>
            <strong style="color:var(--text-primary); font-size:0.85rem;">Exit Node</strong>
            <div style="font-size:0.7rem; color:var(--text-muted); font-family:var(--font-mono);">IP: 51.15.43.205</div>
            <div style="margin-top:0.4rem; font-size:0.65rem; color:var(--cyber-purple); background:rgba(121,40,202,0.1); padding:2px 4px; border-radius:3px;">Peels Layer 3 (K3)</div>
          </div>

          <div style="color:var(--text-muted); font-size:1.2rem;">➔</div>

          <!-- Destination Server -->
          <div class="sim-node" id="tor-dest" style="flex:1; min-width:130px;">
            <div style="font-size:1.5rem;">🌐</div>
            <strong style="color:var(--text-primary); font-size:0.85rem;">Web Server</strong>
            <div style="font-size:0.7rem; color:var(--text-muted); font-family:var(--font-mono);">https://bank.com</div>
            <div style="margin-top:0.4rem; font-size:0.65rem; color:var(--cyber-amber); background:rgba(255,183,3,0.1); padding:2px 4px; border-radius:3px;">Receives Request</div>
          </div>
        </div>

        <!-- Dynamic Packet Inspection Status -->
        <div style="margin-top:2rem; background:rgba(13,18,36,0.8); border:1px solid var(--border-subtle); border-radius:8px; padding:1rem;" id="tor-inspect-panel">
          <div style="font-size:0.75rem; text-transform:uppercase; color:var(--cyber-cyan); font-weight:700; margin-bottom:0.5rem;">Circuit Packet State</div>
          <div id="tor-packet-desc" style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">Click <strong>"Transmit Encrypted Packet"</strong> to begin the multi-hop transmission.</div>
        </div>
      </div>

      <div class="lab-controls-panel">
        <button class="btn-cyber-primary" id="btn-tor-transmit" onclick="SimulatorsEngine.stepTorPacket()">Transmit Encrypted Packet</button>
        <button class="btn-cyber-outline" onclick="SimulatorsEngine.autoPlayTor()">▶ Auto Play Full Circuit</button>
      </div>

      <div class="terminal-box" id="tor-terminal" style="margin-top:1rem;">
        <div class="terminal-line">[TOR CIRCUIT INITIALIZED] 3-hop relay consensus acquired from directory authorities.</div>
        <div class="terminal-line">[DH KEY EXCHANGE] Negotiated K1 (Guard), K2 (Middle), K3 (Exit). Ready for payload encapsulation.</div>
      </div>
    `;

    this.torStep = 0;
  },

  torStep: 0,
  torInterval: null,

  resetTorLab() {
    if (this.torInterval) clearInterval(this.torInterval);
    this.torStep = 0;
    document.querySelectorAll('#tor-canvas-wrap .sim-node').forEach(node => node.classList.remove('active', 'compromised'));
    const desc = document.getElementById('tor-packet-desc');
    if (desc) desc.innerHTML = 'Circuit reset. Ready for new packet transmission.';
    const btn = document.getElementById('btn-tor-transmit');
    if (btn) btn.innerText = 'Transmit Encrypted Packet';
  },

  stepTorPacket() {
    const nodes = ['tor-client', 'tor-guard', 'tor-middle', 'tor-exit', 'tor-dest'];
    const logs = [
      '[STEP 1 - CLIENT ENCAPSULATION] Encrypting Payload with K3 (Exit), then K2 (Middle), then K1 (Guard). Packet: [E1[E2[E3[GET /account HTTP/1.1]]]]',
      '[STEP 2 - ENTRY GUARD NODE] Peeling Layer 1 (K1). Guard sees Source IP: 198.51.100.24 and Next Hop: 185.220.101.5. Guard CANNOT read packet or see destination!',
      '[STEP 3 - MIDDLE RELAY NODE] Peeling Layer 2 (K2). Middle node sees Prev Hop: 104.244.72.11 and Next Hop: 51.15.43.205. Middle node knows NEITHER Source NOR Destination!',
      '[STEP 4 - EXIT RELAY NODE] Peeling Layer 3 (K3). Exit node transmits plaintext request to https://bank.com. Exit node sees Destination IP, but has ZERO knowledge of Source Client IP!',
      '[STEP 5 - WEB SERVER DESTINATION] Target server receives request from Exit Node IP (51.15.43.205). The real client identity remains completely anonymous!'
    ];
    const explanations = [
      '<strong>1. Client Node:</strong> Packet is encrypted with 3 layers like an onion. Outer layer: Guard Key (K1), Middle layer: Middle Key (K2), Inner layer: Exit Key (K3).',
      '<strong>2. Entry / Guard Node:</strong> Peels Layer 1 with K1. Knows YOUR real IP address, but only knows to forward to Middle Node. Cannot read payload or see destination.',
      '<strong>3. Middle Relay Node:</strong> Peels Layer 2 with K2. Knows it received from Guard and forwards to Exit. Has NO idea who you are or where the data is ultimately going.',
      '<strong>4. Exit Node:</strong> Peels Layer 3 with K3. Now it sees the raw destination `https://bank.com`. It forwards the request, but has NO knowledge of the original client IP!',
      '<strong>5. Destination Web Server:</strong> Server sees the connection originating from the Exit Node IP. Source anonymity is fully preserved!'
    ];

    if (this.torStep < nodes.length) {
      document.querySelectorAll('#tor-canvas-wrap .sim-node').forEach(node => node.classList.remove('active'));
      const activeNode = document.getElementById(nodes[this.torStep]);
      if (activeNode) activeNode.classList.add('active');

      const desc = document.getElementById('tor-packet-desc');
      if (desc) desc.innerHTML = explanations[this.torStep];

      const term = document.getElementById('tor-terminal');
      if (term) {
        const line = document.createElement('div');
        line.className = 'terminal-line ' + (this.torStep === 4 ? 'success' : 'warning');
        line.innerText = logs[this.torStep];
        term.appendChild(line);
        term.scrollTop = term.scrollHeight;
      }

      this.torStep++;
      const btn = document.getElementById('btn-tor-transmit');
      if (btn) {
        btn.innerText = this.torStep < nodes.length ? `Step to Next Hop (${this.torStep + 1}/5)` : 'Transmission Complete (Reset)';
      }
    } else {
      this.resetTorLab();
    }
  },

  autoPlayTor() {
    this.resetTorLab();
    this.torInterval = setInterval(() => {
      if (this.torStep < 5) {
        this.stepTorPacket();
      } else {
        clearInterval(this.torInterval);
      }
    }, 1500);
  },

  /* =========================================================================
     LAB 2: PASSWORD STRENGTH & CRYPTOGRAPHIC HASH CRACKER
     ========================================================================= */
  renderPasswordLab(container) {
    container.innerHTML = `
      <div class="lab-header">
        <div>
          <span class="sim-badge">Cryptography & Password Security</span>
          <h3>🔑 Password Entropy, Hashing & Cracking Simulator</h3>
          <p class="text-secondary" style="font-size:0.85rem;">Test password entropy, generate real SHA-256 / MD5 hashes, and simulate live brute-force and dictionary attacks.</p>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:1.5rem;">
        <!-- Left Box: Password Strength & Entropy Analyzer -->
        <div style="background:rgba(13,18,36,0.8); border:1px solid var(--border-subtle); border-radius:12px; padding:1.5rem;">
          <h4 style="color:var(--cyber-cyan); font-size:1rem; margin-bottom:1rem;">1. Real-Time Password Strength & Entropy</h4>
          
          <label style="font-size:0.8rem; color:var(--text-muted); display:block; margin-bottom:0.4rem;">Type a Password to Test:</label>
          <input type="text" id="lab-pwd-input" value="CyberAdmin2024!" oninput="SimulatorsEngine.evaluatePassword(this.value)" 
            style="width:100%; background:var(--bg-tertiary); border:1px solid var(--border-subtle); border-radius:6px; padding:0.65rem 0.85rem; font-family:var(--font-mono); color:var(--text-primary); outline:none; margin-bottom:1rem;" />

          <div style="margin-bottom:1rem;">
            <div style="display:flex; justify-content:space-between; font-size:0.8rem; margin-bottom:0.3rem;">
              <span style="color:var(--text-secondary);">Strength:</span>
              <strong id="pwd-strength-label" style="color:var(--cyber-green);">Strong</strong>
            </div>
            <div style="width:100%; height:8px; background:rgba(255,255,255,0.1); border-radius:4px; overflow:hidden;">
              <div id="pwd-strength-bar" style="width:80%; height:100%; background:var(--cyber-green); transition:width 0.3s ease;"></div>
            </div>
          </div>

          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:0.75rem; font-size:0.8rem; margin-bottom:1rem;">
            <div style="background:rgba(0,0,0,0.3); padding:0.6rem; border-radius:6px; border:1px solid var(--border-subtle);">
              <span style="color:var(--text-muted); display:block; font-size:0.7rem;">Entropy</span>
              <strong id="pwd-entropy" style="color:var(--cyber-cyan); font-family:var(--font-mono);">78.4 bits</strong>
            </div>
            <div style="background:rgba(0,0,0,0.3); padding:0.6rem; border-radius:6px; border:1px solid var(--border-subtle);">
              <span style="color:var(--text-muted); display:block; font-size:0.7rem;">Keyspace (N^L)</span>
              <strong id="pwd-keyspace" style="color:var(--cyber-purple); font-family:var(--font-mono);">3.8 × 10^23</strong>
            </div>
          </div>

          <div style="font-size:0.8rem; color:var(--text-secondary); line-height:1.6; border-top:1px solid var(--border-subtle); padding-top:0.75rem;">
            <div>🖥️ Standard CPU (10M/s): <strong id="time-cpu" style="color:var(--text-primary);">~1.2 Billion Years</strong></div>
            <div>⚡ RTX 4090 GPU (100B/s): <strong id="time-gpu" style="color:var(--text-primary);">~120,000 Years</strong></div>
            <div>⚛️ Quantum/Supercluster: <strong id="time-super" style="color:var(--cyber-amber);">~4.2 Years</strong></div>
          </div>
        </div>

        <!-- Right Box: Hash Generator & Cracker Simulator -->
        <div style="background:rgba(13,18,36,0.8); border:1px solid var(--border-subtle); border-radius:12px; padding:1.5rem;">
          <h4 style="color:var(--cyber-green); font-size:1rem; margin-bottom:1rem;">2. Cryptographic Hash & Rainbow Table Cracker</h4>

          <div style="margin-bottom:1rem;">
            <label style="font-size:0.8rem; color:var(--text-muted); display:block; margin-bottom:0.4rem;">SHA-256 Cryptographic Hash:</label>
            <div id="lab-sha256-output" style="font-family:var(--font-mono); font-size:0.75rem; color:var(--cyber-cyan); word-break:break-all; background:rgba(0,0,0,0.4); padding:0.6rem; border-radius:6px; border:1px solid var(--border-subtle);">
              Computing...
            </div>
          </div>

          <div style="margin-bottom:1rem;">
            <label style="font-size:0.8rem; color:var(--text-muted); display:block; margin-bottom:0.4rem;">Add Cryptographic Salt:</label>
            <div style="display:flex; gap:0.5rem;">
              <input type="text" id="lab-salt-input" value="s@lt#99x" placeholder="Enter salt string" oninput="SimulatorsEngine.evaluatePassword(document.getElementById('lab-pwd-input').value)"
                style="flex:1; background:var(--bg-tertiary); border:1px solid var(--border-subtle); border-radius:6px; padding:0.5rem; font-family:var(--font-mono); font-size:0.8rem; color:var(--text-primary);" />
              <button class="btn-cyber-outline" style="font-size:0.75rem; padding:0.4rem 0.8rem;" onclick="document.getElementById('lab-salt-input').value = Math.random().toString(36).substring(2,10); SimulatorsEngine.evaluatePassword(document.getElementById('lab-pwd-input').value);">Randomize</button>
            </div>
          </div>

          <div style="margin-top:1.25rem;">
            <button class="btn-cyber-primary" style="width:100%; justify-content:center;" onclick="SimulatorsEngine.simulateCrackDemo()">⚡ Run Hash Cracker Simulation (Dictionary & Brute Force)</button>
          </div>

          <div id="crack-sim-result" style="margin-top:1rem; font-size:0.8rem; color:var(--text-secondary); display:none; background:rgba(0,0,0,0.5); padding:0.75rem; border-radius:6px; border:1px solid var(--border-subtle);">
          </div>
        </div>
      </div>
    `;

    this.evaluatePassword("CyberAdmin2024!");
  },

  async evaluatePassword(pwd) {
    if (!pwd) pwd = "";
    const length = pwd.length;
    let pool = 0;
    if (/[a-z]/.test(pwd)) pool += 26;
    if (/[A-Z]/.test(pwd)) pool += 26;
    if (/[0-9]/.test(pwd)) pool += 10;
    if (/[^a-zA-Z0-9]/.test(pwd)) pool += 33;
    if (pool === 0) pool = 1;

    // Entropy formula: L * log2(pool)
    const entropy = (length * Math.log2(pool)).toFixed(1);
    const keyspace = Math.pow(pool, length);

    const entropyEl = document.getElementById('pwd-entropy');
    const keyspaceEl = document.getElementById('pwd-keyspace');
    const barEl = document.getElementById('pwd-strength-bar');
    const labelEl = document.getElementById('pwd-strength-label');

    if (entropyEl) entropyEl.innerText = `${entropy} bits`;
    if (keyspaceEl) keyspaceEl.innerText = keyspace > 1e12 ? keyspace.toExponential(2) : keyspace.toLocaleString();

    let strength = 'Very Weak';
    let color = 'var(--cyber-red)';
    let width = '15%';

    if (entropy < 28) {
      strength = 'Very Weak'; color = 'var(--cyber-red)'; width = '20%';
    } else if (entropy < 45) {
      strength = 'Weak'; color = 'var(--cyber-amber)'; width = '45%';
    } else if (entropy < 65) {
      strength = 'Moderate'; color = 'var(--cyber-blue)'; width = '70%';
    } else if (entropy < 85) {
      strength = 'Strong'; color = 'var(--cyber-green)'; width = '88%';
    } else {
      strength = 'Ultra Secure (Military Grade)'; color = 'var(--cyber-cyan)'; width = '100%';
    }

    if (labelEl) {
      labelEl.innerText = strength;
      labelEl.style.color = color;
    }
    if (barEl) {
      barEl.style.width = width;
      barEl.style.background = color;
    }

    // Time calculations
    const cpuSec = keyspace / 10000000;
    const gpuSec = keyspace / 100000000000;
    const superSec = keyspace / 100000000000000;

    const formatTime = (s) => {
      if (s < 0.001) return 'Instant (< 1 ms)';
      if (s < 60) return `${s.toFixed(1)} seconds`;
      if (s < 3600) return `${(s/60).toFixed(1)} minutes`;
      if (s < 86400) return `${(s/3600).toFixed(1)} hours`;
      if (s < 31536000) return `${(s/86400).toFixed(1)} days`;
      if (s < 31536000 * 1000) return `${(s/31536000).toFixed(1)} years`;
      return `~${(s/31536000).toExponential(1)} years`;
    };

    const timeCpu = document.getElementById('time-cpu');
    const timeGpu = document.getElementById('time-gpu');
    const timeSuper = document.getElementById('time-super');
    if (timeCpu) timeCpu.innerText = formatTime(cpuSec);
    if (timeGpu) timeGpu.innerText = formatTime(gpuSec);
    if (timeSuper) timeSuper.innerText = formatTime(superSec);

    // Compute Web Crypto SHA-256
    const salt = document.getElementById('lab-salt-input') ? document.getElementById('lab-salt-input').value : "";
    const fullText = pwd + salt;
    try {
      const msgBuffer = new TextEncoder().encode(fullText);
      const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
      const hashOut = document.getElementById('lab-sha256-output');
      if (hashOut) hashOut.innerText = hashHex;
    } catch(e) {
      // Fallback
    }
  },

  simulateCrackDemo() {
    const resultBox = document.getElementById('crack-sim-result');
    if (!resultBox) return;
    resultBox.style.display = 'block';
    resultBox.innerHTML = `
      <div style="color:var(--cyber-cyan); font-weight:700; margin-bottom:0.3rem;">⚡ Cracker Process Running...</div>
      <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted);">
        [+] Loading wordlists (rockyou.txt: 14,341,564 entries)...<br>
        [+] Checking Precomputed Rainbow Tables...<br>
        [+] Querying hash database with salt bypass rules...
      </div>
    `;

    setTimeout(() => {
      const salt = document.getElementById('lab-salt-input').value;
      if (salt.length > 3) {
        resultBox.innerHTML = `
          <div style="color:var(--cyber-green); font-weight:700;">🛡️ CRACK FAILED / PROTECTED BY SALT</div>
          <div style="font-size:0.75rem; color:var(--text-secondary); margin-top:0.3rem; line-height:1.4;">
            The Rainbow Table lookup missed because the <strong>Cryptographic Salt ('${salt}')</strong> completely alters the hash! The attacker is forced into an exhaustive brute-force calculation taking decades.
          </div>
        `;
      } else {
        resultBox.innerHTML = `
          <div style="color:var(--cyber-red); font-weight:700;">⚠️ HASH REVERSED (MATCH FOUND IN RAINBOW TABLE)</div>
          <div style="font-size:0.75rem; color:var(--text-secondary); margin-top:0.3rem; line-height:1.4;">
            Without a cryptographic salt, unsalted MD5/SHA256 hashes are looked up instantly in precomputed rainbow tables in under <strong>0.04 seconds</strong>!
          </div>
        `;
      }
    }, 1200);
  },

  /* =========================================================================
     LAB 3: CYBER KILL CHAIN STEP-BY-STEP SCENARIO
     ========================================================================= */
  renderKillChainLab(container) {
    const phases = [
      { num: 1, name: "Reconnaissance", attacker: "Scans LinkedIn, Shodan, and DNS records. Identifies vulnerable Apache server version 2.4.49 on target bank perimeter.", defense: "Minimize public OSINT, deploy deceptive Shodan honey-tokens, monitor threat feeds." },
      { num: 2, name: "Weaponization", attacker: "Pairs CVE-2021-41773 path traversal exploit with a custom Cobalt Strike reverse HTTPS beacon payload.", defense: "Automated vulnerability scanning, SAST/DAST code security audits." },
      { num: 3, name: "Delivery", attacker: "Sends targeted spear-phishing email to Bank Procurement Manager containing invoice link triggering the exploit.", defense: "Email gateway inspection, DMARC/DKIM/SPF enforcement, sandboxed attachment detonator." },
      { num: 4, name: "Exploitation", attacker: "Victim opens weaponized invoice; vulnerability triggers remote code execution in background thread.", defense: "Endpoint Detection and Response (EDR), timely OS zero-day patch management." },
      { num: 5, name: "Installation", attacker: "Drops backdoor payload into System32 directory and installs persistence via Windows Registry Run keys.", defense: "File Integrity Monitoring (FIM), disabling unsigned registry auto-start scripts." },
      { num: 6, name: "Command & Control", attacker: "Malware initiates encrypted HTTPS beacon back to attacker C2 bulletproof server (185.190.x.x) every 60s.", defense: "Network traffic behavioral analytics, DNS sinkholing, outbound TLS inspection." },
      { num: 7, name: "Actions on Objectives", attacker: "Dumps database memory, exfiltrates 500,000 credit card records, and deploys ransomware wiper on domain controller.", defense: "Data Loss Prevention (DLP), network micro-segmentation, immutable air-gapped backups." }
    ];

    container.innerHTML = `
      <div class="lab-header">
        <div>
          <span class="sim-badge">Tactical Attack Lifecycle</span>
          <h3>⚔️ Lockheed Martin Cyber Kill Chain Interactive Stepper</h3>
          <p class="text-secondary" style="font-size:0.85rem;">Follow a realistic enterprise intrusion step-by-step. Discover how breaking a single link stops the adversary.</p>
        </div>
      </div>

      <div style="display:flex; gap:0.5rem; overflow-x:auto; padding-bottom:1rem; margin-bottom:1.5rem;" id="killchain-stepper-tabs">
        ${phases.map((p, i) => `
          <button class="exam-filter-btn ${i === 0 ? 'active' : ''}" onclick="SimulatorsEngine.selectKillChainPhase(${i})" id="kc-btn-${i}" style="white-space:nowrap;">
            ${p.num}. ${p.name}
          </button>
        `).join('')}
      </div>

      <div id="kc-phase-detail-box" style="background:rgba(13,18,36,0.85); border:1px solid var(--border-cyan); border-radius:12px; padding:1.75rem; box-shadow:var(--glow-cyan);">
        <!-- Populated dynamically -->
      </div>
    `;

    this.killChainPhases = phases;
    this.selectKillChainPhase(0);
  },

  selectKillChainPhase(index) {
    this.killChainPhases.forEach((_, i) => {
      const btn = document.getElementById(`kc-btn-${i}`);
      if (btn) btn.className = `exam-filter-btn ${i === index ? 'active' : ''}`;
    });

    const p = this.killChainPhases[index];
    const box = document.getElementById('kc-phase-detail-box');
    if (!box) return;

    box.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
        <span class="unit-code-badge">PHASE ${p.num} OF 7</span>
        <h3 style="color:var(--text-primary); font-size:1.3rem;">${p.name}</h3>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:1.25rem; margin-bottom:1.5rem;">
        <div style="background:rgba(255,51,102,0.08); border:1px solid rgba(255,51,102,0.3); border-radius:8px; padding:1.25rem;">
          <h4 style="color:var(--cyber-red); font-size:0.9rem; text-transform:uppercase; margin-bottom:0.5rem;">🔴 Red Team (Attacker Action)</h4>
          <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">${p.attacker}</p>
        </div>

        <div style="background:rgba(0,255,135,0.08); border:1px solid rgba(0,255,135,0.3); border-radius:8px; padding:1.25rem;">
          <h4 style="color:var(--cyber-green); font-size:0.9rem; text-transform:uppercase; margin-bottom:0.5rem;">🟢 Blue Team (SOC Defense Control)</h4>
          <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">${p.defense}</p>
        </div>
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; padding-top:1rem; border-top:1px solid var(--border-subtle);">
        <button class="btn-cyber-outline" onclick="SimulatorsEngine.selectKillChainPhase(${Math.max(0, index - 1)})" ${index === 0 ? 'disabled style="opacity:0.4; cursor:not-allowed;"' : ''}>← Previous Phase</button>
        <span style="font-size:0.8rem; color:var(--text-muted);">Step ${index + 1} of 7</span>
        <button class="btn-cyber-primary" onclick="SimulatorsEngine.selectKillChainPhase(${Math.min(6, index + 1)})" ${index === 6 ? 'disabled style="opacity:0.4; cursor:not-allowed;"' : ''}>Next Phase →</button>
      </div>
    `;
  },

  /* =========================================================================
     LAB 4: PHISHING & SOCIAL ENGINEERING RADAR
     ========================================================================= */
  renderPhishingLab(container) {
    const samples = [
      {
        id: 1,
        type: "Spear Phishing Email",
        sender: "security@paypa1-verification.com",
        subject: "URGENT: Your PayPal Account Has Been Suspended!",
        body: "Dear Customer,\n\nWe detected suspicious transactions from IP 185.220.101.4. To prevent permanent suspension, you MUST verify your credit card details within 15 minutes.\n\nClick here: http://paypa1-security-check.com/verify?id=92841\n\nSecurity Team",
        isPhish: true,
        redFlags: ["Typosquatting domain (paypa1 with number 1 instead of 'l')", "Artificial urgency trigger (15 minutes limit)", "Insecure HTTP link", "Generic salutation 'Dear Customer'"]
      },
      {
        id: 2,
        type: "CEO Business Email Compromise (BEC)",
        sender: "ceo.direct@gmail-corporate.com",
        subject: "Confidential Wire Transfer Request - Acquisition",
        body: "Hi Jane,\n\nI am in an executive meeting with board investors. We are closing an urgent offshore asset acquisition today. Please wire $85,000 to the attached vendor account immediately. Do not call me as I cannot pick up.\n\nBest,\nRobert Davis, CEO",
        isPhish: true,
        redFlags: ["Spoofed external Gmail address", "Pressure from Authority figure (CEO)", "Instruction to bypass voice/phone confirmation protocol", "Urgent monetary wire"]
      },
      {
        id: 3,
        type: "SMS Smishing Attack",
        sender: "+1-800-BANK-ALERT",
        subject: "SMS Text Notification",
        body: "ALERT: Your Visa Debit Card ending in 4102 was charged $940.00 at Walmart. If you did not authorize this, call immediately or cancel here: bit.ly/bank-cancel-tx",
        isPhish: true,
        redFlags: ["Shortened unverified URL (bit.ly)", "Fear trigger (unexpected $940 charge)", "Generic sender masking phone number"]
      }
    ];

    container.innerHTML = `
      <div class="lab-header">
        <div>
          <span class="sim-badge">Social Engineering Analysis</span>
          <h3>🎣 Phishing & Social Engineering Radar</h3>
          <p class="text-secondary" style="font-size:0.85rem;">Inspect incoming communications, analyze headers, detect psychological pressure triggers, and classify threat verdicts.</p>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: 280px 1fr; gap:1.5rem; align-items:start;">
        <!-- Left Sample Selector -->
        <div style="background:rgba(13,18,36,0.8); border:1px solid var(--border-subtle); border-radius:12px; padding:1rem;">
          <div style="font-size:0.75rem; text-transform:uppercase; color:var(--text-muted); font-weight:700; margin-bottom:0.75rem;">Incoming Inbox Queue</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem;">
            ${samples.map((s, i) => `
              <div onclick="SimulatorsEngine.loadPhishSample(${i})" id="phish-sample-${i}" class="topic-nav-item ${i === 0 ? 'active' : ''}" style="cursor:pointer;">
                <div>
                  <strong style="font-size:0.85rem; display:block;">${s.type}</strong>
                  <span style="font-size:0.7rem; color:var(--text-muted);">${s.subject.substring(0, 24)}...</span>
                </div>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Right Message Inspection Pane -->
        <div id="phish-inspect-pane" style="background:rgba(13,18,36,0.9); border:1px solid var(--border-cyan); border-radius:12px; padding:1.75rem;">
          <!-- Loaded via JS -->
        </div>
      </div>
    `;

    this.phishSamples = samples;
    this.loadPhishSample(0);
  },

  loadPhishSample(index) {
    this.phishSamples.forEach((_, i) => {
      const el = document.getElementById(`phish-sample-${i}`);
      if (el) el.className = `topic-nav-item ${i === index ? 'active' : ''}`;
    });

    const s = this.phishSamples[index];
    const pane = document.getElementById('phish-inspect-pane');
    if (!pane) return;

    pane.innerHTML = `
      <div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1rem; margin-bottom:1.25rem;">
        <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono); margin-bottom:0.25rem;">FROM: <span style="color:var(--cyber-cyan);">${s.sender}</span></div>
        <div style="font-size:1.1rem; font-weight:700; color:var(--text-primary);">${s.subject}</div>
      </div>

      <div style="background:#02040a; border:1px solid var(--border-subtle); border-radius:8px; padding:1.25rem; font-family:var(--font-sans); font-size:0.9rem; color:var(--text-primary); line-height:1.6; white-space:pre-wrap; margin-bottom:1.5rem;">
        ${s.body}
      </div>

      <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem;">
        <div style="display:flex; gap:0.75rem;">
          <button class="btn-cyber-primary" style="background:linear-gradient(135deg, var(--cyber-red), #b91c1c); color:#fff;" onclick="SimulatorsEngine.evaluatePhishVerdict(${index}, true)">🚨 Mark as Malicious Phishing</button>
          <button class="btn-cyber-outline" onclick="SimulatorsEngine.evaluatePhishVerdict(${index}, false)">✅ Mark as Safe</button>
        </div>
      </div>

      <div id="phish-feedback-${index}" style="margin-top:1.25rem; display:none; background:rgba(0,0,0,0.5); border-radius:8px; padding:1.25rem; border:1px solid var(--border-subtle);"></div>
    `;
  },

  evaluatePhishVerdict(index, userChosePhish) {
    const s = this.phishSamples[index];
    const fb = document.getElementById(`phish-feedback-${index}`);
    if (!fb) return;

    fb.style.display = 'block';
    if (userChosePhish === s.isPhish) {
      fb.innerHTML = `
        <div style="color:var(--cyber-green); font-weight:800; font-size:0.95rem; margin-bottom:0.5rem;">🎯 CORRECT VERDICT: THREAT IDENTIFIED!</div>
        <div style="font-size:0.85rem; color:var(--text-secondary); margin-bottom:0.5rem;">Key Red Flags Detected:</div>
        <ul style="list-style:disc; margin-left:1.5rem; font-size:0.8rem; color:var(--text-primary); line-height:1.5;">
          ${s.redFlags.map(rf => `<li>${rf}</li>`).join('')}
        </ul>
      `;
    } else {
      fb.innerHTML = `
        <div style="color:var(--cyber-red); font-weight:800; font-size:0.95rem; margin-bottom:0.5rem;">❌ INCORRECT VERDICT: SECURITY BREACH!</div>
        <p style="font-size:0.85rem; color:var(--text-secondary);">This communication was malicious phishing. Review the red flags above carefully.</p>
      `;
    }
  },

  /* =========================================================================
     LAB 5: WI-FI EVIL TWIN & MITM SNIFFER
     ========================================================================= */
  renderEvilTwinLab(container) {
    container.innerHTML = `
      <div class="lab-header">
        <div>
          <span class="sim-badge">Wireless Security & Eavesdropping</span>
          <h3>📶 Wi-Fi Evil Twin & MITM Packet Sniffer</h3>
          <p class="text-secondary" style="font-size:0.85rem;">Observe how an attacker broadcasts a rogue access point with identical SSID to intercept plaintext credentials.</p>
        </div>
      </div>

      <div class="lab-interactive-canvas-wrap" style="padding:1.5rem;">
        <div style="display:flex; justify-content:space-around; align-items:center; flex-wrap:wrap; gap:1rem; margin-bottom:1.5rem;">
          <div class="sim-node" style="min-width:140px;">
            <div style="font-size:1.6rem;">📱</div>
            <strong>Victim Phone</strong>
            <div style="font-size:0.7rem; color:var(--text-muted);">Auto-associating...</div>
          </div>

          <div style="display:flex; flex-direction:column; gap:1rem;">
            <div class="sim-node" id="legit-ap" style="min-width:160px; opacity:0.6;">
              <div style="font-size:1.4rem;">📡</div>
              <strong>Legitimate AP</strong>
              <div style="font-size:0.7rem; color:var(--cyber-green);">SSID: "Airport_Free_WiFi" (Signal: -75 dBm)</div>
            </div>

            <div class="sim-node" id="rogue-ap" style="min-width:160px; border-color:var(--cyber-red);">
              <div style="font-size:1.4rem;">😈</div>
              <strong style="color:var(--cyber-red);">Evil Twin Rogue AP</strong>
              <div style="font-size:0.7rem; color:var(--cyber-red);">SSID: "Airport_Free_WiFi" (Signal: -30 dBm - STRONGER!)</div>
            </div>
          </div>

          <div class="sim-node" style="min-width:140px;">
            <div style="font-size:1.6rem;">🌐</div>
            <strong>Banking Server</strong>
            <div style="font-size:0.7rem; color:var(--text-muted);">http://auth.bank.com</div>
          </div>
        </div>

        <div class="terminal-box" id="mitm-sniffer-term">
          <div class="terminal-line">[WIRESHARK SNIFFER ATTACHED ON wlan0mon] Promiscuous mode enabled.</div>
          <div class="terminal-line">[BEACON PROBE] Victim smartphone sent Probe Request for "Airport_Free_WiFi".</div>
          <div class="terminal-line warning">[ASSOCIATION] Victim auto-connected to Rogue AP due to stronger RSSI (-30 dBm).</div>
        </div>
      </div>

      <div class="lab-controls-panel">
        <button class="btn-cyber-primary" onclick="SimulatorsEngine.sniffCredentials()">🎣 Simulate User Login & Capture Plaintext Passwords</button>
      </div>
    `;
  },

  sniffCredentials() {
    const term = document.getElementById('mitm-sniffer-term');
    if (!term) return;

    const packets = [
      '[HTTP POST CAPTURED] Source: 192.168.1.104 -> Dest: 203.0.113.15:80',
      'POST /login.php HTTP/1.1 (Host: auth.bank.com)',
      'Content-Type: application/x-www-form-urlencoded',
      'Captured Payload: username=john_doe@email.com&password=BankPassword123!&pin=9842',
      'SESSION TOKEN EXTRACTED: JSESSIONID=8f7a90b1c2d3e4f5'
    ];

    packets.forEach((p, i) => {
      setTimeout(() => {
        const line = document.createElement('div');
        line.className = 'terminal-line ' + (i >= 3 ? 'danger' : 'warning');
        line.innerText = p;
        term.appendChild(line);
        term.scrollTop = term.scrollHeight;
      }, i * 400);
    });
  },

  /* =========================================================================
     LAB 6: MALWARE ANATOMY DISSECTOR
     ========================================================================= */
  renderMalwareLab(container) {
    const components = [
      { name: "1. Replication Engine", role: "Infects Host Files / Memory", code: "void infect_files() { find_all_exe(); append_malware_stub(); modify_entry_point(); }" },
      { name: "2. Propagation Engine", role: "Automated Network Spreader", code: "void scan_subnet() { for(ip in 192.168.1.0/24) { test_port_445(); send_eternalblue_payload(); } }" },
      { name: "3. Trigger Mechanism", role: "Logic Bomb / Time Bomb", code: "if (current_date == 'Friday_13th' || active_users > 100) { unleash_payload(); }" },
      { name: "4. Payload Execution", role: "Destruction / Ransomware / Backdoor", code: "void execute_ransomware() { aes_encrypt_all_files('.doc', '.pdf', '.db'); drop_ransom_note(); }" },
      { name: "5. Concealment Engine", role: "Polymorphism & AV Evasion", code: "void mutate_code() { generate_random_xor_key(); re_encrypt_stub(); insert_junk_nops(); }" }
    ];

    container.innerHTML = `
      <div class="lab-header">
        <div>
          <span class="sim-badge">Malware Engineering</span>
          <h3>🦠 5-Stage Modular Malware Anatomy Dissector</h3>
          <p class="text-secondary" style="font-size:0.85rem;">Click on each architectural component of a self-propagating worm/virus to inspect its internal logic.</p>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
        ${components.map((c, i) => `
          <div onclick="SimulatorsEngine.inspectMalwarePart(${i})" id="mal-part-${i}" class="sim-node ${i === 0 ? 'active' : ''}" style="cursor:pointer; text-align:left; padding:1rem;">
            <strong style="color:var(--cyber-cyan); font-size:0.85rem; display:block;">${c.name}</strong>
            <span style="font-size:0.75rem; color:var(--text-muted);">${c.role}</span>
          </div>
        `).join('')}
      </div>

      <div id="malware-inspect-box" style="background:rgba(13,18,36,0.9); border:1px solid var(--border-cyan); border-radius:12px; padding:1.5rem;">
        <!-- Filled dynamically -->
      </div>
    `;

    this.malwareComponents = components;
    this.inspectMalwarePart(0);
  },

  inspectMalwarePart(index) {
    this.malwareComponents.forEach((_, i) => {
      const el = document.getElementById(`mal-part-${i}`);
      if (el) el.className = `sim-node ${i === index ? 'active' : ''}`;
    });

    const c = this.malwareComponents[index];
    const box = document.getElementById('malware-inspect-box');
    if (!box) return;

    box.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
        <h4 style="color:var(--text-primary); font-size:1.1rem;">${c.name}</h4>
        <span class="unit-code-badge">${c.role}</span>
      </div>
      <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5; margin-bottom:1rem;">
        This module executes the dedicated lifecycle stage within the malware binary. Modern polymorphic malware mutates this block upon each infection to evade antivirus hash signatures.
      </p>
      <div class="diagram-block" style="margin:0;">
        <div class="diagram-header">Pseudocode Implementation</div>
        <pre class="diagram-code" style="color:var(--cyber-green);">${c.code}</pre>
      </div>
    `;
  },

  /* =========================================================================
     LAB 7: DDOS ATTACK STORM & SCRUBBING DEFENSE
     ========================================================================= */
  renderDDoSAttackLab(container) {
    container.innerHTML = `
      <div class="lab-header">
        <div>
          <span class="sim-badge">Network Defense & Availability</span>
          <h3>💥 DDoS Attack Storm & Cloud Scrubbing Center</h3>
          <p class="text-secondary" style="font-size:0.85rem;">Simulate massive volumetric SYN/UDP floods, observe server resource starvation, and activate scrubbing center mitigation.</p>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: 2fr 1fr; gap:1.5rem; align-items:start;">
        <!-- Canvas Visualizer -->
        <div class="lab-interactive-canvas-wrap" style="min-height:300px; position:relative; background:#02050f;">
          <canvas id="ddos-canvas" width="600" height="280" style="width:100%; height:100%;"></canvas>
          <div id="ddos-status-overlay" style="position:absolute; top:15px; left:15px; background:rgba(0,0,0,0.7); padding:0.5rem 0.75rem; border-radius:6px; font-size:0.75rem; font-family:var(--font-mono); color:var(--cyber-cyan);">
            Traffic: 12 Gbps (Normal) | Scrubbing: OFF
          </div>
        </div>

        <!-- Server Health & Controls -->
        <div style="background:rgba(13,18,36,0.85); border:1px solid var(--border-subtle); border-radius:12px; padding:1.25rem;">
          <h4 style="color:var(--text-primary); font-size:0.95rem; margin-bottom:1rem;">Target Server Health</h4>

          <div style="margin-bottom:0.75rem;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; margin-bottom:0.2rem;">
              <span style="color:var(--text-secondary);">CPU Utilization</span>
              <span id="ddos-cpu-val" style="color:var(--cyber-green); font-weight:700;">14%</span>
            </div>
            <div style="width:100%; height:6px; background:rgba(255,255,255,0.1); border-radius:3px; overflow:hidden;">
              <div id="ddos-cpu-bar" style="width:14%; height:100%; background:var(--cyber-green);"></div>
            </div>
          </div>

          <div style="margin-bottom:1rem;">
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; margin-bottom:0.2rem;">
              <span style="color:var(--text-secondary);">TCP Connection Pool</span>
              <span id="ddos-conn-val" style="color:var(--cyber-green); font-weight:700;">120 / 10,000</span>
            </div>
            <div style="width:100%; height:6px; background:rgba(255,255,255,0.1); border-radius:3px; overflow:hidden;">
              <div id="ddos-conn-bar" style="width:5%; height:100%; background:var(--cyber-green);"></div>
            </div>
          </div>

          <div style="display:flex; flex-direction:column; gap:0.5rem; margin-top:1.25rem;">
            <button class="btn-cyber-primary" style="background:linear-gradient(135deg, var(--cyber-red), #e11d48); color:#fff; font-size:0.8rem;" onclick="SimulatorsEngine.triggerDDoSAttack()">🚀 Launch 350 Gbps Botnet Flood</button>
            <button class="btn-cyber-primary" style="background:linear-gradient(135deg, var(--cyber-green), #059669); color:#000; font-size:0.8rem;" onclick="SimulatorsEngine.toggleDDoSScrubbing()">🛡️ Enable Cloud Scrubbing & Anycast</button>
          </div>
        </div>
      </div>
    `;

    this.initDDoSCanvas();
  },

  ddosState: { attacking: false, scrubbing: false },

  initDDoSCanvas() {
    const canvas = document.getElementById('ddos-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let particles = [];

    for (let i = 0; i < 40; i++) {
      particles.push({
        x: Math.random() * canvas.width * 0.4,
        y: Math.random() * canvas.height,
        vx: 2 + Math.random() * 3,
        isBad: false,
        size: 3
      });
    }

    const animate = () => {
      ctx.fillStyle = 'rgba(2, 5, 15, 0.3)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Draw origin server
      ctx.fillStyle = '#10b981';
      ctx.fillRect(canvas.width - 50, canvas.height / 2 - 40, 40, 80);
      ctx.fillStyle = '#ffffff';
      ctx.font = '10px monospace';
      ctx.fillText('SERVER', canvas.width - 48, canvas.height / 2);

      // Draw scrubbing wall if active
      if (this.ddosState.scrubbing) {
        ctx.fillStyle = 'rgba(0, 242, 254, 0.4)';
        ctx.fillRect(canvas.width / 2 - 10, 20, 20, canvas.height - 40);
        ctx.fillStyle = '#00f2fe';
        ctx.fillText('SCRUBBER', canvas.width / 2 - 25, 15);
      }

      particles.forEach(p => {
        p.x += p.vx;
        if (p.x > canvas.width - 50) {
          p.x = 20;
          p.y = Math.random() * canvas.height;
        }

        // Scrubbing filter
        if (this.ddosState.scrubbing && p.isBad && p.x > canvas.width / 2 - 10 && p.x < canvas.width / 2 + 10) {
          p.x = 20;
          p.y = Math.random() * canvas.height;
        }

        ctx.fillStyle = p.isBad ? '#ff3366' : '#00ff87';
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
      });

      requestAnimationFrame(animate);
    };

    animate();
    this.ddosParticles = particles;
  },

  triggerDDoSAttack() {
    this.ddosState.attacking = true;
    const overlay = document.getElementById('ddos-status-overlay');
    const cpuVal = document.getElementById('ddos-cpu-val');
    const cpuBar = document.getElementById('ddos-cpu-bar');
    const connVal = document.getElementById('ddos-conn-val');
    const connBar = document.getElementById('ddos-conn-bar');

    if (this.ddosParticles) {
      for (let i = 0; i < 80; i++) {
        this.ddosParticles.push({
          x: Math.random() * 100,
          y: Math.random() * 250,
          vx: 5 + Math.random() * 4,
          isBad: true,
          size: 4
        });
      }
    }

    if (overlay) overlay.innerText = '⚠️ ATTACK: 350 Gbps Botnet Flood Active! | Scrubbing: OFF';
    if (cpuVal) { cpuVal.innerText = '99% (CRITICAL OVERLOAD)'; cpuVal.style.color = 'var(--cyber-red)'; }
    if (cpuBar) { cpuBar.style.width = '99%'; cpuBar.style.background = 'var(--cyber-red)'; }
    if (connVal) { connVal.innerText = '10,000 / 10,000 (EXHAUSTED)'; connVal.style.color = 'var(--cyber-red)'; }
    if (connBar) { connBar.style.width = '100%'; connBar.style.background = 'var(--cyber-red)'; }
  },

  toggleDDoSScrubbing() {
    this.ddosState.scrubbing = true;
    const overlay = document.getElementById('ddos-status-overlay');
    const cpuVal = document.getElementById('ddos-cpu-val');
    const cpuBar = document.getElementById('ddos-cpu-bar');
    const connVal = document.getElementById('ddos-conn-val');
    const connBar = document.getElementById('ddos-conn-bar');

    if (overlay) overlay.innerText = '🛡️ MITIGATION ACTIVE: Cloud Scrubbing & Anycast Enabled | Clean Traffic Only';
    if (cpuVal) { cpuVal.innerText = '22% (PROTECTED)'; cpuVal.style.color = 'var(--cyber-green)'; }
    if (cpuBar) { cpuBar.style.width = '22%'; cpuBar.style.background = 'var(--cyber-green)'; }
    if (connVal) { connVal.innerText = '450 / 10,000 (HEALTHY)'; connVal.style.color = 'var(--cyber-green)'; }
    if (connBar) { connBar.style.width = '12%'; connBar.style.background = 'var(--cyber-green)'; }
  },

  /* =========================================================================
     LAB 8: MOBILE SECURITY MDM CONFIGURATOR
     ========================================================================= */
  renderMobileMDMLab(container) {
    container.innerHTML = `
      <div class="lab-header">
        <div>
          <span class="sim-badge">Mobile & Endpoint Security</span>
          <h3>📱 Mobile Security MDM & Permission Audit Lab</h3>
          <p class="text-secondary" style="font-size:0.85rem;">Audit dangerous mobile app permissions and configure enterprise Mobile Device Management (MDM) security baselines.</p>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:1.5rem;">
        <!-- Policy Toggles -->
        <div style="background:rgba(13,18,36,0.85); border:1px solid var(--border-subtle); border-radius:12px; padding:1.5rem;">
          <h4 style="color:var(--cyber-cyan); font-size:1rem; margin-bottom:1rem;">Enterprise MDM Baseline Policy</h4>
          
          <div style="display:flex; flex-direction:column; gap:0.85rem; font-size:0.85rem;">
            <label style="display:flex; align-items:center; gap:0.6rem; cursor:pointer;">
              <input type="checkbox" id="mdm-pin" onchange="SimulatorsEngine.calcMDMScore()" checked />
              <span>Enforce Alphanumeric PIN (>=6 Digits)</span>
            </label>
            <label style="display:flex; align-items:center; gap:0.6rem; cursor:pointer;">
              <input type="checkbox" id="mdm-root" onchange="SimulatorsEngine.calcMDMScore()" />
              <span>Block Rooted & Jailbroken Devices</span>
            </label>
            <label style="display:flex; align-items:center; gap:0.6rem; cursor:pointer;">
              <input type="checkbox" id="mdm-enc" onchange="SimulatorsEngine.calcMDMScore()" checked />
              <span>Mandate Hardware Storage Encryption</span>
            </label>
            <label style="display:flex; align-items:center; gap:0.6rem; cursor:pointer;">
              <input type="checkbox" id="mdm-sideload" onchange="SimulatorsEngine.calcMDMScore()" />
              <span>Disable 'Install from Unknown Sources'</span>
            </label>
            <label style="display:flex; align-items:center; gap:0.6rem; cursor:pointer;">
              <input type="checkbox" id="mdm-wipe" onchange="SimulatorsEngine.calcMDMScore()" />
              <span>Enable Remote Selective Enterprise Wipe</span>
            </label>
          </div>
        </div>

        <!-- Compliance Result -->
        <div style="background:rgba(13,18,36,0.85); border:1px solid var(--border-subtle); border-radius:12px; padding:1.5rem;">
          <h4 style="color:var(--cyber-green); font-size:1rem; margin-bottom:1rem;">Compliance Score</h4>
          
          <div style="text-align:center; padding:1.5rem 0;">
            <div id="mdm-score-val" style="font-size:2.8rem; font-weight:800; color:var(--cyber-amber); font-family:var(--font-mono);">60%</div>
            <div id="mdm-score-label" style="font-size:0.85rem; color:var(--text-secondary);">Moderate Compliance</div>
          </div>

          <p style="font-size:0.8rem; color:var(--text-muted); line-height:1.5;">
            Enterprise BYOD security requires achieving 100% compliance across all 5 MDM baseline controls to prevent corporate data leakage.
          </p>
        </div>
      </div>
    `;

    this.calcMDMScore();
  },

  calcMDMScore() {
    const checks = ['mdm-pin', 'mdm-root', 'mdm-enc', 'mdm-sideload', 'mdm-wipe'];
    let count = 0;
    checks.forEach(id => {
      const el = document.getElementById(id);
      if (el && el.checked) count++;
    });

    const score = (count / checks.length) * 100;
    const scoreVal = document.getElementById('mdm-score-val');
    const scoreLabel = document.getElementById('mdm-score-label');

    if (scoreVal) {
      scoreVal.innerText = `${score}%`;
      if (score === 100) {
        scoreVal.style.color = 'var(--cyber-green)';
        if (scoreLabel) scoreLabel.innerText = '🛡️ Full Enterprise Compliance (Zero Trust Standard)';
      } else if (score >= 60) {
        scoreVal.style.color = 'var(--cyber-amber)';
        if (scoreLabel) scoreLabel.innerText = '⚠️ Moderate Compliance (Vulnerable to Sideloading/Rooting)';
      } else {
        scoreVal.style.color = 'var(--cyber-red)';
        if (scoreLabel) scoreLabel.innerText = '❌ Non-Compliant (High Risk of Data Exfiltration)';
      }
    }
  }
};
