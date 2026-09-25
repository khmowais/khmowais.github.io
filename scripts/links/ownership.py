import sys; sys.path.insert(0, "/tmp/opencode/links")
from lg import L, write_cat

A = []
def add(*a, **k): A.append(L(*a, **k))

# --- the ethics aisle ---
add("The Right to Read", "https://www.gnu.org/philosophy/right-to-read.en.html",
    "Richard Stallman's paradigm-shifting dystopian essay (1997) on a world where reading is licensed, not owned — the moral foreword to the whole modern DRM debate.", ["essay","drm","philosophy","stallman"], "article", sub="ethics", year=1997, source="GNU")
add("What is DRM?", "https://www.eff.org/issues/drm",
    "The Electronic Frontier Foundation's primer on digital rights management and why it changes consumers' rights.", ["drm","rights"], "article", sub="ethics", source="EFF")
add("Defective by Design", "https://www.defectivebydesign.org/",
    "The FSF/EFF campaign against DRM — background, actions and the thinking on why DRM is a design defect.", ["drm","activism","org"], "org", sub="ethics")
add("TorrentFreak", "https://torrentfreak.com/",
    "The news site that covers the piracy debates, copyright rulings and preservation stories without an agenda-noise filter.", ["piracy","news","copyright"], "news", sub="ethics")
add("Cory Doctorow — Craphound", "https://craphound.com/",
    "Essays, novels and talks on copyright, DRM and general computation — the literary wing of the digital-ownership argument.", ["essays","copyright","author"], "org", sub="ethics")

# --- FOSS & licensing foundations ---
add("Free Software Foundation", "https://www.fsf.org/",
    "The NGO behind the GPL — campaigning for software freedom since 1985.", ["foss","licensing","org"], "org", sub="foss")
add("GNU Licenses", "https://www.gnu.org/licenses/",
    "The definitive texts of the GPL, LGPL, AGPL and the license-choice guide.", ["licensing","gpl","docs"], "docs", sub="foss")
add("Choose a License", "https://choosealicense.com/",
    "The practical, pick-by-prose license chooser — good for deciding what your repo *you* keeps.", ["licensing","tool"], "tool", sub="foss")
add("Open Source Initiative", "https://opensource.org/",
    "The steward of the OSI-approved list — where 'open source' gets its formal definition.", ["foss","licensing","org"], "org", sub="foss")
add("Software Freedom Conservancy", "https://sfconservancy.org/",
    "The nonprofit that does the legal and fiscal legwork that keeps many free-software projects alive.", ["foss","org","legal"], "org", sub="foss")
add("GNU Philosophy library", "https://www.gnu.org/philosophy/",
    "Essays on free software, from 'Why Open Source misses the point' to the economics of copyleft.", ["philosophy","essays","foss"], "docs", sub="foss")

# --- preservation organs ---
add("Internet Archive (preservation side)", "https://archive.org/",
    "500 billion web pages, millions of books and software — humanity's biggest hedge against digital forgetting.", ["preservation","books","archive"], "org", sub="preservation")
add("Wayback Machine", "https://web.archive.org/",
    "Browse 25+ years of the web as it actually was — the single most important preservation tool for the internet.", ["preservation","web","tool"], "tool", sub="preservation")
add("Software Heritage", "https://www.softwareheritage.org/",
    "The archive of public source code — harvesting every public repo before it vanishes.", ["preservation","source","archive"], "project", sub="preservation")
add("Archive Team", "https://www.archiveteam.org/",
    "The scrappy volunteer force that works to download and save internet history classes before they're deleted.", ["preservation","community"], "org", sub="preservation")
add("Software Library (Internet Archive)", "https://archive.org/details/software",
    "Tens of thousands of archived programs — the closest thing to a public-software museum.", ["preservation","software","archive"], "archive", sub="preservation")
add("Prelinger Archives", "https://archive.org/details/prelinger",
    "The famous collection of ephemeral film — ads, industrial and amateur film from the 20th century.", ["film","archive","preservation"], "archive", sub="preservation")
add("LOCKSS", "https://www.lockss.org/",
    "'Lots of Copies Keep Stuff Safe' — the distributed dark-archive archiving model for scholarly literature.", ["preservation","distributed","journals"], "project", sub="preservation")
add("IIIF — International Image Interoperability Framework", "https://iiif.io/",
    "The shared standard letting museums and libraries serve deep-zoom images to the world.", ["digitization","standards"], "org", sub="preservation")

# --- right to repair ---
add("iFixit", "https://www.ifixit.com/",
    "The repair teardowns, manuals and advocacy that spearheaded the right-to-repair movement.", ["repair","manuals","org"], "org", sub="repair")
add("Right to Repair Europe", "https://repair.eu/",
    "The coalition behind the EU push toward repairable, modular products.", ["repair","policy","org"], "org", sub="repair")
