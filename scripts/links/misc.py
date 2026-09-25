import sys; sys.path.insert(0, "/tmp/opencode/links")
from lg import L, write_cat

A = []
def add(*a, **k): A.append(L(*a, **k))

# --- robotics / hardware (carried) ---
add("PX4 Autopilot Guide", "https://docs.px4.io/main/en/",
    "The professional open-source autopilot for drones and UAVs — where serious autonomous flight begins.", ["uav","drones","autopilot"], "docs", sub="robotics")
add("ArduPilot", "https://ardupilot.org/",
    "The most versatile open-source autopilot — quadcopters to submarines to rovers.", ["uav","robotics","control"], "docs", sub="robotics")
add("ROS 2 Documentation", "https://docs.ros.org/en/rolling/",
    "The robot operating system (a middleware framework) — the lingua franca of modern robotics.", ["robotics","ros","middleware"], "docs", sub="robotics")
add("The Embedded Rust Book", "https://docs.rust-embedded.org/book/",
    "Rust for bare-metal microcontrollers — memory-safe firmware, the future of embedded.", ["rust","embedded","microcontrollers"], "book", sub="robotics")

# --- science & math (carried) ---
add("3Blue1Brown", "https://www.3blue1brown.com/",
    "Grant Sanderson's geometric explanations of linear algebra, calculus and neural networks — pure art.", ["math","visualization","education"], "video", sub="science")
add("BetterExplained", "https://betterexplained.com/",
    "Math lessons that focus on intuition — e, imaginary numbers and Bayes so they actually click.", ["math","intuition","education"], "article", sub="science")
add("The Feynman Lectures on Physics", "https://www.feynmanlectures.caltech.edu/",
    "Feynman's legendary lectures, free online — the gold standard for fundamental physics.", ["physics","feynman","education"], "book", sub="science")
add("Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/",
    "Peer-reviewed entries on every major philosophical topic — the informal reference library of philosophy.", ["philosophy","reference","academic"], "archive", sub="science")

# --- rabbit holes & community (carried) ---
add("Dwarf Fortress", "https://www.bay12games.com/dwarves/",
    "A simulation game of literally infinite depth — worlds with history, geology and civilizations emergent from simple rules.", ["gaming","simulation","emergence"], "project", sub="rabbit-holes")
add("TempleOS", "https://en.wikipedia.org/wiki/TempleOS",
    "A full 64-bit OS written by one man — its own compiler, kernel and graphics stack. The most interesting OS ever written.", ["operating-systems","solo","curiosity"], "archive", sub="rabbit-holes")
add("Permacomputing", "https://permacomputing.net/",
    "A community of practice for resilient, regenerative computing — permaculture thinking for software and hardware.", ["resilience","sustainability","philosophy"], "project", sub="rabbit-holes")
add("Brutalist Websites", "https://brutalistwebsites.com/",
    "A gallery of sites embracing raw, honest, unpolished-by-intent web design.", ["design","brutalism","inspiration"], "project", sub="design")
add("Hacker News", "https://news.ycombinator.com/",
    "Tech's watering hole — engineering discussion, startup news and the occasional existential crisis.", ["news","community"], "forum", sub="community")
add("Lobsters", "https://lobste.rs/",
    "A quieter, more thoughtful tech link aggregator — less noise than HN, more signal.", ["news","community","programming"], "forum", sub="community")
add("Stratechery", "https://stratechery.com/",
    "Ben Thompson's analysis of tech strategy — aggregation theory and the business of software.", ["strategy","business","analysis"], "article", sub="community")
add("Wendover Productions", "https://www.youtube.com/@wendoverproductions",
    "Well-researched videos on infrastructure, logistics and the quiet machinery of the world.", ["infrastructure","logistics","video"], "video", sub="rabbit-holes")

# --- off-road & heavy machinery (carried) ---
add("Toyota Land Cruiser 70 Series", "https://en.wikipedia.org/wiki/Toyota_Land_Cruiser_(J70)",
    "In continuous production since 1984 — the 4x4 of NGOs, militaries and explorers everywhere.", ["land-cruiser","off-road","4x4"], "archive", sub="machines")
add("Toyota Land Cruiser 100 Series", "https://en.wikipedia.org/wiki/Toyota_Land_Cruiser_(J100)",
    "The 100 that paired comfort with serious off-road capability — IFS, solid rear axle and the 2UZ-FE V8.", ["land-cruiser","off-road","v8"], "archive", sub="machines")
