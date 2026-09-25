import sys; sys.path.insert(0, "/tmp/opencode/links")
from lg import L, write_cat

A = []
def add(*a, **k): A.append(L(*a, **k))

# --- systems / ops (carried + curated) ---
add("The Art of Unix Programming", "https://www.catb.org/~esr/writings/taoup/html/",
    "Eric Raymond's study of the Unix philosophy that shaped modern software — the reason the small-tools culture exists.", ["unix","philosophy","programming"], "book", sub="unix")
add("Systems Performance (Brendan Gregg)", "https://www.brendangregg.com/systems-performance-2nd-edition-book.html",
    "The definitive guide from kernel to application — the performance book I keep within arm's reach.", ["performance","linux","kernel"], "book", sub="linux")
add("Brendan Gregg's site", "https://www.brendangregg.com/",
    "Methodologies, tools and one-liners for performance analysis, eBPF and Linux internals.", ["performance","sysadmin","blog"], "article", sub="linux")
add("eBPF — what it is", "https://ebpf.io/",
    "The extended Berkeley Packet Filter that turned the kernel into a programmable observability surface.", ["ebpf","kernel","observability"], "project", sub="linux")
add("MIT 6.824 — Distributed Systems", "https://pdos.csail.mit.edu/6.824/",
    "The canonical distributed systems course — RPC, consensus, replication, fault tolerance.", ["distributed-systems","consensus","course"], "course", sub="distributed")
add("The System Design Primer", "https://github.com/donnemartin/system-design-primer",
    "Load balancers, CDNs and consensus algorithms explained with diagrams — the structured map of how big systems fit together.", ["system-design","architecture","scalability"], "repo", sub="distributed")
add("Google SRE Books", "https://sre.google/books/",
    "Google's free SRE books — how the world's largest systems are engineered, run and kept alive.", ["sre","reliability","monitoring"], "book", sub="distributed")
add("Tailscale Blog", "https://tailscale.com/blog/",
    "Deep dives into WireGuard, mesh networking and building secure networks at scale.", ["networking","wireguard","mesh"], "article", sub="networking")
add("The 9P network protocol & Plan 9", "https://9p.io/plan9/",
    "Plan 9 from Bell Labs — the true Unix successor that made everything files and lost the OS war but won the ideas war.", ["plan9","distributed","unix-history"], "project", sub="unix")
add("Inferno® Operating System", "https://en.wikipedia.org/wiki/Inferno_(operating_system)",
    "The distributed OS from Bell Labs that treats the network as a filesystem — a glimpse at an alternate timeline.", ["operating-systems","distributed","bell-labs"], "archive", sub="unix")
add("The Cathedral and the Bazaar", "https://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/",
    "Raymond's essay on how the internet builds software — cathedral vs. bazaar, one of the founding texts of open-source", ["foss","essay","history"], "article", sub="foss")
add("Sneakernet", "https://en.wikipedia.org/wiki/Sneakernet",
    "The network where data travels on physical media — sometimes the fastest link is a bicycle.", ["offline","networking","resilience"], "archive", sub="networking")

# --- internet infrastructure (carried) ---
add("How DNS works (interactive)", "https://howdns.works/",
    "From browser to root servers to authoritative nameserver — visual DNS explained.", ["dns","networking","tutorial"], "guide", sub="networking")
add("What is BGP?", "https://www.cloudflare.com/learning/security/glossary/what-is-bgp/",
    "Cloudflare's introduction to the routing protocol that holds the internet's autonomous systems together.", ["bgp","routing","protocol"], "guide", sub="networking")
add("Internet Exchange Points", "https://en.wikipedia.org/wiki/Internet_exchange_point",
    "The physical buildings where ISPs exchange traffic — the real fabric of the internet.", ["ixp","peering","infrastructure"], "archive", sub="networking")
add("Submarine Cable Map", "https://www.submarinecablemap.com/",
    "Interactive map of the 400+ undersea fiber cables carrying 99% of international data.", ["submarine-cables","fiber","map"], "tool", sub="networking")
add("Starlink", "https://www.starlink.com/",
    "SpaceX's LEO constellation — a new class of connectivity and the backup many remote sites now buy first.", ["satellite","internet","spacex"], "org", sub="networking")
add("Mesh networking", "https://en.wikipedia.org/wiki/Mesh_networking",
    "How BATMAN, OLSR and 802.11s let communities build internet between themselves without ISPs.", ["mesh","decentralized","community"], "archive", sub="networking")
add("Guifi.net", "https://guifi.net/en",
    "The world's largest open community network — 30,000+ nodes, proof that community internet works.", ["community-network","mesh","isp-alternative"], "org", sub="networking")
add("NYC Mesh", "https://www.nycmesh.net/",
    "New York's community-owned network — rooftop antennas and fiber that belongs to its users.", ["mesh","community","diy"], "project", sub="networking")

# --- large-scale / server computing (carried + curated) ---
add("OpenResty", "https://openresty.org/en/",
    "Nginx + LuaJIT as a full web platform — the stack behind much of the high-throughput internet.", ["nginx","lua","web"], "project", sub="web")
add("Kubernetes", "https://kubernetes.io/",
    "Container orchestration at data-center scale — the standards for running fleets.", ["kubernetes","containers","orchestration"], "org", sub="web")
add("Ceph", "https://ceph.io/en/",
    "Open distributed storage at petabyte scale — the filesystem behind massive clusters.", ["storage","distributed","filesystem"], "project", sub="data")
add("NixOS", "https://nixos.org/",
    "The reproducible operating system — every state defined in config, atomic upgrades, declarative servers.", ["nix","reproducible","linux"], "project", sub="unix")
add("IBM Z mainframes", "https://en.wikipedia.org/wiki/IBM_Z",
    "The 99.999%-reliability machines that still run banking, airlines and government — uptime in decades.", ["mainframe","enterprise","reliability"], "archive", sub="data")
add("High-Performance Computing", "https://en.wikipedia.org/wiki/High-performance_computing",
    "Supercomputer architecture — InfiniBand interconnects, parallel filesystems, SLURM scheduling.", ["hpc","cluster","parallel"], "archive", sub="data")
add("Blade servers — density computing", "https://en.wikipedia.org/wiki/Blade_server",
    "Sharing power, cooling and networking across a chassis — the density play of data centers.", ["server","density","hardware"], "archive", sub="data")
add("Data center cooling", "https://en.wikipedia.org/wiki/Data_center_cooling",
    "From AC to immersion cooling to Arctic siting — the invisible engineering of keeping the cloud cool.", ["data-center","cooling","energy"], "archive", sub="data")
add("Google's Borg", "https://research.google/pubs/pub43438/",
    "The cluster manager that runs billions of containers weekly and fathered Kubernetes.", ["google","borg","cluster-management"], "paper", sub="data", source="Google Research")
add("The Illustrated TLS Connection", "https://tls.ulfheim.net/",
    "A handshake in frame-by-frame glory — TLS explained one byte at a time.", ["tls","crypto","tutorial"], "guide", sub="networking")
add("Julia Evans", "https://jvns.ca/",
    "Zines and posts that turn gnarly systems concepts (DNS, strace, HTTP) into things you can actually carry around.", ["sysadmin","debugging","blog"], "article", sub="unix")

write_cat("systems", A)