import random

# Word fragments organized by syllable counts
syllable_fragments = {
    1: ["dawn", "mist", "spring", "fall", "light", "clouds", "waves", "breeze"],
    2: ["mountain", "river", "whisper", "autumn", "blossom", "meadow"],
    3: ["butterfly", "serenity", "reflection", "waterfall", "harmony"],
    4: ["beneath the trees", "dancing sunlight", "scattered blossoms"],
    5: ["a gentle breeze whispers", "waves crash upon the shore"],
    7: ["through the ancient forest trails", "underneath the glowing moon"],
}

def construct_line(syllables):
    """Construct a line with the specified syllable count."""
    line = []
    while syllables > 0:
        possible = [key for key in syllable_fragments if key <= syllables]
        choice = random.choice(possible)
        line.append(random.choice(syllable_fragments[choice]))
        syllables -= choice
    return " ".join(line)

def generate_haiku():
    """Generate a random haiku following the 5-7-5 structure."""
    return "\n".join([
        construct_line(5),
        construct_line(7),
        construct_line(5),
    ])

# Interactive generation
print("=== Procedural Haiku Generator ===")
print("\nYour Random Haiku:\n")
print(generate_haiku())