add("Cummins B-series diesel", "https://en.wikipedia.org/wiki/Cummins_B_Series_engine",
    "The 5.9L/6.7L engines powering trucks and machinery worldwide — the 12-valve has legendary reliability.", ["diesel","engines","reliability"], "archive", sub="machines")
add("Detroit Diesel 2-stroke", "https://en.wikipedia.org/wiki/Detroit_Diesel",
    "The 'Screaming Jimmy' two-stroke diesels — the sound of heavy equipment and highway trucks for decades.", ["diesel","engines","two-stroke"], "archive", sub="machines")
add("Caterpillar D9", "https://en.wikipedia.org/wiki/Caterpillar_D9",
    "Wisdom. So is the D9's blade. The 100,000-pound bulldozer that moves mountains figuratively and literally.", ["caterpillar","heavy-equipment","diesel"], "archive", sub="machines")
add("Mercedes-Benz Unimog", "https://en.wikipedia.org/wiki/Unimog",
    "A truck, a tractor, a crawler and an implement carrier — portal axles and unstoppable articulation.", ["unimog","off-road","expedition"], "archive", sub="machines")
add("Mitsubishi Pajero", "https://en.wikipedia.org/wiki/Mitsubishi_Pajero",
    "Twelve-time Dakar winner — Super Select 4WD and a masterclass in rally-grade off-road engineering.", ["off-road","dakar","4x4"], "archive", sub="machines")
add("Nissan Patrol Y61", "https://en.wikipedia.org/wiki/Nissan_Patrol",
    "Solid axles front and rear, the TD42 diesel and a near-indestructible reputation — the poor man's Land Cruiser.", ["nissan","off-road","diesel"], "archive", sub="machines")
add("The Wärtsilä-Sulzer RTA96-C", "https://en.wikipedia.org/wiki/W%C3%A4rtsil%C3%A4-Sulzer_RTA96-C",
    "The largest engine in the world — 109,000 hp across fourteen 38-inch bores, the heartbeat of container shipping.", ["marine","diesel","largest"], "archive", sub="machines")
add("Expander Overland", "https://www.expanderoverland.com/",
    "A Toyota Coaster turned into a serious expedition vehicle — the ultimate off-grid mobile workshop build.", ["overlanding","build","expedition"], "article", sub="machines")

# --- resilient & off-grid tech (carried) ---
add("Off Grid Web", "https://www.offgridweb.com/",
    "Public safety communications and off-grid technology — gear reviews and field skills.", ["off-grid","resilience","gear"], "article", sub="resilient")
add("Solar Power World", "https://www.solarpowerworldonline.com/",
    "News and engineering for solar — the tech-reading side of keeping infrastructure alive without the grid.", ["solar","power","news"], "news", sub="resilient")
add("Ready.gov", "https://www.ready.gov/",
    "FEMA's preparedness portal — including guidance on communicating during emergencies, a sober checklist for the worst day.", ["emergency","communication","fema"], "docs", sub="resilient")
add("Low-Tech Magazine", "https://www.lowtechmagazine.com/",
    "Kris De Decker's exploration of low-tech, resilient alternatives — meet the tech of the year 2000 greener and wiser.", ["low-tech","sustainability","essays"], "article", sub="resilient")
add("Low-Tech Magazine (solar version)", "https://solar.lowtechmagazine.com/",
    "Low-Tech's own website, offline whenever its solar battery runs dry, hosting itself on a grid of its own kind.", ["solar","self-hosting","experiment"], "project", sub="resilient")
add("The Prepared", "https://theprepared.com/",
    "Rational, non-bunker preparedness — resilience thinking without the panic-buying.", ["preparedness","resilience","guide"], "article", sub="resilient")
add("Backblaze — the 3-2-1 backup rule", "https://www.backblaze.com/blog/the-3-2-1-backup-strategy/",
    "The one backup rule worth memorizing: three copies, two media, one off-site.", ["backup","data","strategy"], "article", sub="resilient")
add("Fellowship for Intentional Community", "https://www.ic.org/",
    "The longest-running directory and network of intentional and ecovillage communities — resilience as a social practice.", ["community","sustainability","ecovillages"], "org", sub="resilient")
add("Local Exchange Trading Systems", "https://en.wikipedia.org/wiki/Local_exchange_trading_system",
    "Mutual-credit community economies — understanding alternative money as a resilience skill.", ["economics","community","alternatives"], "archive", sub="resilient")

write_cat("misc", A)