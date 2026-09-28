# -*- coding: utf-8 -*-
"""
Master Curriculum Builder for Cyber Security Platform (Units 1 - 4)
Generates exhaustive, textbook-grade theory notes, detailed subsections,
ASCII diagrams, case studies, GTU exam guides, flashcards, and quizzes.
"""

import json
import os

cyber_data = {
    "courseInfo": {
        "title": "Cyber Security Mastery & Exam Readiness Platform",
        "subtitle": "Comprehensive Interactive Syllabus (Units 1 - 4) with Deep-Dive Theory Notes, GTU 10-15 Mark Answers, Live Simulators, Quiz Arena, and 3D Flashcards",
        "totalUnits": 4,
        "academicLevel": "Undergraduate / GTU / Engineering Cyber Security Curriculum",
        "version": "3.0 Master Edition"
    },
    "units": [
        # =========================================================================
        # UNIT 1
        # =========================================================================
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
                    "theoryModules": [
                        {
                            "heading": "1. Understanding Cybercrime vs Traditional Crime",
                            "content": "Traditional crimes require the physical presence of the perpetrator at the crime scene, leaving behind physical traces like fingerprints or toolmarks. In contrast, cybercrime operates across digital telecommunication networks with zero geographical latency. A cybercriminal located on one continent can infiltrate systems located thousands of miles away in milliseconds.",
                            "keyPoints": [
                                "Asymmetry of Attack: A defender must secure every possible port and vulnerability, whereas an attacker only needs to discover a single flaw.",
                                "Scalability: A single automated script or botnet can attack hundreds of thousands of targets simultaneously without additional human effort.",
                                "Anonymity and Obfuscation: The use of proxies, VPN cascades, and onion routing masks the true origin IP address of perpetrators."
                            ]
                        },
                        {
                            "heading": "2. Detailed Breakdown of the Three Roles of Computers",
                            "content": "In cyber jurisprudence and digital forensics, the role played by computing machinery is categorized into three fundamental postures:",
                            "keyPoints": [
                                "Computer as a Target: The system itself is the intended victim. Attacks aim at violating the Confidentiality, Integrity, or Availability (CIA Triad) of the system (e.g. database exfiltration, ransomware encryption, SYN flood DDoS).",
                                "Computer as a Tool / Instrument: The computer is used as a weapon to execute traditional or modern crimes (e.g. sending deceptive phishing emails, spoofing bank web pages, running automated credential stuffing).",
                                "Computer as a Storage Medium / Repository: The computer or digital storage device acts as an incidental container holding stolen credentials, carding dumps, illicit material, or logs of criminal enterprise."
                            ]
                        }
                    ],
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
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Definition (2m) -> 2. Roles Diagram (2m) -> 3. Explanation of Target, Tool, Storage with 2 examples each (6m) -> 4. Traditional vs Cyber Crime Differences (3m) -> 5. Conclusion (1m)"
                    },
                    "keyTakeaways": [
                        "A cyber crime requires at least one digital component (computer, network, mobile device, or cloud).",
                        "Computers can act as a Target, Tool, or Storage medium simultaneously in complex intrusions.",
                        "Traditional crimes committed over digital networks are often categorized under cyber-enabled crime."
                    ]
                },
                {
                    "id": "u1-t2",
                    "unitId": 1,
                    "title": "Historical Evolution & Origins of Cyber Crime",
                    "tag": "History & Trends",
                    "summary": "The chronological progression of digital offenses from 1960s mainframe abuse and phone phreaking to modern AI-driven cyber threats.",
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
                    "theoryModules": [
                        {
                            "heading": "1. The Pre-Internet Era: Phone Phreaking (1970s)",
                            "content": "Before the commercial World Wide Web, telephone switching systems operated on in-band signaling tones. Pioneers like John Draper ('Captain Crunch') discovered that a toy whistle from a cereal box emitted an exact 2600 Hz audio tone. Transmitting this frequency into a telephone receiver reset the AT&T trunk line switch into operator mode, allowing free international calls. This led to the creation of electronic tone generators called 'Blue Boxes', marking the birth of hacking culture.",
                            "keyPoints": [
                                "In-band signaling allowed users to send control signals over the same channel as voice, creating an architectural vulnerability.",
                                "Phreaking demonstrated that systems could be manipulated by reverse-engineering underlying telecommunications protocols."
                            ]
                        },
                        {
                            "heading": "2. Dawn of Viruses and Network Worms (1980s)",
                            "content": "In 1986, the 'Brain' virus was created by two Pakistani brothers to track software piracy of their medical software, spreading via floppy disk boot sectors. In November 1988, Robert Tappan Morris released the Morris Worm on ARPANET. Intended to measure the size of the network, a programming flaw caused it to reinfect machines multiple times, crashing 10% of the entire Internet and prompting the US Defense Department to create the first CERT (Computer Emergency Response Team).",
                            "keyPoints": [
                                "The Morris Worm was the world's first autonomous self-propagating worm utilizing buffer overflow and Sendmail debug flaws.",
                                "It transformed cybersecurity from academic hobbyism into a formal national defense discipline."
                            ]
                        },
                        {
                            "heading": "3. Modern Era: Cybercrime-as-a-Service, APTs & AI (2010s - Present)",
                            "content": "Today, cybercrime is characterized by state-sponsored Advanced Persistent Threats (APTs), Ransomware-as-a-Service (RaaS) cartels, cryptocurrency extortion, and generative AI deepfakes used for real-time voice and video impersonation.",
                            "keyPoints": [
                                "Transition from disruptive vanity hacks to multi-billion-dollar commercial underground cartels.",
                                "Supply chain compromises (like SolarWinds) targeting trusted software updates to breach thousands of downstream enterprises."
                            ]
                        }
                    ],
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
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Introduction to Evolution (1m) -> 2. Detailed Era Breakdown with Year milestones (6m) -> 3. Phone Phreaking technical mechanism (3m) -> 4. Morris Worm impact & CERT creation (3m) -> 5. Modern trends summary (2m)"
                    },
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
                    "definition": "Proliferation of cyber crime refers to the rapid global expansion in the volume, variety, velocity, and sophistication of digital attacks targeting individuals, organizations, and nation-states.",
                    "theoryModules": [
                        {
                            "heading": "1. Key Drivers of Cybercrime Proliferation",
                            "content": "Several socio-technical dynamics drive the exponential surge in cyber offenses:",
                            "keyPoints": [
                                "1. Pervasive Digital Transformation: Critical national infrastructure, healthcare, banking, and government citizen records are now cloud-connected, expanding the attack surface.",
                                "2. Lucrative Financial Returns: Cyber extortion via untraceable cryptocurrencies (Monero, Bitcoin) generates multi-million dollar payouts with negligible physical risk compared to armed robbery.",
                                "3. Low Entry Barriers (Script Kiddies to Cartels): Pre-packaged exploit kits, Automated DDoS-for-hire booters, and darknet phishing templates allow amateurs to launch sophisticated attacks.",
                                "4. Geopolitical Conflicts & State Sponsorship: Nation-states employ cyber warfare units to conduct espionage, disrupt adversary energy grids, and steal intellectual property."
                            ]
                        }
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
                    "definition": "The 4-Pillar Classification categorizes cybercrimes based on the nature of the target: Individual Persons, Tangible/Intangible Property, Sovereign Governments, and Society at large.",
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
                    "theoryModules": [
                        {
                            "heading": "1. Cybercrime Against Individuals",
                            "content": "Targeted directly at specific human beings, violating their privacy, emotional well-being, personal dignity, or direct financial assets.",
                            "keyPoints": [
                                "Identity Theft: Unauthorized acquisition and use of personal identifying data (SSN, Aadhaar, DOB, passport) to obtain fraudulent loans or open bank accounts.",
                                "Cyberstalking & Doxxing: Repeated digital surveillance, unwanted communications, and malicious publication of private home addresses and phone numbers.",
                                "Cyberbullying & Defamation: Posting manipulated pictures, spreading defamatory falsehoods across social media to inflict psychological harm."
                            ]
                        },
                        {
                            "heading": "2. Cybercrime Against Property",
                            "content": "Targeting commercial intellectual property, tangible digital assets, and organizational databases.",
                            "keyPoints": [
                                "Ransomware Extortion: Infiltrating networks, encrypting all disk volumes, and demanding crypto ransom for the private decryption key.",
                                "Intellectual Property & Trade Secret Theft: Exfiltrating proprietary source code, defense schematics, and chemical formulas to sell to foreign competitors.",
                                "Software Piracy & Counterfeiting: Distributing cracked commercial enterprise software, generating economic damage to developers."
                            ]
                        },
                        {
                            "heading": "3. Cybercrime Against Government",
                            "content": "Strikes against sovereign defense databases, electoral systems, and national critical infrastructure (SCADA).",
                            "keyPoints": [
                                "Cyber Terrorism: Coordinated cyber strikes intended to cause mass disruption, panic, death, or severe national economic catastrophe.",
                                "Critical Infrastructure Sabotage: Infiltrating industrial control systems (ICS/SCADA) governing power grids, nuclear centrifuges (e.g. Stuxnet), or municipal water treatment.",
                                "Electoral Interference: Compromising voting registration databases or executing disinformation campaigns to alter democratic election outcomes."
                            ]
                        },
                        {
                            "heading": "4. Cybercrime Against Society",
                            "content": "Offenses undermining the social order, public morals, communal peace, and collective welfare.",
                            "keyPoints": [
                                "Disinformation & Viral Fake News: Fabricating panic during pandemics, communal riots, or financial crashes using AI bot armies.",
                                "Child Sexual Abuse Material (CSAM): Production, dissemination, and hosting of abusive exploitation materials across dark web networks.",
                                "Financial Ponzi & Pyramid Crypto Scams: Fabricating fake high-yield investment programs to defraud large segments of the public."
                            ]
                        }
                    ],
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
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Definition of Classification (1m) -> 2. Taxonomy Box Diagram (2m) -> 3. Explain 4 Pillars with 2 detailed examples each (8m) -> 4. Applicable IT Act Sections (Sec 66C, 66D, 66E, 66F) (3m) -> 5. Conclusion (1m)"
                    },
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
                    "definition": "The transnational nature of cyber crime refers to its borderless operation, where criminal planning, execution, routing, infrastructure, and victimization occur across multiple sovereign legal jurisdictions simultaneously.",
                    "theoryModules": [
                        {
                            "heading": "1. The 4 Fundamental Legal & Investigative Hurdles",
                            "content": "Cybercrime challenges traditional territorial jurisdiction principles in criminal law:",
                            "keyPoints": [
                                "1. Jurisdictional Conflicts: If an attacker in Country A uses command servers in Country B and C to hack a bank in Country D, which court has legal jurisdiction?",
                                "2. Technical Attribution: Attackers use bulletproof hosting, proxy chains, and Tor exit nodes, making it nearly impossible to legally prove who was physically pressing the keys beyond a reasonable doubt.",
                                "3. Extradition Deficits & Safe Havens: Non-extradition treaties and political friction prevent foreign law enforcement from arresting cybercriminals residing in certain sovereign safe havens.",
                                "4. Disparity in National Legislation: Actions classified as severe cybercrimes in one country (e.g. unauthorized port scanning or speech violations) may be legal or unregulated in another."
                            ]
                        }
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
                    "definition": "International Cyber Cooperation encompasses multilateral treaties, law enforcement intelligence networks, and cross-border evidence preservation mechanisms used to investigate and prosecute transnational digital crimes.",
                    "theoryModules": [
                        {
                            "heading": "1. The Budapest Convention on Cybercrime (2001)",
                            "content": "Drafted by the Council of Europe, the Budapest Convention remains the gold standard multilateral treaty addressing internet offenses.",
                            "keyPoints": [
                                "Substantive Criminal Law: Requires signatory nations to enact domestic laws criminalizing unauthorized access, data interception, system interference, and computer-related fraud.",
                                "Procedural Investigative Powers: Grants police the authority to order expedited preservation of volatile digital data, real-time traffic monitoring, and server seizures.",
                                "24/7 Network of Contact Points: Establishes a round-the-clock emergency point of contact in every member state for instant urgent evidence preservation."
                            ]
                        },
                        {
                            "heading": "2. Mutual Legal Assistance Treaties (MLATs)",
                            "content": "MLATs are formal bilateral agreements between national governments enabling domestic prosecutors to request digital evidence, server logs, and subscriber records held by cloud providers in foreign nations.",
                            "keyPoints": [
                                "Limitations of Traditional MLAT: Requests typically require 6 to 18 months to navigate diplomatic channels, during which volatile server logs are often erased.",
                                "Modern Solutions: Initiatives like the US CLOUD Act allow direct law enforcement requests to cloud service providers under bilateral executive agreements."
                            ]
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
                    "definition": "The Cyber Kill Chain is a military-derived threat framework developed by Lockheed Martin that deconstructs a cyberattack into 8 sequential stages, identifying opportunities for defense-in-depth intervention at each step.",
                    "diagram":
"""+--------------------------------------------------------------------------+
|                     THE 8-PHASE CYBER KILL CHAIN                         |
+--------------------------------------------------------------------------+
| [1. Recon] -> [2. Scan] -> [3. Weaponize] -> [4. Deliver]               |
|      |                                             |                     |
| [8. Objectives] <- [7. C2 Beacon] <- [6. Install] <- [5. Exploit]         |
+--------------------------------------------------------------------------+""",
                    "theoryModules": [
                        {
                            "heading": "1. Comprehensive Phase-by-Phase Breakdown",
                            "content": "Advanced adversaries execute methodical multi-stage campaigns:",
                            "keyPoints": [
                                "Phase 1: Reconnaissance — Mining public OSINT, Shodan, WHOIS, DNS records, and employee LinkedIn profiles to map target organizational structure.",
                                "Phase 2: Scanning & Enumeration — Probing firewalls and open ports (using Nmap) to identify unpatched software versions (e.g. outdated Apache servers).",
                                "Phase 3: Weaponization — Coupling an exploit (e.g. CVE-2021-44228 Log4Shell) with a stealthy reverse payload or Trojan backdoor.",
                                "Phase 4: Delivery — Transmitting the weaponized payload to the victim via targeted spear-phishing emails, infected USB drives, or waterhole web attacks.",
                                "Phase 5: Exploitation — Triggering the vulnerability on the target host (e.g. buffer overflow, remote code execution) to execute malicious code.",
                                "Phase 6: Installation & Persistence — Establishing long-term persistence via registry run keys, scheduled background tasks, or hidden system services.",
                                "Phase 7: Command & Control (C2) — Establishing an encrypted channel back to the attacker's server (via HTTPS, DNS tunneling, or Tor) for remote commands.",
                                "Phase 8: Actions on Objectives — Fulfilling the ultimate criminal goal: exfiltrating customer databases, deploying ransomware encryptors, or sabotaging systems."
                            ]
                        }
                    ],
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
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Cyber Kill Chain (2m) -> 2. Draw 8-Phase Flow Diagram (2m) -> 3. Explain each Phase with Attacker Action + Defender SOC Countermeasure (8m) -> 4. Explain the 'Breaking the Chain' Concept (2m) -> 5. Conclusion (1m)"
                    },
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
                    "definition": "Case studies analyze the attack vectors, technical vulnerabilities, operational impacts, and mitigation lessons of landmark real-world cyber disasters.",
                    "theoryModules": [
                        {
                            "heading": "1. Technical Dissection of Major Cyber Attacks",
                            "content": "Real-world breaches illustrate how theoretical vulnerabilities manifest in catastrophic enterprise disruptions:",
                            "keyPoints": [
                                "WannaCry (2017): Autonomous worm exploiting NSA-leaked EternalBlue (SMBv1 MS17-010) flaw. Encrypted 200,000 systems in 150 nations, crippling UK National Health Service hospitals.",
                                "Yahoo Breach (2013-14): Spear-phishing compromised internal employee credentials, enabling attackers to mint forged auth cookies and steal 3 billion accounts.",
                                "Sony Pictures (2014): Destover wiper malware destroyed corporate file shares, leaked unreleased movies, and exposed confidential executive communications."
                            ]
                        }
                    ],
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
                    ],
                    "keyTakeaways": [
                        "Human spear-phishing remains the primary entry point for large-scale enterprise intrusions.",
                        "Legacy protocols (like SMBv1) left unpatched present critical risks to national infrastructure."
                    ]
                }
            ]
        },

        # =========================================================================
        # UNIT 2
        # =========================================================================
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
                    "definition": "Social Media Cybercrime refers to unlawful activities in which social networking platforms (Facebook, Instagram, X, LinkedIn, Telegram) are exploited as an operational vector, communication channel, or intelligence reservoir to execute fraud, harassment, or intrusions.",
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
                    "theoryModules": [
                        {
                            "heading": "1. Why Social Media is the Premier Cybercrime Breeding Ground",
                            "content": "Social media platforms create a unique psychological and technical ecosystem that cybercriminals systematically exploit. Unlike corporate email systems that employ aggressive spam filtering and SPF/DKIM verification, social media platforms allow direct, unvetted access to billions of active users.",
                            "keyPoints": [
                                "1. Massive Open-Source Intelligence (OSINT) Reservoir: Users routinely post vacation dates, birthdates, pet names, workplace promotions, and relationship status. Attackers harvest this telemetry to craft bespoke spear-phishing lures and answer password reset security questions.",
                                "2. Implicit Circle of Trust: Messages received via direct messages (DMs) from a compromised friend's profile bypass human skepticism because individuals instinctively trust their social network connections.",
                                "3. High Velocity of Virality: Deceptive links, fake crypto doubling giveaways, and malicious quizzes can spread to millions of users in minutes through retweets, shares, and automated bot swarms."
                            ]
                        },
                        {
                            "heading": "2. The 6 Core Elements in the Social Media Crime Framework",
                            "content": "Every cybercrime enacted on social platforms consists of 6 interrelated operational components:",
                            "keyPoints": [
                                "Victim: Individual users, corporate brands, teenagers, or employees with public profile exposure.",
                                "Attacker: Fraudsters, state-backed APT groups, commercial competitors, or automated bot networks.",
                                "Platform Infrastructure: The communication medium (Instagram, LinkedIn, X, Telegram, WhatsApp).",
                                "Target Information: Personally Identifiable Information (PII), credentials, or photos harvested from profiles.",
                                "Attack Vector / Mechanism: Phishing DMs, malicious QR codes, impersonation accounts, fake job offers, or romance scams.",
                                "Criminal Objective: Financial theft, corporate espionage, account hijack, reputation blackmail, or ideological propaganda."
                            ]
                        },
                        {
                            "heading": "3. Primary Criminal Objectives on Social Platforms",
                            "content": "Attackers leverage social networks to achieve distinct malicious goals:",
                            "keyPoints": [
                                "Financial Extortion & Fraud: Romance scams, fake cryptocurrency investments, and fake tech support scams.",
                                "Identity Theft & Clone Accounts: Scraping profile pictures to create duplicate accounts requesting money from friends.",
                                "Corporate Espionage: Posing as headhunters on LinkedIn to send weaponized PDF resumes to defense engineers."
                            ]
                        }
                    ],
                    "structureElements": [
                        { "element": "1. Victim", "desc": "Individual users, employees, teenagers, or organizations with exposed public profiles." },
                        { "element": "2. Attacker", "desc": "Fraudsters, state actors, commercial competitors, cyberstalkers, or automated bot networks." },
                        { "element": "3. Platform", "desc": "Social networking channels (Instagram, LinkedIn, X, Facebook, Telegram, WhatsApp)." },
                        { "element": "4. Information", "desc": "Target data mined from posts: workplace, family ties, location tags, habits, and phone numbers." },
                        { "element": "5. Attack Mechanism", "desc": "Phishing DMs, fake customer support handles, malicious links, romance lures, deepfakes." },
                        { "element": "6. Criminal Objective", "desc": "Financial extortion, credential harvesting, corporate espionage, account takeover, reputation ruin." }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Social Media Cybercrime (2m) -> 2. Draw 6-Element Structure Box Diagram (2m) -> 3. Explain 6 Elements in detail (6m) -> 4. Major Objectives with examples (3m) -> 5. Defense Measures & Conclusion (2m)"
                    },
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
                    "definition": "Social Engineering is the psychological manipulation of human beings into performing actions, divulging confidential credentials, or bypassing established security protocols, exploiting human cognitive vulnerabilities rather than software bugs.",
                    "theoryModules": [
                        {
                            "heading": "1. The Psychology of Human Hacking",
                            "content": "Legendary security expert Kevin Mitnick famously stated: 'The human factor is the weakest link in the security chain.' Firewalls, encryption algorithms, and intrusion detection systems are completely bypassed if an authorized administrator voluntarily hands over their password to a persuasive impostor.",
                            "keyPoints": [
                                "Cognitive Heuristics: The human brain relies on mental shortcuts (trusting authority, helping others, acting quickly in emergencies). Attackers deliberately trigger these cognitive reflexes to suppress rational skepticism.",
                                "Lack of Cyber Hygiene: Untrained employees do not recognize the subtle indicators of spoofed domains or suspicious telephone pretexts."
                            ]
                        },
                        {
                            "heading": "2. The 6 Universal Psychological Triggers Exploited by Attackers",
                            "content": "Social engineering attacks rely on manipulating one or more core human emotions:",
                            "keyPoints": [
                                "1. Authority: Humans are conditioned to obey perceived authority figures (CEOs, police officers, tax inspectors, senior IT engineers). Attackers impersonate executives to demand urgent wire transfers.",
                                "2. Urgency: Creating artificial time pressure ('Your bank account will be permanently blocked in 10 minutes!') disables the victim's rational analysis, forcing hasty compliance.",
                                "3. Fear & Intimidation: Threatening legal arrest, public embarrassment, or system shutdown to compel immediate obedience.",
                                "4. Greed / Lure of Reward: Enticing victims with lottery prizes, high-paying work-from-home jobs, or cryptocurrency windfalls.",
                                "5. Trust & Social Proof: Posing as a familiar colleague or leveraging the fact that 'everyone else in the department has already complied'.",
                                "6. Helpfulness & Curiosity: Appealing to the natural human desire to assist someone in distress or clicking intriguing links ('Look at this leaked video!')."
                            ]
                        }
                    ],
                    "psychologicalTriggers": [
                        { "trigger": "1. Authority", "desc": "Victims obey perceived figures of power (e.g. CEO, police officer, IT director, tax department)." },
                        { "trigger": "2. Urgency", "desc": "Creating artificial time pressure ('Account suspended in 15 minutes!') disabling rational cognitive review." },
                        { "trigger": "3. Fear & Intimidation", "desc": "Threatening legal arrest, public humiliation, or malware infection to force compliance." },
                        { "trigger": "4. Greed & Reward", "desc": "Luring victims with crypto prizes, high-paying jobs, discount coupons, or inheritance claims." },
                        { "trigger": "5. Trust & Social Proof", "desc": "Pretending to be a known colleague, mutual friend, or reputable brand." },
                        { "trigger": "6. Curiosity & Helpfulness", "desc": "Appealing to human helpfulness ('Can you hold the door?') or curiosity ('Check this leaked photo!')." }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Social Engineering (2m) -> 2. Quote Kevin Mitnick's principle (1m) -> 3. Explain the 6 Psychological Triggers in detail with real scenarios (8m) -> 4. Organizational Defense Mechanisms (3m) -> 5. Conclusion (1m)"
                    },
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
                    "definition": "Social engineering techniques encompass a diverse taxonomy of digital, telephonic, and physical methodologies used to exploit human behavior.",
                    "theoryModules": [
                        {
                            "heading": "1. In-Depth Dissection of Social Engineering Methodologies",
                            "content": "Examining the mechanisms, vectors, and real-world execution of all major techniques:",
                            "keyPoints": [
                                "Phishing: Broad mass fraudulent communication (emails, SMS, web) imitating trusted institutions (banks, Netflix, Amazon) to harvest credentials.",
                                "Pretexting: Creating an elaborate fabricated story (pretext) to establish trust. The attacker pretends to be an auditor conducting an emergency compliance review requiring temporary VPN access.",
                                "Baiting: Enticing victims with a physical or digital lure. Leaving infected USB drives labeled 'Executive Compensation 2024' in corporate lobbies, relying on victim curiosity to plug them in.",
                                "Quid Pro Quo: Offering an explicit favor or service in direct exchange for passwords or security bypass ('I am from IT support calling to optimize your PC performance; disable your antivirus').",
                                "Tailgating / Piggybacking: Physical social engineering where an attacker dressed as a delivery courier holding heavy boxes asks an employee to hold a badge-access security door open.",
                                "Impersonation & BEC: Posing as a company executive to trick finance managers into executing fraudulent high-value international wire transfers.",
                                "Scareware: Frightening pop-up alerts claiming severe malware infection to trick users into downloading rogue antivirus software."
                            ]
                        }
                    ],
                    "techniques": [
                        {
                            "name": "1. Phishing",
                            "mechanism": "Mass fraudulent communications impersonating reputable entities to trick users into revealing credentials.",
                            "example": "Fake email mimicking Netflix asking user to update credit card details via spoofed link."
                        },
                        {
                            "name": "2. Pretexting",
                            "mechanism": "Creating an elaborate fabricated scenario (pretext) to establish trust and extract specific sensitive info.",
                            "example": "Attacker calls employee claiming to be corporate Auditor needing temporary VPN credentials for audit."
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
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Overview of Social Engineering (2m) -> 2. Differentiate Pretexting vs Phishing & Baiting vs Quid Pro Quo (4m) -> 3. Explain all 7 Techniques with distinct examples (7m) -> 4. Technical + Human Countermeasures (2m)"
                    },
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
                    "definition": "Case studies demonstrating the profound impact of social engineering and third-party data harvesting on global digital platforms.",
                    "theoryModules": [
                        {
                            "heading": "1. Deep Dive: Twitter (X) 2020 Administrative Hijacking",
                            "content": "In July 2020, teenagers used phone spear-phishing (vishing) targeting remote Twitter customer support employees. Posing as Twitter internal IT staff, they tricked employees into entering their VPN credentials into a lookalike phishing portal. Gaining access to Twitter's internal Customer Support Tool ('Admin Dashboard'), the attackers hijacked 130 celebrity accounts (Barack Obama, Elon Musk, Bill Gates, Apple, Joe Biden) and tweeted a Bitcoin doubling scam that netted $120,000 in hours.",
                            "keyPoints": [
                                "Key Failure: Over-privileged internal admin tools lacked hardware multi-factor authentication (FIDO2) and dual-authorization approval for account resets."
                            ]
                        },
                        {
                            "heading": "2. Deep Dive: Cambridge Analytica & Facebook Data Scandal (2018)",
                            "content": "A researcher created a personality quiz app ('This Is Your Digital Life') on Facebook, downloaded by ~270,000 users. Due to Facebook's loose API permissions at the time, the app harvested not just the user's data, but the complete personal data of all their Facebook friends without their explicit consent—compromising 87 million profiles for psychological political profiling.",
                            "keyPoints": [
                                "Key Failure: Inadequate API boundary enforcement and lack of fine-grained third-party data isolation."
                            ]
                        }
                    ],
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
                    ],
                    "keyTakeaways": [
                        "Vishing attacks can successfully compromise internal employee credentials even in major tech companies.",
                        "Third-party API access controls must strictly isolate user social graphs."
                    ]
                },
                {
                    "id": "u2-t5",
                    "unitId": 2,
                    "title": "Cyberstalking: Behaviors, Taxonomy & Legal Protection",
                    "tag": "Cyberstalking",
                    "summary": "Repeated, persistent harassment, surveillance, and intimidation of a victim utilizing digital technology.",
                    "definition": "Cyberstalking is the repeated, deliberate, and hostile pursuit, surveillance, harassment, or intimidation of an individual utilizing telecommunication devices, email, social media, or internet platforms to induce severe emotional distress or fear of physical harm.",
                    "theoryModules": [
                        {
                            "heading": "1. Direct vs Indirect Cyberstalking Taxonomy",
                            "content": "Cyberstalking manifests through two primary operational behaviors:",
                            "keyPoints": [
                                "Direct Cyberstalking: The stalker communicates directly with the victim: sending hundreds of threatening emails/DMs daily, making silent nuisance phone calls, hacking the victim's accounts, or installing stalkerware to track their live GPS location.",
                                "Indirect Cyberstalking: The stalker acts through third parties or the public: creating fake matrimonial/dating profiles in the victim's name, posting false rumors, doxxing personal contact numbers, and inciting cyber mobs to harass the victim."
                            ]
                        },
                        {
                            "heading": "2. Legal Provisions & Digital Evidence Preservation",
                            "content": "Statutory legal frameworks and digital evidence best practices:",
                            "keyPoints": [
                                "Indian Information Technology Act 2000: Section 66E (Privacy violation), Section 67 (Publishing obscene content in electronic form).",
                                "Indian Penal Code (IPC): Section 354D specifically criminalizes stalking (both physical and electronic) with up to 3-5 years imprisonment.",
                                "Digital Evidence Integrity: Victims must preserve unaltered screenshots, full email RFC 822 headers, web URLs, chat logs, and report to national cyber portals (cybercrime.gov.in)."
                            ]
                        }
                    ],
                    "behaviors": [
                        { "type": "Direct Cyberstalking", "details": "Directly sending threatening or abusive emails, DMs, unwanted calls, bombarding messages, and real-time GPS tracking." },
                        { "type": "Indirect Cyberstalking", "details": "Creating fake profiles in the victim's name, posting defamatory rumors, doxxing personal contact info, and inciting mob harassment." }
                    ],
                    "legalAspects": [
                        "Indian IT Act 2000: Section 66E (Privacy violation), Section 67 (Publishing obscene content), Section 354D of Indian Penal Code (IPC) specifically criminalizes stalking.",
                        "Evidence preservation: Retain exact timestamps, message headers, URLs, unaltered screenshots, and report to national cyber portals (cybercrime.gov.in)."
                    ],
                    "keyTakeaways": [
                        "Cyberstalking includes both direct harassment and indirect third-party impersonation.",
                        "Preserving unaltered email headers and timestamps is vital for forensic prosecution."
                    ]
                },
                {
                    "id": "u2-t6",
                    "unitId": 2,
                    "title": "Cybercrime Ecosystem & Cybercrime-as-a-Service (CaaS)",
                    "tag": "Underground Economy",
                    "summary": "How organized digital crime operates as a commercial underground economy with specialized supply chains.",
                    "definition": "Cybercrime-as-a-Service (CaaS) is a commercial underground business model where malware developers, botnet operators, and access brokers lease their cyberweaponry, infrastructure, and technical expertise to other criminals on a subscription or profit-sharing basis.",
                    "theoryModules": [
                        {
                            "heading": "1. The Industrialization of Modern Cybercrime",
                            "content": "Cybercrime has transitioned from isolated hackers into a specialized global marketplace with division of labor:",
                            "keyPoints": [
                                "1. Ransomware-as-a-Service (RaaS): Core authors build military-grade ransomware encryptors and negotiation portals, leasing them to 'affiliates' who execute network intrusions for a 20-30% cut.",
                                "2. Phishing-as-a-Service (PhaaS): Automated platforms (e.g. Evilginx kits) providing ready-to-deploy phishing portals that bypass multi-factor authentication (MFA).",
                                "3. Initial Access Brokers (IABs): Threat actors specializing solely in breaching enterprise networks (via compromised VPN/RDP credentials) and selling active footholds on darknet forums.",
                                "4. DDoS-for-Hire (Booters/Stressers): Web portals allowing non-technical paying customers to launch multi-hundred Gbps floods against gaming servers or competitors.",
                                "5. Cryptocurrency Mixers & Tumblers: Automated laundering services that mix illicit cryptocurrency transactions with legitimate traffic to break the blockchain forensic trail."
                            ]
                        }
                    ],
                    "caasComponents": [
                        { "service": "Ransomware-as-a-Service (RaaS)", "desc": "Core developers lease ransomware builders and payment portals to 'affiliates' for a 20-30% profit split." },
                        { "service": "Phishing-as-a-Service (PhaaS)", "desc": "Ready-to-deploy phishing portals with automated 2FA bypass (Evilginx) available on monthly subscriptions." },
                        { "service": "Initial Access Brokers (IABs)", "desc": "Hackers specializing in compromising enterprise VPN/RDP credentials, selling active footholds to ransomware syndicates." },
                        { "service": "Botnet-for-Hire (DDoS Booters)", "desc": "Commercial web portals allowing paying users to launch multi-hundred Gbps DDoS strikes against targets." },
                        { "service": "Crypto Laundering & Mixers", "desc": "Tumbler services breaking transactional links in public blockchain ledgers to launder illicit extortion proceeds." }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define CaaS and underground economy (2m) -> 2. Draw Supply Chain Diagram (2m) -> 3. Explain RaaS, PhaaS, IABs, Booters, and Mixers (8m) -> 4. Challenges in Forensic Investigation (3m)"
                    },
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
                    "definition": "A Botnet is an interconnected network of Internet-connected computing devices (PCs, servers, IoT cameras, smart home routers) that have been infected with malicious software and placed under the coordinated remote control of a 'Botmaster'.",
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
+-------------------------------------------------------------+""",
                    "theoryModules": [
                        {
                            "heading": "1. Botnet Topologies: Centralized vs Peer-to-Peer (P2P)",
                            "content": "Botnets are engineered with distinct command-and-control (C2) topologies:",
                            "keyPoints": [
                                "Centralized C2 (IRC / HTTP / HTTPS): All zombie bots connect directly to a centralized server. Strengths: Instant command execution and easy synchronization. Vulnerability: Single Point of Failure (SPOF)—taking down or seizing the C2 domain/IP neutralizes the entire botnet.",
                                "Peer-to-Peer (P2P): Bots communicate directly with adjacent peer nodes. Commands are cryptographically signed by the Botmaster and propagated node-to-node across the mesh. Strengths: Highly resilient to law enforcement takedown; no single server to seize.",
                                "Hybrid / DGA (Domain Generation Algorithm): Bots use mathematical seed algorithms to generate thousands of pseudo-random domain names daily, checking which domain the botmaster has registered."
                            ]
                        },
                        {
                            "heading": "2. The 5 Stages of the Botnet Infection Lifecycle",
                            "content": "From initial infiltration to coordinated attack execution:",
                            "keyPoints": [
                                "1. Infiltration & Exploit: Malware infects vulnerable device via credential brute-forcing, unpatched vulnerability, or phishing download.",
                                "2. Installation & Stealth Persistence: Malware establishes itself as a silent background daemon, disabling local security logs and competing malware.",
                                "3. C2 Beaconing (Call Home): The newly infected bot connects to the C2 network and registers its hardware profile, IP address, and bandwidth capacity.",
                                "4. Command Awaiting: The bot enters low-activity sleep mode, polling for encrypted instructions.",
                                "5. Coordinated Execution: The Botmaster issues a synchronous attack order: launching a 500 Gbps DDoS flood, blasting spam emails, or mining cryptocurrency."
                            ]
                        },
                        {
                            "heading": "3. The Mirai Botnet Landmark Case Study (2016)",
                            "content": "In October 2016, the Mirai botnet infected over 600,000 IoT devices (CCTV surveillance cameras, DVRs, home routers) by continuously scanning the Internet for open Telnet ports (23/2323) and testing a hardcoded dictionary of 62 default factory passwords (e.g. admin/admin, root/xc3511). Mirai unleashed a record 1.2 Tbps DDoS attack against Dyn DNS, temporarily knocking major platforms (Twitter, Netflix, GitHub, Spotify) offline across North America and Europe.",
                            "keyPoints": [
                                "Mirai demonstrated the extreme vulnerability of the Internet of Things (IoT) ecosystem.",
                                "Mandated modern IoT security legislation requiring unique per-device factory passwords."
                            ]
                        }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Botnet & Zombie node (2m) -> 2. Draw Centralized vs P2P Topology Diagrams (3m) -> 3. Explain 5-Stage Lifecycle (4m) -> 4. Mirai Botnet Case Study & Technical Impact (4m) -> 5. Mitigation Strategies (2m)"
                    },
                    "keyTakeaways": [
                        "P2P botnets eliminate Single Points of Failure, making them much harder to dismantle.",
                        "The Mirai botnet proved that insecure IoT devices with default passwords pose massive infrastructure risks."
                    ]
                },
                {
                    "id": "u2-t8",
                    "unitId": 2,
                    "title": "Attack Vectors & Defense-in-Depth Strategy",
                    "tag": "Defense Strategy",
                    "summary": "Classifying paths of cyber infiltration and constructing multi-layered organizational defenses.",
                    "definition": "Defense-in-Depth is a comprehensive cybersecurity strategy that deploys multiple layers of defensive controls throughout an information technology ecosystem so that if one mechanism fails, subsequent layers immediately contain the threat.",
                    "theoryModules": [
                        {
                            "heading": "1. The 6 Concentric Layers of Enterprise Defense",
                            "content": "Relying on a single firewall or antivirus is insufficient against modern cyber threats:",
                            "keyPoints": [
                                "1. Perimeter Layer: Next-Generation Firewalls (NGFW), Web Application Firewalls (WAF), and Cloud DDoS Scrubbing filters.",
                                "2. Network Layer: Internal micro-segmentation, Intrusion Detection/Prevention Systems (IDS/IPS), and Zero Trust Network Access (ZTNA).",
                                "3. Endpoint Layer: Endpoint Detection and Response (EDR), Full-Disk Encryption, and Antivirus with behavioral heuristics.",
                                "4. Application Layer: Secure software development lifecycle (SAST/DAST code reviews), input validation, and API authentication tokens.",
                                "5. Data Layer: Strong cryptographic encryption at rest (AES-256) and in transit (TLS 1.3), accompanied by Data Loss Prevention (DLP).",
                                "6. Human Layer: Continuous phishing simulation drills, mandatory Multi-Factor Authentication (MFA), and security awareness training."
                            ]
                        }
                    ],
                    "defenseInDepth": [
                        { "layer": "Perimeter Layer", "controls": "Next-Gen Firewalls, Web Application Firewalls (WAF), DDoS Scrubbing" },
                        { "layer": "Network Layer", "controls": "Network Segmentation, Intrusion Detection & Prevention Systems (IDS/IPS), Zero Trust" },
                        { "layer": "Endpoint Layer", "controls": "Endpoint Detection and Response (EDR), Antivirus, Device Encryption" },
                        { "layer": "Application Layer", "controls": "Secure Code Audits (SAST/DAST), Input Validation, Least Privilege Access" },
                        { "layer": "Data Layer", "controls": "Encryption at rest and in transit (AES-256, TLS 1.3), Data Loss Prevention (DLP)" },
                        { "layer": "Human Layer", "controls": "Periodic Phishing Simulations, Security Training, Multi-Factor Authentication (MFA)" }
                    ],
                    "keyTakeaways": [
                        "Defense-in-Depth ensures that no single point of security failure can compromise the entire enterprise.",
                        "The human layer remains the most frequently targeted boundary."
                    ]
                }
            ]
        },

        # =========================================================================
        # UNIT 3
        # =========================================================================
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
                    "definition": "Mobile Cyber Crime refers to illegal acts targeting or executed via smartphones, tablets, wearables, and wireless communication protocols (Wi-Fi, Cellular 4G/5G, Bluetooth, NFC).",
                    "diagram":
"""+-------------------------------------------------------------+
|               MOBILE / WIRELESS ATTACK SURFACE              |
+-------------------------------------------------------------+
|                                                             |
|   [ Mobile Device ] <=====> [ Wireless Network ] <====> [ Web ]
|         |                           |                     |
|   - Mobile Malware            - Rogue AP / Evil Twin  - Phishing
|   - Insecure Apps             - MITM / Eavesdropping  - SIM Swap
|   - Rooting / Jailbreak       - Bluetooth Bluebugging - Card Fraud
+-------------------------------------------------------------+""",
                    "theoryModules": [
                        {
                            "heading": "1. Why Mobile Devices are Uniquely Vulnerable",
                            "content": "Unlike stationary enterprise desktop computers protected behind corporate firewalls and monitored by Security Operations Centers (SOCs), mobile devices operate in hostile environments:",
                            "keyPoints": [
                                "1. Physical Portability and Theft: Smartphones are easily misplaced, stolen, or physically accessed in public areas, exposing cached corporate email tokens and saved credentials.",
                                "2. Inherent Auto-Association with Wireless: Mobile operating systems actively probe and auto-connect to open Wi-Fi access points without user intervention, making them susceptible to Evil Twin attacks.",
                                "3. OS Ecosystem Fragmentation: Millions of Android smartphones remain on deprecated, unpatched operating system versions due to delays by hardware manufacturers in releasing security updates.",
                                "4. Smartphone as Identity Anchor: Because banks and online services use SMS OTPs and authenticator apps on phones for 2-Factor Authentication, compromising the mobile phone compromises the user's entire digital life."
                            ]
                        }
                    ],
                    "challenges": [
                        { "issue": "1. Physical Portability & Theft", "desc": "High risk of device loss or physical theft carrying enterprise emails, saved sessions, and cached credentials." },
                        { "issue": "2. Insecure Public Wireless Networks", "desc": "Smartphones automatically probe and connect to open Wi-Fi hotspots, exposing traffic to eavesdropping." },
                        { "issue": "3. OS Fragmentation & Slow Updates", "desc": "Android ecosystem fragmentation leads to millions of devices running outdated, unpatched OS versions." },
                        { "issue": "4. Aggressive App Permissions", "desc": "Apps requesting unnecessary permissions (Contacts, Location, Microphone, SMS) and leaking sensitive telemetry." },
                        { "issue": "5. Sideloading & Third-Party App Stores", "desc": "Installing unverified APK files bypassing official Google Play or Apple App Store security checks." }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Mobile Cybercrime (2m) -> 2. Draw Mobile Attack Surface Diagram (2m) -> 3. Explain 5 Core Vulnerabilities in detail (7m) -> 4. Compare Mobile vs Desktop Security (3m) -> 5. Conclusion (1m)"
                    },
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
                    "definition": "Rooting (Android) or Jailbreaking (iOS) is the process of modifying the mobile operating system kernel to bypass built-in security constraints, obtaining root/superuser privileges (UID 0).",
                    "theoryModules": [
                        {
                            "heading": "1. Mobile Operating System Sandboxing Breakdown",
                            "content": "In a secure mobile OS, application sandboxing ensures that every application runs inside its own isolated virtual environment with a unique User ID (UID). App A cannot read App B's memory, databases, or saved passwords.",
                            "keyPoints": [
                                "Catastrophic Impact of Rooting: Rooting destroys the sandbox boundary. A single malicious sideloaded game can request `su` (superuser) permissions to inspect banking apps, dump SMS messages, and harvest encryption keys.",
                                "Disabled Integrity Verification: Rooted devices fail Google SafetyNet and Play Integrity API verification, preventing banking applications and enterprise MDMs from functioning securely.",
                                "Blocked Over-The-Air (OTA) Updates: Rooted devices frequently fail automatic security patch installations, leaving them permanently vulnerable to known zero-day vulnerabilities."
                            ]
                        },
                        {
                            "heading": "2. Primary Classes of Mobile Malware",
                            "content": "Malware engineered specifically for mobile architectures:",
                            "keyPoints": [
                                "Banking Overlay Trojans (e.g. Alien, Cerberus, FluBot): Detects when the user opens a legitimate banking application and instantly draws an identical translucent fake login screen over it to harvest credentials.",
                                "Toll Fraud & SMS Interceptors (e.g. Joker malware): Silently subscribes the victim's device to expensive premium SMS services and intercepts 2FA bank codes.",
                                "Zero-Click Commercial Spyware (e.g. NSO Group Pegasus): Infiltrates devices via iMessage or WhatsApp zero-day memory corruption bugs without requiring user interaction, activating microphones, cameras, and GPS."
                            ]
                        }
                    ],
                    "rootingRisks": [
                        { "risk": "Destruction of OS Sandbox", "detail": "Mobile OS sandboxing prevents App A from accessing App B's memory. Rooting completely dismantles this security barrier." },
                        { "risk": "Root Privilege Escalation", "detail": "Any malicious sideloaded app can obtain superuser (SU) privileges, reading internal database files and keychains." },
                        { "risk": "Disabled Integrity Checks", "detail": "SafetyNet / Play Integrity API fails, preventing secure enterprise MDM and banking apps from functioning." },
                        { "risk": "Blocked OTA Updates", "detail": "Rooted devices often fail automatic security patch installations, remaining permanently vulnerable." }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Rooting/Jailbreaking (2m) -> 2. Explain Mobile OS Sandboxing Architecture (3m) -> 3. Detail 4 Catastrophic Risks of Rooting (5m) -> 4. Explain 3 Mobile Malware Types (Banking Overlay, SMS Interceptor, Spyware) (4m) -> 5. Conclusion (1m)"
                    },
                    "keyTakeaways": [
                        "Rooting permanently breaks the OS security sandbox, allowing any malicious app to access all system data.",
                        "Banking overlay Trojans exploit accessibility services to steal credentials over legitimate apps."
                    ]
                },
                {
                    "id": "u3-t3",
                    "unitId": 3,
                    "title": "Credit Card Frauds, Payment Security & SIM Swap Fraud",
                    "tag": "Payment Security",
                    "summary": "Techniques used to compromise digital payments, skimming, Card Not Present (CNP) fraud, and the complete mechanics of SIM Swap attacks.",
                    "definition": "SIM Swap Fraud is an identity theft attack where an adversary socially engineers a mobile carrier into porting the victim's cellular phone number onto an attacker-controlled SIM card, intercepting SMS-based 2FA one-time passwords (OTPs).",
                    "diagram":
"""+-------------------------------------------------------------+
|                 SIM SWAP ATTACK STEP-BY-STEP                |
+-------------------------------------------------------------+
| 1. OSINT/Phishing -> Attacker steals victim Name & ID data  |
|         |                                                   |
| 2. Carrier Social Eng -> Attacker visits carrier store      |
|         |                claiming "Lost SIM card"           |
| 3. SIM Reissuance -> Carrier issues new SIM to attacker     |
|         |                                                   |
| 4. Outage -> Victim's phone loses network ("No Service")    |
|         |                                                   |
| 5. OTP Intercept -> Attacker resets bank password & drains  |
|                     funds using SMS OTP received on new SIM |
+-------------------------------------------------------------+""",
                    "theoryModules": [
                        {
                            "heading": "1. Digital Payment & Credit Card Fraud Methodologies",
                            "content": "Digital payment channels are targeted through multiple exploitation vectors:",
                            "keyPoints": [
                                "Physical Skimming: Concealing magnetic stripe card readers and pinhole cameras over ATM and POS card insertion slots to clone card data and record PIN numbers.",
                                "Card-Not-Present (CNP) Fraud: Utilizing stolen card numbers, CVVs, and expiry dates on e-commerce websites without possessing physical cards.",
                                "POS RAM Scraping: Deploying memory-scraping malware (e.g. BlackPOS) inside retail point-of-sale systems to capture unencrypted card track 2 data directly from system RAM before encryption occurs."
                            ]
                        },
                        {
                            "heading": "2. Step-by-Step Lifecycle of SIM Swap Fraud",
                            "content": "A high-impact attack vector bypassing traditional SMS-based multi-factor authentication:",
                            "keyPoints": [
                                "Step 1 (Target Profiling): Attacker gathers victim's personal info (Name, DOB, Aadhaar/ID) through phishing or darknet data dumps.",
                                "Step 2 (Carrier Social Engineering): Attacker visits a mobile carrier store presenting forged identity documents, claiming their phone was lost.",
                                "Step 3 (SIM Porting): The carrier representative invalidates the original SIM and activates a replacement blank SIM card in the attacker's phone.",
                                "Step 4 (Network Disconnection): The victim's real mobile phone suddenly displays 'No Service' or 'Emergency Calls Only'.",
                                "Step 5 (OTP Interception & Account Draining): The attacker initiates password resets on the victim's banking and crypto accounts, receiving all 2FA SMS OTP codes directly on the newly activated SIM."
                            ]
                        }
                    ],
                    "simSwapLifecycle": [
                        "1. Target Profiling: Attacker gathers victim's personal data (Name, DOB, ID number) via phishing or leaks.",
                        "2. Telecom Social Engineering: Attacker visits telecom store claiming lost phone with forged identity ID.",
                        "3. SIM Reissuance: Telecom issues a new replacement SIM linked to victim's phone number.",
                        "4. Service Termination: Victim's real SIM card immediately loses network connectivity ('No Service').",
                        "5. OTP Interception: Attacker initiates bank password resets, receiving all 2FA OTP codes on the new SIM.",
                        "6. Account Draining: Funds are instantly transferred to burner crypto wallets or mule accounts."
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Credit Card Fraud & SIM Swap (2m) -> 2. Draw Step-by-Step SIM Swap Box Diagram (2m) -> 3. Detail all 5 Steps of SIM Swap (5m) -> 4. Explain Skimming vs CNP Fraud (3m) -> 5. Prevention Strategies (Tokenization, FIDO2 Keys) (3m)"
                    },
                    "keyTakeaways": [
                        "SMS-based 2FA is fundamentally insecure against SIM Swap attacks.",
                        "Users must adopt hardware security keys (FIDO2) or software TOTP authenticator apps."
                    ]
                },
                {
                    "id": "u3-t4",
                    "unitId": 3,
                    "title": "Registry & Mobile OS Security Configurations",
                    "tag": "OS Hardening",
                    "summary": "Essential security parameters and registry configurations for hardening Android and iOS mobile operating systems.",
                    "definition": "Mobile OS Hardening involves configuring device policies, system permissions, and cryptographic parameters to eliminate attack vectors and prevent unauthorized data exfiltration.",
                    "theoryModules": [
                        {
                            "heading": "1. Comprehensive Mobile Security Baseline Checklist",
                            "content": "Key configurations required to secure mobile endpoints against compromise:",
                            "keyPoints": [
                                "Screen Lock & Automatic Timeout: Enforce a minimum 6-digit alphanumeric PIN or biometrics with automatic lock after 1-2 minutes of inactivity.",
                                "Hardware Storage Encryption: Enable File-Based Encryption (FBE) backed by secure hardware enclaves (ARM TrustZone / Apple Secure Enclave / Samsung Knox).",
                                "Strict Application Permission Auditing: Restrict dangerous background permissions (Location, Camera, Microphone, SMS, Accessibility) on all non-system apps.",
                                "Disable Unknown Sources: Keep 'Install Unknown Apps' permanently disabled to prevent drive-by sideloading of trojanized APKs.",
                                "Lock Developer Options & USB Debugging: Ensure USB Debugging (ADB) is disabled to prevent data theft via malicious public charging stations ('Juice Jacking').",
                                "Enable Remote Lock and Wipe: Maintain active Google Find My / Apple Find My or corporate MDM enrollment for emergency data destruction if the device is lost."
                            ]
                        }
                    ],
                    "keyTakeaways": [
                        "Hardware-backed encryption ensures data remains unreadable even if storage chips are physically extracted.",
                        "USB debugging should always remain disabled on production mobile devices."
                    ]
                },
                {
                    "id": "u3-t5",
                    "unitId": 3,
                    "title": "Authentication Service Security & The 5 Factors",
                    "tag": "Authentication",
                    "summary": "The 5 distinct authentication factor categories used to verify digital identity securely.",
                    "definition": "Authentication is the cryptographic and logical process of verifying the claimed identity of a user or system before granting access to protected resources.",
                    "theoryModules": [
                        {
                            "heading": "1. The 5 Distinct Authentication Factor Categories",
                            "content": "Enterprise security relies on 5 independent authentication dimensions:",
                            "keyPoints": [
                                "1. Something You Know (Knowledge Factor): Passwords, PINs, Passphrases, Security Answers. Vulnerability: Susceptible to brute-force, dictionary attacks, and phishing.",
                                "2. Something You Have (Possession Factor): Hardware FIDO2 keys (YubiKey), Smart cards, TOTP software tokens (Google Authenticator), SMS OTPs. Vulnerability: Physical theft or SIM swapping.",
                                "3. Something You Are (Inherence / Biometric Factor): Fingerprint, Iris scan, Facial recognition, Retina pattern. Vulnerability: Cannot be reset if compromised; biometric mold spoofing.",
                                "4. Somewhere You Are (Location Factor): GPS geofencing, IP geolocation, authorized enterprise subnet ranges. Vulnerability: GPS spoofing apps and VPN proxy tunnels.",
                                "5. Something You Do (Behavioral Factor): Keystroke typing dynamics, touchscreen swipe velocity, mouse trajectory patterns. Vulnerability: Requires continuous baseline machine learning."
                            ]
                        },
                        {
                            "heading": "2. True Multi-Factor Authentication (MFA) vs Two-Step Verification",
                            "content": "A critical examination concept: True MFA requires combining factors from AT LEAST TWO DIFFERENT factor categories (e.g. Knowledge + Inherence = Password + Fingerprint). Combining a Password + Security Question is NOT MFA—it is merely two instances of the Knowledge factor.",
                            "keyPoints": [
                                "Single-Factor (Two instances of same category): Password + PIN (Both 'Something You Know').",
                                "True Multi-Factor: Password ('Know') + Hardware Token ('Have') + Fingerprint ('Are')."
                            ]
                        }
                    ],
                    "factors": [
                        { "factor": "1. Something You Know (Knowledge)", "desc": "Static passwords, PIN codes, passphrases, security answer questions.", "weakness": "Vulnerable to phishing, brute-force, dictionary attacks, and credential reuse." },
                        { "factor": "2. Something You Have (Possession)", "desc": "Hardware security keys (YubiKey), smart cards, software TOTP tokens (Google Authenticator), SMS OTP.", "weakness": "Physical theft or SIM swap interception." },
                        { "factor": "3. Something You Are (Inherence)", "desc": "Biological traits: Fingerprint, Face ID, Iris scan, Retina scan, Voice recognition.", "weakness": "Cannot be changed if compromised; spoofing via high-res molds or deepfakes." },
                        { "factor": "4. Somewhere You Are (Location)", "desc": "GPS coordinates, authorized enterprise subnet IP ranges, cellular cell tower bounds.", "weakness": "GPS spoofing apps, VPN proxy obfuscation." },
                        { "factor": "5. Something You Do (Behavior)", "desc": "Keystroke typing dynamics, touchscreen swipe velocity, mouse trajectory patterns.", "weakness": "Requires continuous machine learning baselining." }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Authentication (2m) -> 2. Detail the 5 Factors with examples and vulnerabilities (8m) -> 3. Explain True MFA vs Single-Factor (3m) -> 4. Conclusion (2m)"
                    },
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
                    "definition": "Wireless Network Attacks exploit vulnerabilities in 802.11 Wi-Fi protocols, radio frequency broadcasts, and network routing to intercept unencrypted communications or hijack active sessions.",
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
+-------------------------------------------------------------+""",
                    "theoryModules": [
                        {
                            "heading": "1. Evil Twin & Rogue Access Point Mechanics",
                            "content": "How attackers exploit 802.11 wireless association protocols:",
                            "keyPoints": [
                                "Evil Twin Attack: The attacker deploys a rogue Wi-Fi hotspot broadcasting the exact same SSID network name as a legitimate public network (e.g. 'Airport_Free_WiFi') with higher signal power (dBm). Victim mobile devices automatically disconnect from the weaker legitimate AP and associate with the rogue AP.",
                                "SSL Stripping: The attacker intercepts HTTPS redirect requests, downgrading the victim's connection to unencrypted HTTP, allowing plaintext credential harvesting.",
                                "ARP Poisoning / Spoofing: Transmitting forged Address Resolution Protocol replies across the local subnet, linking the default gateway's IP to the attacker's MAC address."
                            ]
                        },
                        {
                            "heading": "2. KRACK (Key Reinstallation Attack against WPA2)",
                            "content": "In 2017, researcher Mathy Vanhoef discovered KRACK, which exploits a design flaw in the 4-way cryptographic handshake of WPA2 Wi-Fi. By tricking a client into reinstalling an already-in-use encryption key (nonce reset to 0), attackers can decrypt WPA2 traffic without needing the Wi-Fi password.",
                            "keyPoints": [
                                "Prompted the development and deployment of the WPA3 standard with Simultaneous Authentication of Equals (SAE)."
                            ]
                        }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Overview of Wireless Attacks (2m) -> 2. Draw Evil Twin Network Flow Diagram (2m) -> 3. Step-by-Step Explanation of Evil Twin & SSL Stripping (5m) -> 4. ARP Poisoning & KRACK (4m) -> 5. WPA3 & VPN Defenses (2m)"
                    },
                    "keyTakeaways": [
                        "Never transmit credentials over open public Wi-Fi without an active corporate VPN tunnel.",
                        "WPA3 Enterprise provides robust protection against 4-way handshake downgrade attacks."
                    ]
                },
                {
                    "id": "u3-t7",
                    "unitId": 3,
                    "title": "Bluetooth Security Attacks (Bluejacking, Bluesnarfing, Bluebugging)",
                    "tag": "Bluetooth Security",
                    "summary": "Comparing the triad of Bluetooth exploits by severity, exploitation mechanism, and impact.",
                    "definition": "Bluetooth Attacks exploit vulnerabilities in short-range 2.4 GHz wireless personal area network (PAN) protocols (OBEX, RFCOMM, L2CAP) to spam, extract data, or hijack mobile devices.",
                    "theoryModules": [
                        {
                            "heading": "1. The Triad of Bluetooth Attacks: Comparative Dissection",
                            "content": "Bluetooth exploits range from minor nuisances to full device takeover:",
                            "keyPoints": [
                                "1. Bluejacking (Severity: Low / Nuisance): Sending unsolicited electronic business cards (vCards) or text spam to discoverable Bluetooth devices within a 10-meter radius. Does NOT access device memory or steal data.",
                                "2. Bluesnarfing (Severity: Medium-High / Data Theft): Exploiting flaws in the Bluetooth Object Exchange (OBEX) protocol to bypass pairing authentication and download contacts, SMS messages, calendar entries, and photos.",
                                "3. Bluebugging (Severity: Critical / Complete Hijack): Exploiting firmware bugs to establish an unauthorized RFCOMM serial channel. The attacker gains complete remote control: eavesdropping on live phone calls, placing outbound premium calls, sending SMS messages, and routing cellular data."
                            ]
                        }
                    ],
                    "comparisonTable": {
                        "title": "Bluetooth Threat Matrix",
                        "headers": ["Attack Name", "Primary Objective", "Data Access", "Pairing Required?", "Threat Severity"],
                        "rows": [
                            ["Bluejacking", "Send Spam Messages", "None", "No", "Low (Nuisance)"],
                            ["Bluesnarfing", "Steal Stored Data", "Read Contacts / SMS / Photos", "Bypasses Pairing", "High (Data Theft)"],
                            ["Bluebugging", "Full Remote Device Hijack", "Full Read/Write & Audio Wiretap", "Bypasses Pairing", "Critical (Complete Hijack)"]
                        ]
                    },
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Bluetooth Security & OBEX/RFCOMM protocols (2m) -> 2. Draw 3-Way Comparative Table (4m) -> 3. Detailed Explanation of Bluejacking, Bluesnarfing, and Bluebugging (6m) -> 4. Prevention Measures (2m) -> 5. Conclusion (1m)"
                    },
                    "keyTakeaways": [
                        "Keep Bluetooth in Non-Discoverable mode and turn off when not in active use.",
                        "Bluebugging allows remote audio wiretapping and outbound call generation."
                    ]
                },
                {
                    "id": "u3-t8",
                    "unitId": 3,
                    "title": "Organizational Mobile Security: MDM, MAM & BYOD Policies",
                    "tag": "Enterprise Security",
                    "summary": "Enterprise management frameworks to secure mobile endpoints: Mobile Device Management (MDM), containerization, and BYOD policy guidelines.",
                    "definition": "Mobile Device Management (MDM) is an enterprise software solution that allows IT administrators to enforce security baselines, install enterprise certificates, monitor compliance, and remotely wipe corporate partitions on mobile endpoints.",
                    "theoryModules": [
                        {
                            "heading": "1. Enterprise MDM vs Mobile Application Management (MAM)",
                            "content": "Enterprise mobility security architectures:",
                            "keyPoints": [
                                "MDM (Mobile Device Management): Manages the entire physical device, enforcing full-disk encryption, OS version baselines, and camera disablement.",
                                "MAM & Containerization: Creates an encrypted, isolated corporate workspace partition inside an employee's personal device (BYOD). Corporate data cannot be copied to personal apps.",
                                "Selective Remote Wipe: In the event of employee resignation or device theft, the administrator can remotely erase only the corporate partition without deleting personal photos."
                            ]
                        }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define MDM and MAM (2m) -> 2. Explain Containerization Architecture (3m) -> 3. Key MDM Policy Rules for BYOD (5m) -> 4. Selective Remote Wipe vs Full Wipe (3m) -> 5. Conclusion (2m)"
                    },
                    "keyTakeaways": [
                        "Containerization isolates enterprise data from personal mobile applications.",
                        "Selective wipe allows erasing work data without violating employee personal privacy."
                    ]
                }
            ]
        },

        # =========================================================================
        # UNIT 4
        # =========================================================================
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
                    "definition": "A Proxy Server is an intermediary network application or computer that acts as a gateway between an endpoint client and a destination server, intercepting, evaluating, and forwarding network requests.",
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
                    "theoryModules": [
                        {
                            "heading": "1. Fundamental Functions of Proxy Servers",
                            "content": "Proxy servers serve both legitimate enterprise administration and adversarial obfuscation:",
                            "keyPoints": [
                                "IP Masking & Anonymity: The destination web server sees the proxy's IP address instead of the client's actual IP.",
                                "Content Filtering & Access Control: Blocking corporate employees from visiting malicious, gambling, or unproductive domains.",
                                "Caching & Performance Optimization: Storing local copies of frequently requested web assets to reduce outbound network bandwidth consumption."
                            ]
                        },
                        {
                            "heading": "2. Detailed Breakdown of the 6 Proxy Classifications",
                            "content": "Examining all 6 proxy types and their operational parameters:",
                            "keyPoints": [
                                "1. Forward Proxy: Sits in front of client devices, intercepting outbound requests to the Internet. Enforces corporate acceptable use policies and masks internal private subnet IPs.",
                                "2. Reverse Proxy: Sits in front of backend web servers, receiving public incoming traffic. Distributes load across server clusters, provides SSL/TLS termination, and shields servers from direct DDoS attacks.",
                                "3. Transparent Proxy: Intercepts client requests without modifying headers or hiding client IP (e.g. airport or hotel captive portals). Clients require zero manual configuration.",
                                "4. Anonymous Proxy: Hides the client's real IP address from the destination web server, but transmits HTTP headers (like `HTTP_VIA`) announcing that it is operating as a proxy.",
                                "5. High-Anonymity (Elite) Proxy: Completely conceals the client's true IP AND strips all proxy-identifying headers (`HTTP_VIA`, `X-Forwarded-For`). The destination server cannot distinguish it from a normal standalone direct client.",
                                "6. Open / Public Proxy: Misconfigured or intentionally exposed proxies accessible to any user on the Internet. Heavily abused by cybercriminals to bounce attack traffic."
                            ]
                        }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Proxy Server (2m) -> 2. Draw Forward vs Reverse Proxy Diagram (2m) -> 3. Explain all 6 Proxy Types in detail (8m) -> 4. Elite Proxy vs Anonymous Proxy differences (2m) -> 5. Conclusion (1m)"
                    },
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
                    "definition": "Proxy-Based Cybercrime involves chaining multiple open or residential proxies across international jurisdictions to obfuscate attack origins and defeat geographic IP bans.",
                    "theoryModules": [
                        {
                            "heading": "1. Adversarial Proxy Abuse Techniques",
                            "content": "Cybercriminals employ sophisticated proxy networks to conduct automated attacks:",
                            "keyPoints": [
                                "Proxy Chaining (Multi-Hop Bouncing): Routing malicious traffic sequentially through 5 to 10 global open proxies in different legal jurisdictions, forcing forensic investigators to obtain logs from multiple non-cooperating nations.",
                                "Residential Proxy Botnets: Routing attack traffic through compromised residential IoT and home broadband routers, making malicious credential stuffing requests appear from legitimate residential ISPs."
                            ]
                        },
                        {
                            "heading": "2. Detection and Countermeasures",
                            "content": "Enterprise techniques to identify and block malicious proxy traffic:",
                            "keyPoints": [
                                "IP Reputation Threat Feeds: Continuously blocking known commercial VPN egress nodes, open proxies, and Tor exit relays.",
                                "HTTP Header Inspection: Analyzing `X-Forwarded-For`, `Via`, and TCP window size / MTU anomalies.",
                                "Behavioral Anomaly Scoring: Flagging 'Impossible Travel' where a single user account logs in from New York and Tokyo within 10 minutes."
                            ]
                        }
                    ],
                    "keyTakeaways": [
                        "Residential proxies are used by attackers to bypass geographic IP blacklists.",
                        "Impossible travel algorithms detect proxy abuse by measuring impossible geographic speed."
                    ]
                },
                {
                    "id": "u4-t3",
                    "unitId": 4,
                    "title": "Anonymizers & The Tor Network Architecture",
                    "tag": "Tor & Anonymity",
                    "summary": "Technical operation of Onion Routing: multi-layered cryptographic encapsulation through Guard, Middle, and Exit nodes.",
                    "definition": "The Tor (The Onion Router) Network is a decentralized, open-source overlay network of over 7,000 volunteer relays that provides source anonymity by encrypting traffic in concentric layers (like an onion) across 3 intermediate nodes.",
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
                    "theoryModules": [
                        {
                            "heading": "1. The 3-Hop Onion Routing Cryptographic Principle",
                            "content": "Tor achieves source anonymity because no single relay possesses both the source client IP and destination server IP:",
                            "keyPoints": [
                                "Circuit Negotiation: The client downloads directory consensus data and negotiates 3 separate Diffie-Hellman cryptographic session keys: K1 (Guard), K2 (Middle), K3 (Exit).",
                                "Layered Encryption: The client encrypts the payload 3 times in reverse order: Layer 3 with K3, Layer 2 with K2, Layer 1 with K1. Packet format: `[E1 [E2 [E3 [Data]]]]`.",
                                "1. Entry / Guard Node: Peels Layer 1 using K1. It sees the client's real IP address, but only knows to forward the remaining packet `[E2 [E3 [Data]]]` to the Middle node. It CANNOT see the payload or final destination.",
                                "2. Middle Relay Node: Peels Layer 2 using K2. It knows it received from Guard and forwards `[E3 [Data]]` to Exit. It has NO idea who the client is or where the data is ultimately going.",
                                "3. Exit Node: Peels Layer 3 using K3. It forwards the unencrypted payload (or TLS stream) to the destination server (`https://bank.com`). It knows the destination, but has ZERO knowledge of the original client IP!"
                            ]
                        },
                        {
                            "heading": "2. Hidden Services (.onion)",
                            "content": "Tor Hidden Services (.onion domains) allow both the client AND server to maintain mutual anonymity, meeting at a negotiated 'Rendezvous Point' inside the Tor network without exposing the web server's real IP address.",
                            "keyPoints": [
                                "End-to-End Tor Encryption: Traffic inside hidden services never leaves the Tor network, eliminating exit node eavesdropping risks."
                            ]
                        }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Anonymizers & Tor (2m) -> 2. Draw 3-Node Onion Routing Flow Diagram (3m) -> 3. Step-by-Step Explanation of Guard, Middle, and Exit Node Key Peeling (6m) -> 4. Exit Node Vulnerabilities (2m) -> 5. Conclusion (1m)"
                    },
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
                    "definition": "Operation Bayonet (2017) was a joint international cyber law enforcement operation conducted by the FBI, DEA, Dutch National Police, and Europol that seized AlphaBay and Hansa Market.",
                    "theoryModules": [
                        {
                            "heading": "1. The 3 Phases of Operation Bayonet",
                            "content": "A landmark investigation breaking dark web marketplace operational anonymity:",
                            "keyPoints": [
                                "Phase 1 (AlphaBay Takedown): US authorities seized AlphaBay infrastructure in Lithuania and arrested creator Alexandre Cazes in Thailand. Cazes had committed a critical Operational Security (OPSEC) error by including his personal email address (`pimp_alex_91@hotmail.com`) in welcome email headers.",
                                "Phase 2 (The Honeypot Setup): Anticipating that AlphaBay users and vendors would migrate to the second largest marketplace ('Hansa Market'), Dutch Police secretly seized Hansa servers weeks in advance.",
                                "Phase 3 (27-Day Covert Honeypot): Dutch Police operated Hansa Market covertly for 27 days, modifying the website source code to strip metadata from vendor photo uploads and logging unencrypted delivery physical addresses, PGP keys, and Bitcoin transactions, leading to global mass arrests."
                            ]
                        }
                    ],
                    "keyTakeaways": [
                        "OPSEC errors (like using personal email addresses in server headers) undo darknet cryptographic anonymity.",
                        "International law enforcement honeypots can compromise thousands of dark web vendors simultaneously."
                    ]
                },
                {
                    "id": "u4-t5",
                    "unitId": 4,
                    "title": "Phishing Ecosystem: Lifecycle & Advanced Evasion Techniques",
                    "tag": "Phishing Analysis",
                    "summary": "End-to-end phishing lifecycle, attack classifications, and sophisticated evasion mechanisms.",
                    "definition": "Phishing is a social engineering attack that deploys deceptive digital communications masquerading as trustworthy entities to harvest credentials, financial data, or install malware.",
                    "theoryModules": [
                        {
                            "heading": "1. Detailed Phishing Attack Taxonomy",
                            "content": "Phishing encompasses specialized techniques based on target profile and delivery channel:",
                            "keyPoints": [
                                "Mass Email Phishing: Generic blast emails targeting millions of users with generic themes (fake bank alerts, package tracking).",
                                "Spear Phishing: Tailored attacks directed at specific individuals or companies containing customized background details mined from OSINT.",
                                "Whaling: High-level spear-phishing targeting C-suite executives (CEOs, CFOs) for high-value financial approval or corporate secrets.",
                                "Smishing & Vishing: Phishing conducted via SMS text messaging (Smishing) or telephone voice calls (Vishing).",
                                "Clone Phishing: Intercepting a legitimate email, duplicating its exact visual template, and replacing attachments/links with weaponized equivalents."
                            ]
                        },
                        {
                            "heading": "2. Advanced Evasion & 2FA Bypass Techniques",
                            "content": "Modern sophisticated phishing evasion mechanisms:",
                            "keyPoints": [
                                "1. Reverse Proxy Phishing (Evilginx): Acts as a man-in-the-middle proxy between victim and legitimate website (e.g. Microsoft 365), intercepting session cookies and completely bypassing SMS/TOTP Two-Factor Authentication!",
                                "2. IDN Homograph Punycode Attack: Using Cyrillic characters that look visually identical to Latin letters (`apple.com` encoded as `xn--...`).",
                                "3. Quishing (QR Code Phishing): Embedding malicious phishing links inside QR codes in emails, bypassing automated email text scanning engines."
                            ]
                        }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Phishing & 6-Stage Lifecycle (3m) -> 2. Explain Phishing Types (Spear, Whaling, Smishing, Vishing, Clone) (5m) -> 3. Advanced Evasion Techniques (Reverse Proxy Evilginx, Homograph, Quishing) (5m) -> 4. Prevention (FIDO2, DMARC) (2m)"
                    },
                    "keyTakeaways": [
                        "Reverse proxy phishing tools (Evilginx) can intercept session cookies, defeating SMS/TOTP 2FA.",
                        "Hardware security keys (FIDO2 WebAuthn) are immune to reverse proxy phishing."
                    ]
                },
                {
                    "id": "u4-t6",
                    "unitId": 4,
                    "title": "Password Cracking Methodologies & Auditing Tools",
                    "tag": "Password Cracking",
                    "summary": "Technical methodologies used to recover plaintext passwords from cryptographic hashes.",
                    "definition": "Password Cracking is the computational process of recovering plaintext passwords from stored cryptographic hash representations or authentication challenge handshakes.",
                    "theoryModules": [
                        {
                            "heading": "1. In-Depth Password Cracking Methodologies",
                            "content": "Computational approaches used to crack password hashes:",
                            "keyPoints": [
                                "1. Brute Force Attack: Exhaustively calculating the hash of every possible character combination. Computational complexity: O(C^L). Guaranteed to succeed given infinite time.",
                                "2. Dictionary Attack: Testing hundreds of thousands of words from precompiled dictionaries (e.g. `rockyou.txt`) and breach dumps.",
                                "3. Hybrid & Rule-Based Attack: Applying leetspeak mutation rules to dictionary words (e.g. `password` -> `P@ssw0rd2024!`).",
                                "4. Credential Stuffing: Automated replay of compromised username/password pairs across hundreds of unrelated websites.",
                                "5. Password Spraying: Testing 1 or 2 common passwords (e.g. `Summer2024!`) against thousands of user accounts to avoid account lockout triggers.",
                                "6. Rainbow Tables: Precomputed tables of cryptographic hash reduction chains, trading massive storage space for instantaneous hash reversal."
                            ]
                        },
                        {
                            "heading": "2. Industry Standard Cracking Tools",
                            "content": "Tools utilized by penetration testers and adversaries:",
                            "keyPoints": [
                                "Hashcat: The world's fastest GPU-accelerated rule-based password cracking engine.",
                                "John the Ripper (JtR): Multi-platform CPU/GPU password auditing tool.",
                                "Hydra: Fast network login brute-force tool supporting SSH, FTP, HTTP, and RDP."
                            ]
                        }
                    ],
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Password Cracking (2m) -> 2. Detail 6 Cracking Methods with mathematical complexity (8m) -> 3. Password Spraying vs Credential Stuffing (3m) -> 4. Popular Tools & Countermeasures (2m)"
                    },
                    "keyTakeaways": [
                        "Password spraying avoids account lockouts by testing a single password against many users.",
                        "Rainbow tables are completely defeated by adding a cryptographic salt."
                    ]
                },
                {
                    "id": "u4-t7",
                    "unitId": 4,
                    "title": "Password Hashing Cryptography, Salt, Pepper & Algorithms",
                    "tag": "Cryptography & Hashing",
                    "summary": "Evaluation of cryptographic hash functions, the vital role of Salt & Pepper, and why modern systems use adaptive key-stretching functions.",
                    "definition": "Cryptographic Password Hashing is a one-way mathematical transformation that converts a plaintext password into a fixed-length digest such that it is computationally infeasible to invert.",
                    "theoryModules": [
                        {
                            "heading": "1. Cryptographic Salt and Pepper",
                            "content": "Why salting and peppering are mandatory for secure password storage:",
                            "keyPoints": [
                                "Cryptographic Salt: A unique, cryptographically random string (>=16 bytes) generated per user and combined with the password BEFORE hashing: `Hash(Password + Salt)`. Stored in plaintext alongside the hash in the database. DEFEATS RAINBOW TABLES because attackers cannot use precomputed tables across multiple users!",
                                "Cryptographic Pepper: A high-entropy secret key added before hashing, stored in an external Hardware Security Module (HSM) or separate server OUTSIDE the database. If the database leaks, hashes cannot be cracked without the external pepper."
                            ]
                        },
                        {
                            "heading": "2. Comparative Analysis of Hash Algorithms",
                            "content": "Fast integrity hashes vs adaptive password hashing algorithms:",
                            "keyPoints": [
                                "MD5 & SHA-1: Cryptographically broken, fast GPU execution (billions/sec). NEVER use for passwords.",
                                "SHA-256: Fast integrity hash; vulnerable to rapid GPU brute-forcing unless paired with thousands of PBKDF2 iterations.",
                                "Bcrypt: Key-stretching Blowfish-based algorithm with adjustable cost parameter (work factor) to slow down GPU cracking.",
                                "Argon2 (Argon2id): Winner of Password Hashing Competition. Memory-hard and time-hard; completely neutralizes GPU and ASIC cracking hardware."
                            ]
                        }
                    ],
                    "comparisonTable": {
                        "title": "Password Hashing Algorithm Evaluation",
                        "headers": ["Algorithm", "Security Status", "GPU Cracking Rate", "Memory Hard?", "Verdict"],
                        "rows": [
                            ["MD5 (128-bit)", "BROKEN", "Billions/sec", "No", "Obsolete - Collision Vulnerable"],
                            ["SHA-1 (160-bit)", "DEPRECATED", "Hundreds of Millions/sec", "No", "Broken (SHAttered attack)"],
                            ["SHA-256 (256-bit)", "INTEGRITY ONLY", "Millions/sec", "No", "Too fast for passwords unless iterated"],
                            ["Bcrypt", "RECOMMENDED", "Very Slow (Configurable)", "No", "Adaptive work factor"],
                            ["Argon2id", "GOLD STANDARD", "Extremely Expensive", "Yes (Memory Hard)", "Winner of Password Hashing Comp"]
                        ]
                    },
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Hash Function & One-Way Property (2m) -> 2. Explain Salt vs Pepper with mathematical formula (4m) -> 3. Draw Hash Algorithm Comparative Table (4m) -> 4. Why Argon2 is superior (3m) -> 5. Conclusion (2m)"
                    },
                    "keyTakeaways": [
                        "Salting defeats precomputed Rainbow Tables by forcing per-user calculations.",
                        "Argon2id is memory-hard and time-hard, defeating dedicated GPU/ASIC cracking rigs."
                    ]
                },
                {
                    "id": "u4-t8",
                    "unitId": 4,
                    "title": "Keyloggers & Spyware: Architecture & Detection",
                    "tag": "Keyloggers & Spyware",
                    "summary": "Technical classifications of hardware vs software keyloggers and spyware detection mechanisms.",
                    "definition": "A Keylogger is hardware or software engineered to covertly record every keystroke entered on a keyboard, harvesting passwords, credit card numbers, and confidential messages.",
                    "theoryModules": [
                        {
                            "heading": "1. Hardware vs Software Keyloggers",
                            "content": "Keylogging mechanisms operate at different layers of computing architecture:",
                            "keyPoints": [
                                "1. Software Keyloggers: Utilize Windows API hooks (e.g. `SetWindowsHookEx(WH_KEYBOARD_LL)`), memory injection, or malicious browser extensions capturing DOM keystrokes.",
                                "2. Hardware Keyloggers: Physical inline hardware dongles connected between the keyboard USB cable and computer port. Completely undetectable by software antivirus since no code runs on the OS!",
                                "3. Kernel / Rootkit Keyloggers: Device driver rootkits intercepting keyboard controller hardware interrupts (IRQ 1) before the operating system processes input."
                            ]
                        }
                    ],
                    "keyTakeaways": [
                        "Hardware keyloggers cannot be detected by software antivirus programs.",
                        "Virtual randomized on-screen keyboards help mitigate keystroke interception."
                    ]
                },
                {
                    "id": "u4-t9",
                    "unitId": 4,
                    "title": "Viruses vs Worms: Deep Dissection & 5-Stage Anatomy",
                    "tag": "Malware Anatomy",
                    "summary": "Definitive comparison between Viruses and Worms, and the modular 5-stage architectural anatomy of self-propagating malware.",
                    "definition": "A Computer Virus requires a host executable file and human action to spread, whereas a Computer Worm is an autonomous, standalone executable that self-propagates across computer networks without human interaction.",
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
                    "theoryModules": [
                        {
                            "heading": "1. Comparative Analysis: Virus vs Worm",
                            "content": "Understanding the architectural differences between viruses and worms:",
                            "keyPoints": [
                                "Host Dependency: Virus requires a host file (.exe, .dll, macro) to latch onto; Worm is standalone.",
                                "Human Trigger: Virus requires human execution (clicking an infected file); Worm self-propagates autonomously over network vulnerabilities without human intervention.",
                                "Propagation Velocity: Worms spread exponentially across entire global subnets in seconds (e.g. SQL Slammer infected 75,000 servers in 10 minutes)."
                            ]
                        },
                        {
                            "heading": "2. The 5-Stage Modular Anatomy of Malware",
                            "content": "Every self-propagating malware binary consists of 5 modular engines:",
                            "keyPoints": [
                                "1. Replication Mechanism: The code routine finding clean executable files or memory spaces to inject cloned malware stubs.",
                                "2. Propagation Mechanism: The network scanning engine probing IP ranges, testing open ports (e.g. port 445 SMB), and transmitting copies.",
                                "3. Trigger Mechanism (Logic Bomb): The conditional logic (date/time, system event, user keystroke) that unleashes the destructive payload.",
                                "4. Malicious Payload: The destructive or extortionist routine (file encryption for ransomware, data wiping, reverse shell backdoors).",
                                "5. Concealment Engine (Armoring): Polymorphic/Metamorphic encryption engines, packing/crypters, and rootkit hooks that alter binary signatures upon every infection to defeat antivirus scanners."
                            ]
                        }
                    ],
                    "comparisonTable": {
                        "title": "Virus vs Worm Differentiation Matrix",
                        "headers": ["Characteristic", "Computer Virus", "Computer Worm"],
                        "rows": [
                            ["Host Dependency", "Requires a Host File (.exe, .doc, .dll)", "Standalone Autonomous Executable"],
                            ["Human Execution", "Mandatory (User must execute infected file)", "Zero (Autonomous network self-propagation)"],
                            ["Propagation Speed", "Moderate (Spreads via file sharing)", "Exponential / Rapid (Scans subnets in seconds)"],
                            ["Historical Example", "CIH / Chernobyl, Melissa Virus", "Morris Worm, SQL Slammer, WannaCry"]
                        ]
                    },
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define Virus & Worm (2m) -> 2. Draw 5-Stage Anatomy Diagram (3m) -> 3. Explain all 5 Modular Engines (5m) -> 4. Draw Virus vs Worm Comparison Table (3m) -> 5. Conclusion (2m)"
                    },
                    "keyTakeaways": [
                        "Viruses require a host program and user trigger; worms are autonomous standalone programs.",
                        "Polymorphic concealment engines mutate encryption keys upon every replication to defeat signature-based antivirus."
                    ]
                },
                {
                    "id": "u4-t10",
                    "unitId": 4,
                    "title": "Trojans, RATs & Backdoors",
                    "tag": "Trojans & Backdoors",
                    "summary": "Disguised malicious payloads, Remote Access Trojans (RATs), and persistence backdoors.",
                    "definition": "A Trojan Horse is malicious software disguised as legitimate, useful software (e.g. game, PDF reader, software crack) that tricks the user into executing it, opening a hidden backdoor or stealing data without self-replicating.",
                    "theoryModules": [
                        {
                            "heading": "1. Remote Access Trojans (RATs) & Backdoors",
                            "content": "Trojan classifications and persistence mechanisms:",
                            "keyPoints": [
                                "Remote Access Trojan (RAT): Provides total interactive graphical and command-line remote control over the victim PC (e.g. DarkComet, njRAT), allowing webcam spying, screen capture, and remote shell commands.",
                                "Banking Trojan (e.g. Zeus, Emotet): Intercepts browser sessions (Man-in-the-Browser) to inject fake login forms and steal banking credentials.",
                                "Backdoors: Covert access mechanisms bypassing standard authentication. Persistence is maintained via registry autorun keys (`HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run`), scheduled tasks, or DLL side-loading."
                            ]
                        }
                    ],
                    "keyTakeaways": [
                        "Trojans do NOT self-replicate; they rely on deceptive disguise.",
                        "RATs provide interactive GUI control and file exfiltration capabilities to remote attackers."
                    ]
                },
                {
                    "id": "u4-t11",
                    "unitId": 4,
                    "title": "DoS & DDoS Attacks: Vectors, Scrubbing & Mitigation",
                    "tag": "DDoS Attacks",
                    "summary": "Volumetric, Protocol, and Application-layer Denial of Service attacks and modern cloud scrubbing defense architectures.",
                    "definition": "A Distributed Denial of Service (DDoS) attack is a malicious attempt to disrupt the normal traffic of a targeted server, service, or network by overwhelming the target or its surrounding infrastructure with a flood of Internet traffic from thousands of compromised botnet nodes.",
                    "diagram":
"""+-------------------------------------------------------------+
|             DDoS SCRUBBING DEFENSE ARCHITECTURE             |
+-------------------------------------------------------------+
|  [ Botnet Zombies ] \                                       |
|  [ Real Users     ] ---> [ CLOUD SCRUBBING ] === Clean ===> [ Origin ]|
|                          [     CENTER     ]      Traffic    [ Server ]|
|                          (Discards Floods)                   |
+-------------------------------------------------------------+""",
                    "theoryModules": [
                        {
                            "heading": "1. The 3 Primary DDoS Attack Classifications",
                            "content": "DDoS attacks target different layers of the OSI stack:",
                            "keyPoints": [
                                "1. Volumetric Attacks (Layer 3/4 - Measured in Gbps/Tbps): Floods target network bandwidth with massive traffic volumes. Examples: UDP Flood, DNS Amplification (sending queries with spoofed victim IP to open recursive DNS servers, generating 50x amplified response payloads), NTP Amplification.",
                                "2. Protocol Attacks (Layer 3/4 - Measured in Packets/Sec): Consumes state tables of firewalls and load balancers. Examples: SYN Flood (sending TCP SYN packets without returning ACKs, exhausting the server connection state table), Ping of Death.",
                                "3. Application-Layer Attacks (Layer 7 - Measured in Requests/Sec): Targets web servers and database CPU/RAM. Examples: HTTP Flood, Slowloris (opening hundreds of connections and sending HTTP headers byte-by-byte very slowly to tie up web server worker threads)."
                            ]
                        },
                        {
                            "heading": "2. Modern Cloud Scrubbing & Anycast Defense",
                            "content": "How modern enterprise architectures survive multi-hundred Gbps DDoS floods:",
                            "keyPoints": [
                                "BGP Anycast Routing: Advertising the same IP address across hundreds of global Edge Points of Presence (PoPs), dispersing traffic geographically worldwide.",
                                "Cloud Scrubbing Centers: High-capacity cloud scrubbing centers (Cloudflare, Akamai) ingest all inbound traffic, inspect packet headers and behavioral heuristics, discard malicious packets, and forward clean traffic to the origin server.",
                                "SYN Cookies: The server encodes connection parameters into the initial TCP sequence number without allocating memory state tables until the client returns an ACK, defeating SYN floods."
                            ]
                        }
                    ],
                    "comparisonTable": {
                        "title": "3 DDoS Attack Classes Comparison",
                        "headers": ["Attack Category", "OSI Layer", "Measurement Metric", "Attack Mechanism", "Primary Target"],
                        "rows": [
                            ["Volumetric Attacks", "Layer 3/4", "Gbps / Tbps", "UDP Flood, DNS Amplification", "Internet Bandwidth Pipe"],
                            ["Protocol Attacks", "Layer 3/4", "Packets/Sec (PPS)", "TCP SYN Flood, Smurf Attack", "Firewall & OS State Tables"],
                            ["Application Attacks", "Layer 7", "Requests/Sec (RPS)", "Slowloris, HTTP POST Flood", "Web Server CPU/RAM & Database"]
                        ]
                    },
                    "gtuExamTips": {
                        "marks": "10-15 Marks",
                        "structure": "1. Define DoS vs DDoS (2m) -> 2. Draw Scrubbing Architecture Diagram (2m) -> 3. Detail all 3 DDoS Categories with Examples (6m) -> 4. Explain Cloud Scrubbing, Anycast & SYN Cookies (3m) -> 5. Conclusion (2m)"
                    },
                    "keyTakeaways": [
                        "Volumetric attacks target bandwidth; Protocol attacks target state tables; Application attacks target CPU/RAM.",
                        "Cloud Scrubbing Centers and BGP Anycast routing provide scalable protection against massive botnet floods."
                    ]
                }
            ]
        }
    ],

    # =========================================================================
    # EXAM QUESTIONS BANK (10-15 Marks)
    # =========================================================================
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
                    "Attribution & Evidence Volatility: IP spoofing and Tor routing destroy digital evidence before slow MLAT requests process."
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
                    "4. Quid Pro Quo: Offering a favor/service ('Free IT checkup') in exchange for passwords.",
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
                    "Cloud Scrubbing Centers: Ingests all traffic, inspects packet headers and behavioral heuristics, filters malicious traffic, and forwards clean traffic to origin.",
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

    # =========================================================================
    # FLASHCARDS & QUIZ & GLOSSARY
    # =========================================================================
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
output_js = f"// Cyber Security Mastery Platform - Master Curriculum Dataset\n// Exhaustive Units 1 to 4 Detailed Notes, Theory Modules, Case Studies & Exam Q&A\n\nconst CYBER_DATA = {json.dumps(cyber_data, indent=2, ensure_ascii=False)};\n"

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print("Generated js/data.js successfully!")
