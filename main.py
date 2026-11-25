#!/usr/bin/env python3
"""Pigeon Pitch, One Line (make.fun program/v1).

Writes the entry -- one elevator pitch, in English, from a city pigeon
to investors for its startup -- to /output/entry.txt.

Deterministic: no network, no randomness, no input. The output file is
left naturally readable: umask 022 makes open() create it mode 0644.
"""

import os

ENTRY = (
    "40,000 couriers, paid in breadcrumbs, who never strike \u2014 our "
    "logo is already on every statue in the city. Invest, or keep "
    "losing to birds."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
