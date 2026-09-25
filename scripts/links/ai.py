import sys; sys.path.insert(0, "/tmp/opencode/links")
from lg import L, write_cat

A = []

def add(*a, **k): A.append(L(*a, **k))

# --- foundational papers ---
add("Attention Is All You Need", "https://arxiv.org/abs/1706.03762",
    "The Transformer paper that replaced recurrence with self-attention. The architecture almost every modern LLM is built on.", ["transformer","paper"], "paper", sub="models", year=2017, source="arXiv")
add("BERT: Pre-training of Deep Bidirectional Transformers", "https://arxiv.org/abs/1810.04805",
    "The masked-language-model pretraining recipe that made transfer learning the default in NLP.", ["pretraining","nlp"], "paper", sub="models", year=2018, source="arXiv")
add("Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", "https://arxiv.org/abs/2005.11401",
    "Karpukhin et al.'s original RAG — parametric + non-parametric memory combined at generation time.", ["rag","retrieval"], "paper", sub="rag", year=2020, source="arXiv")
add("Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", "https://arxiv.org/abs/2201.11903",
    "The paper that showed intermediate reasoning steps unlock arithmetic and reasoning in LLMs.", ["prompting","reasoning"], "paper", sub="prompt-engineering", year=2022, source="arXiv")
add("ReAct: Synergizing Reasoning and Acting in Language Models", "https://arxiv.org/abs/2210.03629",
    "Interleaving thought traces with actions — the basis of most modern tool-using agent loops.", ["agents","tool-use"], "paper", sub="agents", year=2022, source="arXiv")
add("Toolformer: Language Models Can Teach Themselves to Use Tools", "https://arxiv.org/abs/2302.04761",
    "Self-supervised learning of when to call external tools.",
    ["agents","tool-use","self-supervised"], "paper", sub="agents", year=2023, source="arXiv")
add("Constitutional AI: Harmlessness from AI Feedback", "https://arxiv.org/abs/2212.08073",
    "Anthropic's method for steering models with written principles instead of pure labeled data.", ["alignment","safety"], "paper", sub="alignment", year=2022, source="arXiv")
add("Self-Refine: Iterative Refinement with Self-Feedback", "https://arxiv.org/abs/2303.17651",
    "Generate, critique, refine — a minimal loop that makes one model act as its own editor.", ["agents","refinement"], "paper", sub="agents", year=2023, source="arXiv")
add("Reflexion: Language Agents with Verbal Reinforcement Learning", "https://arxiv.org/abs/2303.11366",
    "Agents that keep a natural-language memory of what went wrong and improve over episodes.", ["agents","reinforcement"], "paper", sub="agents", year=2023, source="arXiv")
add("Generative Agents: Interactive Simulacra of Human Behavior", "https://arxiv.org/abs/2304.03442",
    "Stanford/Google small-town simulation — memory, reflection and planning inside a multi-agent world.", ["agents","multi-agent"], "paper", sub="agents", year=2023, source="arXiv")
add("The Bitter Lesson", "https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf",
    "Rich Sutton's essay: general methods that leverage computation keep winning over human-engineered knowledge. Short, sharp, often debated, never really refuted.", ["ai","philosophy","scaling"], "article", sub="research", year=2019, source="incompleteideas")
add("LoRA: Low-Rank Adaptation of Large Language Models", "https://arxiv.org/abs/2106.09685",
    "Train a handful of low-rank matrices instead of the whole model — the technique that made fine-tuning affordable.", ["finetuning"], "paper", sub="finetuning", year=2021, source="arXiv")
add("QLoRA: Efficient Finetuning of Quantized LLMs", "https://arxiv.org/abs/2305.14314",
    "Backprop through 4-bit quantized weights, making full fine-tuning fit on a single consumer GPU.", ["finetuning","quantization"], "paper", sub="finetuning", year=2023, source="arXiv")
add("GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers", "https://arxiv.org/abs/2210.17323",
    "Post-training weight quantization that keeps accuracy at 2-4 bits per weight.", ["quantization","inference"], "paper", sub="quantization", year=2022, source="arXiv")
add("AWQ: Activation-aware Weight Quantization", "https://arxiv.org/abs/2306.00978",
    "Quantization that protects the small fraction of weights that matter, protecting fewer, protecting activation-focused salience.", ["quantization","inference"], "paper", sub="quantization", year=2023, source="arXiv")
