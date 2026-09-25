import sys; sys.path.insert(0, "/tmp/opencode/links")
from lg import L, write_cat

A = []
def add(*a, **k): A.append(L(*a, **k))

# --- programming & software (carried + curated) ---
add("Teach Yourself Computer Science", "https://teachyourselfcs.com/",
    "A self-directed CS curriculum with no fluff — the real essential subjects.", ["cs","curriculum","self-study"], "guide", sub="learning")
add("MIT Missing Semester", "https://missing.csail.mit.edu/",
    "The tools every programmer should know and nobody teaches — shell, git, debugging, security.", ["tools","shell","git"], "course", sub="learning")
add("Crafting Interpreters", "https://craftinginterpreters.com/",
    "Build a language from parsing to GC — bytecode, closures, marking — one of the best technical books ever written.", ["compilers","languages","book"], "book", sub="languages")
add("Build Your Own X", "https://github.com/codecrafters-io/build-your-own-x",
    "Learn how things work by building them — databases, git, Docker, compilers, from scratch.", ["learning-by-building","projects"], "repo", sub="learning")
add("The Pragmatic Programmer", "https://pragprog.com/titles/tpp20/",
    "The 20th-anniversary edition of the software-craftsmanship classic — DRY, knowledge portfolios, broken windows.", ["craftsmanship","career","book"], "book", sub="craft")
add("Designing Data-Intensive Applications", "https://dataintensive.net/",
    "The definitive map of reliable, scalable, maintainable data systems — non-negotiable for distributed data work.", ["data","distributed-systems","book"], "book", sub="data")
add("SICP", "https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html",
    "Programming as a way of thinking — Scheme, metacircular evaluators, and the beauty of abstraction.", ["cs","classic","book"], "book", sub="learning")
add("Code: The Hidden Language of Computer Hardware and Software", "https://www.amazon.com/Code-Language-Computer-Hardware-Software/dp/0735611319",
    "Petzold's journey from Morse code to CPUs — how computers work at every layer.", ["computer-science","hardware","book"], "book", sub="learning")
add("The Codeless Code", "https://thecodelesscode.com/contents",
    "Zen-koan parables about software engineering — thoughts on code, teams and craft.", ["philosophy","stories","craft"], "article", sub="craft")
add("Architecture of Open Source Applications", "https://aosabook.org/",
    "The maintainers of big projects explain how they actually fit together — the anatomy of real software.", ["architecture","case-studies"], "book", sub="craft")
add("Gödel, Escher, Bach", "https://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach",
    "Hofstadter's exploration of self-reference and formal systems — a book that rewires how you read systems.", ["consciousness","books","math"], "archive", sub="craft")

# --- tools & utilities (carried) ---
add("Excalidraw", "https://excalidraw.com/",
    "Hand-drawn-style collaborative diagrams — the architecture-sketching tool of choice.", ["diagrams","collaboration"], "tool", sub="tools")
add("Observable", "https://observablehq.com/",
    "Interactive data notebooks — D3 and reactive programming in the browser.", ["data","visualization","d3"], "tool", sub="tools")
add("PostgreSQL documentation", "https://www.postgresql.org/docs/",
    "The reference for the database half the world's data really lives in.", ["postgres","database","docs"], "docs", sub="data")
add("SQLite", "https://sqlite.org/",
    "The library database that outlives everything — zero-config, everywhere, forever.", ["database","embedded","sql"], "org", sub="data")
add("Git — documentation", "https://git-scm.com/doc/",
    "The reference, book, and videos for the tool that version controls our thoughts.", ["git","docs"], "docs", sub="tools")
add("Semantic Versioning", "https://semver.org/",
    "MAJOR.MINOR.PATCH and what it means — worth re-reading twice a year.", ["versioning","spec"], "guide", sub="craft")
add("Keep a Changelog", "https://keepachangelog.com/",
    "Why user-facing changelogs matter, and a format that makes them not-awful.", ["changelog","docs"], "guide", sub="craft")
add("Conventional Commits", "https://www.conventionalcommits.org/",
    "The commit message convention that makes git history machine-readable.", ["git","commit","spec"], "guide", sub="tools")
add("The Twelve-Factor App", "https://12factor.net/",
    "What good, deployable web services look like — config in env, stateless processes, logs as streams.", ["deployment","best-practice"], "guide", sub="craft")
add("Python documentation", "https://docs.python.org/",
    "The humble official docs — the first and last reference for the language that pays the rent.", ["python","docs"], "docs", sub="tools")
add("The Zen of Python — PEP 20", "https://peps.python.org/pep-0020/",
    "Twenty aphorisms that define the Python aesthetic.", ["python","philosophy"], "docs", sub="tools")
add("MDN Web Docs", "https://developer.mozilla.org/en-US/",
    "The web platform reference — HTML, CSS, JS and the standards that carry the web.", ["web","javascript","reference"], "docs", sub="tools")
add("FastAPI", "https://fastapi.tiangolo.com/",
    "The modern Python API framework — async, typed, with auto docs. The default where this site's machines live.", ["python","api","framework"], "org", sub="tools")

write_cat("software", A)