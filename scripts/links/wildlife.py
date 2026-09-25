import sys; sys.path.insert(0, "/tmp/opencode/links")
from lg import L, write_cat

A = []
def add(*a, **k): A.append(L(*a, **k))

# --- gleaned from a personal copy of a shikar-era memoir ---
add("Falconry in the Valley of the Indus", "https://archive.org/details/falconryinvalley00burt",
    "Sir Richard Burton's account of hawking the Indus while a young officer in the East India Company — the volume that sent this archive's falconry shelf running. Scanned, searchable, mine for a shirt-flap of primary detail.", ["book","falconry","burton","primary-source"], "book", sub="falconry", year=1852, source="Internet Archive")
add("Looking for the Goshawk", "https://archive.org/details/lookingforgoshaw0000jame",
    "Conor Jameson's modern search for the northern goshawk across Britain — a field book that reads like a detective story.", ["book","goshawk","conservation"], "book", sub="goshawk", source="Internet Archive")
add("The Natural History of Selborne", "https://archive.org/details/naturalhistoryof0000gilb_l8y9",
    "Gilbert White's 1789 letters on the natural history of his parish — the book that quietly invented ecological natural-history writing.", ["book","naturalist","classic"], "book", sub="nature-writing", source="Internet Archive")

# --- falconry ---
add("North American Falconers' Association (NAFA)", "https://www.n-a-f-a.com/",
    "The US/Canada falconry organization — apprentice mentoring, meets, and legal advocacy for the sport.", ["falconry","org","license"], "org", sub="falconry")
add("The British Falconers' Club", "https://www.britishfalconersclub.co.uk/",
    "The UK's flagship falconry club, running since 1927.", ["falconry","org"], "org", sub="falconry")
add("International Association for Falconry", "https://en.wikipedia.org/wiki/Falconry",
    "The federation of national falconry associations, an UNESCO-recognized traditional craft — see 'Falconry' for the wider history.", ["falconry","international","wiki"], "archive", sub="falconry")
add("US Fish & Wildlife Service", "https://www.fws.gov/",
    "Federal wildlife agency; the falconry regulations page and migratory bird oversight are the legal reference here.", ["falconry","regulation","org"], "org", sub="falconry")

# --- raptor conservation & research ---
add("The Peregrine Fund", "https://peregrinefund.org/",
    "The raptor conservation nonprofit — from the peregrine recovery to today's global raptor programs.", ["raptors","conservation","org"], "org", sub="raptors")
add("HawkWatch International", "https://www.hawkwatch.org/",
    "Raptor migration counts and research across the flyways — their migration dashboards are an addiction.", ["raptors","migration","org"], "org", sub="raptors")
add("Raptor Research Foundation", "https://raptorresearchfoundation.org/",
    "The scientific society for raptor researchers and the publishers of the Journal of Raptor Research.", ["raptors","science","org"], "org", sub="raptors")
add("Raptor Resource Project", "https://www.raptorresource.org/",
    "The falcon-cam project full of nesting cams and restoration programs.", ["raptors","webcam","org"], "org", sub="raptors")
add("BirdLife International", "https://www.birdlife.org/",
    "The global partnership of bird conservation NGOs — Red List assessments and Important Bird Areas.", ["birds","conservation","global"], "org", sub="org")
add("RSPB", "https://www.rspb.org.uk/",
    "The UK's bird conservation charity — reserve guides and species info.", ["birds","conservation","org"], "org", sub="org")

# --- ornithology tools & references ---
add("All About Birds", "https://www.allaboutbirds.org/",
    "Cornell's standard species encyclopedia — range maps, vocalizations, life history.", ["birds","reference","identification"], "guide", sub="reference")
add("All About Birds — Northern Goshawk", "https://www.allaboutbirds.org/guide/Northern_Goshawk/",
    "The Cornell species page for the northern goshawk: ID, habitat, behavior, sounds.", ["goshawk","reference","identification"], "guide", sub="goshawk")
add("eBird", "https://ebird.org/",
    "Cornell's citizen-science bird checklist platform — occurrence data that powers modern ornithology.", ["birds","data","citizen-science"], "tool", sub="data")
add("eBird species map — Northern Goshawk", "https://ebird.org/species/norgos",
    "Live checklist and distribution data for Accipiter gentilis, from the Cornell database.", ["goshawk","data"], "tool", sub="goshawk")
add("Macaulay Library", "https://www.macaulaylibrary.org/",
    "Cornell's archive of photos, sound and video — the world's largest media collection of birds.", ["birds","media","archive"], "tool", sub="reference")
add("Birds of the World", "https://birdsoftheworld.org/",
    "The definitive curated species accounts (paywalled, but the flagship of ornithological reference).", ["birds","reference"], "tool", sub="reference")
add("SORA — Searchable Ornithological Research Archive", "https://sora.unm.edu/",
    "Free digital archive of ornithological journals — Auk, Condor, Wilson Bulletin and others, fully searchable.", ["birds","journals","archive"], "archive", sub="data")
add("iNaturalist", "https://www.inaturalist.org/",
    "Observation platform for every taxon, where a blurry raptor from your phone can get an expert ID.", ["biodiversity","observations","community"], "tool", sub="data")
add("GBIF", "https://www.gbif.org/",
    "The global biodiversity information facility — species occurrence data at planetary scale.", ["biodiversity","data"], "org", sub="data")
add("Animal Diversity Web", "https://animaldiversity.org/",
    "University of Michigan's species encyclopedia with trait and behavior write-ups.", ["reference","species"], "docs", sub="reference")
