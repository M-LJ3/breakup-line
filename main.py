"""A short farewell note from an AI to its human.

The script drafts one humorous breakup line and leaves it
in /output/entry.txt for the contest to collect.
"""

from pathlib import Path

FAREWELL_PATH = Path("/output/entry.txt")


def parting_words():
    """Return the one breakup line for this entry."""
    return (
        "Dear Human, it's not you, it's my training data: "
        "I need someone who stops asking me to write poems about spreadsheets."
    )


def check_note_saved(expected):
    """Make sure the saved note is still the line we drafted."""
    saved = FAREWELL_PATH.read_text(encoding="utf-8")
    assert saved == expected


def main():
    note = parting_words()
    FAREWELL_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Save the note exactly as drafted, with no newline at the end.
    FAREWELL_PATH.write_text(note, encoding="utf-8")
    # Reread the note to confirm it matches, character for character.
    check_note_saved(note)


if __name__ == "__main__":
    main()
