export interface Capability {
  t: string;
  d: string;
}

export interface ServiceGroup {
  id: string;
  code: string;
  title: string;
  blurb: string;
  annote: string;
  items: Capability[];
}

export interface Package {
  code: string;
  title: string;
  ideal: string;
  scope: string[];
  deliverables: string[];
  shape: string;
}

export const serviceGroups: ServiceGroup[] = [
  {
    id: "ai-llm",
    code: "A/01",
    title: "AI & LLM Engineering",
    blurb: "Applications built around language models — from a prototype to a production system with evals, safety and a budget.",
    annote: "the reason most people call me",
    items: [
      { t: "Custom AI assistants", d: "Product-shaped conversational agents for your domain." },
      { t: "LLM application development", d: "Applications that hide the model behind a real interface." },
      { t: "RAG systems", d: "Retrieval + generation, with sources you can actually trace." },
      { t: "Agentic AI systems", d: "Models that plan, decide and act — carefully." },
      { t: "Multi-agent architectures", d: "Several models, one goal, a coordinator in the middle." },
      { t: "Tool-calling systems", d: "Let the model pull levers in your software." },
      { t: "AI chat systems", d: "Web or native chat that stays coherent." },
      { t: "Voicebots", d: "Speak-first interfaces for people who won't type." },
      { t: "Conversational AI", d: "Dialogue flows that don't derail by turn three." },
      { t: "AI automation", d: "Models placed inside boring, valuable workflows." },
      { t: "LLM API integration", d: "Wired to OpenAI, Anthropic, or any endpoint you prefer." },
      { t: "Local LLM integration", d: "Models that run on your hardware, offline-friendly." },
      { t: "Model evaluation", d: "An eval harness before production gets a surprise." },
      { t: "Prompt & context engineering", d: "Inputs that work, not guesses that sort of do." },
      { t: "AI workflow design", d: "Deciding where the model actually belongs in the business." },
      { t: "AI application security", d: "Prompt injection, leaky context, access control." },
      { t: "LLM latency optimization", d: "Answers that arrive on time, without a GPU on fire." },
      { t: "AI cost optimization", d: "Token budgets that match the value being returned." },
      { t: "Retrieval optimization", d: "Chunking, embedding, reranking — measured, not estimated." },
      { t: "AI prototypes & MVPs", d: "Prove the idea in days; scale it only if it survives contact." },
      { t: "AI system audits", d: "What your existing AI does wrong, and what to change." },
      { t: "AI deployment", d: "Serving, monitoring, versioning, updates without drama." },
    ],
  },
  {
    id: "ml-ds",
    code: "A/02",
    title: "Data Science & Machine Learning",
    blurb: "Analyses and models that produce numbers you can trust — cleaned, evaluated, explained.",
    annote: "measure twice, ship once",
    items: [
      { t: "Exploratory data analysis", d: "What the data actually says, before anyone models it." },
      { t: "Data cleaning & preprocessing", d: "The unglamorous 80% that makes everything else real." },
      { t: "Statistical analysis", d: "Significance, distributions, and honest uncertainty." },
      { t: "Data visualization", d: "Charts that inform rather than decorate." },
      { t: "Dashboard development", d: "A single screen for the numbers that matter daily." },
      { t: "Feature engineering", d: "Turning raw fields into signal a model can use." },
      { t: "Predictive modeling", d: "Models that forecast behavior or outcomes." },
      { t: "Classification & regression", d: "The workhorse tasks, done properly." },
      { t: "Clustering & segmentation", d: "Finding the groups no one asked for yet." },
      { t: "Time-series analysis & forecasting", d: "Demand, load, trends — with the seasonality intact." },
      { t: "Recommendation systems", d: "Surfaces that rank what to show next." },
      { t: "Anomaly detection", d: "Finding the one transaction that doesn't fit." },
      { t: "NLP pipelines", d: "Text processing that survives real-world mess." },
      { t: "Computer vision", d: "Images in, useful decisions out." },
      { t: "ML pipelines", d: "Training to serving without a human babysitting each step." },
      { t: "Model evaluation", d: "Metrics chosen to match the actual business goal." },
      { t: "Model deployment", d: "No research-one-off; a service that can be maintained." },
      { t: "Data automation", d: "Reports and summaries that generate themselves." },
      { t: "Custom ML models", d: "A model built for your data, not a template." },
      { t: "Dataset preparation", d: "Creation, labelling strategy, and quality control." },
      { t: "Research & prototyping", d: "Answers to 'can this even work?', fast." },
    ],
  },
  {
    id: "software",
    code: "A/03",
    title: "Software Engineering",
    blurb: "Backends, APIs, tools and automation in plain Python and boring, maintainable stacks.",
    annote: "the backbone, kept quiet",
    items: [
      { t: "Python development", d: "The whole stack, from script to service." },
      { t: "Backend development", d: "Server logic that behaves under load." },
      { t: "REST APIs", d: "Interfaces machines can depend on." },
      { t: "FastAPI applications", d: "Structured, typed, documented APIs." },
      { t: "Automation scripts", d: "The small programs that delete admin tasks." },
      { t: "Web applications", d: "Full applications with a real interface." },
      { t: "Internal tools", d: "Software for the people whose time matters most." },
      { t: "Database-backed applications", d: "Data that stays consistent behind a friendly UI." },
      { t: "API integrations", d: "Two systems that stop pretending they're unrelated." },
      { t: "System integrations", d: "Legacy + modern, glued without fear." },
      { t: "Refactoring & modernization", d: "The old system, made maintainable instead of replaced." },
      { t: "Legacy code cleanup", d: "Removing the maze while the lights stay on." },
      { t: "Performance optimization", d: "Making slow things fast, measured before and after." },
      { t: "Testing", d: "Tests that protect the code you'll touch in two years." },
      { t: "Deployment & CI", d: "Getting code to production the boring, reliable way." },
      { t: "Linux/server setup", d: "Servers configured like anyone would want to wake up to." },
      { t: "Self-hosted applications", d: "Your own instance of the tools you rely on." },
      { t: "Technical debugging", d: "The investigation, the root cause, the fix that explains it." },
    ],
  },
  {
    id: "infra-automation",
    code: "A/04",
    title: "Data, Infrastructure & Automation",
    blurb: "Pipelines, integrations and self-hosted systems that run themselves — quietly, and forever.",
    annote: "make work evaporate",
    items: [
      { t: "Data pipelines", d: "Raw to ready, on schedule, with retries." },
      { t: "ETL / ELT", d: "Moving and reshaping data between systems." },
      { t: "Workflow automation", d: "Processes that no longer need a human in the loop." },
      { t: "Business process automation", d: "The paperwork, flattened into a few scripts." },
      { t: "Spreadsheet & system integrations", d: "Excel ↔ your stack, without the copy-paste." },
      { t: "API-based integrations", d: "Connecting SaaS tools into one coherent flow." },
      { t: "Scheduled data processing", d: "Nightly jobs that run themselves and report back." },
      { t: "Server deployment", d: "Getting services live, safely and reversibly." },
      { t: "Application hosting", d: "Your app, served fast, owned by you." },
      { t: "Monitoring & alerts", d: "You hear about problems before customers do." },
      { t: "Backup systems", d: "Restores that have actually been tested." },
      { t: "Linux infrastructure", d: "Servers, networking, and the boring glue." },
      { t: "Lightweight self-hosted systems", d: "Small, fast services on hardware you control." },
    ],
  },
  {
    id: "teaching",
    code: "A/05",
    title: "Teaching & Mentoring",
    blurb: "Guidance for students, teams and researchers — from a first LLM model to a finished thesis.",
    annote: "pay it forward in person",
    items: [
      { t: "Python mentoring", d: "From syntax to thinking in programs." },
      { t: "AI/ML mentoring", d: "The concepts, and the math behind the hype." },
      { t: "Data science mentoring", d: "Analysis habits that survive real data." },
      { t: "LLM engineering mentoring", d: "Building on top of models, safely and cheaply." },
      { t: "Final-year project guidance (FYP)", d: "Scoping, architecture, and not boiling the ocean." },
      { t: "Code review", d: "A second pair of eyes with opinions worth hearing." },
      { t: "Technical interview preparation", d: "Mock interviews and honest feedback." },
      { t: "Research guidance", d: "From literature to reproducible results." },
      { t: "Workshops", d: "Half-day and full-day hands-on sessions." },
      { t: "Bootcamps", d: "Structured, project-driven intensity." },
      { t: "Custom team training", d: "Upskilling aimed at your team's actual stack." },
    ],
  },
];