add("Language Models are Few-Shot Learners (GPT-3)", "https://arxiv.org/abs/2005.14165",
    "The original scale paper — emergence of in-context learning as models grow.", ["models","scaling","in-context-learning"], "paper", sub="models", year=2020, source="arXiv")
add("Training language models to follow instructions with human feedback (InstructGPT)", "https://arxiv.org/abs/2203.02155",
    "RLHF done right: preferenced-based steering that aligned GPT-3 to instruction following.", ["alignment","rlhf"], "paper", sub="alignment", year=2022, source="arXiv")
add("Direct Preference Optimization: Your Language Model is Secretly a Reward Model", "https://arxiv.org/abs/2305.18290",
    "Replaces the separate reward model in RLHF with the policy itself — simpler, stable preference optimization.", ["alignment","rlhf"], "paper", sub="alignment", year=2023, source="arXiv")
add("Hugging Face Transformers", "https://github.com/huggingface/transformers",
    "The standard library for downloading, using and training open model architectures in PyTorch/TF.", ["models","library","pytorch"], "repo", sub="libraries", year=2018, source="GitHub")
add("Hugging Face Docs", "https://huggingface.co/docs",
    "Documentation for the HF ecosystem — transformers, datasets, tokenizers, diffusers, and the Hub.", ["docs","models","library"], "docs", sub="libraries")
add("PyTorch", "https://github.com/pytorch/pytorch",
    "The deep learning framework most open-model work is built on.", ["ml","framework","pytorch"], "repo", sub="libraries")
add("Ollama", "https://ollama.com/",
    "Run open-weight LLMs locally with a one-line command; ships a model library and a simple REST API.", ["local","models","serving"], "project", sub="local", year=2023)
add("vLLM", "https://github.com/vllm-project/vllm",
    "High-throughput LLM serving with PagedAttention — the de-facto engine for serving LLMs on GPUs.", ["serving","inference","gpu"], "repo", sub="inference")
add("SGLang", "https://github.com/sgl-project/sglang",
    "Fast serving framework with structured generation, radical state sharing and RadixAttention for prefix caching.", ["serving","inference","structured-outputs"], "repo", sub="inference")
add("Text Generation Inference (TGI)", "https://github.com/huggingface/text-generation-inference",
    "Hugging Face's production server for LLMs, powering their hosted inference API.", ["serving","inference"], "repo", sub="inference")
add("ONNX Runtime", "https://github.com/microsoft/onnxruntime",
    "Cross-platform inference engine for ONNX models — the interchange format many quantized models ship in.", ["inference","cross-platform"], "repo", sub="inference")
add("CTranslate2", "https://github.com/OpenNMT/CTranslate2",
    "Fast inference engine for transformer models with efficient CPU/GPU execution and quantization.", ["inference","cpu"], "repo", sub="inference")
add("bitsandbytes", "https://github.com/bitsandbytes-foundation/bitsandbytes",
    "8-bit and 4-bit quantization primitives for training and inference inside PyTorch.", ["quantization","training"], "repo", sub="quantization")
add("PEFT", "https://github.com/huggingface/peft",
    "Parameter-efficient fine-tuning methods (LoRA and friends) in one library.", ["finetuning","lora"], "repo", sub="finetuning")
add("TRL", "https://github.com/huggingface/trl",
    "Transformer Reinforcement Learning — SFT, PPO, DPO and friends for aligning models.", ["alignment","rlhf","finetuning"], "repo", sub="finetuning")
add("Axolotl", "https://github.com/axolotl-ai-cloud/axolotl",
    "Configuration-driven fine-tuning of open models — LoRA, QLoRA, full fine-tune, from one YAML.", ["finetuning"], "repo", sub="finetuning")
add("Unsloth", "https://github.com/unslothai/unsloth",
    "Fast memory-efficient QLoRA/LoRA fine-tuning with hand-optimized kernels; big speedups on consumer GPUs.", ["finetuning","optimization"], "repo", sub="finetuning")
add("DeepSpeed", "https://github.com/microsoft/DeepSpeed",
    "Microsoft's distributed training/inference stack — ZeRO sharding, offload, inference optimizations.", ["training","distributed"], "repo", sub="training-infra")

# --- agents & context engineering ---
add("LangGraph", "https://github.com/langchain-ai/langgraph",
    "Graph-based agent runtime for building stateful, controllable multi-step agent workflows.", ["agents","orchestration"], "repo", sub="agents")
