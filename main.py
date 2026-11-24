from pathlib import Path

ENTRY = "My agent called me Din all night, which is its own nickname, then logged me as the confused one."

def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
