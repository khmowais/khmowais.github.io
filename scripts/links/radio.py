import sys; sys.path.insert(0, "/tmp/opencode/links")
from lg import L, write_cat

A = []
def add(*a, **k): A.append(L(*a, **k))

# --- organizations & foundations ---
add("ARRL — American Radio Relay League", "https://www.arrl.org/",
    "The national amateur radio association: licensing, bands, ARES emergency communications, and the journals that define the hobby.", ["org","licensing","emcomm"], "org", sub="org")
add("ARRL Licensing, Education & Training", "https://www.arrl.org/licensing-education-training",
    "The US licensing path — Technician, General, Extra — plus course materials and the exam question pools.", ["licensing","education"], "docs", sub="licensing")
add("ARRL Band Plan", "https://www.arrl.org/band-plan",
    "The authoritative US HF/VHF/UHF band allocations and segment usage.", ["bands","hf","reference"], "docs", sub="licensing")
add("RSGB — Radio Society of Great Britain", "https://rsgb.org/",
    "The UK's national amateur radio society.", ["org","licensing"], "org", sub="org")
add("IARU — International Amateur Radio Union", "https://www.iaru.org/",
    "The federation of national amateur radio societies — international spectrum, band planning, DXCC cooperation.", ["org","international"], "org", sub="org")
add("FCC ULS — license lookups", "https://www.fcc.gov/uls",
    "The FCC Universal Licensing System — look up any callsign or track your own license.", ["licensing","fcc","lookup"], "tool", sub="licensing")
add("History of amateur radio", "https://en.wikipedia.org/wiki/History_of_amateur_radio",
    "Background on how hams got the airwaves they have, from spark-gap experiments to the receiver wars.", ["history","wiki"], "archive", sub="org")

# --- study & callsigns ---
add("HamStudy", "https://hamstudy.org/",
    "Free practice exams and flashcards for the US pools; search questions, track progress.", ["study","exams"], "tool", sub="licensing")
add("KB6NU No-Nonsense Study Guides", "https://www.kb6nu.com/study-guides/",
    "Dan Romanchik's practical, low-cost guides to the US license exams.", ["study","guides"], "guide", sub="licensing")
add("QRZ.com", "https://www.qrz.com/",
    "The de-facto directory of the amateur radio world — callsign lookups, forums, log search.", ["callsign","directory","community"], "tool", sub="logbook")
add("ARRL Logbook of The World", "https://loTW.arrl.org/",
    "The ARRL's cryptographic QSL confirmation system (LoTW) for contest and DXCC credit.", ["logbook","dxcc","qsl"], "tool", sub="logbook")
add("eQSL.cc", "https://www.eqsl.cc/qslcard/index.cfm",
    "Electronic QSL card bureau — confirm contacts without paper.", ["logbook","qsl"], "org", sub="logbook")
add("Club Log", "https://clublog.org/",
    "Weekly DXCC database, league tables for DXpeditions, and the most-populated log aggregation in DXing.", ["dx","logbook"], "tool", sub="logbook")

# --- HF, DX, contests & portable ---
add("DX Summit", "https://dxsummit.fi/",
    "Real-time HF spotting network — where DXers watch the bands and plan their next QSO.", ["hf","dx","spots"], "tool", sub="hf")
add("POTA — Parks on the Air", "https://pota.app/",
    "Activators and hunters making contacts from parks and wilderness areas; free to join, deeply satisfying.", ["portable","parks"], "project", sub="portable")
add("SOTA — Summits on the Air", "https://www.sota.org.uk/",
    "HF/VHF contacts from mountain summits; hiking meets ham radio.", ["portable","summits"], "project", sub="portable")
add("Contest Calendar (WA7BNM)", "https://www.contestcalendar.com/",
    "The global calendar of radio contests, with notes on each.", ["contesting","hf"], "tool", sub="hf")
add("ARRL Field Day", "https://www.arrl.org/field-day",
    "The annual emergency-preparedness exercise that turns harmless radio people into a field force.", ["emcomm","field"], "docs", sub="hf")