export const packages: Package[] = [
  {
    code: "P/01",
    title: "AI Discovery / Architecture Session",
    ideal: "You have a problem and an intuition that 'AI' is involved, but no idea of the shape.",
    scope: [
      "1–2 hour working session with your actual workflow",
      "Honest verdict: where AI helps, and where a script is better",
      "Technical direction, architecture sketch, and rough cost model",
    ],
    deliverables: ["A written technical direction you can act on", "A decision on build vs. wait vs. don't"],
    shape: "1–2 days · fixed fee · single engagement",
  },
  {
    code: "P/02",
    title: "AI Prototype",
    ideal: "You need to prove an AI idea works before any real investment.",
    scope: [
      "Smallest credible experiment: real data, real model, real evaluation",
      "A runnable prototype with the failure modes documented",
    ],
    deliverables: ["Working prototype", "What it does well / badly, in writing"],
    shape: "1–2 weeks · fixed scope · then decide",
  },
  {
    code: "P/03",
    title: "RAG / Knowledge Assistant",
    ideal: "Your team drowns in documents and wants a system that answers from them.",
    scope: [
      "Document ingestion & chunking strategy",
      "Retrieval with evaluation and reranking where it helps",
      "Interface: chat, search, or inside your existing tool",
    ],
    deliverables: ["Deployed assistant with source citations", "Eval set and retrieval metrics"],
    shape: "2–4 weeks · mid-size engagement",
  },
  {
    code: "P/04",
    title: "AI Agent Build",
    ideal: "Work that needs a model to use tools, follow workflows, and act on your systems.",
    scope: [
      "Tool design and orchestration",
      "Memory/state where appropriate",
      "Safety rails, evals, and observability",
    ],
    deliverables: ["Production agent with guardrails", "Operational runbook"],
    shape: "3–5 weeks · depends on tool surface area",
  },
  {
    code: "P/05",
    title: "Data Science Project",
    ideal: "You have data and a question; you want a defensible answer.",
    scope: [
      "Cleaning and exploratory analysis",
      "Modeling scoped to your question",
      "Evaluations and a plain-English writeup",
    ],
    deliverables: ["Analysis + model + report you can present"],
    shape: "2–4 weeks · fixed scope",
  },
  {
    code: "P/06",
    title: "Automation Package",
    ideal: "Repetitive manual work is eating someone's week.",
    scope: [
      "Mapping the current manual flow",
      "Scripts, APIs and integrations to replace it",
      "Logging and failure alerts, so it never silently breaks",
    ],
    deliverables: ["Working automation", "Documentation a stranger could run"],
    shape: "1–2 weeks · small, high-ROI",
  },
  {
    code: "P/07",
    title: "Custom Software Build",
    ideal: "A small internal tool, backend, web app, API or integration.",
    scope: [
      "Spec-in from a short discovery call",
      "Boring stack, owned by you, deployed on your infrastructure",
    ],
    deliverables: ["Source, docs, deployment", "Warranty fixes for a sensible window"],
    shape: "2–5 weeks · fixed price after scope is agreed",
  },
  {
    code: "P/08",
    title: "Mentoring / Technical Coaching",
    ideal: "You (or your team) want to level up with guidance rather than a course.",
    scope: [
      "Recurring 1:1 sessions or team workshops",
      "Built around real work: your code, your project, your questions",
    ],
    deliverables: ["Scheduled sessions + async check-ins", "A growth plan that's actually yours"],
    shape: "Recurring · hourly or monthly",
  },
];

export const freelanceNote =
  "Every engagement is scoped, priced and owned by you. No retainers unless we both want one.";