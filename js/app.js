/**
 * CYBERNEXUS - Master Application State & Interaction Engine
 * Pure Vanilla JavaScript
 */

const AppState = {
  currentView: 'syllabus',
  currentUnitId: 1,
  currentTopicId: 'u1-t1',
  userXP: 0,
  completedTopics: new Set(),
  bookmarkedTopics: new Set(),
  theme: 'cyber',
  currentFlashcardIndex: 0,
  currentQuizIndex: 0,
  quizScore: 0,
  quizAnswered: false,
  isSpeaking: false,

  // Load persisted user progress from localStorage
  load() {
    try {
      const savedXP = localStorage.getItem('cybernexus_xp');
      if (savedXP) this.userXP = parseInt(savedXP, 10);

      const savedCompleted = localStorage.getItem('cybernexus_completed');
      if (savedCompleted) this.completedTopics = new Set(JSON.parse(savedCompleted));

      const savedBookmarks = localStorage.getItem('cybernexus_bookmarks');
      if (savedBookmarks) this.bookmarkedTopics = new Set(JSON.parse(savedBookmarks));

      const savedTheme = localStorage.getItem('cybernexus_theme');
      if (savedTheme) {
        this.theme = savedTheme;
        document.documentElement.setAttribute('data-theme', savedTheme);
      }
    } catch (e) {
      console.warn('LocalStorage error:', e);
    }
  },

  save() {
    try {
      localStorage.setItem('cybernexus_xp', this.userXP.toString());
      localStorage.setItem('cybernexus_completed', JSON.stringify(Array.from(this.completedTopics)));
      localStorage.setItem('cybernexus_bookmarks', JSON.stringify(Array.from(this.bookmarkedTopics)));
      localStorage.setItem('cybernexus_theme', this.theme);
    } catch (e) {
      console.warn('LocalStorage error:', e);
    }
  },

  addXP(pts) {
    this.userXP += pts;
    this.save();
    this.updateXPDisplay();
  },

  updateXPDisplay() {
    const el = document.getElementById('user-xp-val');
    if (el) el.innerText = `${this.userXP} XP`;
  }
};

