import sys; sys.path.insert(0, "/tmp/opencode/links")
from lg import L, write_cat

A = []
def add(*a, **k): A.append(L(*a, **k))

# --- core low-level texts ---
add("Computer Systems: A Programmer's Perspective", "https://csapp.cs.cmu.edu/",
    "CS:APP — C, memory, linking, processes, systems I/O explained for programmers. The book that makes the machine legible.", ["book","systems","c"], "book", sub="books")
add("The C Programming Language", "https://www.slpress.com/titles/brian-w-kernighan/",
    "K&R — the original C book, still the standard way to argue about C.", ["book","c","classic"], "book", sub="books")
add("The Elements of Computing Systems (Nand2Tetris)", "https://www.nand2tetris.org/",
    "Build a computer from NAND gates up to a running Tetris — hardware, assembler, virtual machine, compiler, OS.", ["book","computer-architecture","course"], "book", sub="courses")
add("Nand2Tetris course", "https://nand2tetris.org/course",
    "The entire course that takes you from a single NAND gate to a bootable OS.", ["course","computer-architecture"], "course", sub="courses")
add("Computer Organization and Design", "https://shop.elsevier.com/books/computer-organization-and-design/patterson/978-0-12-820612-6",
    "Patterson & Hennessy RISC-V edition — the how-the-hardware-really-works classic.", ["book","computer-architecture","risc-v"], "book", sub="books")
add("nandgame", "https://nandgame.com/",
    "Playable online course that walks you from NAND gates to a working CPU.", ["course","interactive","computer-architecture"], "course", sub="courses")
add("Bipolar junction transistors", "https://en.wikipedia.org/wiki/Bipolar_junction_transistor",
    "How a BJT really works — current-controlled operation, three regions, and what makes it amplify.", ["electronics","transistors"], "archive", sub="electronics")
add("How do CPUs work?" , "https://cpu.land/",
    "A friendly book-on-a-page about what CPUs actually do, written for curious programmers.", ["cpu","courses","book"], "guide", sub="guides")
add("OSDev Wiki", "https://wiki.osdev.org/",
    "The reference for writing your own operating system — interrupts, memory, drivers, bootloaders.", ["osdev","kernel"], "docs", sub="os")
add("The Little Book About OS Development", "https://littleosbook.github.io/",
    "A short tutorial that gets a hobby kernel booting and printing.", ["osdev","kernel","tutorial"], "guide", sub="os")
add("Operating Systems: Three Easy Pieces (OSTEP)", "https://pages.cs.wisc.edu/~remzi/OSTEP/",
    "Remzi & Andrea's free, genuinely readable OS textbook — virtualization, concurrency, persistence.", ["book","os","free"], "book", sub="books")
add("The Rust Programming Language", "https://doc.rust-lang.org/book/",
    "The official Rust book — the language that made low-level code memory-safe.", ["book","rust","safe-systems"], "book", sub="books")
add("Programming Rust", "https://github.com/ProgrammingRust",
    "Reference companion code for the O'Reilly Rust book.", ["rust","book"], "repo", sub="books")
add("Beej's Guide to Network Programming", "https://beej.us/guide/bgnet/",
    "Sockets programming in C, explained with humour and no fluff.", ["networking","c","guide"], "guide", sub="guides")
add("Beej's Guide to C", "https://beej.us/guide/bgc/",
    "A modern, friendly introduction to C.", ["c","guide"], "guide", sub="guides")
add("Linux System Programming (docs)", "https://man7.org/linux/man-pages/",
    "man7.org man pages — the ground truth for Linux syscalls.", ["linux","syscalls"], "docs", sub="os")
add("Linux Kernel Documentation", "https://www.kernel.org/doc/html/latest/",
    "The official kernel docs — subsystems, drivers, locking, APIs.", ["kernel","docs"], "docs", sub="os")
add("The Linux Kernel source", "https://github.com/torvalds/linux",
    "The kernel itself; start with kernel/doc or arch/x86 if you want to get lost productively.", ["kernel","source"], "repo", sub="os")

# --- assembly / binary ---
add("Godbolt: Compiler Explorer", "https://godbolt.org/",
    "See what your C/Rust/etc. compiles to in assembly, with any compiler from the last two decades.", ["assembly","compilers","tool"], "tool", sub="assembly")