add("OpenAI Agents SDK", "https://github.com/openai/openai-agents-python",
    "OpenAI's lightweight framework for agents, handoffs and tools.", ["agents","framework"], "repo", sub="agents")
add("Model Context Protocol", "https://modelcontextprotocol.io/",
    "Open standard from Anthropic giving LLMs a uniform way to talk to tools, data and resources.", ["mcp","protocol","tools"], "docs", sub="agents")
add("MCP Specification (GitHub)", "https://github.com/modelcontextprotocol/modelcontextprotocol",
    "The reference specification and SDKs for the Model Context Protocol.", ["mcp","protocol"], "repo", sub="agents")
add("DSPy", "https://github.com/stanfordnlp/dspy",
    "Programming instead of prompting — declare the pipeline, let the compiler optimize prompts/weights.", ["programming","prompting","optimization"], "repo", sub="agents")
add("Guidance", "https://github.com/guidance-ai/guidance",
    "Template-based structured generation that constrains token choice while keeping the prompt readable.", ["structured-outputs","prompting"], "repo", sub="structured-outputs")
add("Outlines", "https://github.com/dottxt-ai/outlines",
    "Guaranteed structured generation — regex, JSON schema, grammars — by constraining the model's token stream.", ["structured-outputs","json"], "repo", sub="structured-outputs")
add("Instructor", "https://github.com/instructor-ai/instructor",
    "Structured outputs from LLMs via Pydantic validation with retries and JSON parsing.", ["structured-outputs","pydantic"], "repo", sub="structured-outputs")
add("CrewAI", "https://github.com/crewAIInc/crewAI",
    "Role-based multi-agent framework for planning, execution and handoff between specialized agents.", ["agents","multi-agent"], "repo", sub="agents")
add("AutoGen", "https://github.com/microsoft/autogen",
    "Microsoft's multi-conversation agent framework for LLM applications.", ["agents","multi-agent"], "repo", sub="agents")
add("MetaGPT", "https://github.com/FoundationAgents/MetaGPT",
    "Multi-agent framework where agents play software-company roles (PM, architect, engineer).", ["agents","multi-agent"], "repo", sub="agents")
add("Anthropic Cookbook", "https://github.com/anthropics/anthropic-cookbook",
    "Working examples for agents, RAG, structured outputs and evaluations on Anthropic models.", ["agents","rag","examples"], "repo", sub="agents")
add("OpenAI Guides: Function Calling", "https://platform.openai.com/docs/guides/function-calling",
    "Official docs on reliable tool calling — schemas, parameters, and when to call tools.", ["tool-use","docs"], "docs", sub="agents")
add("OpenAI Guides: Structured Outputs", "https://platform.openai.com/docs/guides/structured-outputs",
    "Constraints that guarantee model outputs match a JSON schema.", ["structured-outputs","docs"], "docs", sub="structured-outputs")
add("Effective context engineering for AI agents (Anthropic)", "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
    "Anthropic engineering's practical guide to context windows — what to load, when, and how to keep agents on task.", ["context-engineering","agents","blog"], "article", sub="context-engineering", source="Anthropic")
add("Claude Code Docs", "https://docs.anthropic.com/en/docs/claude-code",
    "Official docs for Anthropic's terminal coding agent — a real production agent loop you can study.", ["agents","coding","docs"], "docs", sub="agents")

# --- RAG & retrieval & vector db ---
add("LlamaIndex", "https://github.com/run-llama/llama_index",
    "Data framework for connecting LLMs to your data — ingestion, indexes, retrievers and query engines.", ["rag","retrieval"], "repo", sub="rag")
add("Microsoft GraphRAG", "https://github.com/microsoft/graphrag",
    "Graph-based RAG: builds a knowledge graph then answers over communities — for global, relational questions.", ["rag","knowledge-graph"], "repo", sub="rag")
add("Ragas", "https://github.com/explodinggradients/ragas",
    "Evaluation framework for RAG pipelines — faithfulness, answer relevance, context precision.", ["rag","evaluation"], "repo", sub="eval")
add("Chroma", "https://github.com/chroma-core/chroma",
    "Embedding database that runs in-process — a simple on-ramp to vector search.", ["vector-db","embeddings"], "repo", sub="vector-db")
add("Qdrant", "https://github.com/qdrant/qdrant",
    "Rust vector search engine with filtering, payloads and similarity scoring.", ["vector-db","search"], "repo", sub="vector-db")
add("Weaviate", "https://github.com/weaviate/weaviate",
    "Open vector database with hybrid search (dense + sparse) and modules.", ["vector-db","hybrid-search"], "repo", sub="vector-db")