const CyberApp = {
  init() {
    AppState.load();
    AppState.updateXPDisplay();
    this.renderUnitsGrid();
    this.renderTopicContent(AppState.currentUnitId, AppState.currentTopicId);
    this.renderExamQuestions('all');
    this.renderFlashcard();
    this.renderQuizQuestion();
    this.renderGlossary();
    this.setupEventListeners();
    this.updateStats();

    // Auto-open first lab in background
    if (typeof SimulatorsEngine !== 'undefined') {
      SimulatorsEngine.loadLab('tor');
    }
  },

  // Switch Main Views (Syllabus, Simulators, Exam Master, Flashcards, Quiz, Glossary)
  switchView(viewName) {
    AppState.currentView = viewName;

    document.querySelectorAll('.nav-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.view === viewName);
    });

    document.querySelectorAll('.view-section').forEach(sec => {
      sec.classList.toggle('active', sec.id === `view-${viewName}`);
    });

    // Scroll to top of view
    window.scrollTo({ top: 0, behavior: 'smooth' });

    if (viewName === 'simulators') {
      SimulatorsEngine.loadLab(SimulatorsEngine.activeLabId || 'tor');
    }
  },

  // Render Units Selection Cards
  renderUnitsGrid() {
    const container = document.getElementById('units-grid-container');
    if (!container || !CYBER_DATA) return;

    container.innerHTML = CYBER_DATA.units.map(u => {
      const isSelected = u.id === AppState.currentUnitId;
      const completedCount = u.topics.filter(t => AppState.completedTopics.has(t.id)).length;
      const totalTopics = u.topics.length;
      const pct = Math.round((completedCount / totalTopics) * 100);

      return `
        <div class="unit-card ${isSelected ? 'active' : ''}" onclick="CyberApp.selectUnit(${u.id})">
          <div class="unit-header-top">
            <span class="unit-code-badge">${u.code}</span>
            <span class="unit-weightage-badge">${u.weightage}</span>
          </div>
          <h3>${u.title}</h3>
          <p>${u.overview.substring(0, 115)}...</p>
          <div class="unit-meta-bar">
            <span>⏱️ ${u.estimatedTime}</span>
            <div class="unit-progress-ring-wrap">
              <span>${pct}% Done</span>
            </div>
          </div>
        </div>
      `;
    }).join('');
  },

  // Select Unit & Show Topics
  selectUnit(unitId) {
    AppState.currentUnitId = unitId;
    const unit = CYBER_DATA.units.find(u => u.id === unitId);
    if (unit && unit.topics.length > 0) {
      AppState.currentTopicId = unit.topics[0].id;
    }
    this.renderUnitsGrid();
    this.renderTopicContent(unitId, AppState.currentTopicId);
  },

  // Render Topic Detailed Notes
  renderTopicContent(unitId, topicId) {
    const unit = CYBER_DATA.units.find(u => u.id === unitId);
    if (!unit) return;

    AppState.currentTopicId = topicId;
    const topic = unit.topics.find(t => t.id === topicId) || unit.topics[0];

    // Render Sidebar Topics List
    const sidebar = document.getElementById('topic-sidebar-list');
    if (sidebar) {
      sidebar.innerHTML = unit.topics.map(t => {
        const isActive = t.id === topic.id;
        const isDone = AppState.completedTopics.has(t.id);
        return `
          <li class="topic-nav-item ${isActive ? 'active' : ''}" onclick="CyberApp.renderTopicContent(${unitId}, '${t.id}')">
            <span>${t.title}</span>
            <span class="topic-status-check ${isDone ? 'completed' : ''}"></span>
          </li>
        `;
      }).join('');
    }

    // Render Main Article Box
    const mainEl = document.getElementById('topic-main-article');
    if (!mainEl) return;

    const isDone = AppState.completedTopics.has(topic.id);
    const isBookmarked = AppState.bookmarkedTopics.has(topic.id);

    let html = `
      <div class="topic-hero-header">
        <span class="topic-tag-pill">${topic.tag || 'Core Syllabus'}</span>
        <h2>${topic.title}</h2>
        <p style="font-size:1.05rem; color:var(--text-secondary); line-height:1.6;">${topic.summary}</p>
        
        <div class="topic-actions-row">
          <button class="btn-cyber-primary" onclick="CyberApp.toggleTopicCompleted('${topic.id}')">
            ${isDone ? '✓ Completed (+50 XP)' : 'Mark as Completed (+50 XP)'}
          </button>
          <button class="btn-cyber-outline" onclick="CyberApp.speakTopicText('${topic.id}')">
            🔊 ${AppState.isSpeaking ? 'Stop Audio' : 'Listen Aloud (TTS)'}
          </button>
          <button class="btn-cyber-outline" onclick="CyberApp.toggleBookmark('${topic.id}')">
            ${isBookmarked ? '★ Bookmarked' : '☆ Bookmark'}
          </button>
        </div>
      </div>
    `;

    // Definition Box
    if (topic.definition) {
      html += `
        <div class="callout-box definition">
          <div class="callout-title">Formal Examination Definition</div>
          <p style="font-size:0.95rem; color:var(--text-primary); font-weight:500; line-height:1.6;">${topic.definition}</p>
        </div>
      `;
    }

    // Three Roles (Unit 1)
    if (topic.threeRoles) {
      html += `<h3 class="content-subheading">Triple Roles of a Computer</h3>
      <div class="feature-cards-grid">
        ${topic.threeRoles.map(r => `
          <div class="feature-card">
            <div class="feature-card-title">${r.role}</div>
            <p class="feature-card-desc">${r.description}</p>
            <div style="margin-top:0.6rem; font-size:0.75rem; color:var(--cyber-cyan);">
              <strong>Examples:</strong> ${r.examples.join(', ')}
            </div>
          </div>
        `).join('')}
      </div>`;
    }

    // Timeline (Unit 1)
    if (topic.timeline) {
      html += `<h3 class="content-subheading">Chronological Evolution</h3>
      <div style="display:flex; flex-direction:column; gap:0.85rem; margin:1rem 0;">
        ${topic.timeline.map(e => `
          <div style="background:rgba(13,18,36,0.5); border-left:3px solid var(--cyber-cyan); padding:0.85rem 1.15rem; border-radius:0 8px 8px 0; border-top:1px solid var(--border-subtle); border-right:1px solid var(--border-subtle); border-bottom:1px solid var(--border-subtle);">
            <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
              <strong style="color:var(--text-primary); font-size:0.9rem;">${e.name}</strong>
              <span style="font-size:0.75rem; color:var(--cyber-cyan); font-family:var(--font-mono);">${e.era}</span>
            </div>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">${e.details}</p>
          </div>
        `).join('')}
      </div>`;
    }

    // Classification Categories (Unit 1)
    if (topic.categories) {
      html += `<h3 class="content-subheading">Classification Breakdown</h3>
      <div class="feature-cards-grid">
        ${topic.categories.map(c => `
          <div class="feature-card">
            <div class="feature-card-title">${c.category}</div>
            <p style="font-size:0.8rem; color:var(--cyber-cyan); margin-bottom:0.5rem;">${c.target}</p>
            <div style="display:flex; flex-direction:column; gap:0.4rem;">
              ${c.offenses.map(o => `
                <div style="font-size:0.75rem; color:var(--text-secondary);">
                  <strong style="color:var(--text-primary);">${o.name}:</strong> ${o.detail}
                </div>
              `).join('')}
            </div>
          </div>
        `).join('')}
      </div>`;
    }

    // Kill Chain Phases (Unit 1)
    if (topic.killChainPhases) {
      html += `<h3 class="content-subheading">8-Phase Cyber Kill Chain Lifecycle</h3>
      <div style="display:flex; flex-direction:column; gap:0.75rem;">
        ${topic.killChainPhases.map(p => `
          <div style="background:rgba(13,18,36,0.6); border:1px solid var(--border-subtle); border-radius:8px; padding:1rem;">
            <strong style="color:var(--cyber-cyan); font-size:0.95rem; display:block; margin-bottom:0.4rem;">${p.phase}</strong>
            <div style="font-size:0.85rem; color:var(--text-primary); margin-bottom:0.4rem;">🔴 <strong>Attacker Action:</strong> ${p.action}</div>
            <div style="font-size:0.85rem; color:var(--cyber-green);">🟢 <strong>Defense Control:</strong> ${p.defense}</div>
          </div>
        `).join('')}
      </div>`;
    }

    // Social Engineering Techniques (Unit 2)
    if (topic.techniques) {
      html += `<h3 class="content-subheading">Social Engineering Attack Taxonomy</h3>
      <div class="feature-cards-grid">
        ${topic.techniques.map(t => `
          <div class="feature-card">
            <div class="feature-card-title">${t.name}</div>
            <p class="feature-card-desc">${t.mechanism}</p>
            <div style="margin-top:0.6rem; font-size:0.75rem; color:var(--cyber-amber); background:rgba(255,183,3,0.08); padding:0.4rem; border-radius:4px;">
              <strong>Example:</strong> ${t.example}
            </div>
          </div>
        `).join('')}
      </div>`;
    }

    // Botnet Architectures (Unit 2)
    if (topic.architectures) {
      html += `<h3 class="content-subheading">Botnet Topologies</h3>
      <div class="feature-cards-grid">
        ${topic.architectures.map(a => `
          <div class="feature-card">
            <div class="feature-card-title">${a.type}</div>
            <p style="font-size:0.8rem; color:var(--cyber-green); margin-bottom:0.3rem;">✓ Pros: ${a.pros}</p>
            ${a.cons ? `<p style="font-size:0.8rem; color:var(--cyber-red);">✗ Cons: ${a.cons}</p>` : ''}
          </div>
        `).join('')}
      </div>`;
    }

    // Bluetooth Comparison (Unit 3)
    if (topic.bluetoothAttacks) {
      html += `<h3 class="content-subheading">Bluetooth Threat Spectrum</h3>
      <div class="feature-cards-grid">
        ${topic.bluetoothAttacks.map(b => `
          <div class="feature-card">
            <div class="feature-card-title">${b.name}</div>
            <span style="font-size:0.7rem; color:${b.severity.includes('Critical') ? 'var(--cyber-red)' : 'var(--cyber-amber)'}; font-weight:700;">${b.severity}</span>
            <p class="feature-card-desc" style="margin-top:0.4rem;">${b.mechanism}</p>
            <div style="margin-top:0.4rem; font-size:0.75rem; color:var(--text-muted);">Impact: ${b.impact}</div>
          </div>
        `).join('')}
      </div>`;
    }

    // 5 Factors of Authentication (Unit 3)
    if (topic.factors) {
      html += `<h3 class="content-subheading">The 5 Authentication Factors</h3>
      <div class="feature-cards-grid">
        ${topic.factors.map(f => `
          <div class="feature-card">
            <div class="feature-card-title">${f.factor}</div>
            <p class="feature-card-desc">${f.desc}</p>
            <div style="margin-top:0.5rem; font-size:0.75rem; color:var(--cyber-red);">
              ⚠️ Vulnerability: ${f.weakness}
            </div>
          </div>
        `).join('')}
      </div>`;
    }

    // Proxy Types (Unit 4)
    if (topic.types) {
      html += `<h3 class="content-subheading">6 Proxy Server Classifications</h3>
      <div class="feature-cards-grid">
        ${topic.types.map(pt => `
          <div class="feature-card">
            <div class="feature-card-title">${pt.name}</div>
            <p class="feature-card-desc">${pt.desc}</p>
          </div>
        `).join('')}
      </div>`;
    }

    // Hash Algorithm Matrix (Unit 4)
    if (topic.hashComparison) {
      html += `<h3 class="content-subheading">Password Hash Algorithms Comparison</h3>
      <div style="overflow-x:auto; margin:1rem 0;">
        <table style="width:100%; border-collapse:collapse; font-size:0.85rem; text-align:left;">
          <thead>
            <tr style="border-bottom:1px solid var(--border-cyan); color:var(--cyber-cyan);">
              <th style="padding:0.6rem;">Algorithm</th>
              <th style="padding:0.6rem;">Security Status</th>
              <th style="padding:0.6rem;">GPU Crack Speed</th>
              <th style="padding:0.6rem;">Assessment</th>
            </tr>
          </thead>
          <tbody>
            ${topic.hashComparison.map(h => `
              <tr style="border-bottom:1px solid var(--border-subtle);">
                <td style="padding:0.6rem; font-family:var(--font-mono); font-weight:700;">${h.algo}</td>
                <td style="padding:0.6rem; color:${h.status === 'GOLD STANDARD' ? 'var(--cyber-green)' : (h.status === 'BROKEN' ? 'var(--cyber-red)' : 'var(--cyber-amber)')}; font-weight:700;">${h.status}</td>
                <td style="padding:0.6rem; color:var(--text-secondary);">${h.gpuRate}</td>
                <td style="padding:0.6rem; color:var(--text-secondary);">${h.verdict}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>`;
    }

    // ASCII Concept Diagram
    if (topic.diagram) {
      html += `
        <div class="diagram-block">
          <div class="diagram-header">
            <span>Architecture & Concept Diagram</span>
            <button class="btn-cyber-outline" style="font-size:0.7rem; padding:0.2rem 0.5rem;" onclick="navigator.clipboard.writeText(\`${topic.diagram}\`); alert('Diagram copied to clipboard!')">Copy ASCII</button>
          </div>
          <pre class="diagram-code">${topic.diagram}</pre>
        </div>
      `;
    }

    // Real-World Case Studies
    if (topic.caseStudies) {
      html += `
        <div class="case-study-banner">
          <div class="case-study-title">🔍 Real-World Historic Case Studies</div>
          <div class="case-study-grid">
            ${topic.caseStudies.map(cs => `
              <div class="case-study-item">
                <strong style="color:var(--text-primary); font-size:0.9rem; display:block; margin-bottom:0.4rem;">${cs.title}</strong>
                <div class="case-study-label">Vector & Exploit:</div>
                <div class="case-study-val">${cs.vector}</div>
                <div class="case-study-label" style="margin-top:0.4rem;">Impact:</div>
                <div class="case-study-val">${cs.impact}</div>
                <div class="case-study-label" style="margin-top:0.4rem; color:var(--cyber-green);">Key Takeaway:</div>
                <div class="case-study-val" style="color:var(--cyber-green);">${cs.keyLesson}</div>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    }

    // Key Takeaways
    if (topic.keyTakeaways) {
      html += `
        <div style="background:rgba(0,255,135,0.04); border:1px solid var(--border-green); border-radius:12px; padding:1.25rem; margin-top:1.5rem;">
          <strong style="color:var(--cyber-green); font-size:0.9rem; text-transform:uppercase; display:block; margin-bottom:0.5rem;">🎯 Key Takeaways & Exam Points</strong>
          <ul style="list-style:disc; margin-left:1.5rem; font-size:0.85rem; color:var(--text-secondary); line-height:1.6;">
            ${topic.keyTakeaways.map(kt => `<li>${kt}</li>`).join('')}
          </ul>
        </div>
      `;
    }

    mainEl.innerHTML = html;
  },

  // Toggle Topic Completed State & Add XP
  toggleTopicCompleted(topicId) {
    if (AppState.completedTopics.has(topicId)) {
      AppState.completedTopics.delete(topicId);
    } else {
      AppState.completedTopics.add(topicId);
      AppState.addXP(50);
      alert('🎉 +50 XP Earned! Topic marked as mastered.');
    }
    AppState.save();
    this.renderUnitsGrid();
    this.renderTopicContent(AppState.currentUnitId, topicId);
    this.updateStats();
  },

  toggleBookmark(topicId) {
    if (AppState.bookmarkedTopics.has(topicId)) {
      AppState.bookmarkedTopics.delete(topicId);
    } else {
      AppState.bookmarkedTopics.add(topicId);
    }
    AppState.save();
    this.renderTopicContent(AppState.currentUnitId, topicId);
  },

  // Text to Speech
  speakTopicText(topicId) {
    if (AppState.isSpeaking) {
      window.speechSynthesis.cancel();
      AppState.isSpeaking = false;
      this.renderTopicContent(AppState.currentUnitId, topicId);
      return;
    }

    const unit = CYBER_DATA.units.find(u => u.id === AppState.currentUnitId);
    const topic = unit ? unit.topics.find(t => t.id === topicId) : null;
    if (!topic || !window.speechSynthesis) return;

    const utterance = new SpeechSynthesisUtterance(`${topic.title}. ${topic.summary}. ${topic.definition || ''}`);
    utterance.rate = 1.0;
    utterance.pitch = 1.0;

    utterance.onend = () => {
      AppState.isSpeaking = false;
      this.renderTopicContent(AppState.currentUnitId, topicId);
    };

    window.speechSynthesis.speak(utterance);
    AppState.isSpeaking = true;
    this.renderTopicContent(AppState.currentUnitId, topicId);
  },

  // Render 10-15 Mark Exam Questions
  renderExamQuestions(filterUnit) {
    const container = document.getElementById('exam-questions-container');
    if (!container || !CYBER_DATA) return;

    let list = CYBER_DATA.examQuestions;
    if (filterUnit !== 'all') {
      list = list.filter(q => q.unit === parseInt(filterUnit, 10));
    }

    container.innerHTML = list.map((q, idx) => `
      <div class="exam-question-card">
        <div class="exam-q-header">
          <div>
            <span class="unit-code-badge" style="margin-bottom:0.4rem; display:inline-block;">UNIT ${q.unit} • QUESTION ${idx + 1}</span>
            <h3>${q.question}</h3>
          </div>
          <span class="exam-marks-pill">${q.marks}</span>
        </div>

        <div class="marking-scheme-box">
          <div class="marking-scheme-title">📊 GTU / University Marking Scheme Breakdown</div>
          <ul class="marking-scheme-list">
            ${q.markingScheme.map(m => `<li>• ${m}</li>`).join('')}
          </ul>
        </div>

        <div style="background:rgba(0,0,0,0.4); border:1px solid var(--border-subtle); border-radius:8px; padding:1.25rem;">
          <div style="font-size:0.85rem; font-weight:700; color:var(--cyber-cyan); text-transform:uppercase; margin-bottom:0.5rem;">Model Answer Architecture:</div>
          <p style="font-size:0.9rem; color:var(--text-primary); line-height:1.6; margin-bottom:0.75rem;">${q.modelAnswer.introduction}</p>

          ${q.modelAnswer.diagram ? `
            <div class="diagram-block" style="margin:0.75rem 0;">
              <pre class="diagram-code" style="font-size:0.75rem;">${q.modelAnswer.diagram}</pre>
            </div>
          ` : ''}

          ${q.modelAnswer.threeRolesDetailed ? `
            <ul style="list-style:disc; margin-left:1.5rem; font-size:0.85rem; color:var(--text-secondary); line-height:1.6; margin-bottom:0.75rem;">
              ${q.modelAnswer.threeRolesDetailed.map(r => `<li>${r}</li>`).join('')}
            </ul>
          ` : ''}

          ${q.modelAnswer.pillars ? `
            <ul style="list-style:disc; margin-left:1.5rem; font-size:0.85rem; color:var(--text-secondary); line-height:1.6; margin-bottom:0.75rem;">
              ${q.modelAnswer.pillars.map(p => `<li>${p}</li>`).join('')}
            </ul>
          ` : ''}

          ${q.modelAnswer.techniques ? `
            <ul style="list-style:disc; margin-left:1.5rem; font-size:0.85rem; color:var(--text-secondary); line-height:1.6; margin-bottom:0.75rem;">
              ${q.modelAnswer.techniques.map(t => `<li>${t}</li>`).join('')}
            </ul>
          ` : ''}

          ${q.modelAnswer.fiveStageAnatomy ? `
            <ul style="list-style:disc; margin-left:1.5rem; font-size:0.85rem; color:var(--text-secondary); line-height:1.6; margin-bottom:0.75rem;">
              ${q.modelAnswer.fiveStageAnatomy.map(a => `<li>${a}</li>`).join('')}
            </ul>
          ` : ''}

          <div style="margin-top:0.75rem; font-size:0.85rem; color:var(--cyber-green);">
            <strong>Conclusion:</strong> ${q.modelAnswer.conclusion}
          </div>
        </div>
      </div>
    `).join('');
  },

  filterExamQuestions(unitVal, btnEl) {
    document.querySelectorAll('.exam-filter-btn').forEach(b => b.classList.remove('active'));
    if (btnEl) btnEl.classList.add('active');
    this.renderExamQuestions(unitVal);
  },

  // 3D Flashcards Deck
  renderFlashcard() {
    if (!CYBER_DATA || !CYBER_DATA.flashcards) return;
    const fc = CYBER_DATA.flashcards[AppState.currentFlashcardIndex];
    if (!fc) return;

    const card = document.getElementById('flashcard-3d-element');
    const frontEl = document.getElementById('flashcard-front-text');
    const backEl = document.getElementById('flashcard-back-text');
    const counterEl = document.getElementById('flashcard-counter-label');
    const unitBadge = document.getElementById('flashcard-unit-badge');

    if (card) card.classList.remove('flipped');
    if (frontEl) frontEl.innerText = fc.front;
    if (backEl) backEl.innerText = fc.back;
    if (counterEl) counterEl.innerText = `Card ${AppState.currentFlashcardIndex + 1} of ${CYBER_DATA.flashcards.length}`;
    if (unitBadge) unitBadge.innerText = `UNIT 0${fc.unit}`;
  },

  flipFlashcard() {
    const card = document.getElementById('flashcard-3d-element');
    if (card) card.classList.toggle('flipped');
  },

  nextFlashcard(known = false) {
    if (known) AppState.addXP(15);
    AppState.currentFlashcardIndex = (AppState.currentFlashcardIndex + 1) % CYBER_DATA.flashcards.length;
    this.renderFlashcard();
  },

  prevFlashcard() {
    AppState.currentFlashcardIndex = (AppState.currentFlashcardIndex - 1 + CYBER_DATA.flashcards.length) % CYBER_DATA.flashcards.length;
    this.renderFlashcard();
  },

  // Interactive Quiz Arena
  renderQuizQuestion() {
    if (!CYBER_DATA || !CYBER_DATA.quizzes) return;
    const q = CYBER_DATA.quizzes[AppState.currentQuizIndex];
    if (!q) return;

    AppState.quizAnswered = false;
    const titleEl = document.getElementById('quiz-q-title');
    const badgeEl = document.getElementById('quiz-unit-badge');
    const progressEl = document.getElementById('quiz-progress-text');
    const optionsWrap = document.getElementById('quiz-options-container');
    const feedbackEl = document.getElementById('quiz-feedback-container');

    if (titleEl) titleEl.innerText = q.question;
    if (badgeEl) badgeEl.innerText = `UNIT 0${q.unit}`;
    if (progressEl) progressEl.innerText = `Question ${AppState.currentQuizIndex + 1} of ${CYBER_DATA.quizzes.length} • Score: ${AppState.quizScore}`;
    if (feedbackEl) {
      feedbackEl.className = 'quiz-feedback-box';
      feedbackEl.innerHTML = '';
    }

    if (optionsWrap) {
      optionsWrap.innerHTML = q.options.map((opt, i) => `
        <button class="quiz-option-btn" id="quiz-opt-${i}" onclick="CyberApp.handleQuizOptionClick(${i})">
          <span style="font-family:var(--font-mono); color:var(--cyber-cyan); font-weight:700;">${String.fromCharCode(65 + i)}.</span>
          <span>${opt}</span>
        </button>
      `).join('');
    }
  },

  handleQuizOptionClick(selectedIdx) {
    if (AppState.quizAnswered) return;
    AppState.quizAnswered = true;

    const q = CYBER_DATA.quizzes[AppState.currentQuizIndex];
    const isCorrect = selectedIdx === q.correct;
    const feedbackEl = document.getElementById('quiz-feedback-container');

    // Highlight options
    q.options.forEach((_, i) => {
      const btn = document.getElementById(`quiz-opt-${i}`);
      if (!btn) return;
      btn.disabled = true;
      if (i === q.correct) {
        btn.classList.add('correct');
      } else if (i === selectedIdx && !isCorrect) {
        btn.classList.add('incorrect');
      }
    });

    if (isCorrect) {
      AppState.quizScore += 10;
      AppState.addXP(25);
    }

    if (feedbackEl) {
      feedbackEl.classList.add('active');
      feedbackEl.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
          <strong style="color:${isCorrect ? 'var(--cyber-green)' : 'var(--cyber-red)'}; font-size:1rem;">
            ${isCorrect ? '🎯 Correct Answer! (+25 XP)' : '❌ Incorrect Selection'}
          </strong>
        </div>
        <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">${q.explanation}</p>
        <button class="btn-cyber-primary" style="margin-top:1rem;" onclick="CyberApp.nextQuizQuestion()">
          Next Question →
        </button>
      `;
    }

    const progressEl = document.getElementById('quiz-progress-text');
    if (progressEl) progressEl.innerText = `Question ${AppState.currentQuizIndex + 1} of ${CYBER_DATA.quizzes.length} • Score: ${AppState.quizScore}`;
  },

  nextQuizQuestion() {
    if (AppState.currentQuizIndex < CYBER_DATA.quizzes.length - 1) {
      AppState.currentQuizIndex++;
      this.renderQuizQuestion();
    } else {
      this.showQuizCompletion();
    }
  },

  showQuizCompletion() {
    const box = document.getElementById('quiz-content-box');
    if (!box) return;

    let rank = 'Script Kiddie';
    let color = 'var(--cyber-amber)';
    const pct = Math.round((AppState.quizScore / (CYBER_DATA.quizzes.length * 10)) * 100);

    if (pct >= 90) { rank = 'Cyber Commander / CISO'; color = 'var(--cyber-green)'; }
    else if (pct >= 70) { rank = 'Senior Penetration Tester'; color = 'var(--cyber-cyan)'; }
    else if (pct >= 50) { rank = 'SOC Incident Responder'; color = 'var(--cyber-blue)'; }

    box.innerHTML = `
      <div style="text-align:center; padding:2rem 1rem;">
        <div style="font-size:3rem; margin-bottom:1rem;">🏆</div>
        <h2 style="font-size:1.8rem; font-weight:800; color:var(--text-primary); margin-bottom:0.5rem;">Grand Exam Arena Completed!</h2>
        <p style="color:var(--text-secondary); margin-bottom:1.5rem;">You scored <strong>${AppState.quizScore} / ${CYBER_DATA.quizzes.length * 10} points</strong> (${pct}%).</p>
        
        <div style="background:rgba(0,0,0,0.5); border:1px solid var(--border-cyan); border-radius:12px; padding:1.5rem; display:inline-block; margin-bottom:2rem;">
          <span style="font-size:0.75rem; text-transform:uppercase; color:var(--text-muted); display:block; font-weight:700;">Awarded Cyber Rank:</span>
          <strong style="font-size:1.4rem; color:${color}; font-family:var(--font-mono);">${rank}</strong>
        </div>

        <div>
          <button class="btn-cyber-primary" onclick="AppState.currentQuizIndex = 0; AppState.quizScore = 0; CyberApp.renderQuizQuestion();">
            🔄 Retake Quiz Arena
          </button>
        </div>
      </div>
    `;
  },

  // Glossary
  renderGlossary(searchQuery = '') {
    const grid = document.getElementById('glossary-cards-grid');
    if (!grid || !CYBER_DATA) return;

    let items = CYBER_DATA.glossary;
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      items = items.filter(g => g.term.toLowerCase().includes(q) || g.def.toLowerCase().includes(q));
    }

    grid.innerHTML = items.map(g => `
      <div class="glossary-card">
        <div class="glossary-term">${g.term}</div>
        <div class="glossary-def">${g.def}</div>
      </div>
    `).join('');
  },

  // Global Search Modal
  openSearchModal() {
    const modal = document.getElementById('search-modal-backdrop');
    const input = document.getElementById('global-search-input');
    if (modal) modal.classList.add('active');
    if (input) {
      input.value = '';
      input.focus();
      this.handleGlobalSearch('');
    }
  },

  closeSearchModal() {
    const modal = document.getElementById('search-modal-backdrop');
    if (modal) modal.classList.remove('active');
  },

  handleGlobalSearch(query) {
    const resultsWrap = document.getElementById('search-results-list');
    if (!resultsWrap) return;

    if (!query.trim()) {
      resultsWrap.innerHTML = `<p style="font-size:0.85rem; color:var(--text-muted);">Type keywords like "Tor", "Botnet", "SIM Swap", "WannaCry", "Password" to search the entire curriculum...</p>`;
      return;
    }

    const q = query.toLowerCase();
    let matches = [];

    // Search Topics
    CYBER_DATA.units.forEach(u => {
      u.topics.forEach(t => {
        if (t.title.toLowerCase().includes(q) || t.summary.toLowerCase().includes(q) || (t.definition && t.definition.toLowerCase().includes(q))) {
          matches.push({
            type: `UNIT ${u.id} TOPIC`,
            title: t.title,
            snippet: t.summary,
            action: () => {
              this.closeSearchModal();
              this.switchView('syllabus');
              this.selectUnit(u.id);
              this.renderTopicContent(u.id, t.id);
            }
          });
        }
      });
    });

    // Search Glossary
    CYBER_DATA.glossary.forEach(g => {
      if (g.term.toLowerCase().includes(q) || g.def.toLowerCase().includes(q)) {
        matches.push({
          type: 'GLOSSARY TERM',
          title: g.term,
          snippet: g.def,
          action: () => {
            this.closeSearchModal();
            this.switchView('glossary');
            this.renderGlossary(g.term);
          }
        });
      }
    });

    if (matches.length === 0) {
      resultsWrap.innerHTML = `<p style="font-size:0.85rem; color:var(--text-muted);">No results found for "${query}".</p>`;
      return;
    }

    window._currentSearchResults = matches;
    resultsWrap.innerHTML = matches.slice(0, 8).map((m, i) => `
      <div onclick="window._currentSearchResults[${i}].action()" class="topic-nav-item" style="cursor:pointer; padding:0.85rem; margin-bottom:0.5rem; background:rgba(13,18,36,0.6); border:1px solid var(--border-subtle); display:block;">
        <span class="unit-code-badge" style="font-size:0.65rem; margin-bottom:0.3rem; display:inline-block;">${m.type}</span>
        <strong style="color:var(--text-primary); display:block; font-size:0.95rem;">${m.title}</strong>
        <p style="font-size:0.8rem; color:var(--text-secondary); margin-top:0.2rem;">${m.snippet.substring(0, 100)}...</p>
      </div>
    `).join('');
  },

  // Toggle Themes (Dark Cyber / Matrix / Light)
  cycleTheme() {
    const themes = ['cyber', 'matrix', 'light'];
    const curIdx = themes.indexOf(AppState.theme);
    const nextTheme = themes[(curIdx + 1) % themes.length];
    AppState.theme = nextTheme;
    document.documentElement.setAttribute('data-theme', nextTheme === 'cyber' ? '' : nextTheme);
    AppState.save();
  },

  // Update Hero Stats
  updateStats() {
    const totalTopics = CYBER_DATA ? CYBER_DATA.units.reduce((acc, u) => acc + u.topics.length, 0) : 35;
    const completedCount = AppState.completedTopics.size;

    const topicStat = document.getElementById('stat-mastered-topics');
    if (topicStat) topicStat.innerText = `${completedCount} / ${totalTopics}`;
  },

  // Setup Keyboard Shortcuts
  setupEventListeners() {
    window.addEventListener('keydown', (e) => {
      // Ctrl+K or Cmd+K opens search
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        this.openSearchModal();
      }
      // Esc closes search modal
      if (e.key === 'Escape') {
        this.closeSearchModal();
      }
    });
  }
};

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  CyberApp.init();
});