# --- digital modes ---
add("WSJT-X", "https://sourceforge.net/projects/wsjt/",
    "The suite that made weak-signal digital modes standard: FT8, FT4, JT65, JT9, WSPR, MSK144.", ["digital-modes","weak-signal","ft8"], "project", sub="digital")
add("WSJT Home / documentation", "https://wsjt.sourceforge.io/wsjtx.html",
    "Official site and manuals for WSJT-X and its protocols.", ["docs","ft8","wspr"], "docs", sub="digital")
add("FT8 — the digital mode that changed HF", "https://en.wikipedia.org/wiki/FT8",
    "What FT8/FT4 are, protocol-wise, and why they changed weak-signal HF overnight.", ["ft8","digital-modes","wiki"], "archive", sub="digital")
add("PSK Reporter", "https://pskreporter.info/",
    "A worldwide live map of who can decode whom — the graph that illustrates propagation in real time.", ["propagation","digital-modes"], "tool", sub="digital")
add("JS8Call", "https://js8call.com/",
    "Weak-signal keyboard chat built on FT8's engine, with messaging, relaying and lightweight QSOs.", ["keyboard","weak-signal","network"], "project", sub="digital")
add("JS8Call GitHub", "https://github.com/js8call/js8call",
    "Source and issues for JS8Call.", ["keyboard","source"], "repo", sub="digital")
add("Winlink Global Radio Email", "https://winlink.org/",
    "Radio-based email network — messages ride HF, VHF or Pactor when the internet goes away.", ["emcomm","email","hf"], "org", sub="emcomm")
add("fldigi / FLdigi suite (W1HKJ)", "https://www.w1hkj.com/",
    "The FLDigi/FLMsg/FLamp suite of free digital-mode software — PSK31, RTTY, Olivia, DominoEx, and more.", ["digital-modes","psk31","software"], "project", sub="digital")
add("Direwolf", "https://github.com/wb2osz/direwolf",
    "Software TNC for APRS and packet over a sound card — robust and well-documented.", ["packet","aprs","tnc"], "repo", sub="packet")
add("APRS-IS", "http://www.aprs-is.net/",
    "The APRS Internet System — the backbone that relays APRS packets between RF and the internet.", ["aprs","protocol","network"], "org", sub="aprs")
add("aprs.fi", "https://aprs.fi/",
    "The live map of APRS traffic worldwide — positions, weather, telemetry and digipeaters.", ["aprs","map","telemetry"], "tool", sub="aprs")
add("APRSdroid", "https://aprsdroid.org/",
    "APRS on an Android phone with a $10 radio cable — position, messaging, telemetry.", ["aprs","android"], "project", sub="aprs")
add("YAAC", "https://www.ka2ddo.org/ka2ddo/yaac.html",
    "Yet Another APRS Client — Java, works headless/small, no bloat.", ["aprs","client"], "project", sub="aprs")
add("Xastir", "https://github.com/Xastir/Xastir",
    "The classic Linux APRS tracker and mapping client.", ["aprs","linux","mapping"], "repo", sub="aprs")

# --- AX.25 & packet radio ---
add("AX.25 Link Layer Protocol Specification 2.2", "https://www.ax25.net/AX25.2.2-Jul%2098-2.pdf",
    "The AX.25 protocol spec — the link-layer format behind packet radio, APRS and direwolf.", ["ax.25","protocol","packet"], "paper", sub="packet", source="AX25.net/TAPR")
add("TAPR", "https://www.tapr.org/",
    "Tucson Amateur Packet Radio — the nonprofit behind packet radio history and the laboratory amateur radio.", ["org","packet","research"], "org", sub="packet")
add("Packet radio — the '80s BBS network", "https://en.wikipedia.org/wiki/Packet_radio",
    "How hams built a store-and-forward text network on HF/VHF decades before the public internet.", ["packet","history","bbs"], "archive", sub="packet")