add("Milvus", "https://github.com/milvus-io/milvus",
    "Purpose-built vector database for large-scale similarity search.", ["vector-db"], "repo", sub="vector-db")
add("pgvector", "https://github.com/pgvector/pgvector",
    "Postgres extension for vector similarity — keep relational and vector data in one database.", ["vector-db","postgres"], "repo", sub="vector-db")
add("FAISS", "https://github.com/facebookresearch/faiss",
    "Meta's library for efficient similarity search and clustering of dense vectors.", ["vector-search","similarity"], "repo", sub="vector-db")
add("MTEB", "https://github.com/embeddings-benchmark/mteb",
    "Massive Text Embedding Benchmark — the standard across embedding models.", ["embeddings","benchmark","evaluation"], "repo", sub="eval")
add("FlagEmbedding (BGE)", "https://github.com/FlagOpen/FlagEmbedding",
    "BAAI's open embedding family (BGE) plus training/inference code for retrieval and reranking.", ["embeddings","reranking"], "repo", sub="embeddings")
add("Sentence Transformers", "https://github.com/UKPLab/sentence-transformers",
    "The library most embedding models were served from.", ["embeddings"], "repo", sub="embeddings")
add("LLMTest Needle In A Haystack", "https://github.com/gkamradt/LLMTest_NeedleInAHaystack",
    "The tool that made everyone measure real long-context behavior instead of trusting the spec sheet.", ["long-context","evaluation","context-engineering"], "repo", sub="eval")
add("LongBench", "https://github.com/THUDM/LongBench",
    "Adversarial and long-document eval suite for long-context LLMs.", ["long-context","evaluation"], "repo", sub="eval")

# --- evaluation ---
add("lm-evaluation-harness", "https://github.com/EleutherAI/lm-evaluation-harness",
    "EleutherAI's harness for running standard benchmarks (MMLU, GSM8K, etc.) on local or API models.", ["evaluation","benchmark","local"], "repo", sub="eval")
add("OpenAI Evals", "https://github.com/openai/evals",
    "OpenAI's framework for creating and running evals; great pattern reference for grading scaffolding.", ["evaluation"], "repo", sub="eval")
add("DeepEval", "https://github.com/confident-ai/deepeval",
    "Unit-testing for LLM apps — metrics for answer relevance, faithfulness, hallucination, plus Pytest integration.", ["evaluation","testing"], "repo", sub="eval")
add("HELM", "https://github.com/stanford-crfm/helm",
    "Stanford's Holistic Evaluation of Language Models — 80+ scenarios, broad and transparent.", ["evaluation","benchmark"], "repo", sub="eval")
add("BIG-bench", "https://github.com/google/BIG-bench",
    "Collaborative benchmark of 200+ tasks designed to stay useful as models get smarter.", ["evaluation","benchmark"], "repo", sub="eval")
add("SWE-bench", "https://github.com/princeton-nlp/SWE-bench",
    "Real GitHub issues + tests — the benchmark that made coding agents measurable.", ["evaluation","coding","agents"], "repo", sub="eval")
add("MMLU (paper)", "https://arxiv.org/abs/2009.03300",
    "Measuring Massive Multitask Language Understanding — 57 subjects, the academic benchmark that defined a generation.", ["evaluation","benchmark"], "paper", sub="eval", year=2020, source="arXiv")
add("MT-Bench & Chatbot Arena (FastChat)", "https://github.com/lm-sys/FastChat",
    "The LMSYS codebase behind MT-Bench and the (now LMArena) crowdsourced model comparisons.", ["benchmark","arena"], "repo", sub="eval")
add("LMArena", "https://chat.lmsys.org/",
    "Crowdsourced blind comparison of models — millions of votes, Elo rankings.", ["benchmark","arena"], "tool", sub="eval")
add("Promptfoo", "https://github.com/promptfoo/promptfoo",
    "CLI/CI evaluation and red-teaming for prompts and providers — assert on outputs, catch regressions.", ["evaluation","red-teaming"], "repo", sub="eval")
add("MLflow(LLM tracing)", "https://github.com/mlflow/mlflow",
    "Open platform for the ML lifecycle; its LLM tracing complements evaluation with run-level insight.", ["observability","mlops"], "repo", sub="observability")
add("Hugging Face Open LLM Leaderboard", "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard",
    "Community leaderboard of open models across standard benchmarks.", ["benchmark","models"], "tool", sub="eval")

