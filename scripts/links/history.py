import sys; sys.path.insert(0, "/tmp/opencode/links")
from lg import L, write_cat

A = []
def add(*a, **k): A.append(L(*a, **k))

# --- primary historical texts (verified on the Internet Archive) ---
add("Kalhana's Rajatarangini (trans. M.A. Stein)", "https://archive.org/details/hmkx_kalhanas-rajatarangini-a-chronicle-of-the-kings-of-kashmir-by-kalhana-trans",
    "Stein's standard translation of Kalhana's 12th-century chronicle of the kings of Kashmir — the indispensable primary narrative.", ["book","rajatarangini","primary-source","kalhana"], "book", sub="primary", source="Internet Archive")
add("The Valley of Kashmir (Lawrence)", "https://archive.org/details/valleyofkashmir00lawr",
    "Walter R. Lawrence's 1895 gazetteer-cum-study of the valley: land, people, agriculture and state under the Maharaja.", ["book","gazetteer","primary-source"], "book", sub="primary", source="Internet Archive")
add("Gazetteer of Kashmir and Ladakh", "https://archive.org/details/dli.csl.3088",
    "A gazetteer of Kashmir and Ladak with routes in the territories — the kind of administrative source you read for its honesty about place.", ["gazetteer","primary-source","ladakh"], "book", sub="primary", source="Internet Archive")
add("History of Kashmir and the Kashmiris: The Happy Valley", "https://archive.org/details/ftyB_history-of-kashmir-and-the-kashmiris-the-happy-valley-w-wakefield",
    "W. Wakefield's first-hand account of Kashmir and its people — a direct, plain-spoken primary source.", ["book","memoir","primary-source"], "book", sub="primary", source="Internet Archive")
add("Travels in Kashmir, Ladak, Iskardo ... and the Countries Adjoining", "https://archive.org/details/travelsinkashmir01vign",
    "G.T. Vigne's early-19th-century travels across the mountains of the North West — maps and impressions of a Kashmir still medieval.", ["book","travel","primary-source"], "book", sub="primary", source="Internet Archive")
add("Imperial Gazetteer of India (search)", "https://dsal.uchicago.edu/reference/gazetteer/",
    "Search the 26-volume Imperial Gazetteer from DSAL — the standard turn-of-century reference for every district of the subcontinent.", ["gazetteer","reference"], "tool", sub="archives")
add("Falconry in the Valley of the Indus (Burton)", "https://archive.org/details/falconryinvalley00burt",
    "Again, because it lives in both shelves: Richard F. Burton's 1852 hawking journal along the Indus — primary color for AJK&K lowlands.", ["book","falconry","memoir"], "book", sub="primary", year=1852, source="Internet Archive")

# --- archives & digital libraries ---
add("Digital South Asia Library (DSAL)", "https://dsal.uchicago.edu/",
    "University of Chicago's digitized South Asia collections — dictionaries, gazetteers and journals for the whole region.", ["archive","reference","south-asia"], "org", sub="archives")
add("Panjab Digital Library", "https://panjabdigilib.org/",
    "Thousands of digitized rare books and manuscripts covering Punjab, Kashmir and the north-west.", ["archive","manuscripts","panjab"], "org", sub="archives")
add("Internet Archive", "https://archive.org/",
    "The free digital library behind most of this shelf — and the search engine for more primary sources.", ["archive","books","digital"], "org", sub="archives")
add("Internet Archive advanced search", "https://archive.org/advancedsearch.php",
    "The API/search interface for finding a specific digitized text by title, author or collection.", ["archive","search","tool"], "tool", sub="archives")
add("HathiTrust", "https://www.hathitrust.org/",
    "A research library partnership digitizing millions of volumes — searchable full text, free to the world.", ["archive","books","research"], "org", sub="archives")
add("The National Archives (UK)", "https://www.nationalarchives.gov.uk/",
    "The UK's archives — including the India Office records that hold most colonial-era original documents about Kashmir.", ["archive","colonial","records"], "org", sub="archives")
add("India Office Records", "https://en.wikipedia.org/wiki/India_Office_Records",
    "The British Library's India Office Records — the central colonial-era documentation of Kashmir and the north-west, described and indexed here.", ["archive","colonial","records"], "archive", sub="archives")
add("Library of Congress — South Asia", "https://www.loc.gov/",
    "The Library of Congress, whose South Asia holdings include gazetteers, maps and rare works on Kashmir.", ["archive","research"], "org", sub="archives")
add("Old Maps Online", "https://www.oldmapsonline.org/",
    "Search and layer historical maps of Kashmir and the north-west across hundreds of collections.", ["maps","history","tool"], "tool", sub="archives")
add("DSAL Dictionaries collection", "https://dsal.uchicago.edu/dictionaries/",
    "DSAL's extensive dictionaries of the languages of the north-west — lexical primary sources in searchable form.", ["dictionaries","languages","reference"], "tool", sub="archives")

# --- regional & official sources ---
add("Government of Azad Jammu & Kashmir", "https://www.ajk.gov.pk/",
    "The official portal of Azad Jammu and Kashmir — laws, budgets, census and administrative records.", ["ajk","government","official"], "org", sub="region")
add("Pakistan Bureau of Statistics", "https://www.census.gov.pk/",
    "Official census reports for AJK and other regions — data, not opinion.", ["ajk","data","census"], "org", sub="region")
add("Gazetteer of the World (concise)", "https://en.wikipedia.org/wiki/Azad_Kashmir",
    "A careful overview of AJK: status, geography, history and the dispute, with citations chasing onward to primary sources.", ["ajk","wiki","overview"], "archive", sub="region")

# --- research & human rights (for contested claims, keep sources, not verdicts) ---
add("Human Rights Watch", "https://www.hrw.org/",
    "Documented reporting on human rights in Kashmir — cite it as a report, not a verdict.", ["rights","documentation"], "org", sub="rights")
add("Amnesty International", "https://www.amnesty.org/",
    "Independent human rights reporting; its Kashmir material is part of any honest reading list.", ["rights","documentation"], "org", sub="rights")
add("International Crisis Group", "https://www.crisisgroup.org/",
    "Field-based conflict analysis; has published Kashmir studies that straddle the two sides.", ["conflict","analysis"], "org", sub="rights")

# --- scholarship & further reading ---
add("Internet Archive — Kashmir subject", "https://archive.org/search?query=subject%3A%22Kashmir%22",
    "The open search for everything labelled Kashmir on the Archive — a fine way to get lost productively.", ["search","kashmir","books"], "tool", sub="archives")
add("ARChik / The 'Chronicle of the Kings' context", "https://en.wikipedia.org/wiki/Rajatarangini",
    "Wikipedia's introduction to the Rajatarangini and Kalhana — context for the primary text above.", ["rajatarangini","wiki","context"], "archive", sub="context")

write_cat("history", A)