add("APRS protocol reference", "http://www.aprs.org/",
    "WB4APR's original APRS protocol documentation — the ground truth behind aprs.fi and direwolf.", ["aprs","protocol","docs"], "docs", sub="aprs")

# --- LoRa / Meshtastic / Reticulum ---
add("LoRa Alliance", "https://lora-alliance.org/",
    "The standards body for LoRaWAN — low-power, long-range IoT networking.", ["lora","lorawan","iot"], "org", sub="lora")
add("The Things Network", "https://www.thethingsnetwork.org/",
    "Community LoRaWAN infrastructure — gateways and a worldwide public data network for sensors.", ["lora","lorawan","community"], "org", sub="lora")
add("Meshtastic", "https://meshtastic.org/",
    "Open GPS-mesh radios over LoRa — no cell towers, no internet, your own encrypted text network for off-grid areas.", ["lora","mesh","off-grid"], "project", sub="lora")
add("Meshtastic documentation", "https://meshtastic.org/docs/",
    "Config, firmware, radios and the Python SDK for Meshtastic nodes.", ["docs","lora","mesh"], "docs", sub="lora")
add("Reticulum", "https://reticulum.network/",
    "A cryptographic networking stack that works over packet radio, LoRa, TCP/UDP and even audio — the 'internet that doesn't need the internet'.", ["reticulum","mesh","encryption"], "project", sub="reticulum")
add("Reticulum (GitHub)", "https://github.com/markqvist/Reticulum",
    "The cryptographic networking stack itself — source, issues and the manual for RNS transports and building self-created networks.", ["docs","reticulum"], "repo", sub="reticulum")
add("Sideband", "https://github.com/markqvist/Sideband",
    "LoRa/radio chat client for the Reticulum stack, on phone and desktop.", ["reticulum","chat","lora"], "repo", sub="reticulum")
add("Nomad Network", "https://github.com/markqvist/NomadNet",
    "Peer-to-peer text sites over Reticulum — RSS-like without servers.", ["reticulum","p2p","content"], "repo", sub="reticulum")

# --- SDR & signal ---
add("GNU Radio", "https://www.gnuradio.org/",
    "Free software-defined radio toolkit — build signal-processing flows with Python and C++.", ["sdr","dsp","signal"], "org", sub="sdr")
add("GNU Radio Wiki & Tutorials", "https://wiki.gnuradio.org/",
    "The tutorials that get you from hello world to a working demodulator block.", ["docs","sdr","tutorials"], "docs", sub="sdr")
add("RTL-SDR dongles and the blog", "https://www.rtl-sdr.com/",
    "The $25 dongle that launched desktop SDR — blog with reviews, experiments and tutorials.", ["sdr","hardware","tutorials"], "article", sub="sdr")
add("SDR++", "https://github.com/AlexandreRouma/SDRPlusPlus",
    "Cross-platform SDR receiver with a clean interface, wide device support and iPhone port.", ["sdr","receiver"], "repo", sub="sdr")
add("Gqrx SDR", "https://gqrx.dk/",
    "Popular multi-platform SDR receiver ideal for RTL-SDR and Airspy on Linux.", ["sdr","receiver","linux"], "project", sub="sdr")
add("CubicSDR", "https://cubicsdr.com/",
    "Cross-platform SDR client that keeps the waterfall the center of the world.", ["sdr","receiver"], "project", sub="sdr")
add("OpenWebRX", "https://www.openwebrx.de/",
    "Multi-user SDR server that turns one radio into a web-accessible receiver anyone can tune.", ["sdr","web","multi-user"], "project", sub="sdr")
add("WebSDR", "http://websdr.org/",
    "University-run online shortwave receivers — tune real radios around the world from your browser.", ["sdr","receiver","web"], "tool", sub="sdr")
add("KiwiSDR", "https://kiwisdr.com/",
    "Wideband HF receiver built as a Raspberry Pi cape; there's a growing public network of them.", ["sdr","hf","hardware"], "project", sub="sdr")