# --- security / safety ---
add("OWASP Top 10 for LLM Applications", "https://github.com/OWASP/www-project-top-10-for-large-language-model-applications",
    "The community-driven risk catalog for LLM apps — prompt injection, data poisoning, and the rest.", ["security","prompt-injection"], "repo", sub="security")
add("Universal and Transferable Attacks on Aligned LLMs", "https://arxiv.org/abs/2307.15043",
    "The GCG optimisation that showed even aligned models can be jailbroken with a crafted suffix.", ["security","jailbreaks"], "paper", sub="security", year=2023, source="arXiv")
add("Indirect Prompt Injection (Not what you've signed up for)", "https://arxiv.org/abs/2302.12173",
    "Greshake et al.: attacks that arrive through the content an app ingests, not user input.", ["security","prompt-injection"], "paper", sub="security", year=2023, source="arXiv")
add("Prompt Injection attack against LLM-integrated applications", "https://arxiv.org/abs/2306.05499",
    "Appfluent attack toolkit and taxonomy of prompt-injection vectors across apps.", ["security","prompt-injection"], "paper", sub="security", year=2023, source="arXiv")
add("EleutherAI Pythia", "https://github.com/EleutherAI/pythia",
    "A fully documented, interpretable suite of 70M-to-12B models for studying scaling and safety.", ["research","interpretability","models"], "repo", sub="research")
add("Anthropic Research", "https://www.anthropic.com/research",
    "Interpretability, alignment and scaling research from Anthropic.", ["research","alignment"], "org", sub="research")
add("OpenAI Research Index", "https://openai.com/research/",
    "Papers and technical reports from OpenAI — from GPT to evals.", ["research"], "docs", sub="research")

# --- open-weight & small models ---
add("Meta Llama (official)", "https://www.llama.com/",
    "Meta's open-weight family — model docs, licensing and the hosted API.", ["models","open-weights"], "docs", sub="models")
add("Mistral", "https://mistral.ai/",
    "European open-weights lab — small dense models and the MoE line.", ["models","open-weights"], "org", sub="models")
add("Qwen (Alibaba Cloud)", "https://github.com/QwenLM/Qwen3",
    "Open-weight model family known for strong small models and aggressive context windows.", ["models","open-weights"], "repo", sub="models")
add("Phi-3 (Microsoft)", "https://huggingface.co/microsoft/Phi-3.5-mini-instruct",
    "Microsoft's small model line — surprisingly good reasoning per parameter.", ["models","small-models"], "repo", sub="models")
add("SmolLM / SmolLM2 (HF)", "https://huggingface.co/blog/smollm",
    "Hugging Face's tiny (135M-1.7B) models trained on high-quality data, plus the blog explaining the recipe.", ["models","small-models"], "article", sub="models")
add("TinyLlama", "https://huggingface.co/TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T",
    "A 1.1B model from a 3-trillion-token pretraining experiment — small-scale training, unexpectedly capable.", ["models","small-models","open-weights"], "repo", sub="models")
add("Gemma (Google)", "https://github.com/google-deepmind/gemma",
    "Google's open-weight family for research and experimentation.", ["models","open-weights"], "repo", sub="models")
add("Whisper (OpenAI)", "https://github.com/openai/whisper",
    "Robust speech recognition across dozens of languages — the open ASR standard.", ["speech","asr"], "repo", sub="voice")
add("faster-whisper", "https://github.com/SYSTRAN/faster-whisper",
    "Reimplementation of Whisper with CTranslate2 — several times faster, surprisingly cheap.", ["speech","asr","optimization"], "repo", sub="voice")
add("Piper", "https://github.com/rhasspy/piper",
    "Fast, local, neural text-to-speech that runs great on a Raspberry Pi.", ["speech","tts","offline"], "repo", sub="voice")
add("Coqui TTS", "https://github.com/coqui-ai/TTS",
    "Deep learning TTS research library — XTTS and friends.", ["speech","tts"], "repo", sub="voice")
add("Vosk", "https://github.com/alphacep/vosk-api",
    "Offline speech recognition languages, small models, works on embedded devices.", ["speech","asr","offline"], "repo", sub="voice")
add("sherpa-onnx", "https://github.com/k2-fsa/sherpa-onnx",
    "Speech + LLM inference (ASR, TTS, speaker ID) on the edge via ONNX — phones, Pi, browsers.", ["speech","edge","asr","tts"], "repo", sub="voice")

