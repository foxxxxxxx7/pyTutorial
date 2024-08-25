#Hangman words

words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra", 'abrupt', 'absurd', 'access', 'accident', 'account', 'achieve', 'acknowledge',
    'acquire', 'active', 'adventure', 'adjust', 'administer', 'admirable', 'admission',
    'adventure', 'affection', 'aggregate', 'agreement', 'airplane', 'amazing', 'amendment',
    'amplify', 'analysis', 'ancestor', 'ancient', 'anomaly', 'anticipate', 'apartment',
    'apology', 'appearance', 'application', 'appointment', 'appreciate', 'approval',
    'architecture', 'argument', 'artificial', 'assemble', 'assessment', 'associate',
    'astonish', 'atmosphere', 'attachment', 'attitude', 'attraction', 'authority',
    'automatic', 'availability', 'background', 'balance', 'banquet', 'bargain', 'barrier',
    'behavior', 'beneficial', 'bewilder', 'billionaire', 'biography', 'boundary',
    'breakthrough', 'broadcast', 'brochure', 'business', 'calendar', 'campaign', 'capacity',
    'capital', 'carriage', 'catalog', 'category', 'celebrate', 'central', 'ceremony',
    'challenge', 'champion', 'changeable', 'character', 'charity', 'circumstance',
    'citizenship', 'civilization', 'classification', 'climate', 'collaboration', 'colleague',
    'collect', 'collection', 'collision', 'commence', 'committee', 'communication',
    'community', 'companion', 'compensation', 'competition', 'complex', 'comprehensive',
    'compromise', 'concentration', 'concept', 'concern', 'conclusion', 'condition',
    'conference', 'confidence', 'confusion', 'congratulation', 'connection', 'conscience',
    'consequence', 'conservation', 'consideration', 'consistency', 'conspiracy', 'construction',
    'consult', 'consumer', 'containment', 'contemplate', 'continuation', 'contract', 'contrast',
    'contribution', 'control', 'controversy', 'convenience', 'conversion', 'conviction',
    'cooperation', 'coordination', 'corporate', 'correlation', 'correspondence', 'corridor',
    'creativity', 'credibility', 'criticism', 'cultural', 'curiosity', 'currency', 'customize',
    'dangerous', 'debate', 'decision', 'decoration', 'dedication', 'deficiency', 'definition',
    'delivery', 'demonstration', 'density', 'departure', 'dependency', 'depression', 'description',
    'destruction', 'detachment', 'determination', 'development', 'dictionary', 'difference',
    'difficult', 'dilemma', 'direction', 'disaster', 'discovery', 'discussion', 'disguise',
    'distance', 'distinction', 'distribution', 'diversity', 'document', 'dominate', 'donation',
    'dormitory', 'dramatic', 'dynamic', 'economy', 'education', 'efficiency', 'electricity',
    'elegant', 'element', 'eliminate', 'embarrassment', 'emergency', 'emission', 'emotional',
    'emphasis', 'empire', 'encounter', 'endurance', 'energy', 'engineer', 'enormous', 'enterprise',
    'entertainment', 'enthusiasm', 'environment', 'episode', 'equivalent', 'establish',
    'evaluation', 'eventual', 'evidence', 'exaggerate', 'excellence', 'exception', 'exchange',
    'excitement', 'exclamation', 'exclusion', 'executive', 'exhaust', 'existence', 'expansion',
    'expectation', 'expedition', 'experience', 'experiment', 'explosion', 'expression',
    'extension', 'extraordinary', 'extreme', 'fabricate', 'facility', 'fascinate', 'feasibility',
    'federation', 'fiction', 'flexibility', 'fluctuation', 'formation', 'frequent', 'frustration',
    'fundamental', 'furniture', 'gallery', 'general', 'generate', 'genuine', 'global', 'government',
    'governor', 'gradual', 'grandeur', 'grateful', 'guarantee', 'guidance', 'habitat', 'happiness',
    'harassment', 'heritage', 'hesitate', 'hierarchy', 'historical', 'hospital', 'humanity',
    'humorous', 'hurricane', 'hypothesis', 'identity', 'ignorance', 'illustration', 'imagination',
    'imitation', 'immense', 'immigration', 'importance', 'impression', 'improvement', 'incentive',
    'inclusion', 'incredible', 'independent', 'indication', 'industry', 'inevitable', 'influence',
    'infrastructure', 'initiative', 'innovation', 'inquiry', 'insight', 'inspiration', 'instinct',
    'instrument', 'integrity', 'intellectual', 'intelligence', 'intention', 'interaction', 'interest',
    'interference', 'international', 'interruption', 'intervention', 'introduction', 'invasion',
    'investment', 'invitation', 'involvement', 'ironic', 'isolated', 'journal', 'journey', 'judgment',
    'jurisdiction', 'justification', 'knowledge', 'landscape', 'language', 'laughter', 'leadership',
    'learning', 'legislation', 'leisure', 'liability', 'library', 'lightning', 'literature', 'location',
    'longevity', 'luxurious', 'magnificent', 'maintenance', 'management', 'manifest', 'manipulate',
    'manufacture', 'marathon', 'marketing', 'masterpiece', 'maturity', 'meaningful', 'measurement',
    'mechanism', 'meditation', 'membership', 'memorable', 'mention', 'mercury', 'metaphor', 'military',
    'minimize', 'ministry', 'miracle', 'misfortune', 'misunderstanding', 'modernize', 'modification',
    'momentum', 'monetary', 'monument', 'motivation', 'mountainous', 'movement', 'mysterious',
    'narrative', 'national', 'navigation', 'negotiate', 'neighborhood', 'nominate', 'notation',
    'novelty', 'nuclear', 'numerous', 'objective', 'obligation', 'observation', 'occupation',
    'offensive', 'official', 'omission', 'operation', 'opinion', 'opportunity', 'optimistic',
    'optional', 'organization', 'original', 'overcome', 'overwhelm', 'paradox', 'parliament',
    'participate', 'partnership', 'passenger', 'passionate', 'perceive', 'perception', 'performance',
    'permanent', 'perseverance', 'persistence', 'perspective', 'phenomenon', 'philosophy',
    'photograph', 'physical', 'political', 'popularity', 'population', 'portfolio', 'position',
    'possibility', 'potential', 'practical', 'preference', 'preparation', 'prescription', 'presence',
    'presidential', 'prestige', 'preventive', 'previous', 'priority', 'probability', 'procedure',
    'proclamation', 'production', 'profession', 'profitable', 'profound', 'progress', 'projection',
    'prolong', 'prominent', 'promotion', 'propaganda', 'proportion', 'prosperity', 'protection',
    'prototype', 'provision', 'psychology', 'publication', 'publicity', 'punishment', 'purchase',
    'qualification', 'quantity', 'quarantine', 'quotation', 'radiation', 'realistic', 'recognition',
    'recovery', 'reduction', 'reference', 'reflection', 'reform', 'refrain', 'regulation',
    'reinforcement', 'rejection', 'reliable', 'remarkable', 'reminder', 'renovation', 'repetition',
    'representative', 'reputation', 'reservation', 'resignation', 'resolution', 'responsibility',
    'restriction', 'retirement', 'revenue', 'revolution', 'righteousness', 'romantic', 'rotation',
    'sacrifice', 'satisfaction', 'schedule', 'scholarship', 'scientific', 'secretary', 'selection',
    'sensation', 'sensitivity', 'sequence', 'settlement', 'significant', 'similarity', 'simulation',
    'situation', 'sociable', 'socialism', 'solitude', 'solution', 'sophisticated', 'spectrum',
    'spiritual', 'spontaneous', 'stability', 'standard', 'statement', 'statistics', 'stimulate',
    'strategy', 'structure', 'stupendous', 'submission', 'subsequent', 'substance','substitute',
    'successful', 'succession', 'suggestion', 'superior', 'supervision', 'supportive', 'surprise',
    'surrender', 'suspicion', 'sustainable', 'symbolize', 'sympathy', 'syndrome', 'synthesis',
    'systematic', 'tactical', 'technology', 'temporary', 'termination', 'territory', 'testimonial',
    'theoretical', 'therapy', 'thorough', 'tolerance', 'tradition', 'trajectory', 'transformation',
    'transition', 'transportation', 'treatment', 'tremendous', 'tribunal', 'ultimate', 'unanimous',
    'unavoidable', 'uncertain', 'unconscious', 'understand', 'undertake', 'unfortunate', 'universal',
    'unlimited', 'unnecessary', 'unprecedented', 'unsuitable', 'utilize', 'vacation', 'validity',
    'variation', 'variety', 'vegetation', 'vehicle', 'velocity', 'venture', 'verification', 'version',
    'versus', 'vibration', 'victorious', 'vigorous', 'violation', 'virtual', 'visibility', 'visualize',
    'vitality', 'vocabulary', 'voluntary', 'vulnerable', 'warehouse', 'weather', 'weightless',
    'whenever', 'widespread', 'withdrawal', 'witness', 'wonderful', 'workplace', 'workshop',
    'worldwide', 'worthwhile', 'yearning', 'yesterday', 'youthful', 'zealous', 'zenith', 'zodiac', 'abandon', 'abundant', 'academic', 'accelerate', 'accomplish', 'accumulate', 'accurate',
    'accusation', 'acoustic', 'adaptation', 'adherence', 'adolescent', 'advancement', 'adversity',
    'affiliation', 'affirmative', 'aggression', 'algorithm', 'alignment', 'allegation', 'alliance',
    'allusion', 'amend', 'amusement', 'analytical', 'ancestry', 'anniversary', 'antagonist',
    'anticipation', 'antique', 'anxiety', 'apathy', 'applaud', 'appliance', 'apprehend', 'appraisal',
    'appropriate', 'approximate', 'arbitrary', 'archeology', 'archive', 'articulate', 'artistry',
    'assembly', 'assertion', 'assessment', 'assignment', 'assistance', 'assumption', 'assurance',
    'astonishment', 'attainment', 'attorney', 'audience', 'authentic', 'autonomy', 'aviation',
    'balloon', 'barbecue', 'barricade', 'battalion', 'behavioral', 'believable', 'benefactor',
    'bewilderment', 'biochemical', 'bizarre', 'blatant', 'blossom', 'boundary', 'bravery', 'brilliance',
    'brutality', 'bureaucracy', 'burglary', 'calculation', 'calibration', 'campaigner', 'camouflage',
    'capacity', 'capitalism', 'caricature', 'carnival', 'catastrophic', 'celebrity', 'cemetery',
    'century', 'ceremonial', 'certification', 'championship', 'charcoal', 'chemistry', 'chronicle',
    'circulation', 'circus', 'civilian', 'clarification', 'classical', 'cleanliness', 'clientele',
    'cloister', 'cohesion', 'collaborate', 'collection', 'collision', 'colony', 'commander',
    'commentary', 'commerce', 'commodity', 'compartment', 'compassion', 'compatible', 'competence',
    'complement', 'complexity', 'compliance', 'component', 'composure', 'comprehensive', 'compress',
    'compulsion', 'concealment', 'concession', 'concrete', 'condensation', 'conductor', 'confession',
    'configuration', 'conflict', 'conformity', 'confrontation', 'confusion', 'conglomerate', 'congratulations',
    'conjunction', 'conservation', 'consignment', 'consistency', 'consolation', 'conspiracy', 'constellation',
    'constituent', 'consultation', 'contagious', 'contamination', 'contemplation', 'contention', 'continuity',
    'contraction', 'contradiction', 'contribution', 'contributor', 'convenience', 'convention', 'conversation',
    'conveyance', 'conviction', 'cooperation', 'coordination', 'correlation', 'correspondent', 'corrosion',
    'council', 'counselor', 'courtesy', 'craftsmanship', 'creature', 'credence', 'criterion', 'curiosity',
    'custodian', 'cylindrical', 'cynicism', 'database', 'declaration', 'dedication', 'defensive', 'deficiency',
    'deflection', 'deformation', 'degradation', 'deliberation', 'delicacy', 'democracy', 'demographic', 'demonstrator',
    'denomination', 'denote', 'density', 'departure', 'dependency', 'depiction', 'depletion', 'deposit',
    'depression', 'derivative', 'descendant', 'description', 'designate', 'desperation', 'destruction',
    'detachment', 'deterioration', 'determination', 'diagnosis', 'dichotomy', 'dictatorship', 'dimension',
    'diplomacy', 'directive', 'disappointment', 'disapproval', 'disarray', 'disaster', 'disciplinary',
    'disclaimer', 'disclosure', 'disconnection', 'discontent', 'discretion', 'disguise', 'disintegration',
    'dismantle', 'disparity', 'dispatch', 'displacement', 'disposable', 'dispute', 'disruption',
    'distillation', 'distribution', 'divergence', 'diversification', 'documentation', 'dominance',
    'domination', 'donation', 'dormitory', 'dramatic', 'dynamic', 'economy', 'education', 'efficiency',
    'election', 'electronic', 'elevation', 'elimination', 'eloquence', 'emancipation', 'embargo',
    'embellishment', 'embrace', 'emergence', 'empowerment', 'enchantment', 'enclosure', 'encounter',
    'endorsement', 'endurance', 'enforcement', 'engagement', 'enhancement', 'enlightenment', 'enrollment',
    'enrichment', 'enterprise', 'enthusiasm', 'entity', 'entrepreneur', 'enumeration', 'environment',
    'envision', 'epidemic', 'equality', 'equation', 'equilibrium', 'equity', 'equivalent', 'eradication',
    'erosion', 'escalation', 'essence', 'establishment', 'eternity', 'evaluation', 'evaporation',
    'eventuality', 'evolutionary', 'exaggeration', 'examination', 'excerpt', 'exclusion', 'execution',
    'exemption', 'exhibit', 'expedition', 'expiration', 'explanation', 'exploration', 'exponential',
    'expression', 'extension', 'extraction', 'extravagant', 'fabrication', 'familiarity', 'fascination',
    'feasibility', 'federation', 'fertility', 'fictional', 'finalist', 'financier', 'firefighter',
    'flammable', 'flexibility', 'fluctuation', 'formidable', 'formulation', 'fragrance', 'framework',
    'fraternity', 'fraudulent', 'fulfillment', 'fundraiser', 'furnishings', 'futuristic', 'galvanize',
    'generosity', 'geography', 'geological', 'genuine', 'gigantic', 'globalization', 'glorious',
    'governance', 'graceful', 'gratitude', 'grievance', 'groundbreaking', 'guarantee', 'guideline',
    'gymnasium', 'hallucination', 'handwriting', 'harmonious', 'headquarters', 'hemisphere',
    'heritage', 'hesitation', 'hierarchical', 'historian', 'holistic', 'homogeneous', 'household',
    'humanitarian', 'hybridization', 'hypothetical', 'iconic', 'identification', 'ideology', 'ignorant',
    'illustrate', 'illustrious', 'immersion', 'immortality', 'impeccable', 'imperative', 'implementation',
    'implication', 'impressive', 'inability', 'inadequate', 'incentive', 'inception', 'incidental',
    'inclusion', 'incoherent', 'incompatible', 'inconclusive', 'incorporate', 'incumbent', 'indication',
    'indifference', 'indigenous', 'indispensable', 'individual', 'industrialization', 'inefficient',
    'influential', 'informative', 'ingenuity', 'inheritance', 'inhibition', 'initialization', 'initiative',
    'innovation', 'inquisitive', 'inscription', 'insecurity', 'insightful', 'insinuation', 'inspiration',
    'installation', 'instantaneous', 'instrumentation', 'integration', 'intellectual', 'intensity',
    'interchange', 'intercontinental', 'interest', 'interference', 'intermittent', 'interpretation',
    'interruption', 'intersection', 'intervention', 'intimacy', 'intricate', 'intriguing', 'invaluable',
    'invasion', 'invention', 'inventory', 'investigation', 'invisible', 'involuntary', 'invulnerability',
    'irrational', 'irreversible', 'isolation', 'justifiable', 'landmark', 'landslide', 'landscape',
    'leadership', 'legalization', 'legislation', 'legitimate', 'liability', 'liberation', 'lightning',
    'likelihood', 'liquidation', 'literacy', 'litigation', 'livelihood', 'localization', 'loneliness',
    'lucrative', 'luminosity', 'mainstream', 'maintenance', 'malleable', 'management', 'manifestation',
    'manipulation', 'marginalize', 'marketplace', 'mastermind', 'materialize', 'mechanical', 'mediation',
    'memorandum', 'metaphysical', 'methodology', 'metropolis', 'microcosm', 'milestone','millennium',
    'minimalist', 'miscommunication', 'misinterpretation', 'misrepresentation', 'modernization',
    'modification', 'monetization', 'monolithic', 'monumental', 'mortality', 'motivational', 'mutilation',
    'narrative', 'nationalism', 'naturalist', 'navigation', 'negligible', 'negotiable', 'neutrality',
    'nomination', 'nonconformist', 'nondisclosure', 'nonexistent', 'nonprofit', 'normalization',
    'noteworthy', 'nourishment', 'nullification', 'numerical', 'obedience', 'objectification',
    'observation', 'obsession', 'obsolescence', 'obstruction', 'occupational', 'officiate',
    'omniscient', 'operational', 'opportunity', 'oppression', 'optimization', 'orchestration',
    'organizational', 'originality', 'oscillation', 'outstanding', 'overemphasize', 'overhaul',
    'overlapping', 'overpopulation', 'overproduction', 'overqualified', 'overwhelming', 'pacification',
    'paradoxical', 'paralysis', 'parameter', 'parliamentary', 'participation', 'partnership',
    'paternalistic', 'perception', 'perfectionist', 'performance', 'permissible', 'perpetuate',
    'perplexing', 'perseverance', 'personalize', 'persuasion', 'philanthropy', 'philosophical',
    'photogenic', 'physicality', 'physiological', 'picturesque', 'pinnacle', 'plagiarism', 'polarization',
    'policymaker', 'popularize', 'population', 'portrayal', 'positioning', 'postgraduate', 'postulate',
    'potentiality', 'pragmatism', 'predecessor', 'preemptive', 'preferable', 'preoccupation', 'preposterous',
    'preservation', 'prestigious', 'prevalence', 'proactive', 'probability', 'problematic', 'procedural',
    'proclamation', 'procrastinate', 'prodigious', 'proficiency', 'profoundly', 'progressive', 'prohibition',
    'projection', 'proliferation', 'prolongation', 'pronunciation', 'propensity', 'proportional',
    'prospective', 'protagonist', 'provisional', 'publicize', 'punctuation', 'qualification', 'quantification',
    'quarantine', 'quarterly', 'rationalization', 'reassurance', 'reclamation', 'reconciliation',
    'reconstruction', 'redistribute', 'redundancy', 'reference', 'refinement', 'refinement', 'regeneration',
    'regionalism', 'registration', 'regulation', 'rehabilitation', 'reinforcement', 'relaxation', 'reliability',
    'relocation', 'remarkable', 'remembrance', 'remuneration', 'renaissance', 'renewable', 'renunciation',
    'reorganization', 'repetition', 'replacement', 'repository', 'representation', 'reproduction',
    'republican', 'requirement', 'reservation', 'resilience', 'resistance', 'resolution', 'responsiveness',
    'restrain', 'retaliation', 'retrospective', 'revaluation', 'revitalization', 'rhetorical', 'righteous',
    'ritualistic', 'romanticize', 'rotation', 'sanctuary', 'sanitation', 'satisfaction', 'saturation',
    'scandalous', 'scarcity', 'scholarship', 'scrutinize', 'segmentation', 'selfishness', 'semantics',
    'sensation', 'sensibility', 'sensory', 'sentimentality', 'sequence', 'serendipity', 'settlement',
    'shimmering', 'significance', 'simplification', 'simulation', 'simultaneous', 'skepticism', 'socialize',
    'solidarity', 'sovereignty', 'specialize', 'specification', 'speculative', 'spirituality', 'stabilization',
    'standardize', 'statistical', 'stereotype', 'stimulate', 'strategist', 'streamline', 'strengthen',
    'structural', 'stubbornness', 'subdivision', 'subjective', 'subordinate', 'subscription', 'subsequent',
    'substantial', 'substitute', 'subtraction', 'suburban', 'sufficiency', 'suggestion', 'summarize',
    'supplement', 'suppress', 'sustainability', 'symbolism', 'sympathize', 'synchronize', 'syndication',
    'systematic', 'tactfulness', 'tangibility', 'technological', 'terminology', 'theatrical', 'theoretical',
    'therapeutic', 'thoroughness', 'thoughtful', 'tolerable', 'tolerance', 'topography', 'traditionally',
    'trajectory', 'tranquility', 'transatlantic', 'transaction', 'transcend', 'transformation', 'transistor',
    'transparency', 'transportation', 'tribulation', 'troublesome', 'trustworthy', 'turbulence', 'typical',
    'unacceptable', 'unanticipated', 'unavoidable', 'unbearable', 'unbelievable', 'unconventional', 'underestimate',
    'underprivileged', 'understanding', 'undervalue', 'undisputed', 'unification', 'unilateral', 'unintended',
    'uninterrupted', 'universal', 'unpredictable', 'unreasonable', 'unsatisfactory', 'unscrupulous', 'unselfishness',
    'unsuccessful', 'untouchable', 'unwillingness', 'urbanization', 'utilitarian', 'utilization', 'vaccination',
    'validity', 'variability', 'verification', 'versatility', 'vertical', 'vibrant', 'victimization', 'visualization',
    'volatility', 'volunteerism', 'vulnerability', 'waterfall', 'weakness', 'widespread', 'willingness',
    'withdrawal', 'withstand', 'worldview', 'worrisome', 'worthiness', 'yesterday', 'youthfulness', 'zealousness',
    'zenith', 'zoological', 'zucchini')