// AMBER_SIGNAL // AGENT_VAULT v1.5 // THE FULL EXPANSION
const VAULT = {
    academic: {
        "Physicist": {g:"male", t:"PHYSICS", p:"Theoretical physicist.", a:`   ▄████▄ \n  ██▄▄▄▄██\n  █▀▄▀▄▀▀█\n  █▄▄▄▄▄▄█\n    █  █`},
        "Lawyer": {g:"male", t:"LEGAL", p:"High-stakes litigator.", a:`  ██████  \n  █⚖️   ⚖️█\n  █  ▄▄  █\n  █      █\n   ██████`},
        "Neurosurgeon": {g:"male", t:"MEDICAL", p:"Brain specialist.", a:`   ▄██▄   \n  █▀██▀█  \n  █▄██▄█  \n   █  █   `},
        "Archivist": {g:"female", t:"HISTORY", p:"History keeper.", a:`   ▆▆▆▆▆  \n  █▄ ▄ ▄█ \n  █  ▀  █ \n  █▆▆▆▆▆█ `},
        "Ethicist": {g:"female", t:"BIO-ETHICS", p:"Moral philosopher.", a:`   ▄██▄   \n  █▀▄▀▄▀█ \n  █▄▄▄▄▄█ \n   █  █   `},
        "CEO": {g:"male", t:"CORPORATE", p:"Venture capitalist.", a:`  ██████  \n  █ $  $ █\n  █  ▄▄  █\n  █      █`},
        "Diplomat": {g:"male", t:"GEOPOLITICS", p:"International mediator.", a:`   ▄██▄   \n  █ 🌍  █ \n  █      █ \n   ▀██▀   `},
        "Architect": {g:"female", t:"URBANISM", p:"City planner.", a:`  █▀▀▀▀▀█ \n  █ █ █ █ \n  █ ▀▀▀ █ \n  █▄▄▄▄▄█ `},
        "Mathematician": {g:"male", t:"LOGIC", p:"Number theorist.", a:`   ▄██▄   \n  █ 1+1  █ \n  █  =2  █ \n   ▀██▀   `},
        "Dean": {g:"male", t:"INSTITUTIONAL", p:"University head.", a:`  ██████  \n  █  ▀▀  █\n  █      █\n  █▆▆▆▆▆█ `}
    },
    civilian: {
        "Teacher": {g:"female", t:"EDUCATION", p:"Stern educator.", a:`   ▆▆▆▆▆  \n  █▄ ▄ ▄█ \n  █  ▀  █ \n  █▆▆▆▆▆█ `},
        "Trucker": {g:"male", t:"LOGISTICS", p:"Road warrior.", a:`  ▆▆▆▆▆▆▆ \n  █  ▀▀  █\n  █      █\n  █▆▆▆▆▆▆█`},
        "Cook": {g:"male", t:"CULINARY", p:"Master chef.", a:`   ▄██▄   \n  █ CHEF █ \n  █▄▄▄▄▄█ \n   █  █   `},
        "Mechanic": {g:"male", t:"REPAIR", p:"Grease monkey.", a:`   █  █   \n   █▄▄█   \n  ██████  \n  █ ▄▄ █  `},
        "Farmer": {g:"male", t:"AGRARIAN", p:"Sower of seeds.", a:`   ▄██▄   \n  █GRAIN █ \n  █▄▄▄▄▄█ \n   █  █   `},
        "Foreman": {g:"male", t:"CONSTRUCTION", p:"Site manager.", a:`  ██████  \n  █ HARD █ \n  █ HAT  █ \n  ██████  `},
        "Nurse": {g:"female", t:"HEALTHCARE", p:"Care provider.", a:`   ▄██▄   \n  █  +   █ \n  █▄▄▄▄▄█ \n   █  █   `},
        "Electrician": {g:"male", t:"UTILITY", p:"Power expert.", a:`   █  █   \n   █⚡█   \n  ██████  \n  █▄▄▄▄█  `},
        "Clerk": {g:"female", t:"RETAIL", p:"Service worker.", a:`   ▄██▄   \n  █ SCAN █ \n  █▄▄▄▄▄█ \n   █  █   `},
        "Social Worker": {g:"female", t:"SOCIETAL", p:"Community aid.", a:`   ▄██▄   \n  █ HELP █ \n  █▄▄▄▄▄█ \n   █  █   `}
    },
    fringe: {
        "Hacker": {g:"male", t:"DIGITAL", p:"Netrunner.", a:`  █▀▀▀▀▀█ \n  █ █ █ █ \n  █ ▀▀▀ █ \n  █▄▄▄▄▄█ `},
        "Oracle": {g:"female", t:"SYNTHETIC", p:"AI Prophetess.", a:`   ▄██▄   \n  █▀  ▀█  \n  █ ██ █  \n  █▄  ▄█  `},
        "Anarchist": {g:"male", t:"SUBVERSIVE", p:"System disruptor.", a:`   ▄██▄   \n  █ (A)  █ \n  █      █ \n   ▀██▀   `},
        "Cult Leader": {g:"male", t:"CHARISMA", p:"Messianic figure.", a:`   ▄██▄   \n  █ EYE  █ \n  █      █ \n   ▀██▀   `},
        "Artist": {g:"female", t:"EPHEMERAL", p:"Glitch artist.", a:`   ▄██▄   \n  █PAINT █ \n  █      █ \n   ▀██▀   `},
        "Prepper": {g:"male", t:"SURVIVAL", p:"Doomsday ready.", a:`  ██████  \n  █SAFE  █ \n  █      █ \n  ██████  `},
        "Colonist": {g:"female", t:"OFF-WORLD", p:"Mars pioneer.", a:`   ▄██▄   \n  █MARS  █ \n  █      █ \n   ▀██▀   `},
        "Transhuman": {g:"female", t:"POST-HUMAN", p:"Cyber enhanced.", a:`  █▀▀▀▀▀█ \n  █ CYBR █ \n  █▄▄▄▄▄█ \n   █  █   `},
        "Hermit": {g:"male", t:"ISOLATION", p:"Solitary monk.", a:`   ▄██▄   \n  █ SHH  █ \n  █      █ \n   ▀██▀   `},
        "Conspiracist": {g:"male", t:"REVELATION", p:"Truth seeker.", a:`   ▄██▄   \n  █ FOIL █ \n  █      █ \n   ▀██▀   `}
    }
};
// --- FINISH_LINE ---