add("x86 Assembly Guide", "https://www.cs.virginia.edu/~evans/cs216/guides/x86.html",
    "UVa's compact x86-64 cheat sheet and tutorial.", ["assembly","x86"], "guide", sub="assembly")
add("The Art of Assembly Language (AoA)", "https://www.plantation-productions.com/Webster/www.artofasm.com/",
    "Randy Hyde's massive, opinionated textbook on assembly programming, now with a 64-bit edition.", ["book","assembly","x86"], "book", sub="books")
add("ARM Assembly (AArch64)", "https://developer.arm.com/documentation/den0024/",
    "ARM's learn-the-architecture guide to AArch64 assembly.", ["assembly","arm"], "docs", sub="assembly")
add("How x86 boot works", "https://github.com/cfenollosa/os-tutorial",
    "A guided walkthrough building a boot sector to a working OS — with commentary the whole way.", ["osdev","bootloader","tutorial"], "repo", sub="os")
add("radare2", "https://github.com/radareorg/radare2",
    "The reverse-engineering command-line framework — disassemble, patch, analyse binaries.", ["reverse-engineering","binary"], "repo", sub="binary")
add("Ghidra", "https://github.com/NationalSecurityAgency/ghidra",
    "NSA's open-source reverse engineering suite — decompiler, disassembler, scripting.", ["reverse-engineering","decompiler"], "repo", sub="binary")
add("Binary Ninja", "https://binary.ninja/",
    "A modern reverse engineering platform; the cloud demo lets you decompile in a browser.", ["reverse-engineering","decompiler"], "tool", sub="binary")
add("GNU objdump / binutils", "https://www.gnu.org/software/binutils/",
    "The classic toolkit — objdump, nm, readelf — for looking at the inside of binaries.", ["binary","toolkit","elf"], "org", sub="binary")
add("How ELF files work", "https://man7.org/linux/man-pages/man5/elf.5.html",
    "The ELF format man page — headers, sections, symbols, segments, from the ground truth.", ["elf","binary","format"], "docs", sub="binary")
add("Reading a hex dump", "https://en.wikipedia.org/wiki/Hex_dump",
    "How to read hex dumps and why they still matter when the format docs stop.", ["binary","hex"], "archive", sub="binary")

# --- emulators / hardware emulation ---
add("QEMU", "https://www.qemu.org/",
    "The emulator/virtualizer at the heart of most low-level tinkering and CI.",
    ["emulation","virtualization"], "project", sub="emulation")
add("QEMU docs", "https://www.qemu.org/docs/master/",
    "Official QEMU documentation.", ["docs","emulation"], "docs", sub="emulation")
add("Tiny Emulators Index (Fogleman)", "https://github.com/fogleman/nes",
    "Michael Fogleman's NES emulator in Go — GitHub's most famous 'how an emulator works' example.", ["emulation","nes","tutorial"], "repo", sub="emulation")
add("Game Boy hardware reference (Pan Docs)", "https://gbdev.io/pandocs/",
    "The community-written, extremely detailed Game Boy hardware documentation.", ["emulation","gameboy","docs"], "docs", sub="emulation")
add("How to write an emulator (CHIP-8)", "https://tobiasvl.github.io/blog/write-a-chip-8-emulator/",
    "Tobias's gentle intro — a CHIP-8 emulator in ~100 lines of any language.", ["emulation","chip-8","tutorial"], "article", sub="emulation", source="tobiasvl.github.io")

# --- retro computing & homebrew ---
add("Ben Eater's 8-bit computer (YouTube)", "https://www.youtube.com/@BenEater",
    "Building a working 8-bit computer from breadboards — the video series that taught a generation how CPUs actually work.", ["8-bit","breadboard","cpu","video"], "video", sub="homebrew")
add("Ben Eater 8-bit computer (site)", "https://eater.net/8bit",
    "Companion course site and kit for the breadboard CPU series.", ["8-bit","course"], "course", sub="homebrew")
add("Z80 CPU documentation", "https://www.z80.info/",
    "The community hub for the Z80 microprocessor that powered the 80s home-computer wave — datasheets, docs, forums.", ["z80","microprocessor","retro"], "archive", sub="retro")
