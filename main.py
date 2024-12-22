import random

# Word banks
nouns = ["ocean", "dream", "shadow", "mountain", "whisper", "star", "river", "time", "forest", "flame"]
verbs = ["dances", "sings", "melts", "rises", "falls", "flows", "hides", "wanders", "shines", "drifts"]
adjectives = ["silent", "eternal", "hidden", "golden", "shimmering", "forgotten", "lonely", "wild", "broken", "ancient"]
prepositions = ["beneath", "above", "within", "beyond", "around", "through"]
articles = ["the", "a"]

# Poem structure templates
templates = [
    "{article} {adjective} {noun} {verb} {preposition} {article} {adjective} {noun}.",
    "{article} {noun} {verb}, {article} {adjective} {noun} {verb} {preposition} {article} {noun}.",
    "{adjective} {nouns}, {adjective} {nouns}, {verb} {preposition} {article} {noun}.",
    "Oh, {adjective} {noun}, how you {verb} {preposition} {article} {adjective} {noun}.",
]

def generate_line():
    """Generates a random line of poetry."""
    template = random.choice(templates)
    return template.format(
        article=random.choice(articles),
        adjective=random.choice(adjectives),
        noun=random.choice(nouns),
        nouns=random.choice(nouns) + "s",  # Plural form
        verb=random.choice(verbs),
        preposition=random.choice(prepositions),
    )

def generate_poem(lines=4):
    """Generates a poem with a specified number of lines."""
    return "\n".join(generate_line() for _ in range(lines))

# Generate and print a poem
print("Here is your random poem:\n")
print(generate_poem())
