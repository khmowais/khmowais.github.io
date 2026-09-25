import sys; sys.path.insert(0, "/tmp/opencode/links")
from lg import L, write_cat

A = []
def add(*a, **k): A.append(L(*a, **k))

# --- local inference engines ---
add("llama.cpp", "https://github.com/ggml-org/llama.cpp",
    "LLM inference in plain C/C++, no GPU required — the backbone of the local-AI movement and the reference for GGUF.", ["inference","cpu","c++"], "repo", sub="engines")
add("Ollama", "https://github.com/ollama/ollama",
    "The repo behind the one-command local model runner; server, model library and desktop apps.", ["local","serving"], "repo", sub="engines")
add("LocalAI", "https://github.com/mudler/LocalAI",
    "Drop-in OpenAI-compatible local inference covering text, vision, TTS and embeddings.", ["local","serving","api"], "repo", sub="engines")
add("LM Studio", "https://lmstudio.ai/",
    "Grab-and-run local models with a nice GUI and OpenAI-compatible server.", ["local","gui"], "project", sub="engines")
add("Jan", "https://github.com/janhq/jan",
    "Offline-first desktop AI assistant — your data stays in your machine.", ["local","offline","desktop"], "repo", sub="engines")
add("GPT4All", "https://github.com/nomic-ai/gpt4all",
    "Local chat with open models on consumer hardware, plus a training data consciousness claim — run anything on a laptop.", ["local","offline","desktop"], "repo", sub="engines")
add("llama-cpp-python", "https://github.com/abetlen/llama-cpp-python",
    "Python bindings for llama.cpp with an OpenAI-compatible server — the fastest way to prototype GGUF apps.", ["python","llama.cpp","api"], "repo", sub="engines")
add("exllamav2", "https://github.com/turboderp/exllamav2",
    "Fast GPU inference for EXL2/GPTQ models — strong speed and low memory for dense models on desktop GPUs.", ["inference","gpu","quantization"], "repo", sub="engines")
add("koboldcpp", "https://github.com/LostRuins/koboldcpp",
    "A self-contained llama.cpp fork tuned for roleplay/story flows with a web UI — also a good generic single-file server.", ["inference","ui"], "repo", sub="engines")
add("KTransformers", "https://github.com/kvcache-ai/KTransformers",
    "Long-context, low-latency local inference — exploits CPU/GPU heterogeneity to run big models on small machines.", ["inference","cpu","long-context"], "repo", sub="engines")
add("whisper.cpp", "https://github.com/ggml-org/whisper.cpp",
    "Whisper speech recognition ported to plain C/C++ — runs on phone, Pi, laptop, no GPU.", ["speech","offline","c++"], "repo", sub="engines")
add("ggml", "https://github.com/ggml-org/ggml",
    "The tensor library behind llama.cpp and whisper.cpp; GGUF is defined here.", ["inference","c++","format"], "repo", sub="engines")

# --- self-hosted LLM apps ---
add("Open WebUI", "https://github.com/open-webui/open-webui",
    "Self-hosted ChatGPT-style interface for Ollama/OpenAI-compatible backends — users, models, RAG chat.", ["ui","rag","ollama"], "repo", sub="apps")
add("PrivateGPT", "https://github.com/zylon-ai/private-gpt",
    "Ask questions over private documents with no data leaving your machine.", ["rag","privacy","offline"], "repo", sub="apps")
add("AnythingLLM", "https://github.com/Mintplex-Labs/anything-llm",
    "All-in-one local AI workspace: documents → private knowledge base + chat, many backend options.", ["rag","workspace"], "repo", sub="apps")
add("Text Generation WebUI (oobabooga)", "https://github.com/oobabooga/text-generation-webui",
    "The classic browser UI for local models — LoRA loading, multimodal, extensions.", ["ui","local"], "repo", sub="apps")
add("ComfyUI", "https://github.com/comfyanonymous/ComfyUI",
    "Node-based interface for stable diffusion and image workflows — the power-user's local image tool.", ["image","generative","ui"], "repo", sub="apps")
add("Stable Diffusion WebUI (AUTOMATIC1111)", "https://github.com/AUTOMATIC1111/stable-diffusion-webui",
    "The browser interface that made local image generation accessible to everyone.", ["image","generative","ui"], "repo", sub="apps")
add("Docs: Open WebUI", "https://docs.openwebui.com/",
    "Official docs for the self-hosted chat frontend.", ["docs","ui"], "docs", sub="apps")

# --- homelab / self-hosting foundation ---
add("Home Assistant", "https://github.com/home-assistant/core",
    "Open-source home automation that runs entirely on your own hardware.", ["homelab","automation"], "repo", sub="homelab")
add("Nextcloud", "https://github.com/nextcloud/server",
    "Self-hosted files, calendar, contacts, talk and notes — your own cloud.", ["homelab","files","cloud"], "repo", sub="homelab")
add("Immich", "https://github.com/immich-app/immich",
    "Self-hosted Google Photos replacement with on-device face/object data and mobile apps.", ["homelab","photos"], "repo", sub="homelab")
add("Frigate", "https://github.com/blakeblackshear/frigate",
    "NVR with real-time local object detection — cameras that never phone home.", ["homelab","cameras","computer-vision"], "repo", sub="homelab")
add("Jellyfin", "https://jellyfin.org/",
    "Free media server — own your movies, music and TV, stream to every device.", ["homelab","media"], "org", sub="homelab")
add("Podman", "https://podman.io/",
    "Daemonless container engine — containers without a central daemon, rootless by design.", ["containers","linux"], "project", sub="containers")
add("Docker Docs", "https://docs.docker.com/",
    "The docs every self-hoster ends up reading before breakfast.", ["containers","docs"], "docs", sub="containers")