add("The Retrocomputing Stack Exchange", "https://retrocomputing.stackexchange.com/",
    "Q&A with the people who actually remember punching cards.", ["community","retro"], "forum", sub="retro")
add("Vintage Computer Federation (VCF)", "https://vcfed.org/",
    "Org behind VCF events — museums, forums, and a whole community keeping old iron running.", ["org","retro"], "org", sub="retro")
add("The Computer History Museum", "https://www.computerhistory.org/",
    "The world's best history of computing, with enormous artifact and document archives online.", ["museum","history"], "archive", sub="retro")
add("CHM Software History collection", "https://www.computerhistory.org/collections/",
    "The Computer History Museum's collected software, manuals and source artifacts.", ["history","software","archive"], "archive", sub="retro")
add("Adrian's Digital Basement (YouTube)", "https://www.youtube.com/@adriansdigitalbasement",
    "Restoring and reverse-engineering 80s/90s hardware — endgame electronics content for the homebrew crowd.", ["retro","restoration","video"], "video", sub="retro")
add("The Terminal: MITS Altair 8800", "https://vintagecomputer.com/",
    "Altair Historical Society page tracking the Altair 8800 and the beginning of microcomputing.", ["altair","history"], "archive", sub="reverence")
add("The CPU Shack", "https://www.cpushack.com/",
    "Museum-grade archives of retro processors — die photos, silicon, and processor history.", ["cpu","retro","silicon"], "archive", sub="silicon")
add("Macintosh.js (classic Mac emulator)", "https://github.com/felixrieseberg/macintosh.js",
    "A downloadable Classic Mac emulator; the fun demonstration of how far browser-served emulation has come.", ["mac","emulation"], "repo", sub="emulation")
add("Basilisk II", "https://basilisk.cebix.net/",
    "The mainline Classic Mac emulator — emulates a full 68K Mac OS system.", ["mac","emulation"], "project", sub="emulation")
add("MAME", "https://www.mamedev.org/",
    "The Multiple Arcade Machine Emulator — preservation of arcade hardware in software.", ["arcade","emulation","preservation"], "project", sub="emulation")
add("Tiny-C Compiler (tcc)", "https://bellard.org/tcc/",
    "Fabrice Bellard's tiny C compiler — compiles C in a flash; a marvel of minimalism.", ["compiler","c","bellard"], "tool", sub="compiler")
add("Fabrice Bellard", "https://bellard.org/",
    "The personal page of Fabrice Bellard — QEMU, FFmpeg, tcc, and a Pi-record program. A masterclass in lone-engineer output.", ["engineer","author"], "org", sub="personas")
add("Pico-8", "https://www.lexaloffle.com/pico-8.php",
    "The fantasy console that keeps a whole scene coding within a deliberately tiny spec.", ["pico-8","game","fantasy-console"], "project", sub="homebrew")

# --- silicon / inside the chip ---
add("The MOS 6502", "https://www.waitingforfriday.com/index.php/Visual_6502",
    "Visual 6502 — play with the actual transistor layout of the 6502 in-browser.", ["6502","silicon","chip"], "tool", sub="silicon")
add("Visual 6502 project", "https://www.visual6502.org/",
    "Transistor-level simulation of classic microprocessors, built from microscope photographs of the silicon.", ["6502","silicon","chip"], "project", sub="silicon")
add("Ken Shirriff's Blog", "https://www.righto.com/",
    "Reverse-engineering silicon: integrated circuits from calculators to FPGAs, photographed and explained.", ["silicon","reverse-engineering","blog"], "article", sub="silicon", source="righto.com")
add("The Transistor", "https://en.wikipedia.org/wiki/Transistor",
    "The background article on the device everything here is built on.", ["electronics","transistors"], "archive", sub="electronics")
add("The Transistor-level journey of a RISC-V", "https://www.zeete.com/",
    "Documentation and die photos of home-built microprocessors.", ["risc-v","silicon"], "project", sub="silicon")
add("Open-source silicon (Libre Silicon)", "https://libresilicon.com/",
    "A serious attempt at open silicon as an economic venture — fascinating engineering economics.", ["silicon","open-source"], "project", sub="silicon")

write_cat("lowlevel", A)