add("HackRF One", "https://greatscottgadgets.com/hackrf/",
    "The $300 half-duplex transceiver that broke SDR cost barriers — 1 MHz to 6 GHz.", ["sdr","transceiver","hardware"], "project", sub="sdr")
add("Airspy", "https://airspy.com/",
    "High-performance SDR hardware — the software-defined radio darling of the HF/VHF hobby.", ["sdr","hardware"], "org", sub="sdr")
add("SDRplay", "https://www.sdrplay.com/",
    "Wideband SDR receivers with excellent HF performance at consumer prices.", ["sdr","hardware","hf"], "org", sub="sdr")
add("PlutoSDR (Analog Devices)", "https://wiki.analog.com/university/tools/pluto",
    "A $200 self-contained SDR transceiver that's a full lab instrument — and GNU Radio friendly.", ["sdr","transceiver","education"], "docs", sub="sdr")
add("USRP / Ettus Research", "https://www.ettus.com/products/",
    "The professional-grade SDR family behind serious DSP research.", ["sdr","hardware","research"], "org", sub="sdr")

# --- antennas & propagation ---
add("Antenna Theory", "https://www.antenna-theory.com/",
    "Clear, no-nonsense antenna theory — the tutorial for understanding what you actually hang in the sky.", ["antennas","theory","tutorial"], "guide", sub="antennas")
add("NOAA Space Weather Prediction Center", "https://www.swpc.noaa.gov/",
    "Solar flux, K-index, alerts — the data ham HF propagation forecasts are built on.", ["propagation","space-weather"], "org", sub="propagation")
add("SolarHam", "https://www.solarham.net/",
    "The ham-friendly home of current solar conditions and their HF implications", ["propagation","solar"], "article", sub="propagation")
add("VOACAP", "https://www.voacap.com/",
    "HF propagation prediction tools — entering from HF, making IONCAP-style predictions accessible.", ["propagation","hf","prediction"], "tool", sub="propagation")
add("PropNET", "http://www.propnet.net/",
    "A 6m/2m propagation beacon and reporting network used to watch opens.", ["propagation","vhf"], "tool", sub="propagation")
add("Shortwave.info", "https://www.short-wave.info/",
    "Live shortwave news and frequency schedules.", ["shortwave","frequencies"], "tool", sub="propagation")

# --- off-grid / culture ---
add("Ham Radio Crash Course", "https://www.youtube.com/@HamRadioCrashCourse",
    "Josh (KI6NAZ)'s channel — modern ham video content from beginner to field ops.", ["youtube","video","culture"], "video", sub="culture")
add("W2AEW — Alan Wolke", "https://www.youtube.com/@w2aew",
    "Oscilloscope and analog electronics explanations that deserve a textbook audience.", ["youtube","electronics","video"], "video", sub="culture")
add("Off Grid Ham", "https://offgridham.com/",
    "Notes and reviews for running amateur radio where there's no grid and no internet.", ["off-grid","emcomm"], "article", sub="offgrid")
add("OH8STN Ham Radio Station", "https://oh8stn.org/",
    "How to be a portable off-grid ham — solar, batteries, lightweight gear that works.", ["off-grid","portable"], "article", sub="offgrid")
add("AREDN — Amateur Radio Emergency Data Network", "https://www.arednmesh.org/",
    "Building high-speed data mesh networks on amateur microwave bands for emergencies.", ["emcomm","mesh","broadband"], "project", sub="emcomm")
add("ARES — Amateur Radio Emergency Service", "https://www.arrl.org/ares",
    "The ARRL's organized emergency-response ham network.", ["emcomm","org"], "docs", sub="emcomm")
add("Broadcastify", "https://www.broadcastify.com/",
    "The largest collection of live scanner feeds — listen to public safety radio worldwide.", ["scanner","streams"], "tool", sub="culture")
add("RadioReference", "https://www.radioreference.com/",
    "The definitive reference for scanner frequencies, trunking systems and radio IDs.", ["scanner","database","reference"], "org", sub="culture")

write_cat("radio", A)