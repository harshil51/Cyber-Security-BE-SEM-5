# -*- coding: utf-8 -*-
"""
Script to generate js/data.js with comprehensive Unit 1, Unit 2, Unit 3, and Unit 4
Cyber Security Curriculum data, case studies, exam questions, interactive labs,
flashcards, quiz arena, and glossary.
"""

import json
import os

cyber_data = {
    "courseInfo": {
        "title": "Cyber Security Mastery & Exam Readiness Platform",
        "subtitle": "Interactive Syllabus (Units 1 - 4) with Deep-Dive Notes, GTU 10-15 Mark Answers, Live Simulators, Quiz Arena, and 3D Flashcards",
        "totalUnits": 4,
        "academicLevel": "Undergraduate / GTU / Engineering Cyber Security Curriculum",
        "version": "2.0 Pro"
    },
    "units": [
        {
            "id": 1,
            "code": "UNIT-01",
            "title": "Introduction to Cyber Crime & Global Perspectives",
            "badge": "Foundational Security",
            "weightage": "15-20 Marks",
            "estimatedTime": "4-5 Hours",
            "overview": "Explores the fundamental concepts of cyber crime, historical evolution from phreaking to modern APTs, the triple role of computers, 4-pillar crime taxonomy, transnational jurisdictional hurdles, global treaties, and the Cyber Kill Chain attack lifecycle.",
            "topics": [
                {
                    "id": "u1-t1",
                    "unitId": 1,
                    "title": "Definition, Core Concepts & 3 Roles of Computers",
                    "tag": "Fundamentals",
                    "summary": "Cyber crime is any unlawful activity where a computer or digital system is the target, tool, or storage environment.",
                    "definition": "Cyber crime refers to any illegal or unauthorized activity in which a computer, computer network, digital device, or the Internet is utilized as a target, a tool, or a storage medium for committing an offense.",
                    "threeRoles": [
                        {
                            "role": "Computer as a Target",
                            "description": "The computer system, server, or network itself is the object of the cyber attack aimed at stealing data, disrupting services, or damaging infrastructure.",
                            "examples": ["Hacking a database server", "DDoS attacks disabling a website", "Ransomware encrypting hospital files", "Buffer overflow exploit against a web service"]
                        },
                        {
                            "role": "Computer as a Tool",
                            "description": "The computer and internet are used as an instrument to execute traditional or modern crimes against victims.",
                            "examples": ["Sending phishing emails to harvest credentials", "Online financial banking fraud", "Cyber stalking and harassment via social media", "Credit card fraud and forged identity documents"]
                        },
                        {
                            "role": "Computer as a Storage Medium / Incidental",
                            "description": "The computer or digital drive is used to store illegal data, stolen intellectual property, encryption keys, or logs of criminal acts.",
                            "examples": ["Storing stolen credit card numbers (dumps)", "Hosting pirated commercial software and movies", "Keeping encrypted logs of illicit transactions", "Storing illegal contraband and documents"]
                        }
                    ],
                    "diagram": 
"""+-------------------------------------------------------------+
|               ROLES OF A COMPUTER IN CYBERCRIME             |
+-------------------------------------------------------------+
|                                                             |
|   1. COMPUTER AS TARGET                                     |
|      [ Attacker ] ======= Exploit ======> [ Server/DB ]     |
|      (Examples: Server Hacking, Ransomware, DDoS attack)    |
|                                                             |
|   2. COMPUTER AS TOOL                                       |
|      [ Attacker ] --- (Uses PC & Net) ---> [ Victim ]       |
|      (Examples: Phishing, Banking Fraud, Cyberstalking)     |
|                                                             |
|   3. COMPUTER AS STORAGE                                    |
|      [ Attacker ] ======= Saves Data =====> [ Hard Drive ]  |
|      (Examples: Stolen DBs, Card Dumps, Illicit Files)      |
+-------------------------------------------------------------+""",
                    "keyTakeaways": [
                        "A cyber crime requires at least one digital component (computer, network, mobile device, or cloud).",
                        "Computers can act as a Target, Tool, or Storage medium simultaneously in complex intrusions.",
                        "Traditional crimes committed over digital networks are often categorized under cyber-enabled crime."
                    ],
                    "examNote": "In 10-15 mark exams, begin with the formal definition, provide the 3-column table of roles with concrete examples, draw the tripartite role diagram, and contrast cyber-dependent vs cyber-enabled crime."
                },
                {
                    "id": "u1-t2",
                    "unitId": 1,
                    "title": "Historical Evolution & Origins of Cyber Crime",
                    "tag": "History & Trends",
                    "summary": "The chronological progression of digital offenses from 1960s mainframe abuse and phone phreaking to modern AI-driven cyber threats.",
                    "timeline": [
                        {
                            "era": "1960s – 1970s",
                            "name": "Early Computer Misuse & Mainframe Era",
                            "details": "Computers were large, centralized mainframes housed in universities and government defense centers. Misuse was primarily physical unauthorized access, password sharing, or logic bomb planting by disgruntled operators."
                        },
                        {
                            "era": "1970s – 1980s",
                            "name": "Phone Phreaking Era",
                            "details": "Pioneered by figures like John Draper ('Captain Crunch'). Phreakers used audio frequencies (e.g. 2600 Hz tone from toy whistles or 'Blue Boxes') to manipulate AT&T telephone switches and obtain free unauthorized long-distance calls."
                        },
                        {
                            "era": "1980s – 1990s",
                            "name": "First Viruses & Network Worms",
                            "details": "Introduction of floppy disk boot-sector viruses like 'Brain' (1986). In 1988, Robert Tappan Morris released the Morris Worm, bringing down ~10% of the ARPANET and leading to the creation of the first CERT (Computer Emergency Response Team)."
                        },
                        {
                            "era": "1990s – 2000s",
                            "name": "Commercial Internet Expansion & Script Kiddies",
                            "details": "Rapid rise of the World Wide Web. Emergence of email mass-mailer worms (ILOVEYOU, Melissa), website defacements, and early banking scams. Cybercrime transitioned from technical curiosity to initial financial monetization."
                        },
                        {
                            "era": "2010s – Present",
                            "name": "Organized Cybercrime, APTs, Ransomware & AI",
                            "details": "State-sponsored Advanced Persistent Threats (APTs), Ransomware-as-a-Service (RaaS), cryptocurrency extortion, supply chain attacks (SolarWinds), dark web bazaars, and generative AI deepfake frauds."
                        }
                    ],
                    "diagram":
"""+-------------------------------------------------------------------------+
|                  EVOLUTIONARY TIMELINE OF CYBERCRIME                    |
+-------------------------------------------------------------------------+
| 1960s-70s: Mainframe Physical Misuse & Logic Bombs                      |
|      |                                                                  |
| 1970s-80s: Phone Phreaking (2600 Hz tone, Blue Boxes, Free Calls)       |
|      |                                                                  |
| 1980s-90s: Floppy Viruses (Brain 1986) & ARPANET Morris Worm (1988)     |
|      |                                                                  |
| 1990s-00s: Web Commercialization, Email Worms (ILOVEYOU), Defacements  |
|      |                                                                  |
| 2010s-Now: Organized Cyber Syndicates, APTs, RaaS, Darknet & Deepfakes  |
+-------------------------------------------------------------------------+""",
                    "keyTakeaways": [
                        "Phreaking was the direct technological precursor to modern computer network exploitation.",
                        "The Morris Worm (1988) was a watershed moment establishing the discipline of Incident Response (CERT).",
                        "Modern cybercrime is industrialized with specialization, underground markets, and crypto monetization."
                    ]
                },
                {
                    "id": "u1-t3",
                    "unitId": 1,
                    "title": "Motivations & Proliferation of Cyber Crime",
                    "tag": "Threat Landscape",
                    "summary": "Why cybercrime has grown exponentially: anonymity, financial windfall, low barriers to entry, and global connectivity.",
                    "drivers": [
                        { "title": "Exponential Internet & Device Adoption", "desc": "Billions of connected IoT devices, smartphones, and cloud instances enlarge the attack surface." },
                        { "title": "Perceived Anonymity & IP Obfuscation", "desc": "Tools like Tor, VPN chains, and bulletproof hosting allow criminals to operate with obscured identities." },
                        { "title": "Massive Financial Incentive", "desc": "Ransomware payments in untraceable cryptocurrencies yield billions in illicit revenue with minimal physical risk." },
                        { "title": "Low Technical Barrier (CaaS)", "desc": "Cybercrime-as-a-Service allows novice actors ('script kiddies') to rent ready-made botnets and phishing kits." },
                        { "title": "Critical Infrastructure Digitalization", "desc": "Hospitals, electrical power grids (SCADA), and financial exchanges operate online, creating high-value extortion targets." }
                    ],
                    "keyTakeaways": [
                        "Cybercrime offers asymmetrical advantage: defense must protect every vulnerability, whereas attackers only need one flaw.",
                        "Financial gain accounts for over 80% of all reported cybercriminal activity."
                    ]
                },
                {
                    "id": "u1-t4",
                    "unitId": 1,
                    "title": "4-Pillar Classification of Cyber Crime",
                    "tag": "Taxonomy",
                    "summary": "Comprehensive classification based on target categories: Against Individuals, Property, Government, and Society.",
                    "categories": [
                        {
                            "category": "1. Cyber Crime Against Individuals",
                            "target": "Targeting specific persons, privacy, dignity, and personal safety.",
                            "offenses": [
                                { "name": "Identity Theft", "detail": "Stealing personal identifiers (SSN/Aadhaar, DOB, passwords) to open fraudulent accounts." },
                                { "name": "Cyberstalking", "detail": "Persistent online surveillance, unwanted electronic messaging, and location tracking causing fear." },
                                { "name": "Cyberbullying & Harassment", "detail": "Humiliating, trolling, and abusing individuals via social media forums and messaging apps." },
                                { "name": "Phishing & Impersonation", "detail": "Sending deceptive links to harvest individual banking credentials and sensitive photos." }
                            ]
                        },
                        {
                            "category": "2. Cyber Crime Against Property",
                            "target": "Targeting digital assets, intellectual property, corporate funds, and commercial trade secrets.",
                            "offenses": [
                                { "name": "Data & Intellectual Property Theft", "detail": "Exfiltrating proprietary code, patents, customer databases, and design blueprints." },
                                { "name": "Ransomware Extortion", "detail": "Encrypting organizational file systems and demanding crypto ransoms to restore business access." },
                                { "name": "Unauthorized Financial Transfers", "detail": "Injecting banking malware (Trojans) or manipulating SWIFT wire transactions." },
                                { "name": "Website Defacement & Software Piracy", "detail": "Vandalizing commercial web portals and redistributing cracked commercial software." }
                            ]
                        },
                        {
                            "category": "3. Cyber Crime Against Government",
                            "target": "Targeting national security, defense databases, sovereign administration, and critical infrastructure.",
                            "offenses": [
                                { "name": "Cyber Terrorism", "detail": "Coordinated cyber strikes intended to cause public panic, casualty, or severe economic catastrophe." },
                                { "name": "Cyber Warfare & Espionage", "detail": "Nation-state military operations targeting adversary military networks and intelligence." },
                                { "name": "Critical Infrastructure Attacks", "detail": "Disrupting SCADA systems controlling electrical grids, nuclear facilities, or water filtration plants." },
                                { "name": "Electoral System Interference", "detail": "Hacking voter registration databases or manipulating automated balloting software." }
                            ]
                        },
                        {
                            "category": "4. Cyber Crime Against Society",
                            "target": "Targeting the general public peace, social harmony, ethical order, and community welfare.",
                            "offenses": [
                                { "name": "Disinformation & Fake News", "detail": "Deploying bot armies to spread mass fabricated panic, communal discord, or health falsehoods." },
                                { "name": "Child Sexual Exploitation (CSAM)", "detail": "Producing, transmitting, or possessing illicit exploitation material over dark web channels." },
                                { "name": "Illegal Online Gambling & Narcotics", "detail": "Operating unregulated darknet marketplaces for illicit substance distribution." },
                                { "name": "Financial Ponzi & Pyramid Scams", "detail": "Luring large sections of the populace into deceptive crypto or fake investment schemes." }
                            ]
                        }
                    ],
                    "diagram":
"""+--------------------------------------------------------------------------+
|                  4-PILLAR CLASSIFICATION OF CYBERCRIME                   |
+--------------------------------------------------------------------------+
|  1. AGAINST INDIVIDUALS    |  2. AGAINST PROPERTY                        |
|  - Identity Theft          |  - Ransomware & Data Theft                  |
|  - Cyberstalking & Bullying|  - IP Theft & Trade Secrets                 |
|  - Phishing & Harassment   |  - Bank Frauds & Website Defacement         |
|----------------------------+---------------------------------------------|
|  3. AGAINST GOVERNMENT     |  4. AGAINST SOCIETY                         |
|  - Cyber Warfare & Spying  |  - Disinformation / Fake News               |
|  - Critical Infra (SCADA)  |  - Online Trafficking & CSAM                |
|  - Cyber Terrorism         |  - Large-scale Financial Ponzi Scams        |
+--------------------------------------------------------------------------+""",
                    "keyTakeaways": [
                        "Exam questions frequently ask for this 4-way classification with 2 detailed examples for each pillar.",
                        "Classifying by target helps determine applicable statutory sections (e.g. IT Act 2000 sections 66C, 66D, 66E, 66F)."
                    ]
                },
                {
                    "id": "u1-t5",
                    "unitId": 1,
                    "title": "Global Perspective & Transnational Nature of Cyber Crime",
                    "tag": "International Law",
                    "summary": "Why cybercrime transcends national boundaries and creates unprecedented jurisdictional, attribution, and extradition challenges.",
                    "challenges": [
                        { "title": "1. Transnational Jurisdictional Clashes", "desc": "An attacker in Country A uses servers in Country B and C to hack victims in Country D. Determining which judicial court holds legal jurisdiction is difficult." },
                        { "title": "2. Attribution Difficulty", "desc": "IP spoofing, proxy bouncing, and darknet routing make it difficult to prove the identity of the physical person behind the keyboard beyond reasonable doubt." },
                        { "title": "3. Extradition Hurdles & Safe Havens", "desc": "Many nations lack bilateral extradition treaties or refuse to extradite their own citizens, providing safe operational bases for rogue hacker collectives." },
                        { "title": "4. Disparate Legal Definitions", "desc": "What is deemed illegal online speech or cyber offense in one country may be protected or unregulated in another." }
                    ],
                    "keyTakeaways": [
                        "Cybercrime has zero geographical latency: physical distance is irrelevant to attack propagation.",
                        "Effective cyber defense requires harmonized international legal frameworks and instant intelligence exchange."
                    ]
                },
                {
                    "id": "u1-t6",
                    "unitId": 1,
                    "title": "International Cooperation & Global Security Treaties",
                    "tag": "Governance",
                    "summary": "Mechanisms like the Budapest Convention, Interpol, Europol EC3, and Mutual Legal Assistance Treaties (MLATs) that combat global cyber threats.",
                    "frameworks": [
                        {
                            "name": "Budapest Convention on Cybercrime (2001)",
                            "description": "The first binding international treaty addressing internet and computer crime by harmonizing national laws, improving investigative techniques, and increasing cooperation among nations.",
                            "pillars": ["Harmonization of criminal substantive offenses", "Procedural investigative powers (data preservation)", "International 24/7 point-of-contact network"]
                        },
                        {
                            "name": "INTERPOL Cybercrime Directorate",
                            "description": "Global police organization facilitating cross-border cyber threat intelligence sharing, operation coordinates (e.g. Operation African Cyber Surge), and capacity building."
                        },
                        {
                            "name": "Europol European Cybercrime Centre (EC3)",
                            "description": "Coordinates European Union investigations against high-level cyber syndicates, bulletproof hosters, and ransomware operators."
                        },
                        {
                            "name": "Mutual Legal Assistance Treaties (MLATs)",
                            "description": "Formal agreements between countries allowing law enforcement to request digital evidence, server logs, and witness testimony held in foreign jurisdictions."
                        }
                    ],
                    "keyTakeaways": [
                        "MLAT processes traditionally suffer from multi-month bureaucratic delays, which cybercriminals exploit to destroy digital trails.",
                        "The 24/7 Network of Contact Points allows emergency preservation of volatile cloud server logs."
                    ]
                },
                {
                    "id": "u1-t7",
                    "unitId": 1,
                    "title": "Planning of Cyber Offences: The Cyber Kill Chain",
                    "tag": "Attack Lifecycle",
                    "summary": "The 8-stage operational methodology used by advanced cyber criminals to plan and execute sophisticated cyber offensives.",
                    "killChainPhases": [
                        { "phase": "1. Reconnaissance", "action": "Researching target via OSINT, LinkedIn, Shodan, DNS records, and social media footprinting.", "defense": "Threat intelligence monitoring, public info minimization." },
                        { "phase": "2. Scanning & Enumeration", "action": "Port scanning (Nmap), service banner grabbing, and identifying unpatched software vulnerabilities.", "defense": "Vulnerability scanning, firewall rule hardening." },
                        { "phase": "3. Weaponization", "action": "Coupling an exploit code with a malicious payload/backdoor tailored to the target operating system.", "defense": "Threat intelligence, static code analysis." },
                        { "phase": "4. Delivery", "action": "Transmitting payload via spear-phishing emails, malicious USB drives, or drive-by web downloads.", "defense": "Email security gateways, spam filtering, user awareness." },
                        { "phase": "5. Exploitation", "action": "Executing malicious code by triggering vulnerability (e.g. buffer overflow, zero-day flaw).", "defense": "Patch management, Endpoint Detection and Response (EDR)." },
                        { "phase": "6. Installation & Persistence", "action": "Installing backdoors, registry run keys, scheduled tasks, or kernel rootkits for permanent access.", "defense": "File integrity monitoring, application allowlisting." },
                        { "phase": "7. Command & Control (C2)", "action": "Opening an encrypted beacon back to the attacker's server (via HTTPS, DNS tunneling, or Tor).", "defense": "Network traffic analysis, DNS sinkholing, IDS/IPS." },
                        { "phase": "8. Actions on Objectives", "action": "Exfiltrating confidential databases, encrypting volumes for ransom, or destroying system files.", "defense": "Data Loss Prevention (DLP), network segmentation, offline backups." }
                    ],
                    "diagram":
"""+--------------------------------------------------------------------------+
|                     THE 8-PHASE CYBER KILL CHAIN                         |
+--------------------------------------------------------------------------+
| [1. Recon] -> [2. Scan] -> [3. Weaponize] -> [4. Deliver]               |
|      |                                             |                     |
| [8. Objectives] <- [7. C2 Beacon] <- [6. Install] <- [5. Exploit]         |
+--------------------------------------------------------------------------+""",
                    "keyTakeaways": [
                        "Breaking any single link in the Cyber Kill Chain halts the entire offensive campaign.",
                        "Exam questions frequently require explaining each phase with attacker action and defender countermeasure."
                    ]
                },
                {
                    "id": "u1-t8",
                    "unitId": 1,
                    "title": "Major Real-World Case Studies (Unit 1)",
                    "tag": "Case Studies",
                    "summary": "Analysis of historic cyber intrusions: WannaCry Ransomware, Yahoo Data Breach, and the Sony Pictures Cyberattack.",
                    "caseStudies": [
                        {
                            "title": "WannaCry Ransomware Epidemic (2017)",
                            "victim": "200,000+ computers across 150 countries (including UK NHS, FedEx, Renault)",
                            "vector": "EternalBlue SMBv1 vulnerability exploit (MS17-010) coupled with DoublePulsar backdoor.",
                            "impact": "Encrypted hard drives and demanded $300-$600 in Bitcoin. Crippled hospital emergency wards.",
                            "resolution": "A security researcher (Marcus Hutchins) discovered and activated a hardcoded domain 'kill-switch'.",
                            "keyLesson": "Urgent necessity of timely patch management and disabling legacy protocols like SMBv1."
                        },
                        {
                            "title": "Yahoo Massive Data Breach (2013 – 2014)",
                            "victim": "All 3 billion Yahoo user accounts",
                            "vector": "Spear-phishing email sent to a Yahoo employee yielding internal network access and proprietary user database backup tools.",
                            "impact": "Names, email addresses, phone numbers, birthdates, and MD5/bcrypt hashed passwords stolen.",
                            "keyLesson": "Mandatory employee security training and adoption of strong salting/hashing standards."
                        },
                        {
                            "title": "Sony Pictures Entertainment Cyberattack (2014)",
                            "victim": "Sony Pictures internal infrastructure and executive communications",
                            "vector": "Sophisticated spear-phishing campaign by APT group 'Guardians of Peace' deploying Destover wiper malware.",
                            "impact": "Complete erasure of corporate servers, leak of unreleased movies, and private executive emails.",
                            "keyLesson": "Zero-trust network segmentation and prompt incident containment capabilities."
                        }
                    ]
                }
            ]
        },
        {
            "id": 2,
            "code": "UNIT-02",
            "title": "Cybercrime & Social Media, Social Engineering & Botnets",
            "badge": "Social & Threat Vector",
            "weightage": "20-25 Marks",
            "estimatedTime": "5-6 Hours",
            "overview": "Deep dive into social media cybercrime ecosystems, psychological principles of social engineering, complete taxonomies of phishing and pretexting, cyberstalking classifications, the Cybercrime-as-a-Service (CaaS) business model, and Botnet architectures (Mirai).",
            "topics": [
                {
                    "id": "u2-t1",
                    "unitId": 2,
                    "title": "Social Media Cybercrime: Structure & Objectives",
                    "tag": "Social Media Ecosystem",
                    "summary": "Social media serves as a prime environment for criminal operations due to user oversharing, trusted connections, and vast target demographics.",
                    "structureElements": [
                        { "element": "1. Victim", "desc": "Individual users, employees, teenagers, or organizations with exposed public profiles." },
                        { "element": "2. Attacker", "desc": "Fraudsters, state actors, commercial competitors, cyberstalkers, or automated bot networks." },
                        { "element": "3. Platform", "desc": "Social networking channels (Instagram, LinkedIn, X, Facebook, Telegram, WhatsApp)." },
                        { "element": "4. Information", "desc": "Target data mined from posts: workplace, family ties, location tags, habits, and phone numbers." },
                        { "element": "5. Attack Mechanism", "desc": "Phishing DMs, fake customer support handles, malicious links, romance lures, deepfakes." },
                        { "element": "6. Criminal Objective", "desc": "Financial extortion, credential harvesting, corporate espionage, account takeover, reputation ruin." }
                    ],
                    "diagram":
"""+-------------------------------------------------------------+
|          STRUCTURE OF CYBERCRIME ON SOCIAL MEDIA            |
+-------------------------------------------------------------+
|  [ Attacker ] ---> Exploits ---> [ Social Media Platform ]  |
|         |                                    |              |
|   (Social Eng / DM)                   (Mined Data / OSINT)  |
|         v                                    v              |
|  [ Victim Profile ] <----------------- [ Attack Vector ]    |
|         |                                                   |
|         v                                                   |
|  [ Outcome: Fraud / Account Hijack / Cyberstalking / Theft ]|
+-------------------------------------------------------------+""",
                    "keyTakeaways": [
                        "Social media amplifies social engineering because targets inherently trust messages appearing from connections.",
                        "OSINT (Open Source Intelligence) gathered from social media forms the basis for spear-phishing campaigns."
                    ]
                },
                {
                    "id": "u2-t2",
                    "unitId": 2,
                    "title": "Social Engineering: Psychology & The 6 Human Vulnerabilities",
                    "tag": "Social Engineering",
                    "summary": "The art of manipulating individuals into divulging confidential information or executing actions compromising security.",
                    "psychologicalTriggers": [
                        { "trigger": "1. Authority", "desc": "Victims obey perceived figures of power (e.g. CEO, police officer, IT director, tax department)." },
                        { "trigger": "2. Urgency", "desc": "Creating artificial time pressure ('Account suspended in 15 minutes!') disabling rational cognitive review." },
                        { "trigger": "3. Fear & Intimidation", "desc": "Threatening legal arrest, public humiliation, or malware infection to force compliance." },
                        { "trigger": "4. Greed & Reward", "desc": "Luring victims with crypto prizes, high-paying jobs, discount coupons, or inheritance claims." },
                        { "trigger": "5. Trust & Social Proof", "desc": "Pretending to be a known colleague, mutual friend, or reputable brand." },
                        { "trigger": "6. Curiosity & Helpfulness", "desc": "Appealing to human helpfulness ('Can you hold the door?') or curiosity ('Check this leaked photo!')." }
                    ],
                    "keyTakeaways": [
                        "Kevin Mitnick's maxim: 'People are the weakest link in the security chain.'",
                        "Technical firewalls cannot filter out trusted human compliance triggered by deception."
                    ]
                },
                {
                    "id": "u2-t3",
                    "unitId": 2,
                    "title": "Types of Social Engineering Attacks",
                    "tag": "Attack Types",
                    "summary": "Detailed exploration of Phishing, Pretexting, Baiting, Quid Pro Quo, Tailgating, Impersonation, and Scareware.",
                    "techniques": [
                        {
                            "name": "1. Phishing",
                            "mechanism": "Mass fraudulent communications impersonating reputable entities to trick users into revealing credentials.",
                            "example": "Fake email mimicking Netflix asking user to update credit card details via spoofed link."
                        },
                        {
                            "name": "2. Pretexting",
                            "mechanism": "Creating an elaborate fabricated scenario (pretext) to establish trust and extract specific sensitive info.",
                            "example": "Attacker calls calling employee claiming to be corporate Auditor needing temporary VPN credentials for audit."
                        },
                        {
                            "name": "3. Baiting",
                            "mechanism": "Promising a good/lure (physical or digital) to entice victims into infecting their own system.",
                            "example": "Dropping malware-infected USB flash drives labeled 'Confidential Executive Salaries Q4' in corporate parking lots."
                        },
                        {
                            "name": "4. Quid Pro Quo",
                            "mechanism": "Offering a service, assistance, or favor in explicit exchange for credentials or security compromise.",
                            "example": "Calling employees pretending to be Helpdesk offering 'free OS performance tuning' if they disable their antivirus."
                        },
                        {
                            "name": "5. Tailgating / Piggybacking",
                            "mechanism": "Physical intrusion where an unauthorized person follows an authorized employee through secure doors.",
                            "example": "Attacker dressed as delivery courier carrying heavy boxes asking employee to hold badge-access door open."
                        },
                        {
                            "name": "6. Impersonation & BEC",
                            "mechanism": "Directly assuming the identity of a trusted individual to command financial wire transfers.",
                            "example": "Business Email Compromise (BEC) where attacker poses as CEO instructing CFO to execute urgent vendor wire."
                        },
                        {
                            "name": "7. Scareware",
                            "mechanism": "Deceiving victims with frightening alerts claiming severe malware infection to force downloading fake antivirus.",
                            "example": "Flashing browser pop-up: 'Warning! 43 Trojan Viruses Detected! Call Toll-Free Support Now!'"
                        }
                    ],
                    "keyTakeaways": [
                        "Exam questions frequently ask to differentiate Pretexting vs Phishing and Baiting vs Quid Pro Quo.",
                        "Mitigation involves continuous security awareness training, out-of-band verification, and clean-desk policies."
                    ]
                },
                {
                    "id": "u2-t4",
                    "unitId": 2,
                    "title": "Social Media Security Case Studies",
                    "tag": "Case Studies",
                    "summary": "Real-world breaches rooted in social media vectors: Twitter 2020 Bitcoin Compromise and Cambridge Analytica.",
                    "caseStudies": [
                        {
                            "title": "Twitter (X) 2020 Bitcoin Social Engineering Hack",
                            "vector": "Phone spear-phishing (vishing) targeted Twitter customer support employees to obtain internal admin dashboard credentials.",
                            "execution": "Attackers hijacked 130 high-profile accounts (Elon Musk, Barack Obama, Apple, Joe Biden, Bill Gates) and tweeted a Bitcoin doubling scam.",
                            "yield": "Generated ~$120,000 in Bitcoin in a few hours before Twitter revoked admin dashboard access.",
                            "lesson": "Internal administrative tools must enforce hardware MFA keys and strict access privilege separation."
                        },
                        {
                            "title": "Cambridge Analytica Data Scandal (2018)",
                            "vector": "A personality quiz app ('This Is Your Digital Life') harvested personal data of 87 million Facebook users and their friends without informed consent.",
                            "impact": "Data used to build psychological voter profiles for precision political microtargeting in elections.",
                            "lesson": "Social platforms must enforce strict third-party API data isolation and clear user consent mechanisms."
                        }
                    ]
                },
                {
                    "id": "u2-t5",
                    "unitId": 2,
                    "title": "Cyberstalking: Behaviors, Taxonomy & Legal Protection",
                    "tag": "Cyberstalking",
                    "summary": "Repeated, persistent harassment, surveillance, and intimidation of a victim utilizing digital technology.",
                    "behaviors": [
                        { "type": "Direct Cyberstalking", "details": "Directly sending threatening or abusive emails, DMs, unwanted calls, bombarding messages, and real-time GPS tracking." },
                        { "type": "Indirect Cyberstalking", "details": "Creating fake profiles in the victim's name, posting defamatory rumors, doxxing personal contact info, and inciting mob harassment." }
                    ],
                    "legalAspects": [
                        "Indian IT Act 2000: Section 66E (Privacy violation), Section 67 (Publishing obscene content), Section 354D of Indian Penal Code (IPC) specifically criminalizes stalking.",
                        "Evidence preservation: Retain exact timestamps, message headers, URLs, unaltered screenshots, and report to national cyber portals (cybercrime.gov.in)."
                    ]
                },
                {
                    "id": "u2-t6",
                    "unitId": 2,
                    "title": "Cybercrime Ecosystem & Cybercrime-as-a-Service (CaaS)",
                    "tag": "Underground Economy",
                    "summary": "How organized digital crime operates as a commercial underground economy with specialized supply chains.",
                    "caasComponents": [
                        { "service": "Ransomware-as-a-Service (RaaS)", "desc": "Core developers lease ransomware builders and payment portals to 'affiliates' for a 20-30% profit split." },
                        { "service": "Phishing-as-a-Service (PhaaS)", "desc": "Ready-to-deploy phishing portals with automated 2FA bypass (Evilginx) available on monthly subscriptions." },
                        { "service": "Initial Access Brokers (IABs)", "desc": "Hackers specializing in compromising enterprise VPN/RDP credentials, selling active footholds to ransomware syndicates." },
                        { "service": "Botnet-for-Hire (DDoS Booters)", "desc": "Commercial web portals allowing paying users to launch multi-hundred Gbps DDoS strikes against targets." },
                        { "service": "Crypto Laundering & Mixers", "desc": "Tumbler services breaking transactional links in public blockchain ledgers to launder illicit extortion proceeds." }
                    ],
                    "keyTakeaways": [
                        "CaaS lowers the barrier to entry, enabling non-technical criminals to execute advanced cyber attacks.",
                        "Investigation requires blockchain analysis, server seizures, and infiltrating dark web broker forums."
                    ]
                },
                {
                    "id": "u2-t7",
                    "unitId": 2,
                    "title": "Botnets: Architecture, Lifecycle & Case Study",
                    "tag": "Botnets",
                    "summary": "A network of compromised computers or IoT devices ('zombies') remotely commanded by a central botmaster.",
                    "architectures": [
                        {
                            "type": "1. Centralized C2 (IRC / HTTP / HTTPS)",
                            "pros": "Simple command structure, instantaneous execution.",
                            "cons": "Single Point of Failure (SPOF) - taking down the C2 server disables the entire botnet."
                        },
                        {
                            "type": "2. Peer-to-Peer (P2P)",
                            "pros": "Decentralized resilience; bots exchange encrypted commands with neighbor peers. No single server to seize.",
                            "cons": "Higher latency in command propagation, complex implementation."
                        },
                        {
                            "type": "3. Hybrid / Domain Generation Algorithm (DGA)",
                            "pros": "Bots algorithmically generate thousands of random daily domain names to find the active C2 server, defeating static IP blocking."
                        }
                    ],
                    "botLifecycle": [
                        "1. Infection: Vulnerability exploit or malicious download installs bot agent.",
                        "2. Execution & Persistence: Bot registers as a stealth background daemon/service.",
                        "3. Beaconing (Check-in): Bot connects to C2 infrastructure and announces its IP and specs.",
                        "4. Awaiting Instruction: Bot sleeps or polls for new commands (DDoS, spam, mining).",
                        "5. Attack Execution: Synchronized execution of commands alongside thousands of peer bots."
                    ],
                    "caseStudy": {
                        "name": "Mirai Botnet (2016)",
                        "target": "Infected over 600,000 IoT devices (CCTV cameras, home routers, DVRs) by scanning for 62 default factory passwords (e.g. admin/admin, root/xc3511).",
                        "attack": "Launched a 1.2 Tbps DDoS flood against Dyn DNS, temporarily crippling major services including Twitter, Netflix, GitHub, and Spotify across North America and Europe.",
                        "lesson": "Manufacturers must eliminate default hardcoded credentials and enforce mandatory password change on first boot."
                    },
                    "diagram":
"""+-------------------------------------------------------------+
|               CENTRALIZED VS P2P BOTNET ARCHITECTURE        |
+-------------------------------------------------------------+
|  CENTRALIZED BOTNET:                                        |
|             [ Botmaster ]                                   |
|                  |                                          |
|            [ C2 Server ] (Single Point of Failure!)         |
|            /     |     \                                    |
|       [Bot 1] [Bot 2] [Bot 3] ----> [ DDoS Attack Target ]  |
|                                                             |
|  PEER-TO-PEER (P2P) BOTNET:                                 |
|       [Bot 1] <====> [Bot 2] <====> [Bot 3]                 |
|          ^             ^              ^                     |
|          |             |              |                     |
|          +---- All bots communicate & relay commands -------+
+-------------------------------------------------------------+"""
                },
                {
                    "id": "u2-t8",
                    "unitId": 2,
                    "title": "Attack Vectors & Defense-in-Depth Strategy",
                    "tag": "Defense Strategy",
                    "summary": "Classifying paths of cyber infiltration and constructing multi-layered organizational defenses.",
                    "vectors": ["Email & Phishing", "Web Application Flaws", "Wireless & Rogue APs", "Compromised Supply Chain", "Removable USB Media", "Insider Threats"],
                    "defenseInDepth": [
                        { "layer": "Perimeter Layer", "controls": "Next-Gen Firewalls, Web Application Firewalls (WAF), DDoS Scrubbing" },
                        { "layer": "Network Layer", "controls": "Network Segmentation, Intrusion Detection & Prevention Systems (IDS/IPS), Zero Trust" },
                        { "layer": "Endpoint Layer", "controls": "Endpoint Detection and Response (EDR), Antivirus, Device Encryption" },
                        { "layer": "Application Layer", "controls": "Secure Code Audits (SAST/DAST), Input Validation, Least Privilege Access" },
                        { "layer": "Data Layer", "controls": "Encryption at rest and in transit (AES-256, TLS 1.3), Data Loss Prevention (DLP)" },
                        { "layer": "Human Layer", "controls": "Periodic Phishing Simulations, Security Training, Multi-Factor Authentication (MFA)" }
                    ]
                }
            ]
        },
        {
            "id": 3,
            "code": "UNIT-03",
            "title": "Cyber Crime with Mobile & Wireless Devices",
            "badge": "Mobile & Wireless Security",
            "weightage": "20-25 Marks",
            "estimatedTime": "5-6 Hours",
            "overview": "Examines mobile vulnerabilities, mobile malware ecosystem, credit card and digital payment frauds, SIM swap mechanics, registry and OS security configurations, 5-factor authentication security, wireless attacks (Evil Twin, KRACK), Bluetooth threats (Bluebugging), and Mobile Device Management (MDM) frameworks.",
            "topics": [
                {
                    "id": "u3-t1",
                    "unitId": 3,
                    "title": "Mobile Device Proliferation & Unique Security Challenges",
                    "tag": "Mobile Landscape",
                    "summary": "Why portable smartphones and wireless ecosystems present radically different attack surfaces compared to traditional desktop computers.",
                    "challenges": [
                        { "issue": "1. Physical Portability & Theft", "desc": "High risk of device loss or physical theft carrying enterprise emails, saved sessions, and cached credentials." },
                        { "issue": "2. Insecure Public Wireless Networks", "desc": "Smartphones automatically probe and connect to open Wi-Fi hotspots, exposing traffic to eavesdropping." },
                        { "issue": "3. OS Fragmentation & Slow Updates", "desc": "Android ecosystem fragmentation leads to millions of devices running outdated, unpatched OS versions." },
                        { "issue": "4. Aggressive App Permissions", "desc": "Apps requesting unnecessary permissions (Contacts, Location, Microphone, SMS) and leaking sensitive telemetry." },
                        { "issue": "5. Sideloading & Third-Party App Stores", "desc": "Installing unverified APK files bypassing official Google Play or Apple App Store security checks." }
                    ],
                    "keyTakeaways": [
                        "Mobile devices have blurred corporate perimeters through Bring Your Own Device (BYOD) adoption.",
                        "Smartphones act as identity anchors (receiving 2FA SMS/push prompts), making them high-value targets."
                    ]
                },
                {
                    "id": "u3-t2",
                    "unitId": 3,
                    "title": "Mobile Malware & Jailbreaking / Rooting Risks",
                    "tag": "Mobile Malware",
                    "summary": "Technical analysis of mobile malware classes and the catastrophic security breakdown caused by OS rooting and jailbreaking.",
                    "malwareTypes": [
                        { "name": "Banking Overlay Trojans", "desc": "Draws fake fake translucent login screens over legitimate banking apps to capture customer credentials (e.g. Alien, Cerberus)." },
                        { "name": "SMS Interceptor / Toll Fraud", "desc": "Subscribes the victim device to premium SMS services or intercepts banking OTPs (e.g. Joker malware)." },
                        { "name": "Advanced Mobile Spyware", "desc": "Zero-click exploits activating microphone, camera, and GPS silently (e.g. Pegasus spyware)." },
                        { "name": "Mobile Ransomware", "desc": "Locks the device screen or encrypts external SD cards, demanding crypto ransom." }
                    ],
                    "rootingRisks": [
                        { "risk": "Destruction of OS Sandbox", "detail": "Mobile OS sandboxing prevents App A from accessing App B's memory. Rooting completely dismantles this security barrier." },
                        { "risk": "Root Privilege Escalation", "detail": "Any malicious sideloaded app can obtain superuser (SU) privileges, reading internal database files and keychains." },
                        { "risk": "Disabled Integrity Checks", "detail": "SafetyNet / Play Integrity API fails, preventing secure enterprise MDM and banking apps from functioning." },
                        { "risk": "Blocked OTA Updates", "detail": "Rooted devices often fail automatic security patch installations, remaining permanently vulnerable." }
                    ]
                },
                {
                    "id": "u3-t3",
                    "unitId": 3,
                    "title": "Credit Card Frauds, Payment Security & SIM Swap Fraud",
                    "tag": "Payment Security",
                    "summary": "Techniques used to compromise digital payments, skimming, Card Not Present (CNP) fraud, and the complete mechanics of SIM Swap attacks.",
                    "frauds": [
                        { "type": "Physical Card Skimming", "detail": "Installing magnetic stripe reader overlays and pinhole cameras on ATM / POS terminals to clone cards." },
                        { "type": "Card-Not-Present (CNP) Fraud", "detail": "Using stolen card numbers, CVVs, and expiry dates on e-commerce portals without possessing the physical card." },
                        { "type": "Point-of-Sale (POS) RAM Scraping", "detail": "Injecting memory-scraping malware into retail POS terminals to intercept unencrypted card track data in RAM." },
                        { "type": "SIM Swap Fraud", "detail": "Socially engineering the telecom provider into porting the victim's mobile number onto an attacker's blank SIM card." }
                    ],
                    "simSwapLifecycle": [
                        "1. Target Profiling: Attacker gathers victim's personal data (Name, DOB, ID number) via phishing or leaks.",
                        "2. Telecom Social Engineering: Attacker visits telecom store claiming lost phone with forged identity ID.",
                        "3. SIM Reissuance: Telecom issues a new replacement SIM linked to victim's phone number.",
                        "4. Service Termination: Victim's real SIM card immediately loses network connectivity ('No Service').",
                        "5. OTP Interception: Attacker initiates bank password resets, receiving all 2FA OTP codes on the new SIM.",
                        "6. Account Draining: Funds are instantly transferred to burner crypto wallets or mule accounts."
                    ],
                    "prevention": [
                        "Use Authenticator Apps (TOTP) or hardware security keys (FIDO2) instead of insecure SMS-based 2FA.",
                        "Enable carrier SIM lock PINs to prevent unauthorized number porting.",
                        "Banks implementing tokenization (Virtual Cards) and continuous behavioral fraud scoring."
                    ]
                },
                {
                    "id": "u3-t4",
                    "unitId": 3,
                    "title": "Registry & Mobile OS Security Configurations",
                    "tag": "OS Hardening",
                    "summary": "Essential security parameters and registry configurations for hardening Android and iOS mobile operating systems.",
                    "settings": [
                        { "setting": "Screen Lock & Biometrics", "action": "Enforce strong alphanumeric PIN (>=6 digits) or biometrics with automatic lock after 1-2 minutes of inactivity." },
                        { "setting": "Device Storage Encryption", "action": "Enable Full-Disk Encryption (FDE) or File-Based Encryption (FBE) backed by hardware secure enclave (TPM / Knox)." },
                        { "setting": "Application Permissions", "action": "Audit and restrict background permissions for Camera, Microphone, Exact Location, and SMS access." },
                        { "setting": "Unknown Sources & Sideloading", "action": "Ensure 'Install Unknown Apps' is strictly disabled for all web browsers and messaging applications." },
                        { "setting": "Developer Options & USB Debugging", "action": "Keep USB Debugging disabled to prevent unauthorized ADB shell access when connecting to charging stations." },
                        { "setting": "Remote Lock & Wipe Capability", "action": "Enable Google 'Find My Device' or Apple 'Find My' with remote enterprise MDM wipe capability." }
                    ]
                },
                {
                    "id": "u3-t5",
                    "unitId": 3,
                    "title": "Authentication Service Security & The 5 Factors",
                    "tag": "Authentication",
                    "summary": "The 5 distinct authentication factor categories used to verify digital identity securely.",
                    "factors": [
                        { "factor": "1. Something You Know (Knowledge)", "desc": "Static passwords, PIN codes, passphrases, security answer questions.", "weakness": "Vulnerable to phishing, brute-force, dictionary attacks, and credential reuse." },
                        { "factor": "2. Something You Have (Possession)", "desc": "Hardware security keys (YubiKey), smart cards, software TOTP tokens (Google Authenticator), SMS OTP.", "weakness": "Physical theft or SIM swap interception." },
                        { "factor": "3. Something You Are (Inherence)", "desc": "Biological traits: Fingerprint, Face ID, Iris scan, Retina scan, Voice recognition.", "weakness": "Cannot be changed if compromised; spoofing via high-res molds or deepfakes." },
                        { "factor": "4. Somewhere You Are (Location)", "desc": "GPS coordinates, authorized enterprise subnet IP ranges, cellular cell tower bounds.", "weakness": "GPS spoofing apps, VPN proxy obfuscation." },
                        { "factor": "5. Something You Do (Behavior)", "desc": "Keystroke typing dynamics, touchscreen swipe velocity, mouse trajectory patterns.", "weakness": "Requires continuous machine learning baselining." }
                    ],
                    "keyTakeaways": [
                        "True Multi-Factor Authentication (MFA) requires factors from AT LEAST TWO DIFFERENT categories (e.g. Password + Fingerprint).",
                        "Using a password + security question is only Single-Factor Authentication (two knowledge factors)."
                    ]
                },
                {
                    "id": "u3-t6",
                    "unitId": 3,
                    "title": "Wireless Network Attacks (Evil Twin, MITM, Sniffing)",
                    "tag": "Wireless Attacks",
                    "summary": "Mechanisms of Wi-Fi exploitation: Evil Twin rogue access points, ARP poisoning, SSL stripping, and packet sniffing.",
                    "attacks": [
                        {
                            "name": "1. Evil Twin & Rogue Access Point",
                            "mechanism": "Attacker sets up a rogue Wi-Fi hotspot broadcasting the exact same SSID name as a legitimate network (e.g. 'Airport_Free_WiFi') with higher signal power.",
                            "consequence": "Victim devices auto-associate with the rogue AP; attacker intercepts all plaintext traffic and serves credential harvesting captive portals."
                        },
                        {
                            "name": "2. Man-in-the-Middle (MITM) & ARP Poisoning",
                            "mechanism": "Attacker transmits forged ARP replies across the local subnet, binding the default gateway's IP to the attacker's MAC address.",
                            "consequence": "All outbound victim packets route through the attacker's machine before reaching the Internet."
                        },
                        {
                            "name": "3. Wi-Fi Packet Sniffing",
                            "mechanism": "Placing wireless NIC in Promiscuous / Monitor mode using tools like Wireshark or Aircrack-ng.",
                            "consequence": "Capturing unencrypted 802.11 frames, cleartext HTTP credentials, and DNS queries."
                        },
                        {
                            "name": "4. KRACK (Key Reinstallation Attack)",
                            "mechanism": "Exploiting a 4-way handshake cryptographic flaw in WPA2 Wi-Fi protocol to reinstall an all-zero encryption key.",
                            "consequence": "Allows decryption of WPA2 traffic without needing the Wi-Fi pre-shared key."
                        }
                    ],
                    "diagram":
"""+-------------------------------------------------------------+
|               EVIL TWIN / ROGUE AP ATTACK FLOW               |
+-------------------------------------------------------------+
|  [ Legitimate Wi-Fi ] (SSID: "CoffeeShop_WiFi")             |
|                                                             |
|  [ Attacker Rogue AP ] (SSID: "CoffeeShop_WiFi" - Stronger) |
|         ^                                                   |
|         | (Auto-Connects)                                   |
|   [ Victim Phone ] ===== Cleartext Traffic =====> [ Attacker]|
|                                                          |   |
|   [ Real Internet ] <====================================+   |
|   (Attacker intercepts passwords, cookies, and tokens!)      |
+-------------------------------------------------------------+"""
                },
                {
                    "id": "u3-t7",
                    "unitId": 3,
                    "title": "Bluetooth Security Attacks (Bluejacking, Bluesnarfing, Bluebugging)",
                    "tag": "Bluetooth Security",
                    "summary": "Comparing the triad of Bluetooth exploits by severity, exploitation mechanism, and impact.",
                    "bluetoothAttacks": [
                        {
                            "name": "1. Bluejacking",
                            "severity": "Low (Harassment)",
                            "mechanism": "Sending unsolicited electronic business cards (vCards) or text messages to discoverable Bluetooth devices within a 10-meter range.",
                            "impact": "Annoyance and spam; does NOT access device memory or steal personal data."
                        },
                        {
                            "name": "2. Bluesnarfing",
                            "severity": "Medium-High (Data Theft)",
                            "mechanism": "Exploiting flaws in Bluetooth OBEX (Object Exchange) protocol to gain unauthorized access to device data without pairing consent.",
                            "impact": "Theft of contacts, phone logs, calendar appointments, SMS messages, and photos."
                        },
                        {
                            "name": "3. Bluebugging",
                            "severity": "Critical (Full Remote Control)",
                            "mechanism": "Exploiting legacy Bluetooth firmware vulnerabilities to create an unprompted RFCOMM serial port channel.",
                            "impact": "Total device takeover: eavesdropping on phone calls, making outbound premium calls, sending SMS, and accessing internet data."
                        }
                    ],
                    "comparisonTable": [
                        { "criteria": "Objective", "bluejacking": "Send Spam Messages", "bluesnarfing": "Steal Stored Data", "bluebugging": "Full Remote Control" },
                        { "criteria": "Data Access", "bluejacking": "None", "bluesnarfing": "Read Contacts/SMS/Files", "bluebugging": "Full Read/Write & Audio Tap" },
                        { "criteria": "Pairing Required?", "bluejacking": "No", "bluesnarfing": "Bypasses Pairing", "bluesnarfing": "Bypasses Pairing" },
                        { "criteria": "Threat Level", "bluejacking": "Nuisance", "bluesnarfing": "Confidentiality Breach", "bluebugging": "Complete System Hijack" }
                    ],
                    "prevention": [
                        "Keep Bluetooth in 'Non-Discoverable' (Hidden) mode or turn off when not in active use.",
                        "Never accept pairing requests from unknown nearby devices in public places.",
                        "Keep device OS and Bluetooth firmware updated to patch OBEX and RFCOMM stack flaws."
                    ]
                },
                {
                    "id": "u3-t8",
                    "unitId": 3,
                    "title": "Organizational Mobile Security: MDM, MAM & BYOD Policies",
                    "tag": "Enterprise Security",
                    "summary": "Enterprise management frameworks to secure mobile endpoints: Mobile Device Management (MDM), containerization, and BYOD policy guidelines.",
                    "mdmFeatures": [
                        { "feature": "1. Device Containerization", "desc": "Separating personal apps/data from encrypted corporate workspaces on the same device." },
                        { "feature": "2. Enforced Security Baselines", "desc": "Mandating minimum OS versions, strong PIN complexity, and blocking rooted/jailbroken devices." },
                        { "feature": "3. Remote Selective Wipe", "desc": "Instantly deleting corporate emails and work files upon employee resignation or device loss without wiping personal photos." },
                        { "feature": "4. Enterprise Wi-Fi & VPN", "desc": "Pushing WPA3-Enterprise 802.1X certificates and always-on split-tunnel VPN profiles to mobile devices." }
                    ],
                    "byodPolicyRules": [
                        "Written acceptable use policy defining monitoring rights.",
                        "Mandatory MDM agent enrollment prior to accessing internal corporate networks.",
                        "Explicit prohibition of unauthorized third-party cloud storage and sideloaded apps.",
                        "Immediate obligation to report lost or compromised devices within 1 hour."
                    ]
                }
            ]
        },
        {
            "id": 4,
            "code": "UNIT-04",
            "title": "Tools Used in Cybercrime & Advanced Malware",
            "badge": "Tools & Malware",
            "weightage": "25-30 Marks",
            "estimatedTime": "6-7 Hours",
            "overview": "Comprehensive technical study of cybercrime tooling: 6 Proxy Server classifications, Tor Onion Routing architecture, dark web law enforcement takedowns (Operation Bayonet), advanced phishing evasion, password cracking methods and hashing algorithms (Bcrypt, Argon2, Salt/Pepper), keyloggers, 5-stage virus/worm anatomy, Trojans, Backdoors, and DDoS attack vectors with scrubbing mitigation.",
            "topics": [
                {
                    "id": "u4-t1",
                    "unitId": 4,
                    "title": "Proxy Servers: Working & 6 Classifications",
                    "tag": "Proxy Architecture",
                    "summary": "An intermediary server that receives client requests and forwards them to destination servers, acting as a gateway for caching, filtering, or IP obfuscation.",
                    "types": [
                        {
                            "name": "1. Forward Proxy",
                            "desc": "Positioned between internal clients and the external Internet. Intercepts outbound client requests, evaluating firewall rules, caching web pages, and masking internal client IP addresses."
                        },
                        {
                            "name": "2. Reverse Proxy",
                            "desc": "Positioned in front of internal web servers. Receives incoming public Internet traffic and distributes it across backend server clusters (load balancing, SSL termination, DDoS protection)."
                        },
                        {
                            "name": "3. Transparent Proxy",
                            "desc": "Intercepts client requests without modifying request headers or masking the client IP address. Clients are unaware of its presence (commonly used in corporate content filtering and school networks)."
                        },
                        {
                            "name": "4. Anonymous Proxy",
                            "desc": "Hides the client's true IP address from the destination web server, but sends headers (e.g. HTTP_VIA) identifying itself as a proxy."
                        },
                        {
                            "name": "5. High-Anonymity (Elite) Proxy",
                            "desc": "Completely hides the client's real IP address AND removes all proxy-identifying headers. The destination server cannot distinguish it from a regular standalone client."
                        },
                        {
                            "name": "6. Open / Public Proxy",
                            "desc": "Misconfigured or intentionally exposed public proxies accessible to any Internet user. Frequently abused by cybercriminals to launch anonymous attacks."
                        }
                    ],
                    "diagram":
"""+-------------------------------------------------------------+
|              FORWARD PROXY VS REVERSE PROXY                 |
+-------------------------------------------------------------+
|  FORWARD PROXY (Protects/Hides Clients):                    |
|  [ Client 1 ] \                                             |
|  [ Client 2 ] ---> [ FORWARD PROXY ] ====> [ Public Web ]   |
|  [ Client 3 ] /                                             |
|                                                             |
|  REVERSE PROXY (Protects/Balances Servers):                 |
|                                        /--> [ Web Server 1 ]|
|  [ Public Internet ] ===> [ REVERSE ] ----> [ Web Server 2 ]|
|                            [ PROXY ]   \--> [ Web Server 3 ]|
+-------------------------------------------------------------+""",
                    "keyTakeaways": [
                        "Forward proxy hides the CLIENT; Reverse proxy hides and protects the SERVERS.",
                        "Elite proxies do not append 'X-Forwarded-For' headers, making attribution difficult."
                    ]
                },
                {
                    "id": "u4-t2",
                    "unitId": 4,
                    "title": "Proxy-Based Cybercrime, Detection & Mitigation",
                    "tag": "Proxy Security",
                    "summary": "How attackers chain proxies into bulletproof multi-hop tunnels to evade geolocation bans, and technical defense countermeasures.",
                    "abuseMethods": [
                        { "method": "Proxy Chaining", "detail": "Routing malicious traffic through a sequence of 5-10 global open proxies in different legal jurisdictions to defeat log tracing." },
                        { "method": "Residential Proxy Networks", "detail": "Routing attacks through infected residential IoT/home connections, making malicious requests appear from legitimate residential ISPs." }
                    ],
                    "detectionMitigation": [
                        { "technique": "IP Threat Intelligence Feeds", "detail": "Real-time blocklists matching known open proxies, TOR exit nodes, and commercial VPN egress IPs." },
                        { "technique": "Header & Packet Inspection", "detail": "Inspecting 'X-Forwarded-For', 'Via', TCP window size, and MTU anomalies." },
                        { "technique": "Behavioral Anomaly Scoring", "detail": "Flagging accounts logging in from two distant geographic continents within a 10-minute window (Impossible Travel)." }
                    ]
                },
                {
                    "id": "u4-t3",
                    "unitId": 4,
                    "title": "Anonymizers & The Tor Network Architecture",
                    "tag": "Tor & Anonymity",
                    "summary": "Technical operation of Onion Routing: multi-layered cryptographic encapsulation through Guard, Middle, and Exit nodes.",
                    "onionRoutingPrinciples": [
                        { "node": "1. Client Construction", "desc": "Tor client fetches network consensus and negotiates Diffie-Hellman cryptographic session keys with 3 distinct Tor relays." },
                        { "node": "2. Layered Encryption", "desc": "Client encrypts the packet 3 times in reverse order: Layer 3 (Exit Node key), Layer 2 (Middle Relay key), Layer 1 (Guard Node key)." },
                        { "node": "3. Entry / Guard Node", "desc": "Peels Layer 1 encryption. Knows the Client's REAL IP address, but only sees the Middle Node's IP. CANNOT see packet contents or final destination." },
                        { "node": "4. Middle Relay Node", "desc": "Peels Layer 2 encryption. Knows Guard Node IP and Exit Node IP. Knows NEITHER client IP nor final destination." },
                        { "node": "5. Exit Node", "desc": "Peels Layer 3 encryption. Transmits plaintext request to destination server. Knows final destination, but has ZERO knowledge of client IP." }
                    ],
                    "diagram":
"""+--------------------------------------------------------------------------+
|                  TOR ONION ROUTING ARCHITECTURE                          |
+--------------------------------------------------------------------------+
|  [ Client ]                                                              |
|     | (3-Layer Encrypted Packet: [E3 [E2 [E1 Payload]]])                 |
|     v                                                                    |
|  [ ENTRY / GUARD NODE ]   ==> Peels Layer 1 (Knows Client IP, not Dest)   |
|     | (2-Layer Encrypted Packet: [E3 [E2 Payload]])                      |
|     v                                                                    |
|  [ MIDDLE RELAY NODE ]    ==> Peels Layer 2 (Knows Guard & Exit only)     |
|     | (1-Layer Encrypted Packet: [E3 Payload])                           |
|     v                                                                    |
|  [ EXIT NODE ]            ==> Peels Layer 3 (Knows Destination, not Client)|
|     | (Plaintext/TLS)                                                    |
|     v                                                                    |
|  [ Destination Web Server ]                                              |
+--------------------------------------------------------------------------+""",
                    "keyTakeaways": [
                        "No single Tor node possesses both the source IP and destination IP.",
                        "Exit node traffic is unencrypted unless the client uses end-to-end HTTPS/TLS.",
                        "Hidden Services (.onion) use rendezvous points where both client and server maintain anonymity."
                    ]
                },
                {
                    "id": "u4-t4",
                    "unitId": 4,
                    "title": "Dark Web Case Study: Operation Bayonet & AlphaBay / Hansa Takedown",
                    "tag": "Case Studies",
                    "summary": "Masterclass in international cyber law enforcement coordination targeting darknet marketplaces.",
                    "caseStudy": {
                        "operation": "Operation Bayonet (FBI, DEA, Dutch National Police, Europol - 2017)",
                        "phase1": "AlphaBay Seizure: US law enforcement seized AlphaBay infrastructure in Lithuania and arrested creator Alexandre Cazes in Thailand.",
                        "phase2": "The Honeypot Trap: Anticipating users would flee to the 2nd largest marketplace ('Hansa Market'), Dutch Police secretly seized Hansa servers weeks in advance.",
                        "phase3": "Covert Operation: Dutch Police ran Hansa Market as a honeypot for 27 days, modifying source code to log unencrypted PGP communications, vendor Bitcoin wallets, and delivery delivery physical addresses.",
                        "outcome": "Massive global arrest wave of top darknet narcotics and weapon vendors across 3 continents.",
                        "keyLessons": [
                            "Operational Security (OPSEC) failures (creator used personal Hotmail email in site headers) reveal anonymous operators.",
                            "International police cooperation and joint infrastructure seizure break dark web anonymity."
                        ]
                    }
                },
                {
                    "id": "u4-t5",
                    "unitId": 4,
                    "title": "Phishing Ecosystem: Lifecycle & Advanced Evasion Techniques",
                    "tag": "Phishing Analysis",
                    "summary": "End-to-end phishing lifecycle, attack classifications, and sophisticated evasion mechanisms.",
                    "phishingTypes": [
                        { "name": "Email Phishing", "desc": "Broad mass-blasting generic lures (e.g. 'Your Bank Statement is Ready')." },
                        { "name": "Spear Phishing", "desc": "Highly tailored attack targeting specific individuals with customized background info." },
                        { "name": "Whaling", "desc": "Spear-phishing targeting C-level executives (CEO, CFO) for major financial approvals." },
                        { "name": "Smishing & Vishing", "desc": "Phishing via SMS text messages (Smishing) or voice phone calls (Vishing)." },
                        { "name": "Clone Phishing", "desc": "Intercepting legitimate email, copying exact content, replacing real attachment/link with malware." }
                    ],
                    "advancedEvasion": [
                        { "technique": "Typosquatting & Look-alike Domains", "desc": "Registering visually identical domains (e.g. `paypa1.com`, `arnazon.com`)." },
                        { "technique": "IDN Homograph Attack (Punycode)", "desc": "Using Cyrillic characters that look identical to Latin letters (`apple.com` rendered via `xn--...`)." },
                        { "technique": "Reverse Proxy Phishing (Evilginx)", "desc": "Acting as a real-time proxy to intercept Session Cookies, completely bypassing SMS/TOTP 2-Factor Authentication!" },
                        { "technique": "Quishing (QR Code Phishing)", "desc": "Embedding malicious URLs inside QR codes in emails, bypassing traditional email text scanners." }
                    ]
                },
                {
                    "id": "u4-t6",
                    "unitId": 4,
                    "title": "Password Cracking Methodologies & Auditing Tools",
                    "tag": "Password Cracking",
                    "summary": "Technical methodologies used to recover plaintext passwords from cryptographic hashes.",
                    "methods": [
                        { "name": "1. Brute Force Attack", "desc": "Exhaustively attempting every possible permutation of characters. Complexity: O(C^L). Guaranteed to succeed given infinite time.", "countermeasure": "Account lockout thresholds and long passphrases." },
                        { "name": "2. Dictionary Attack", "desc": "Testing hundreds of thousands of predefined words from wordlists (e.g. `rockyou.txt`) and leaked password databases.", "countermeasure": "Prohibiting common dictionary words." },
                        { "name": "3. Hybrid & Rule-Based Attack", "desc": "Applying linguistic transformation rules to dictionary words (e.g. `Password` -> `P@ssw0rd2024!`, leetspeak substitution).", "countermeasure": "Enforcing true entropy over simple substitution." },
                        { "name": "4. Credential Stuffing", "desc": "Automated replay of breached username/password combos across hundreds of other unrelated web portals.", "countermeasure": "Multi-Factor Authentication (MFA) and CAPTCHA." },
                        { "name": "5. Password Spraying", "desc": "Attempting 1 or 2 common passwords (e.g. `Winter2024!`) against thousands of user accounts to avoid account lockout triggers.", "countermeasure": "Enterprise password anomaly detection." },
                        { "name": "6. Rainbow Tables", "desc": "Precomputed tables of cryptographic hash chains using reduction functions, trading massive pre-computation storage for near-instant hash lookups.", "countermeasure": "Cryptographic Salts!" }
                    ],
                    "tools": ["John the Ripper (CPU/GPU multi-hash cracker)", "Hashcat (World fastest GPU-accelerated rule engine)", "Hydra (Fast online network login cracker)"]
                },
                {
                    "id": "u4-t7",
                    "unitId": 4,
                    "title": "Password Hashing Cryptography, Salt, Pepper & Algorithms",
                    "tag": "Cryptography & Hashing",
                    "summary": "Evaluation of cryptographic hash functions, the vital role of Salt & Pepper, and why modern systems use adaptive key-stretching functions.",
                    "saltAndPepper": {
                        "salt": "A unique, random cryptographic string generated for each user and appended to the password BEFORE hashing: Hash(Password + Salt). Stored alongside hash in database. COMPLETELY DEFEATS RAINBOW TABLES because attackers must compute a unique table for every single user!",
                        "pepper": "A high-entropy secret key added to password before hashing, stored in an external Hardware Security Module (HSM) or separate configuration server OUTSIDE the main database."
                    },
                    "hashComparison": [
                        { "algo": "MD5 (128-bit)", "status": "BROKEN", "gpuRate": "Billions/sec", "verdict": "Vulnerable to collisions and instant GPU cracking. NEVER use for passwords." },
                        { "algo": "SHA-1 (160-bit)", "status": "DEPRECATED", "gpuRate": "Hundreds of millions/sec", "verdict": "Cryptographically broken (SHAttered attack). Do not use." },
                        { "algo": "SHA-256 (256-bit)", "status": "INTEGRITY ONLY", "gpuRate": "Millions/sec", "verdict": "Fast hash function designed for data integrity, NOT passwords unless paired with high salt and thousands of rounds." },
                        { "algo": "Bcrypt (Blowfish)", "status": "RECOMMENDED", "gpuRate": "Very Slow (Configurable)", "verdict": "Adaptive work factor (cost parameter) forces CPU to slow down cracking." },
                        { "algo": "Argon2 (Argon2id)", "status": "GOLD STANDARD", "gpuRate": "Extremely Expensive", "verdict": "Winner of Password Hashing Competition. Memory-hard and time-hard; renders GPU and ASIC hardware crackers ineffective!" }
                    ]
                },
                {
                    "id": "u4-t8",
                    "unitId": 4,
                    "title": "Keyloggers & Spyware: Architecture & Detection",
                    "tag": "Keyloggers & Spyware",
                    "summary": "Technical classifications of hardware vs software keyloggers and spyware detection mechanisms.",
                    "keyloggerTypes": [
                        { "type": "Software Keyloggers", "desc": "Windows API hooks (e.g. `SetWindowsHookEx(WH_KEYBOARD_LL)`), memory injection, or malicious browser extensions capturing DOM input." },
                        { "type": "Hardware Keyloggers", "desc": "Physical hardware inline dongles connected between keyboard USB cable and motherboard port. Completely undetectable by software antivirus!" },
                        { "type": "Kernel / Rootkit Keyloggers", "desc": "Kernel-mode device drivers intercepting raw keystrokes directly from keyboard controller IRQ before OS processing." }
                    ],
                    "detection": [
                        "Virtual on-screen randomized soft-keyboards (defeats basic hardware/software keyloggers).",
                        "Behavioral Endpoint Detection and Response (EDR) detecting anomalous API hook installations.",
                        "Physical port audits to check for inline USB interceptor dongles."
                    ]
                },
                {
                    "id": "u4-t9",
                    "unitId": 4,
                    "title": "Viruses vs Worms: Deep Dissection & 5-Stage Anatomy",
                    "tag": "Malware Anatomy",
                    "summary": "Definitive comparison between Viruses and Worms, and the modular 5-stage architectural anatomy of self-propagating malware.",
                    "virusVsWorm": [
                        { "feature": "Host Dependency", "virus": "Dependent on a Host File (Appends code to .exe, .dll, docs)", "worm": "Standalone Autonomous Executable" },
                        { "feature": "Human Interaction", "virus": "Requires human execution (user clicks infected file)", "worm": "Zero human interaction required (self-propagates via network)" },
                        { "feature": "Propagation Speed", "virus": "Moderate (spreads as users share files)", "worm": "Exponential / Rapid (scans and infects entire subnets in seconds)" },
                        { "feature": "Historical Example", "virus": "CIH / Chernobyl, Melissa Virus", "worm": "Morris Worm, Slammer, Conficker, WannaCry" }
                    ],
                    "fiveStageAnatomy": [
                        { "component": "1. Replication Mechanism", "desc": "The code routine responsible for finding uninfected files or memory spaces and injecting malware replicas." },
                        { "component": "2. Propagation Mechanism", "desc": "The routine scanning local subnets, generating IP addresses, or blasting emails to distribute copies across networks." },
                        { "component": "3. Trigger Mechanism (Logic Bomb)", "desc": "The conditional logic (time/date, system event, user action) that determines when the harmful payload is unleashed." },
                        { "component": "4. Payload", "desc": "The destructive or monetizing action: data wiping, file encryption (ransomware), keylogging, or establishing reverse shells." },
                        { "component": "5. Concealment (Armoring)", "desc": "Polymorphic/Metamorphic engines, packing, rootkit hooks, and anti-debugging routines that evade antivirus signatures." }
                    ],
                    "diagram":
"""+-------------------------------------------------------------+
|                 MODULAR ANATOMY OF A VIRUS / WORM           |
+-------------------------------------------------------------+
|  +-------------------------------------------------------+  |
|  | 1. REPLICATION ENGINE  (Injects code into host/memory)|  |
|  +-------------------------------------------------------+  |
|  | 2. PROPAGATION ENGINE  (Scans network IPs / Exploits) |  |
|  +-------------------------------------------------------+  |
|  | 3. TRIGGER MECHANISM   (Date, Event, Time Bomb logic) |  |
|  +-------------------------------------------------------+  |
|  | 4. PAYLOAD             (Encrypts Data / Deletes Files)|  |
|  +-------------------------------------------------------+  |
|  | 5. CONCEALMENT ENGINE  (Polymorphism / Rootkit Cloak) |  |
|  +-------------------------------------------------------+  |
+-------------------------------------------------------------+"""
                },
                {
                    "id": "u4-t10",
                    "unitId": 4,
                    "title": "Trojans, RATs & Backdoors",
                    "tag": "Trojans & Backdoors",
                    "summary": "Disguised malicious payloads, Remote Access Trojans (RATs), and persistence backdoors.",
                    "trojanTypes": [
                        { "type": "Remote Access Trojan (RAT)", "desc": "Provides total interactive graphical/command-line control over victim PC (e.g. DarkComet, njRAT)." },
                        { "type": "Banking Trojan", "desc": "Monitors browser sessions to inject fake login forms and steal banking credentials (e.g. Zeus, Emotet)." },
                        { "type": "Downloader / Dropper Trojan", "desc": "Stealthy initial payload whose sole mission is to evade antivirus and download heavy secondary ransomware payloads." }
                    ],
                    "backdoorMechanisms": [
                        { "mech": "Registry Autorun Keys", "desc": "Persisting in `HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run`." },
                        { "mech": "Scheduled Tasks & Services", "desc": "Creating background services running as `NT AUTHORITY\\SYSTEM`." },
                        { "mech": "DLL Side-Loading", "desc": "Placing malicious DLL in app folder matching legitimate Windows executable dependency." }
                    ]
                },
                {
                    "id": "u4-t11",
                    "unitId": 4,
                    "title": "DoS & DDoS Attacks: Vectors, Scrubbing & Mitigation",
                    "tag": "DDoS Attacks",
                    "summary": "Volumetric, Protocol, and Application-layer Denial of Service attacks and modern cloud scrubbing defense architectures.",
                    "ddosCategories": [
                        {
                            "category": "1. Volumetric Attacks (Layer 3/4)",
                            "metric": "Measured in Gigabits / Terabits Per Second (Gbps / Tbps)",
                            "methods": "UDP Flood, ICMP Flood, DNS Amplification (exploiting open recursive DNS resolvers with spoofed victim IP to amplify traffic 50x), NTP Amplification.",
                            "goal": "Completely saturate the victim's Internet bandwidth pipe."
                        },
                        {
                            "category": "2. Protocol / Network Attacks (Layer 3/4)",
                            "metric": "Measured in Packets Per Second (PPS)",
                            "methods": "SYN Flood (transmitting thousands of TCP SYN packets without finishing 3-way handshake, exhausting server connection state table), Ping of Death, Smurf Attack.",
                            "goal": "Exhaust memory resources of intermediate routers, firewalls, and load balancers."
                        },
                        {
                            "category": "3. Application Layer Attacks (Layer 7)",
                            "metric": "Measured in Requests Per Second (RPS)",
                            "methods": "HTTP Flood, Slowloris (opening hundreds of HTTP connections and sending incomplete headers byte-by-byte very slowly to tie up web server threads), HTTPS POST floods.",
                            "goal": "Crash database backend or web server application CPU/RAM while using minimal attacker bandwidth."
                        }
                    ],
                    "mitigationStrategies": [
                        { "name": "BGP Anycast Routing", "desc": "Advertising the same IP address from hundreds of global points of presence (PoPs) to disperse volumetric attack traffic worldwide." },
                        { "name": "Cloud Scrubbing Centers", "desc": "High-capacity scrubbing centers (Cloudflare, Akamai) analyzing incoming traffic, discarding malicious packets, and forwarding clean traffic." },
                        { "name": "SYN Cookies", "desc": "Server encodes connection parameters into TCP sequence number without allocating kernel state table memory until client returns ACK." },
                        { "name": "Rate Limiting & CAPTCHA", "desc": "Challenging anomalous Layer 7 HTTP request spikes with managed JavaScript / CAPTCHA puzzles." }
                    ]
                }
            ]
        }
    ],
    "examQuestions": [
        {
            "id": "eq-01",
            "unit": 1,
            "marks": "10-15 Marks",
            "question": "Define Cyber Crime. Explain the historical origins and evolution of cyber crime, and describe the three distinct roles played by computers in cyber offenses with concrete examples.",
            "markingScheme": [
                "Definition of Cyber Crime: 2 Marks",
                "Historical Evolution & Eras (1960s to Present): 4 Marks",
                "Three Roles of a Computer (Target, Tool, Storage): 4 Marks",
                "Architecture/Diagram representation: 2 Marks",
                "Examples and Conclusion: 2 Marks"
            ],
            "modelAnswer": {
                "introduction": "Cyber crime is defined as any unlawful activity in which a computer, digital device, communication network, or the Internet is utilized as a tool, a target, or a storage medium for committing a crime. With the comprehensive digitalization of society, cyber crimes have grown from minor technical pranks into multi-billion dollar transnational criminal enterprises.",
                "diagram": 
"""+-------------------------------------------------------------+
|               ROLES OF A COMPUTER IN CYBERCRIME             |
+-------------------------------------------------------------+
|   1. AS A TARGET  : Server Hacking, DDoS, Ransomware        |
|   2. AS A TOOL    : Phishing, Banking Fraud, Cyberstalking  |
|   3. AS A STORAGE : Stolen Databases, Pirated IP, Card Dumps|
+-------------------------------------------------------------+""",
                "historicalEras": [
                    "1. Early Mainframe Era (1960s-1970s): Physical unauthorized access, disgruntled operator sabotage.",
                    "2. Phone Phreaking Era (1970s-1980s): Manipulating telephone switching frequencies (2600 Hz) using Blue Boxes to obtain free long-distance calls.",
                    "3. Virus & Worm Dawn (1980s-1990s): Floppy boot viruses (Brain 1986) and first ARPANET network worm (Morris Worm 1988).",
                    "4. Web Expansion Era (1990s-2000s): Web defacements, email worms (ILOVEYOU), early banking fraud.",
                    "5. Modern Organized Crime (2010s-Present): Ransomware-as-a-Service, APTs, IoT botnets, crypto extortion, AI deepfakes."
                ],
                "threeRolesDetailed": [
                    "Computer as Target: The system itself is attacked. Focus is on disrupting CIA (Confidentiality, Integrity, Availability). Example: WannaCry ransomware encrypting server files.",
                    "Computer as Tool: The system is an instrument to victimize individuals or enterprises. Example: Sending spear-phishing emails or credit card identity scams.",
                    "Computer as Storage / Repository: Digital hardware stores stolen data, credentials, encryption keys, or illicit records. Example: Storing stolen customer databases."
                ],
                "conclusion": "Understanding the triple role of computers enables cyber security professionals to formulate comprehensive defense strategies across endpoint hardening, network monitoring, and digital forensics."
            }
        },
        {
            "id": "eq-02",
            "unit": 1,
            "marks": "10-15 Marks",
            "question": "Explain the 4-Pillar Classification of Cyber Crime in detail with relevant examples. Discuss why cyber crime transcends national boundaries and the challenges in international law enforcement.",
            "markingScheme": [
                "4-Pillar Classification (Individual, Property, Government, Society): 6 Marks",
                "Transnational Nature & Jurisdictional Challenges: 4 Marks",
                "International Treaties (Budapest Convention, MLAT): 3 Marks",
                "Diagram and Structure: 2 Marks"
            ],
            "modelAnswer": {
                "introduction": "Cyber crime is broadly classified based on the nature of the target or victim into four distinct pillars: Against Individuals, Against Property, Against Government, and Against Society.",
                "diagram":
"""+-------------------------------------------------------------------------+
|                  4-PILLAR CYBERCRIME TAXONOMY                           |
+-------------------------------------------------------------------------+
| [1. Individuals]  : Identity Theft, Cyberstalking, Phishing, Harassment  |
| [2. Property]     : Data/IP Theft, Ransomware, Unauthorized Bank Transfer|
| [3. Government]   : Cyber Warfare, SCADA Grid Attacks, Cyber Terrorism   |
| [4. Society]      : Misinformation, CSAM, Illegal Gambling, Ponzi Scams  |
+-------------------------------------------------------------------------+""",
                "pillars": [
                    "1. Cyber Crime Against Individuals: Inflicts personal harm, harassment, or financial loss on specific persons. Examples: Identity theft, cyberbullying, cyberstalking, revenge pornography.",
                    "2. Cyber Crime Against Property: Targets tangible and intangible digital assets, intellectual property, and funds. Examples: Ransomware extortion, corporate IP exfiltration, website defacement, credit card theft.",
                    "3. Cyber Crime Against Government: Attacks sovereign infrastructure, defense networks, and state operations. Examples: Cyber espionage, SCADA electrical grid sabotage, cyber warfare.",
                    "4. Cyber Crime Against Society: Compromises public order, communal peace, and community welfare. Examples: Viral fake news/disinformation, financial ponzi schemes, illegal darknet trafficking."
                ],
                "transnationalHurdles": [
                    "Jurisdictional Limits: Criminal resides in Country A, routes through Country B, attacks Country C. No single national law applies automatically.",
                    "Extradition Deficits: Countries lacking bilateral treaties refuse to extradite sovereign citizens.",
                    "Attribution & Evidence Volatility: IP spoofing and Tor routing destroy digital evidence before slow MLAT (Mutual Legal Assistance Treaty) requests process."
                ],
                "conclusion": "Combatting global cybercrime mandates global harmonization via treaties like the Budapest Convention and 24/7 law enforcement threat intelligence exchange."
            }
        },
        {
            "id": "eq-03",
            "unit": 2,
            "marks": "10-15 Marks",
            "question": "What is Social Engineering? Explain the psychological triggers manipulated by attackers. Describe the 7 major social engineering techniques and discuss the Twitter 2020 Bitcoin Compromise case study.",
            "markingScheme": [
                "Definition & Psychological Triggers: 4 Marks",
                "7 Social Engineering Techniques: 5 Marks",
                "Twitter 2020 Case Study Analysis: 3 Marks",
                "Prevention & Countermeasures: 3 Marks"
            ],
            "modelAnswer": {
                "introduction": "Social Engineering is the psychological manipulation of people into performing actions or divulging confidential information. Unlike technical software exploits, social engineering exploits human cognitive vulnerabilities.",
                "psychologicalTriggers": [
                    "Authority: Deference to perceived leaders (CEOs, police, IT administrators).",
                    "Urgency: Artificial time limits forcing rushed decisions without verification.",
                    "Fear / Intimidation: Threats of account termination or legal prosecution.",
                    "Greed / Reward: Promises of free gifts, crypto prizes, or high earnings.",
                    "Trust / Social Proof: Mimicking friends or reputable corporate brands."
                ],
                "techniques": [
                    "1. Phishing: Deceptive emails impersonating trusted institutions to harvest logins.",
                    "2. Pretexting: Fabricating an elaborate scenario (e.g. internal IT auditor) to extract credentials.",
                    "3. Baiting: Leaving infected USB drives labeled 'Executive Salaries' in target parking lots.",
                    "4. Quid Pro Quo: Offering a favor/service ('Free PC tuneup') in exchange for passwords.",
                    "5. Tailgating / Piggybacking: Physically following an authorized employee into secure premises.",
                    "6. Impersonation & BEC: Posing as the CEO to direct urgent fraudulent wire transfers.",
                    "7. Scareware: Deceptive pop-ups alerting fake virus infections to push malware downloads."
                ],
                "caseStudy": "In July 2020, hackers used phone vishing to impersonate Twitter internal IT staff, tricking support employees into entering credentials into a spoofed VPN portal. The attackers accessed the internal Admin Dashboard, hijacked 130 celebrity accounts (Elon Musk, Barack Obama, Apple), and tweeted a Bitcoin doubling scam netting ~$120,000.",
                "prevention": "Implement mandatory multi-factor authentication (FIDO2 hardware keys), regular employee phishing simulations, and strict dual-authorization controls for administrative changes."
            }
        },
        {
            "id": "eq-04",
            "unit": 2,
            "marks": "10-15 Marks",
            "question": "Explain Botnets, their architecture (Centralized vs P2P), infection lifecycle, and monetization strategies. Discuss the Mirai Botnet case study in detail.",
            "markingScheme": [
                "Botnet Definition & Components: 2 Marks",
                "Architectures (Centralized C2 vs P2P): 4 Marks",
                "Botnet Infection Lifecycle: 3 Marks",
                "Mirai Botnet Case Study & Mitigation: 4 Marks",
                "Diagrams: 2 Marks"
            ],
            "modelAnswer": {
                "introduction": "A Botnet is a network of Internet-connected devices (PCs, servers, IoT devices) infected with malicious software and controlled remotely as a group by a cybercriminal known as a 'Botmaster'.",
                "diagram":
"""+-------------------------------------------------------------+
|             CENTRALIZED VS P2P BOTNET TOPOLOGY              |
+-------------------------------------------------------------+
|  Centralized: [Botmaster] -> [C2 Server] -> [Zombies/Bots]  |
|  (Weakness: Taking down C2 server terminates the botnet)    |
|                                                             |
|  P2P: [Bot 1] <---> [Bot 2] <---> [Bot 3] (No Central C2)   |
|  (Strength: Resilient to takedown; decentralized commands)  |
+-------------------------------------------------------------+""",
                "lifecycle": [
                    "1. Infection: Exploit vulnerability or brute force default credentials.",
                    "2. Execution & Persistence: Install stealth agent and establish autorun.",
                    "3. Beaconing: Connect to C2 server and register system hardware profile.",
                    "4. Command Execution: Receive tasks (DDoS, spamming, crypto mining, proxying)."
                ],
                "miraiCaseStudy": "In 2016, the Mirai botnet infected over 600,000 IoT devices (CCTV cameras, DVRs, routers) by continuously scanning the Internet for open Telnet ports (23/2323) and testing a hardcoded list of 62 default factory username/password pairs (e.g. admin/admin, root/xc3511). Mirai unleashed a 1.2 Tbps DDoS flood against Dyn DNS, taking down Twitter, Spotify, Netflix, and GitHub.",
                "mitigation": "Enforce mandatory default password changes on IoT devices, disable insecure protocols (Telnet, UPnP), apply network segmentation, and deploy DDoS mitigation scrubbing."
            }
        },
        {
            "id": "eq-05",
            "unit": 3,
            "marks": "10-15 Marks",
            "question": "Discuss the security vulnerabilities of Mobile and Wireless Devices. Explain SIM Swap Fraud step-by-step and contrast Bluetooth security attacks (Bluejacking, Bluesnarfing, Bluebugging).",
            "markingScheme": [
                "Mobile Vulnerabilities & Inherent Risks: 3 Marks",
                "Step-by-Step SIM Swap Fraud Mechanics & Defense: 4 Marks",
                "Bluetooth Attacks Comparative Analysis: 4 Marks",
                "Diagram & Exam Presentation: 2 Marks",
                "Conclusion: 2 Marks"
            ],
            "modelAnswer": {
                "introduction": "Mobile devices possess unique security challenges due to physical portability, ubiquitous wireless connectivity, application sandboxing limitations, OS fragmentation, and their role as identity anchors for 2-factor authentication.",
                "simSwapSteps": [
                    "Step 1 (Target Reconnaissance): Attacker gathers victim's personal data (Name, DOB, ID number) via phishing or dark web leaks.",
                    "Step 2 (Carrier Social Engineering): Attacker visits mobile carrier store with forged credentials claiming a lost SIM card.",
                    "Step 3 (SIM Reissuance): Carrier cancels original SIM and activates duplicate SIM card for the attacker.",
                    "Step 4 (Interception & Account Takeover): Victim loses cellular signal. Attacker initiates password resets on bank and email accounts, intercepting all SMS-based 2FA OTPs to drain funds."
                ],
                "bluetoothComparison": [
                    "1. Bluejacking: Sending unsolicited text/vCard messages to discoverable Bluetooth devices within 10 meters. Nuisance spam; does NOT access device data.",
                    "2. Bluesnarfing: Exploiting OBEX protocol flaws to steal contacts, calendar entries, SMS messages, and photos without pairing authorization.",
                    "3. Bluebugging: Establishing unauthorized RFCOMM serial channels to take complete remote control: tapping phone calls, sending SMS, and accessing cellular data."
                ],
                "mitigation": "Migrate from insecure SMS 2FA to hardware tokens (FIDO2) or TOTP apps; keep Bluetooth in Non-Discoverable mode; disable unknown app sideloading; enroll corporate devices in MDM."
            }
        },
        {
            "id": "eq-06",
            "unit": 3,
            "marks": "10-15 Marks",
            "question": "Explain Authentication Service Security and the 5 Factors of Authentication. Describe Wireless Network Attacks including Evil Twin and Man-in-the-Middle (MITM).",
            "markingScheme": [
                "5 Factors of Authentication: 5 Marks",
                "Evil Twin Rogue AP Attack & Packet Flow: 4 Marks",
                "MITM & ARP Poisoning: 3 Marks",
                "Countermeasures: 3 Marks"
            ],
            "modelAnswer": {
                "introduction": "Authentication verifies digital identity before granting system access. Robust enterprise architectures combine multiple independent authentication factors to prevent unauthorized entry.",
                "fiveFactors": [
                    "1. Something You Know (Knowledge): Passwords, PINs, Passphrases.",
                    "2. Something You Have (Possession): Smart cards, YubiKey hardware tokens, TOTP Authenticator apps.",
                    "3. Something You Are (Inherence): Biometrics (Fingerprint, Face ID, Iris scan).",
                    "4. Somewhere You Are (Location): GPS geofencing, enterprise IP subnet restrictions.",
                    "5. Something You Do (Behavior): Keystroke dynamics, touchscreen swipe velocity."
                ],
                "evilTwinAttack": "An attacker deploys a rogue wireless access point broadcasting the exact SSID name as a legitimate hotspot (e.g. 'Airport_Free_WiFi') with higher signal amplification. Victim devices auto-associate with the rogue AP. The attacker intercepts all unencrypted traffic, executes SSL stripping, and serves spoofed login portals to harvest credentials.",
                "mitigation": "Enforce WPA3-Enterprise 802.1X certificate-based authentication, mandate corporate VPN with kill-switch on untrusted networks, and deploy Wireless Intrusion Prevention Systems (WIPS)."
            }
        },
        {
            "id": "eq-07",
            "unit": 4,
            "marks": "10-15 Marks",
            "question": "What is a Proxy Server? Explain the 6 types of Proxy Servers and their applications. Detail the Tor Network Architecture and Onion Routing mechanism.",
            "markingScheme": [
                "Proxy Server Definition & Functions: 2 Marks",
                "6 Proxy Server Classifications: 5 Marks",
                "Tor Onion Routing Architecture & 3-Node Chain: 5 Marks",
                "Diagrams and Security Assessment: 3 Marks"
            ],
            "modelAnswer": {
                "introduction": "A Proxy Server acts as an intermediary gateway between client devices and destination servers, intercepting requests to provide caching, content filtering, load balancing, or IP masking.",
                "proxyTypes": [
                    "1. Forward Proxy: Intercepts internal client requests going out to the public web (masks client IP, enforces corporate filtering).",
                    "2. Reverse Proxy: Positioned in front of web servers; balances traffic, provides SSL termination and DDoS defense.",
                    "3. Transparent Proxy: Filters traffic without altering request headers or masking client IP (used in schools/hotels).",
                    "4. Anonymous Proxy: Hides client IP but declares itself as a proxy via HTTP headers (`HTTP_VIA`).",
                    "5. High-Anonymity (Elite) Proxy: Completely hides client IP and removes all proxy headers, appearing as a regular client.",
                    "6. Open Proxy: Publicly misconfigured proxy accessible to any user; widely abused by hackers to conceal origins."
                ],
                "torArchitecture": [
                    "Tor (The Onion Router) directs traffic through a free, worldwide volunteer overlay network of over 7,000 relays.",
                    "Client negotiates session keys with 3 relays and encrypts the packet in 3 concentric layers (like an onion).",
                    "Entry/Guard Node: Peels outer Layer 1 encryption. Sees client's real IP, but only knows Middle Node IP.",
                    "Middle Relay Node: Peels Layer 2 encryption. Knows Guard and Exit nodes; knows neither source nor destination.",
                    "Exit Node: Peels Layer 3 encryption. Transmits plaintext/TLS traffic to destination web server. Knows destination, but has ZERO knowledge of client IP."
                ],
                "diagram":
"""+-------------------------------------------------------------+
|               TOR ONION ROUTING PACKET FLOW                 |
+-------------------------------------------------------------+
| [Client] ==[E3[E2[E1 Data]]]==> [Guard] ==[E3[E2 Data]]==>  |
|                                                              |
| ==> [Middle] ==[E3 Data]==> [Exit] ==[Data]==> [Destination] |
+-------------------------------------------------------------+""",
                "conclusion": "Tor provides robust source anonymity because no single relay knows both source and destination simultaneously."
            }
        },
        {
            "id": "eq-08",
            "unit": 4,
            "marks": "10-15 Marks",
            "question": "Differentiate between Virus, Worm, Trojan Horse, and Backdoor. Describe the 5-Stage Anatomy of a Virus/Worm with a detailed diagram.",
            "markingScheme": [
                "4-Way Malware Differentiation Matrix: 5 Marks",
                "5-Stage Virus/Worm Anatomy: 5 Marks",
                "Diagram Representation: 3 Marks",
                "Real-World Examples & Conclusion: 2 Marks"
            ],
            "modelAnswer": {
                "introduction": "Malicious software (Malware) encompasses distinct classes of malicious code engineered to infiltrate, compromise, or destroy digital systems.",
                "comparisonMatrix": [
                    "Virus: Requires a host file (.exe, .doc); requires human execution to trigger; spreads via file sharing.",
                    "Worm: Standalone executable; requires ZERO human execution; autonomously scans and spreads across networks via exploits.",
                    "Trojan Horse: Disguised as legitimate software (games, utilities); does not self-replicate; opens backdoors or steals data.",
                    "Backdoor: A covert mechanism bypassing normal authentication to provide persistent remote root/admin access."
                ],
                "fiveStageAnatomy": [
                    "1. Replication Mechanism: The code routine locating uninfected files or memory sectors to inject malware clones.",
                    "2. Propagation Mechanism: The network scanning engine discovering vulnerable IP addresses to transmit copies.",
                    "3. Trigger Mechanism: Logic bomb condition (e.g. specific date/time or keyboard event) that unleashes payload.",
                    "4. Payload: The harmful action: file encryption (ransomware), data wiping, credential theft, or DDoS flood.",
                    "5. Concealment Engine: Polymorphic/Metamorphic encryption routines and rootkit cloaking that defeat static antivirus signatures."
                ],
                "diagram":
"""+-------------------------------------------------------------+
|                 5-STAGE VIRUS/WORM ANATOMY                  |
+-------------------------------------------------------------+
|  [ 1. Replication Engine  ] -> Injects into host/memory     |
|  [ 2. Propagation Engine  ] -> Scans subnet for exploits     |
|  [ 3. Trigger Mechanism   ] -> Logic bomb conditional check  |
|  [ 4. Malicious Payload   ] -> Ransomware / Wiper / Exfil    |
|  [ 5. Concealment Engine  ] -> Polymorphic crypter evasion   |
+-------------------------------------------------------------+""",
                "conclusion": "Modern endpoint security utilizes behavioral heuristic analysis and EDR to detect malware even when concealment engines bypass signature-based scanners."
            }
        },
        {
            "id": "eq-09",
            "unit": 4,
            "marks": "10-15 Marks",
            "question": "Explain Password Cracking methodologies (Brute Force, Dictionary, Rainbow Tables, Spraying). Discuss Password Hashing, Salt, Pepper, and compare hash algorithms (MD5, SHA-256, Bcrypt, Argon2).",
            "markingScheme": [
                "Password Cracking Methods: 4 Marks",
                "Role of Cryptographic Salt & Pepper: 3 Marks",
                "Comparison of Hash Algorithms (MD5 to Argon2): 4 Marks",
                "Defense & Countermeasures: 4 Marks"
            ],
            "modelAnswer": {
                "introduction": "Passwords represent the primary knowledge factor in authentication. Secure storage mandates converting plaintext passwords into one-way cryptographic hashes backed by salt and work factor algorithms.",
                "crackingMethods": [
                    "1. Brute Force: Testing all character permutations. Guaranteed success over infinite time ($O(C^L)$).",
                    "2. Dictionary Attack: Testing common words from wordlists (`rockyou.txt`) and leaked breach collections.",
                    "3. Rainbow Tables: Precomputed tables of hash reduction chains allowing rapid inverse hash lookups.",
                    "4. Password Spraying: Testing 1-2 common passwords against thousands of accounts to bypass lockout thresholds."
                ],
                "saltAndPepper": [
                    "Salt: A unique, cryptographically random string generated per user and combined with password before hashing. Defeats Rainbow Tables because attackers cannot precompute universal lookup tables.",
                    "Pepper: A high-entropy secret key added before hashing, stored in an external HSM or separate server outside the database."
                ],
                "hashComparison": [
                    "MD5 & SHA-1: Cryptographically broken, high GPU speed (billions/sec). NEVER use for passwords.",
                    "SHA-256: Fast integrity hash; vulnerable to rapid GPU brute-force unless salted and iterated thousands of times.",
                    "Bcrypt: Key-stretching Blowfish-based algorithm with adjustable cost factor (work factor) to slow GPU cracking.",
                    "Argon2: Modern gold standard; memory-hard and time-hard; completely neutralizes GPU and ASIC cracking clusters."
                ],
                "conclusion": "Enterprises must mandate Argon2id / Bcrypt password hashing, minimum 12-character passphrases, and multi-factor authentication."
            }
        },
        {
            "id": "eq-10",
            "unit": 4,
            "marks": "10-15 Marks",
            "question": "Explain Denial of Service (DoS) and Distributed Denial of Service (DDoS) Attacks. Classify DDoS attacks into Volumetric, Protocol, and Application-Layer attacks, and explain detection and mitigation techniques.",
            "markingScheme": [
                "DoS vs DDoS Definition & Architecture: 2 Marks",
                "3 DDoS Attack Classifications with Examples: 5 Marks",
                "Detection & Cloud Scrubbing Mitigation: 5 Marks",
                "Diagram: 3 Marks"
            ],
            "modelAnswer": {
                "introduction": "A Denial of Service (DoS) attack aims to render an online service or network unavailable to legitimate users. A Distributed Denial of Service (DDoS) leverages thousands of compromised botnet nodes to overwhelm target infrastructure simultaneously.",
                "ddosClassifications": [
                    "1. Volumetric Attacks (Gbps/Tbps): Floods network bandwidth. Examples: UDP Flood, DNS Amplification (50x amplification via open DNS resolvers), NTP Amplification.",
                    "2. Protocol Attacks (Packets/Sec): Consumes state tables of firewalls and OS kernel. Examples: SYN Flood (exhausts TCP connection table), Ping of Death, Smurf attack.",
                    "3. Application-Layer Attacks (Requests/Sec): Targets web servers and database CPU/RAM. Examples: HTTP Flood, Slowloris (transmits headers byte-by-byte very slowly to hold connection threads open)."
                ],
                "mitigationTechniques": [
                    "BGP Anycast Routing: Disperses volumetric flood traffic across hundreds of global Edge PoPs.",
                    "Cloud Scrubbing Centers: Ingests all traffic, inspects packet headers and behavioral heuristics, filters malicious traffic, and forwards clean packets to origin.",
                    "SYN Cookies: Encodes TCP parameters into sequence numbers, preventing state table memory exhaustion.",
                    "Web Application Firewall (WAF) & Rate Limiting: Challenges anomalous Layer 7 traffic with CAPTCHA puzzles."
                ],
                "diagram":
"""+-------------------------------------------------------------+
|             DDoS SCRUBBING DEFENSE ARCHITECTURE             |
+-------------------------------------------------------------+
|  [ Botnet Zombies ] \                                       |
|  [ Real Users     ] ---> [ CLOUD SCRUBBING ] === Clean ===> [ Origin ]|
|                          [     CENTER     ]      Traffic    [ Server ]|
|                          (Discards Floods)                   |
+-------------------------------------------------------------+"""
            }
        }
    ],
    "flashcards": [
        { "id": "fc-1", "unit": 1, "front": "What is Cyber Crime?", "back": "Any illegal activity where a computer, digital system, or network is used as a Target, a Tool, or a Storage Medium." },
        { "id": "fc-2", "unit": 1, "front": "What are the 3 Roles of a Computer in cyber crime?", "back": "1. Target (e.g. Server Hacking, DDoS)\n2. Tool (e.g. Phishing, Fraud)\n3. Storage Medium (e.g. Stolen DBs, Card Dumps)." },
        { "id": "fc-3", "unit": 1, "front": "What was Phone Phreaking?", "back": "1970s-80s activity using audio frequencies (like 2600 Hz tone from Captain Crunch whistles or Blue Boxes) to manipulate phone switches for free calls." },
        { "id": "fc-4", "unit": 1, "front": "What was the significance of the Morris Worm (1988)?", "back": "The first major network worm on ARPANET, infecting ~10% of connected systems and prompting the establishment of the first CERT." },
        { "id": "fc-5", "unit": 1, "front": "What are the 4 Pillars of Cyber Crime Classification?", "back": "1. Against Individuals\n2. Against Property\n3. Against Government\n4. Against Society." },
        { "id": "fc-6", "unit": 1, "front": "What is the Budapest Convention (2001)?", "back": "The first binding international treaty harmonizing national cybercrime laws, investigative procedures, and 24/7 law enforcement cooperation." },
        { "id": "fc-7", "unit": 1, "front": "Name the 8 phases of the Cyber Kill Chain.", "back": "1. Reconnaissance\n2. Scanning\n3. Weaponization\n4. Delivery\n5. Exploitation\n6. Installation\n7. Command & Control (C2)\n8. Actions on Objectives." },
        { "id": "fc-8", "unit": 1, "front": "What vulnerability did WannaCry exploit in 2017?", "back": "EternalBlue (MS17-010), exploiting a Windows SMBv1 vulnerability to spread autonomously across 200,000+ computers." },
        { "id": "fc-9", "unit": 2, "front": "Define Social Engineering.", "back": "The psychological manipulation of individuals into divulging confidential information or performing actions that compromise security." },
        { "id": "fc-10", "unit": 2, "front": "What are the 6 key psychological triggers used in social engineering?", "back": "1. Authority\n2. Urgency\n3. Fear\n4. Greed / Reward\n5. Trust / Social Proof\n6. Curiosity / Helpfulness." },
        { "id": "fc-11", "unit": 2, "front": "Differentiate Phishing vs Pretexting.", "back": "Phishing: Broad mass fraudulent communication.\nPretexting: Elaborate fabricated scenario (e.g. IT auditor) to extract specific trust-based data." },
        { "id": "fc-12", "unit": 2, "front": "What is Baiting?", "back": "Promising a physical or digital lure (e.g. infected USB flash drive left in a parking lot or free software crack) to trick victims into self-infection." },
        { "id": "fc-13", "unit": 2, "front": "What is Quid Pro Quo in social engineering?", "back": "Offering an explicit service or benefit ('Free IT security check') in direct exchange for credentials or disabled controls." },
        { "id": "fc-14", "unit": 2, "front": "What is Tailgating / Piggybacking?", "back": "Physical intrusion where an unauthorized person closely follows an authorized person through a secure access door." },
        { "id": "fc-15", "unit": 2, "front": "What is Scareware?", "back": "Alarming pop-ups or alerts falsely claiming extreme malware infection to force victims into downloading malicious 'antivirus' software." },
        { "id": "fc-16", "unit": 2, "front": "What is Cybercrime-as-a-Service (CaaS)?", "back": "An underground commercial business model where malware, botnets, phishing kits, and stolen credentials are sold or rented on subscription." },
        { "id": "fc-17", "unit": 2, "front": "What is a Botnet?", "back": "A network of compromised computers or IoT devices ('zombies') remotely controlled by a central Botmaster." },
        { "id": "fc-18", "unit": 2, "front": "Compare Centralized vs P2P Botnets.", "back": "Centralized: Relies on single C2 server (Single Point of Failure).\nP2P: Decentralized; bots exchange encrypted commands with peer nodes, resisting server takedowns." },
        { "id": "fc-19", "unit": 2, "front": "How did the Mirai Botnet spread in 2016?", "back": "Scanned open Telnet ports (23/2323) on IoT devices (cameras/routers) and brute-forced 62 default factory passwords, launching a 1.2 Tbps DDoS attack." },
        { "id": "fc-20", "unit": 3, "front": "Why is OS Rooting / Jailbreaking dangerous?", "back": "Completely removes OS sandboxing, allows any malicious app to obtain root privileges, fails integrity checks, and blocks official security updates." },
        { "id": "fc-21", "unit": 3, "front": "Explain SIM Swap Fraud in 1 sentence.", "back": "Attacker socially engineers telecom provider to issue a duplicate SIM card, seizing the victim's phone number to intercept 2FA SMS banking OTPs." },
        { "id": "fc-22", "unit": 3, "front": "What are the 5 Factors of Authentication?", "back": "1. Something You Know\n2. Something You Have\n3. Something You Are\n4. Somewhere You Are\n5. Something You Do." },
        { "id": "fc-23", "unit": 3, "front": "What is an Evil Twin Attack?", "back": "A rogue Wi-Fi access point broadcasting the exact SSID name as a legitimate hotspot to trick victims into connecting and intercepting their traffic." },
        { "id": "fc-24", "unit": 3, "front": "Differentiate Bluejacking, Bluesnarfing, and Bluebugging.", "back": "Bluejacking: Unsolicited spam messages.\nBluesnarfing: Unauthorized data theft (contacts/SMS).\nBluebugging: Complete remote control and audio wiretapping." },
        { "id": "fc-25", "unit": 3, "front": "What is MDM (Mobile Device Management)?", "back": "Enterprise software enforcing security policies, encryption, app allowlisting, and remote wiping capabilities on mobile devices." },
        { "id": "fc-26", "unit": 4, "front": "What is the difference between Forward Proxy and Reverse Proxy?", "back": "Forward Proxy: Sits in front of CLIENTS (protects clients, hides client IP).\nReverse Proxy: Sits in front of SERVERS (balances load, protects backend servers)." },
        { "id": "fc-27", "unit": 4, "front": "What is a High-Anonymity (Elite) Proxy?", "back": "A proxy that completely conceals the client's real IP AND removes all proxy-identifying headers (like `X-Forwarded-For`), appearing as a normal client." },
        { "id": "fc-28", "unit": 4, "front": "Explain how Tor Onion Routing protects privacy.", "back": "Encrypts packets in 3 layers across 3 nodes (Guard, Middle, Exit). No single node knows both the source client IP and destination web server IP." },
        { "id": "fc-29", "unit": 4, "front": "What was Operation Bayonet (2017)?", "back": "Joint law enforcement takedown where the FBI seized AlphaBay and the Dutch Police ran Hansa Market as a honeypot for 27 days to identify global vendors." },
        { "id": "fc-30", "unit": 4, "front": "What is Reverse Proxy Phishing (e.g. Evilginx)?", "back": "A phishing attack where the proxy transparently relays requests between victim and real server, stealing active Session Cookies and bypassing 2FA!" },
        { "id": "fc-31", "unit": 4, "front": "Differentiate Virus vs Worm.", "back": "Virus: Requires a host file (.exe) and human execution to spread.\nWorm: Standalone executable that spreads autonomously across network vulnerabilities without human action." },
        { "id": "fc-32", "unit": 4, "front": "Name the 5 components of Virus/Worm Anatomy.", "back": "1. Replication Mechanism\n2. Propagation Mechanism\n3. Trigger Mechanism (Logic Bomb)\n4. Payload\n5. Concealment Engine (Polymorphism)." },
        { "id": "fc-33", "unit": 4, "front": "What is a Cryptographic Salt and why is it essential?", "back": "A unique random string appended to a password before hashing. Defeats Rainbow Tables because attackers cannot precompute universal hash chains." },
        { "id": "fc-34", "unit": 4, "front": "Why is Argon2 superior to MD5/SHA-256 for password hashing?", "back": "Argon2 is memory-hard and time-hard with configurable cost factors, rendering high-speed GPU and ASIC cracking hardware ineffective." },
        { "id": "fc-35", "unit": 4, "front": "Differentiate Volumetric, Protocol, and Application-Layer DDoS attacks.", "back": "Volumetric (Gbps): Saturates bandwidth (UDP flood, DNS amp).\nProtocol (PPS): Exhausts state tables (SYN flood).\nApplication (RPS): Crashes server CPU/RAM (Slowloris, HTTP flood)." }
    ],
    "quizzes": [
        {
            "id": "q1",
            "unit": 1,
            "question": "A cyber attack where an attacker launches a Ransomware attack that encrypts a corporate database server classifies the computer primarily as what role?",
            "options": ["Computer as a Storage", "Computer as a Tool", "Computer as a Target", "Computer as an Intermediary"],
            "correct": 2,
            "explanation": "When the computer system, server, or database itself is attacked and encrypted, the computer plays the role of a Target."
        },
        {
            "id": "q2",
            "unit": 1,
            "question": "Which historic cyber activity involved manipulating telephone switching frequencies (like 2600 Hz tones) to obtain free unauthorized phone calls?",
            "options": ["Wardriving", "Phone Phreaking", "Bluebugging", "Doxxing"],
            "correct": 1,
            "explanation": "Phone Phreaking (pioneered in 1970s by John Draper using toy whistles and Blue Boxes) manipulated telecom frequencies."
        },
        {
            "id": "q3",
            "unit": 1,
            "question": "Which international treaty, opened for signature in 2001, was the first binding convention addressing internet and computer crime?",
            "options": ["Geneva Digital Accord", "Budapest Convention on Cybercrime", "Paris Cyber Charter", "Wassenaar Arrangement"],
            "correct": 1,
            "explanation": "The Budapest Convention on Cybercrime (2001) is the landmark international treaty harmonizing cyber laws and cross-border cooperation."
        },
        {
            "id": "q4",
            "unit": 1,
            "question": "In the Cyber Kill Chain framework, which phase involves coupling an exploit code with a malicious backdoor payload?",
            "options": ["Reconnaissance", "Weaponization", "Installation", "Command and Control"],
            "correct": 1,
            "explanation": "Weaponization is the phase where an attacker pairs an exploit tailored to a vulnerability with a malicious payload or backdoor."
        },
        {
            "id": "q5",
            "unit": 1,
            "question": "What vulnerability and exploit did the 2017 WannaCry Ransomware utilize to propagate autonomously across networks?",
            "options": ["Heartbleed (OpenSSL)", "EternalBlue (SMBv1 MS17-010)", "Log4Shell (Apache)", "Shellshock (Bash)"],
            "correct": 1,
            "explanation": "WannaCry leveraged the EternalBlue exploit targeting Microsoft Windows SMBv1 protocol vulnerability MS17-010."
        },
        {
            "id": "q6",
            "unit": 2,
            "question": "An attacker leaves an infected USB drive labeled 'Executive Bonuses Q4' in a company cafeteria. What social engineering attack is this?",
            "options": ["Pretexting", "Baiting", "Tailgating", "Quid Pro Quo"],
            "correct": 1,
            "explanation": "Baiting relies on enticing a victim with a physical or digital lure (like an infected USB drive) that prompts them to infect their own system."
        },
        {
            "id": "q7",
            "unit": 2,
            "question": "An attacker calls an employee pretending to be an IT technician offering 'free system optimization' if they provide their admin credentials. What is this?",
            "options": ["Quid Pro Quo", "Tailgating", "Scareware", "Whaling"],
            "correct": 0,
            "explanation": "Quid Pro Quo involves offering an explicit service or benefit in direct exchange for passwords or security bypass."
        },
        {
            "id": "q8",
            "unit": 2,
            "question": "What botnet architecture eliminates the Single Point of Failure (SPOF) by having infected zombie nodes relay commands directly among themselves?",
            "options": ["Centralized IRC Architecture", "Peer-to-Peer (P2P) Architecture", "Client-Server Star Topology", "HTTP Polling Architecture"],
            "correct": 1,
            "explanation": "P2P botnets distribute command-and-control across all peer bots, ensuring no single server seizure can bring down the network."
        },
        {
            "id": "q9",
            "unit": 2,
            "question": "How did the 2016 Mirai Botnet compromise over 600,000 IoT devices worldwide?",
            "options": ["Exploited zero-day browser bugs", "Brute-forced 62 default factory passwords on open Telnet ports", "Distributed infected USB drives", "Exploited WPA2 Wi-Fi KRACK"],
            "correct": 1,
            "explanation": "Mirai scanned open Telnet ports (23/2323) on IoT devices and brute-forced factory default logins (e.g. admin/admin, root/xc3511)."
        },
        {
            "id": "q10",
            "unit": 2,
            "question": "What attack vector was used in the July 2020 Twitter Bitcoin Hack to breach internal administrator dashboards?",
            "options": ["SQL Injection on Twitter database", "Phone Spear-Phishing (Vishing) targeting Twitter employees", "DDoS attack overwhelming login servers", "Physical hardware keylogger"],
            "correct": 1,
            "explanation": "Attackers called Twitter employees (vishing) posing as IT support to steal VPN credentials, gaining access to the internal customer support dashboard."
        },
        {
            "id": "q11",
            "unit": 3,
            "question": "Why is rooting an Android device or jailbreaking an iOS device catastrophic for device security?",
            "options": ["It increases cellular data usage", "It completely dismantles the OS application sandbox and security boundaries", "It permanently disables Wi-Fi", "It prevents taking screenshots"],
            "correct": 1,
            "explanation": "Rooting/jailbreaking breaks down the OS sandbox, enabling any malicious app to access other apps' private memory, databases, and keychains."
        },
        {
            "id": "q12",
            "unit": 3,
            "question": "In a SIM Swap Fraud attack, what is the primary goal of the attacker?",
            "options": ["To increase the victim's phone bill", "To intercept SMS-based Two-Factor Authentication (OTP) codes", "To record video via camera", "To format the victim's SD card"],
            "correct": 1,
            "explanation": "By taking control of the victim's mobile number on a duplicate SIM, the attacker intercepts banking OTPs and password-reset SMS messages."
        },
        {
            "id": "q13",
            "unit": 3,
            "question": "Which Bluetooth attack is the most severe, providing complete remote control, audio eavesdropping, and phone call capabilities?",
            "options": ["Bluejacking", "Bluesnarfing", "Bluebugging", "Blueprinting"],
            "correct": 2,
            "explanation": "Bluebugging creates an unauthorized RFCOMM serial channel giving the attacker full remote control and wiretapping capabilities."
        },
        {
            "id": "q14",
            "unit": 3,
            "question": "An attacker sets up a rogue Wi-Fi hotspot with the exact same SSID name ('Hotel_Guest_WiFi') as the legitimate hotel network. What attack is this?",
            "options": ["Evil Twin Attack", "Bluejacking Attack", "Smishing Attack", "Replay Attack"],
            "correct": 0,
            "explanation": "An Evil Twin attack uses a rogue access point with an identical SSID and stronger signal to lure victims into auto-connecting."
        },
        {
            "id": "q15",
            "unit": 3,
            "question": "Which of the following represents True Multi-Factor Authentication (MFA)?",
            "options": ["Password + Security Question", "Password + PIN", "Password + Fingerprint Biometric", "SMS OTP + Email OTP"],
            "correct": 2,
            "explanation": "True MFA requires factors from AT LEAST TWO different categories. Password (Knowledge) + Fingerprint (Inherence) fulfills this requirement."
        },
        {
            "id": "q16",
            "unit": 4,
            "question": "Which type of Proxy Server completely conceals the client's IP address AND removes all proxy-identifying HTTP headers?",
            "options": ["Transparent Proxy", "Anonymous Proxy", "High-Anonymity (Elite) Proxy", "Reverse Proxy"],
            "correct": 2,
            "explanation": "High-Anonymity (Elite) proxies do not forward headers like `X-Forwarded-For` or `Via`, making them indistinguishable from regular clients."
        },
        {
            "id": "q17",
            "unit": 4,
            "question": "In the Tor network, which node has knowledge of the client's real IP address, but CANNOT see the final destination web server?",
            "options": ["Exit Node", "Middle Relay Node", "Entry / Guard Node", "Directory Authority Node"],
            "correct": 2,
            "explanation": "The Entry/Guard node knows the client's IP to accept connection, but only knows the Middle node IP, having zero visibility into the destination."
        },
        {
            "id": "q18",
            "unit": 4,
            "question": "What is the primary technical difference between a Computer Virus and a Computer Worm?",
            "options": ["A virus is written in C; a worm is written in Python", "A virus requires a host file and human execution; a worm is standalone and self-propagates", "A virus only affects Linux; a worm only affects Windows", "A worm cannot contain a destructive payload"],
            "correct": 1,
            "explanation": "A virus must attach to a host executable and requires human execution to trigger, whereas a worm is a standalone program that self-propagates across networks autonomously."
        },
        {
            "id": "q19",
            "unit": 4,
            "question": "Why is adding a Cryptographic Salt essential before hashing user passwords in a database?",
            "options": ["It compresses the hash string size", "It completely defeats precomputed Rainbow Table attacks", "It makes hashing faster", "It converts the hash into reversible symmetric encryption"],
            "correct": 1,
            "explanation": "Salting adds a unique random string per user, forcing attackers to compute dedicated tables for every individual salt, defeating global Rainbow Tables."
        },
        {
            "id": "q20",
            "unit": 4,
            "question": "Which type of DDoS attack uses tools like Slowloris to open hundreds of connections and send partial HTTP headers very slowly to exhaust server threads?",
            "options": ["Volumetric Network Flood", "Protocol SYN Flood", "Application-Layer (Layer 7) Attack", "DNS Amplification Attack"],
            "correct": 2,
            "explanation": "Slowloris is a Layer 7 Application attack that ties up server connection threads by keeping HTTP header transmissions incomplete."
        }
    ],
    "glossary": [
        { "term": "Advanced Persistent Threat (APT)", "def": "A stealthy threat actor (typically nation-state sponsored) that gains unauthorized access to a network and remains undetected for an extended period." },
        { "term": "Argon2", "def": "The modern gold-standard password hashing algorithm (winner of the Password Hashing Competition); memory-hard and time-hard, resistant to GPU/ASIC attacks." },
        { "term": "Baiting", "def": "A social engineering attack where an attacker leaves malware-infected physical media (like a USB drive) in public areas to lure curious victims into executing it." },
        { "term": "Bcrypt", "def": "An adaptive, Blowfish-based cryptographic password hashing algorithm with an adjustable work factor (cost parameter) to slow brute-force cracking." },
        { "term": "Bluebugging", "def": "The most dangerous Bluetooth attack, establishing an unprompted RFCOMM serial channel granting full remote control and call eavesdropping." },
        { "term": "Bluejacking", "def": "Sending unsolicited spam messages or digital business cards (vCards) to nearby discoverable Bluetooth devices." },
        { "term": "Bluesnarfing", "def": "The unauthorized theft of data (contacts, SMS, calendar events, photos) from a device via an insecure Bluetooth connection." },
        { "term": "Botnet", "def": "A network of compromised computers or IoT devices ('zombies') commanded remotely by a central 'botmaster' for coordinated attacks." },
        { "term": "Budapest Convention", "def": "The 2001 landmark international treaty addressing cybercrime by harmonizing national legislation, investigation powers, and international cooperation." },
        { "term": "Cyber Kill Chain", "def": "An 8-phase model developed by Lockheed Martin detailing the phases of a cyberattack: Recon, Scan, Weaponize, Deliver, Exploit, Install, C2, Actions on Objectives." },
        { "term": "Cybercrime-as-a-Service (CaaS)", "def": "An underground commercial business model where malware builders, botnets, and hacking tools are leased to affiliates for a subscription or profit split." },
        { "term": "Credential Stuffing", "def": "The automated injection of breached username/password pairs across hundreds of unrelated websites to compromise user accounts." },
        { "term": "DNS Amplification", "def": "A volumetric DDoS attack that sends small requests with spoofed victim IP to open recursive DNS resolvers, generating 50x larger responses flooding the victim." },
        { "term": "Evil Twin", "def": "A rogue Wi-Fi access point broadcasting the identical SSID name as a legitimate hotspot to trick nearby devices into connecting and intercepting traffic." },
        { "term": "High-Anonymity (Elite) Proxy", "def": "A proxy server that hides the client's real IP and removes all proxy headers, making it indistinguishable from a standard direct client." },
        { "term": "Keylogger", "def": "Hardware or software engineered to record every keystroke pressed on a keyboard to harvest passwords, credit cards, and confidential messages." },
        { "term": "Logic Bomb", "def": "A malicious code segment intentionally inserted into software that lies dormant until triggered by a specific event or date condition." },
        { "term": "Mobile Device Management (MDM)", "def": "Enterprise software allowing administrators to monitor, secure, configure, and remotely wipe smartphones and tablets." },
        { "term": "Onion Routing", "def": "A technique for anonymous communication over a network (used in Tor) where messages are encapsulated in layers of encryption like an onion." },
        { "term": "Phishing", "def": "The fraudulent practice of sending emails or messages masquerading as reputable companies to trick individuals into revealing credentials." },
        { "term": "Pretexting", "def": "A social engineering attack where an attacker fabricates an elaborate fictional scenario (pretext) to establish trust and extract confidential information." },
        { "term": "Quid Pro Quo", "def": "A social engineering attack where an attacker offers a service or benefit (e.g. 'free IT help') in explicit exchange for credentials or access." },
        { "term": "Rainbow Table", "def": "A precomputed lookup table of cryptographic hash chains used to reverse cryptographic hash functions and crack passwords in seconds." },
        { "term": "Ransomware", "def": "A class of malware that encrypts files on a victim's device, demanding cryptocurrency payment in exchange for the decryption key." },
        { "term": "Remote Access Trojan (RAT)", "def": "A malware program that includes a back door for administrative control over the target computer without the user's knowledge." },
        { "term": "Rooting / Jailbreaking", "def": "The process of bypassing operating system security controls on mobile devices to obtain superuser (root) privileges, dismantling OS sandboxing." },
        { "term": "Salt (Cryptography)", "def": "A random string added to passwords before hashing to ensure identical passwords produce different hashes, defeating rainbow tables." },
        { "term": "Scareware", "def": "Malicious pop-ups designed to frighten users with fake virus warnings into downloading rogue security software." },
        { "term": "SIM Swap Fraud", "def": "A fraud scheme where an attacker tricks a mobile carrier into porting the victim's phone number to an attacker's SIM to intercept 2FA SMS codes." },
        { "term": "Slowloris", "def": "A Layer 7 DDoS attack tool that opens numerous connections to a web server and sends HTTP headers very slowly to exhaust server connection slots." },
        { "term": "Spear Phishing", "def": "A targeted phishing attack directed at a specific individual or organization with customized, highly relevant background context." },
        { "term": "SYN Flood", "def": "A protocol DDoS attack where an attacker floods a target with TCP SYN packets without returning ACKs, exhausting the server connection state table." },
        { "term": "Tailgating", "def": "A physical social engineering attack where an unauthorized individual closely follows an authorized person through a secure door." },
        { "term": "Tor (The Onion Router)", "def": "An open-source anonymity network that directs internet traffic through a worldwide volunteer overlay network of over 7,000 relays." },
        { "term": "Typosquatting", "def": "Registering domain names that look or sound similar to legitimate brands (e.g. `g00gle.com`) to mislead visitors." },
        { "term": "Vishing", "def": "Voice Phishing: conducting phishing attacks over phone calls to extract banking or personal credentials." },
        { "term": "Worm", "def": "A standalone piece of malicious software that autonomously self-replicates and spreads across computer networks without human interaction." }
    ]
}

# Write to js/data.js
output_js = f"// Cyber Security Mastery Platform - Comprehensive Curriculum Dataset\n// Auto-generated from complete Units 1 - 4 Syllabus Notes\n\nconst CYBER_DATA = {json.dumps(cyber_data, indent=2, ensure_ascii=False)};\n"

os.makedirs('js', exist_ok=True)
with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print(f"Successfully generated js/data.js with {len(cyber_data['units'])} units, {len(cyber_data['examQuestions'])} exam questions, {len(cyber_data['flashcards'])} flashcards, {len(cyber_data['quizzes'])} quiz questions, and {len(cyber_data['glossary'])} glossary items.")