add("U.S. PIRG", "https://pirg.org/",
    "The consumer advocacy group driving state-level right-to-repair — the policy engine behind repairable gadgets.", ["repair","policy","consumer"], "org", sub="repair")
add("The Repair Association", "https://www.repair.org/",
    "US/global trade association and advocacy network for the right to repair.", ["repair","org"], "org", sub="repair")
add("Framework", "https://frame.work/",
    "The repairable, upgradeable laptop — repair advocacy sold as a product.", ["repair","hardware"], "project", sub="repair")
add("Fairphone", "https://www.fairphone.com/",
    "The modular, user-repairable phone — counterpoint to the sealed-tight smartphone era.", ["repair","hardware","phone"], "project", sub="repair")

# --- abandonware & game history ---
add("Video Game History Foundation", "https://gamehistory.org/",
    "Research library and preservation project documenting video game history before it evaporates.", ["games","preservation","org"], "org", sub="games")
add("DOSBox", "https://www.dosbox.com/",
    "Emulator for DOS-era software — the gateway to three decades of abandoned DOS titles.", ["dos","emulator","games"], "project", sub="games")
add("ScummVM", "https://www.scummvm.org/",
    "The engine re-implementation that keeps LucasArts-style point-and-click adventures playable.", ["games","preservation","project"], "project", sub="games")
add("BlueMaxima's Flashpoint", "https://bluemaxima.org/flashpoint/",
    "The full Flash-compatible archive — tens of thousands of swf animations and games rescued from the URL-bar era.", ["flash","games","preservation"], "project", sub="games")
add("Archive.org 'Classic PC Games'", "https://archive.org/details/classicpcgames",
    "Browser-playable classic DOS/Windows games hosted on the Internet Archive.", ["games","preservation","archive"], "archive", sub="games")

# --- local-first & data ownership ---
add("Local-first software: you own your data", "https://www.inkandswitch.com/local-first/",
    "Ink & Switch's landmark essay on software where your data lives on your device and syncs peer-to-peer.", ["local-first","essay","sync"], "article", sub="local-first", source="Ink & Switch")
add("Localfirst Web", "https://localfirstweb.dev/",
    "A directory of local-first technology and a friendly index into the movement.", ["local-first","directory"], "project", sub="local-first")
add("Solid — your data, your choice", "https://solidproject.org/",
    "Tim Berners-Lee's framework for web apps where users own and re-purpose their own data.", ["data-ownership","web","solid"], "project", sub="local-first")
add("Calibre", "https://calibre-ebook.com/",
    "The open ebook manager — the tool that makes 'your library is yours' practical.", ["ebooks","library","tool"], "project", sub="books")
add("DeDRM_tools", "https://github.com/noDRM/DeDRM_tools",
    "Plugins that remove DRM from ebooks you already own, for the ever-allowed backups and cross-device reading. Also: get the plugin from CRedM for a signed build.", ["drm","ebooks","plugins"], "repo", sub="books")

# --- device sovereignty (carried over) ---
add("YunoHost", "https://yunohost.org/",
    "Debian-based self-hosting for everyone — one-click installs of Nextcloud, Jellyfin, WordPress and hundreds of apps.", ["self-hosted","server","apps"], "project", sub="devices")
add("Pi-hole", "https://pi-hole.net/",
    "Network-wide DNS ad-blocking — install on a Raspberry Pi and protect the whole home network from trackers.", ["dns","ad-blocking","raspberry-pi"], "project", sub="devices")
add("Tor Project", "https://www.torproject.org/",
    "The Onion Router — anonymous browsing and the circumvention tool for censored networks.", ["privacy","anonymity","tool"], "org", sub="devices")
add("Standard Notes", "https://standardnotes.com/",
    "End-to-end encrypted notes you can self-host — private notes without the cloud.", ["notes","encryption","privacy"], "project", sub="devices")
add("CalyxOS", "https://calyxos.org/",
    "Privacy-focused Android without Google services — own your phone again.", ["android","privacy","os"], "project", sub="devices")
add("GrapheneOS", "https://grapheneos.org/",
    "The hardened-Android gold standard — hardened kernel, verified boot, no Google by default.", ["android","privacy","security"], "project", sub="devices")
add("F-Droid", "https://f-droid.org/",
    "The catalog of free and open-source Android apps — no tracking, no ads.", ["android","apps","foss"], "project", sub="devices")
add("Shadow libraries — what they are", "https://en.wikipedia.org/wiki/Shadow_library",
    "The background on shadow libraries: scale, legality and the preservation arguments around them — read the topic, not the services.", ["piracy","knowledge","ethics","wiki"], "archive", sub="ethics")

write_cat("ownership", A)