add("Kubernetes Docs", "https://kubernetes.io/docs/",
    "Container orchestration at scale — the boring coordination layer for fleets.", ["orchestration","k8s"], "docs", sub="containers")
add("k3s", "https://k3s.io/",
    "A lightweight certified Kubernetes for small machines and labs.", ["orchestration","k8s","edge"], "project", sub="containers")
add("Caddy", "https://caddyserver.com/docs/",
    "Web server / reverse proxy with automatic HTTPS — the friendly face of self-hosting.", ["reverse-proxy","https"], "docs", sub="networking")
add("Traefik", "https://traefik.io/",
    "Cloud-native reverse proxy and edge router that watches your containers.", ["reverse-proxy"], "project", sub="networking")
add("Nginx Proxy Manager", "https://github.com/NginxProxyManager/nginx-proxy-manager",
    "GUI-based reverse proxy with Let's Encrypt — the homelab staple.", ["reverse-proxy","gui"], "repo", sub="networking")
add("Tailscale", "https://tailscale.com/",
    "WireGuard-based mesh VPN that makes your machines feel like one network, anywhere.", ["vpn","mesh"], "project", sub="networking")
add("Headscale", "https://github.com/juanfont/headscale",
    "Self-hosted implementation of the Tailscale control server — your mesh, your server.", ["vpn","mesh","self-hosted"], "repo", sub="networking")
add("WireGuard", "https://www.wireguard.com/",
    "The crypto-audited, fast VPN that replaced a decade of complexity.", ["vpn","crypto"], "project", sub="networking")
add("OpenSSH", "https://www.openssh.com/",
    "The system every Linux box runs on; also your tunnelling Swiss-army knife.", ["ssh","security"], "org", sub="networking")

# --- monitoring / ops ---
add("Prometheus", "https://prometheus.io/docs/",
    "Time-series monitoring and alerting — the default metrics backend of the self-hosted world.", ["monitoring","metrics"], "docs", sub="monitoring")
add("Grafana", "https://grafana.com/docs/",
    "Dashboards over Prometheus (and everything else) — turning numbers into pictures.", ["monitoring","dashboards"], "docs", sub="monitoring")
add("Netdata", "https://github.com/netdata/netdata",
    "Real-time, per-second system monitoring with almost zero setup.", ["monitoring"], "repo", sub="monitoring")
add("Uptime Kuma", "https://github.com/louislam/uptime-kuma",
    "Self-hosted uptime monitoring with status pages and notifications.", ["monitoring","uptime"], "repo", sub="monitoring")
add("Grafana Loki", "https://github.com/grafana/loki",
    "Horizontally scalable log aggregation built to be cheap to run at home.", ["logs","monitoring"], "repo", sub="monitoring")

# --- storage / backup ---
add("OpenZFS Docs", "https://openzfs.github.io/openzfs-docs/",
    "Documentation for the ZFS filesystem — checksumming, snapshots, RAID-Z, self-healing.", ["filesystem","zfs","storage"], "docs", sub="storage")
add("TrueNAS", "https://www.truenas.com/",
    "Open-source NAS operating system built on ZFS — the serious home data appliance.", ["nas","zfs"], "project", sub="storage")
add("OpenMediaVault", "https://github.com/openmediavault/openmediavault",
    "Debian-based NAS OS — lightweight, plugins for everything.", ["nas"], "repo", sub="storage")
add("rclone", "https://rclone.org/",
    "Sync and mount files to/from 40+ cloud and local backends — the Swiss-army copy tool.", ["sync","backup"], "tool", sub="backup")
add("restic", "https://github.com/restic/restic",
    "Fast, encrypted, deduplicated backups that actually restore.", ["backup","encryption"], "repo", sub="backup")
add("BorgBackup", "https://github.com/borgbackup/borg",
    "Deduplicating backup program with compression and encryption.", ["backup","dedup"], "repo", sub="backup")
add("Sanoid", "https://github.com/jimsalterjrs/sanoid",
    "Policy-driven ZFS snapshot management and replication.", ["zfs","snapshots","backup"], "repo", sub="backup")
add("Syncthing", "https://syncthing.net/",
    "Continuous peer-to-peer file sync without a central server — your data, your devices.", ["sync","p2p"], "project", sub="backup")
add("Proxmox VE", "https://www.proxmox.com/",
    "Open-source virtualization platform (KVM + LXC) — the homelab hypervisor of choice.", ["virtualization","homelab"], "project", sub="homelab")
add("Proxmox Docs", "https://pve.proxmox.com/wiki/",
    "The wiki/docs for Proxmox VE administration.", ["docs","virtualization"], "docs", sub="homelab")

# --- communities / indexes ---
add("awesome-selfhosted", "https://github.com/awesome-selfhosted/awesome-selfhosted",
    "The canonical list of self-hosted alternatives to mainstream services, with licenses.", ["list","self-hosted"], "repo", sub="index")
add("r/selfhosted", "https://www.reddit.com/r/selfhosted/",
    "Reddit community — what people actually run, and what breaks.", ["community","self-hosted"], "forum", sub="index")
add("r/homelab", "https://www.reddit.com/r/homelab/",
    "Homelab hardware, racks and the eternal 'how much is this costing me' thread.", ["community","homelab"], "forum", sub="index")
add("Talos Linux", "https://github.com/siderolabs/talos",
    "Kubernetes-optimized minimal Linux — you only ever write YAML, never SSH.", ["linux","k8s"], "repo", sub="containers")
add("RaspberryPi Official Documentation", "https://www.raspberrypi.com/documentation/",
    "The docs for the little board that powers half of homelab-land.", ["docs","hardware","pi"], "docs", sub="homelab")

write_cat("local-ai", A)