# --- multimodal ---
add("CLIP (OpenAI)", "https://arxiv.org/abs/2103.00020",
    "Contrastive image-text pretraining — the embedding backbone behind modern vision-language systems.", ["multimodal","vision"], "paper", sub="multimodal", year=2021, source="arXiv")
add("LLaVA: Large Language and Vision Assistant", "https://arxiv.org/abs/2304.08485",
    "The open vision-language assistant recipe that kicked off the VLM boom.", ["multimodal","vision"], "paper", sub="multimodal", year=2023, source="arXiv")
add("Vision Transformers (ViT)", "https://arxiv.org/abs/2010.11929",
    "Applying the Transformer directly to image patches — no convolutions.", ["multimodal","vision","transformer"], "paper", sub="multimodal", year=2020, source="arXiv")
add("ColPali", "https://arxiv.org/abs/2407.01449",
    "Retrieval over documents by embedding page + query jointly — strong results for RAG over PDFs/slides.", ["multimodal","retrieval","rag"], "paper", sub="multimodal", year=2024, source="arXiv")

# --- observability & production ---
add("Langfuse", "https://github.com/langfuse/langfuse",
    "Open-source LLM engineering platform — tracing, prompts, evals, experiments.", ["observability","tracing"], "repo", sub="observability")
add("Phoenix (Arize)", "https://github.com/Arize-ai/phoenix",
    "Open observability and evaluation for AI apps — tracing, embedding inference, evals.", ["observability","tracing","evaluation"], "repo", sub="observability")
add("OpenTelemetry GenAI semantic conventions", "https://opentelemetry.io/docs/specs/semconv/gen-ai/",
    "The vendor-neutral trace spec for LLM apps — the boring, durable way to observe agents.", ["observability","tracing","protocol"], "docs", sub="observability")
add("LiteLLM", "https://github.com/BerriAI/litellm",
    "One interface to 100+ LLM providers, plus a proxy with routing, budgets and logging.", ["routing","api","proxy"], "repo", sub="production")
add("OpenRouter", "https://openrouter.ai/",
    "Universal gateway/routing across many models with a single API key.", ["routing","api"], "tool", sub="production")
add("Replicate", "https://replicate.com/",
    "Hosted running of open models (and fine-tunes) behind a simple API.", ["serving","api"], "tool", sub="production")
add("Vercel AI SDK", "https://github.com/vercel/ai",
    "TypeScript toolkit for streaming generative UI and agent tools across providers.", ["framework","streaming"], "repo", sub="production")
add("Braintrust", "https://github.com/braintrustdata/braintrust-sdk",
    "Evaluation, tracing and prompt management with datacenter-grade collaboration.", ["evaluation","observability"], "repo", sub="production")
add("LangSmith", "https://docs.smith.langchain.com/",
    "Production tracing, evaluation and prompt management for LLM apps — LangChain's observability platform.", ["observability","evaluation","tracing"], "docs", sub="observability")

add("Lil'Log — Lillian Weng", "https://lilianweng.github.io/",
    "Some of the clearest technical writing on LLMs, RLHF and agents — the masterclass blog of the field.", ["blog","papers","research"], "article", sub="research", source="LilianWeng")
add("Distill", "https://distill.pub/",
    "Interactive explanations of machine learning ideas — the gold standard for making research genuinely understandable.", ["visualization","interactive","research"], "archive", sub="research")
add("The Annotated Transformer", "https://nlp.seas.harvard.edu/2018/04/03/attention.html",
    "The Transformer paper with a line-by-line PyTorch implementation — the fastest way from idea to 'I can build it'.", ["transformer","tutorial","pytorch"], "article", sub="models", source="Harvard NLP")
add("Karpathy — Neural Networks: Zero to Hero", "https://karpathy.ai/zero-to-hero.html",
    "Andrej Karpathy builds neural networks from absolute scratch — no frameworks, just math and code.", ["education","video","backprop"], "video", sub="models")
add("Gwern", "https://gwern.net/",
    "A meticulous essay library covering scaling laws, model memorization and rationality — long-form analysis at its best.", ["essays","scaling","research"], "article", sub="research")
add("Reinforcement Learning: An Introduction (Sutton & Barto)", "http://incompleteideas.net/book/the-book-2nd.html",
    "The textbook of RL — if you want agents that learn from interaction, this is non-negotiable.", ["rl","book","agents"], "book", sub="models")

write_cat("ai", A)