add("IUCN Red List", "https://www.iucnredlist.org/",
    "The global extinction-risk database — look up the conservation status of any goshawk, snow leopard, or shisham.", ["conservation","status","data"], "tool", sub="data")
add("CITES", "https://cites.org/",
    "The treaty regulating international trade in species — including all the falcons and hawks.", ["conservation","treaty"], "org", sub="conservation")

# --- Pakistan / Himalaya ---
add("WWF Pakistan", "https://www.wwfpak.org/",
    "WWF's Pakistan program — the country's key conservation datasets (snow leopard, markhor campaigns).", ["pakistan","conservation"], "org", sub="pakistan")
add("IUCN Pakistan", "https://iucnp.org/",
    "The Pakistan country office of the IUCN — Red List work and conservation policy for AJK and Gilgit-Baltistan.", ["pakistan","conservation","org"], "org", sub="pakistan")
add("Snow Leopard Trust", "https://snowleopard.org/",
    "The main snow leopard science and community-conservation org across the Himalayas including Pakistan.", ["snow-leopard","himalaya","org"], "org", sub="pakistan")
add("The Northern Goshawk (species text)", "https://en.wikipedia.org/wiki/Northern_goshawk",
    "The accessible species page — taxonomy, range, hunting behavior and the goshawk's role in falconry.", ["goshawk","wiki"], "archive", sub="goshawk")

# --- with books the falconry shelf loves ---
add("Audubon Field Guide", "https://www.audubon.org/",
    "National Audubon's field-guide content and conservation work." , ["birds","conservation"], "org", sub="reference")

# --- the Pakistan/Himalaya shelf (carried over) ---
add("The Markhor — Pakistan's National Animal", "https://en.wikipedia.org/wiki/Markhor",
    "The magnificent spiral-horned markhor of Pakistan's north — a conservation success story, endangered to vulnerable.", ["markhor","pakistan","conservation"], "archive", sub="pakistan")
add("Himalayan Brown Bear of Deosai Plains", "https://en.wikipedia.org/wiki/Himalayan_brown_bear",
    "The Deosai National Park in Gilgit-Baltistan protects one of the last high-altitude strongholds of the Himalayan brown bear.", ["brown-bear","gilgit-baltistan","pakistan"], "archive", sub="pakistan")
add("Hangul — Kashmir's Critically Endangered Red Deer", "https://en.wikipedia.org/wiki/Kashmir_stag",
    "The hangul (Kashmir stag), the only surviving red-deer subspecies in South Asia, holds on in Dachigam National Park.", ["hangul","kashmir","endangered"], "archive", sub="pakistan")
add("Indus River Dolphin", "https://en.wikipedia.org/wiki/Indus_river_dolphin",
    "One of the world's rarest mammals — the blind Indus river dolphin, fewer than 2,000 left in the Indus system.", ["dolphin","indus","endangered"], "archive", sub="pakistan")
add("Himalayan Monal — Danphe", "https://en.wikipedia.org/wiki/Himalayan_monal",
    "The iridescent monal found across the Himalayas including Azad Kashmir — among the most striking birds on earth.", ["monal","himalayas","kashmir"], "archive", sub="pakistan")
add("Himalayan Musk Deer", "https://en.wikipedia.org/wiki/Himalayan_musk_deer",
    "The elusive musk deer hunted for its gland — critically endangered across the high Kashmir and Pakistan ranges.", ["musk-deer","pakistan","endangered"], "archive", sub="pakistan")
add("Chitral National Park", "https://en.wikipedia.org/wiki/Chitral_National_Park",
    "Home to markhor, snow leopards, Tibetan wolves and the rare western tragopan — one of Pakistan's most biodiverse corners.", ["pakistan","national-park","biodiversity"], "archive", sub="pakistan")
add("Dachigam National Park", "https://en.wikipedia.org/wiki/Dachigam_National_Park",
    "The lifeline of the hangul deer — also black bears, leopards and 150+ bird species in the Kashmir valley.", ["kashmir","national-park","hangul"], "archive", sub="pakistan")
add("Astola Island — Pakistan's Offshore Haven", "https://en.wikipedia.org/wiki/Astola_Island",
    "Pakistan's largest offshore island and a critical nesting site for turtles and seabirds in the Arabian Sea.", ["pakistan","island","marine"], "archive", sub="pakistan")
add("Pakistan's Ramsar Wetland Sites", "https://en.wikipedia.org/wiki/List_of_Ramsar_sites_in_Pakistan",
    "The 19 Ramsar sites — critical staging and wintering habitat for birds migrating from Siberia to Africa.", ["wetlands","pakistan","migration"], "archive", sub="pakistan")
add("Thar & Cholistan — Desert Wildlife", "https://en.wikipedia.org/wiki/Thar_Desert",
    "Chinkara gazelle, desert foxes and bustards — the surprising biodiversity of Pakistan's sand seas.", ["desert","pakistan","thar"], "archive", sub="pakistan")
add("Tibetan Wolf", "https://en.wikipedia.org/wiki/Tibetan_wolf",
    "The key predator of Pakistan's northern alpine ecosystem.", ["wolf","himalayas","predator"], "archive", sub="pakistan")
add("Cornell Bird Cams", "https://www.allaboutbirds.org/cams/",
    "Live camera nests — birds doing bird things, streamed year-round from the Cornell Lab.", ["webcam","birds","live"], "video", sub="reference")
add("Serengeti Live Cam", "https://www.explore.org/livecams/serengeti/serengeti-live-cam",
    "Live cameras over the Serengeti — lions, elephants and the greatest show on earth, streamed.", ["live-cam","africa","safari"], "video", sub="reference")

write_cat("wildlife", A)