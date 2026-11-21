#!/usr/bin/env python3
"""Zero-dependency cohort pairing and topic-reshuffling engine for SDL Dev Lab.

Reads ``cohort/roster.json`` and a module's ``topics.json`` pool, randomly
shuffles mentees into non-repeating pairs (avoiding ``past_pairs`` unless all
unique pairings are exhausted), assigns distinct individual and group topics
without overlap, and emits a formatted Markdown ``ASSIGNMENTS.md`` file.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


Pair = tuple[str, str]


def canonical_pair(a: str, b: str) -> Pair:
    """Return an order-independent canonical representation of a pair."""
    return (a, b) if a <= b else (b, a)


def slugify_mentee(name: str) -> str:
    """Convert a mentee name to a lowercase hyphenated branch slug."""
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return slug or "mentee"


def derive_module_code(module_slug: str) -> str:
    """Extract a short branch prefix such as ``m03`` from ``module-03-foo``."""
    match = re.search(r"module[-_]?(\d+)", module_slug, re.IGNORECASE)
    if match:
        return f"m{int(match.group(1)):02d}"
    cleaned = re.sub(r"[^a-z0-9]+", "-", module_slug.strip().lower()).strip("-")
    return cleaned or "mod"


def find_non_repeating_pairs(
    mentees: list[str],
    past_pairs: set[Pair],
    rng: random.Random,
) -> tuple[list[list[str]], int]:
    """Partition ``mentees`` into pairs minimizing overlap with ``past_pairs``.

    Returns ``(pairs, repeat_count)``. Uses randomized backtracking to guarantee
    finding a zero-repeat perfect matching whenever one exists. If all unique
    pairings are exhausted, falls back to a minimum-repeat matching.
    """
    if len(mentees) % 2 != 0:
        raise ValueError(f"Roster must contain an even number of mentees; got {len(mentees)}.")

    shuffled = list(mentees)
    rng.shuffle(shuffled)

    def backtrack_exact(remaining: list[str]) -> list[list[str]] | None:
        if not remaining:
            return []
        first = remaining[0]
        candidates = list(range(1, len(remaining)))
        rng.shuffle(candidates)
        for idx in candidates:
            partner = remaining[idx]
            if canonical_pair(first, partner) in past_pairs:
                continue
            next_remaining = [m for i, m in enumerate(remaining) if i not in (0, idx)]
            rest = backtrack_exact(next_remaining)
            if rest is not None:
                return [[first, partner]] + rest
        return None

    exact = backtrack_exact(shuffled)
    if exact is not None:
        return exact, 0

    # Fallback when all unique pairings are exhausted: minimize repeated pairs.
    best_pairs: list[list[str]] | None = None
    best_repeats = len(mentees)

    def backtrack_min(remaining: list[str], current: list[list[str]], repeats: int) -> None:
        nonlocal best_pairs, best_repeats
        if repeats >= best_repeats:
            return
        if not remaining:
            best_repeats = repeats
            best_pairs = [list(p) for p in current]
            return
        first = remaining[0]
        candidates = list(range(1, len(remaining)))
        rng.shuffle(candidates)
        candidates.sort(key=lambda i: 1 if canonical_pair(first, remaining[i]) in past_pairs else 0)
        for idx in candidates:
            partner = remaining[idx]
            is_repeat = 1 if canonical_pair(first, partner) in past_pairs else 0
            next_remaining = [m for i, m in enumerate(remaining) if i not in (0, idx)]
            current.append([first, partner])
            backtrack_min(next_remaining, current, repeats + is_repeat)
            current.pop()

    backtrack_min(shuffled, [], 0)
    assert best_pairs is not None
    return best_pairs, best_repeats


def normalize_topic(entry: Any) -> str:
    """Extract a topic title string from either a plain string or an object."""
    if isinstance(entry, str):
        return entry.strip()
    if isinstance(entry, dict) and "title" in entry:
        return str(entry["title"]).strip()
    raise ValueError(f"Unsupported topic format: {entry!r}")


def load_topics(topics_path: Path, mentee_count: int, group_count: int) -> tuple[list[str], list[str]]:
    """Load and validate individual and group topic pools with no overlap."""
    if not topics_path.exists():
        raise FileNotFoundError(
            f"Topic pool not found at '{topics_path}'. "
            "Create a topics.json with 'individual_topics' and 'group_topics' lists "
            "or pass --topics <path>."
        )

    data = json.loads(topics_path.read_text(encoding="utf-8"))
    raw_ind = data.get("individual_topics", [])
    raw_grp = data.get("group_topics", [])

    ind_topics = list(dict.fromkeys(normalize_topic(t) for t in raw_ind))
    grp_topics = list(dict.fromkeys(normalize_topic(t) for t in raw_grp))

    overlap = set(ind_topics).intersection(grp_topics)
    if overlap:
        raise ValueError(f"Topics must not overlap between individual and group pools: {sorted(overlap)}")
    if len(ind_topics) < mentee_count:
        raise ValueError(f"Need at least {mentee_count} distinct individual topics; found {len(ind_topics)}.")
    if len(grp_topics) < group_count:
        raise ValueError(f"Need at least {group_count} distinct group topics; found {len(grp_topics)}.")

    return ind_topics, grp_topics


def render_markdown(
    module_slug: str,
    seed: int,
    timestamp: str,
    individual_rows: list[tuple[int, str, str, str]],
    group_rows: list[tuple[int, str, str, str, str]],
    repeat_count: int,
) -> str:
    """Format individual and group assignments into a Markdown document."""
    lines = [
        f"# {module_slug}: Cohort Assignments",
        "",
        f"> **Generated:** `{timestamp}` | **Seed:** `{seed}` | **Repeated Past Pairs:** `{repeat_count}`",
        "",
        "---",
        "",
        "## Part A: Individual Projects",
        "",
        "| # | Mentee | Assigned Topic | Branch Name |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for idx, mentee, topic, branch in individual_rows:
        lines.append(f"| {idx} | **{mentee}** | {topic} | `{branch}` |")

    lines.extend([
        "",
        "---",
        "",
        "## Part B: Pair Group Projects",
        "",
        "| Group | Pair | Assigned Topic | Branch Name |",
        "| :--- | :--- | :--- | :--- |",
    ])
    for group_num, member_a, member_b, topic, branch in group_rows:
        lines.append(f"| **Group {group_num}** | {member_a} & {member_b} | {topic} | `{branch}` |")

    lines.append("")
    return "\n".join(lines)


def resolve_topics_path(module_slug: str, explicit_topics: str | None) -> Path:
    """Resolve the topic pool JSON path for a module."""
    if explicit_topics:
        return Path(explicit_topics)
    candidates = [
        Path("modules") / module_slug / "topics.json",
        Path("cohort") / "topics" / f"{module_slug}.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Shuffle SDL cohort mentees into non-repeating pairs and assign unique topics."
    )
    parser.add_argument(
        "--module",
        required=True,
        help="Target module slug (e.g., module-03 or module-03-frontend-arch).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional integer RNG seed for reproducibility. Defaults to secrets.randbelow(10**8).",
    )
    parser.add_argument(
        "--record-history",
        action="store_true",
        help="Append generated pairs to past_pairs and history in cohort/roster.json.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Path to write formatted Markdown assignment tables (prints to stdout if omitted).",
    )
    parser.add_argument(
        "--roster",
        default="cohort/roster.json",
        help="Path to roster JSON file (default: cohort/roster.json).",
    )
    parser.add_argument(
        "--topics",
        default=None,
        help="Path to module topic pool JSON (default: modules/<module>/topics.json).",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    roster_path = Path(args.roster)
    if not roster_path.exists():
        print(f"Error: Roster file not found at '{roster_path}'.", file=sys.stderr)
        return 1

    roster = json.loads(roster_path.read_text(encoding="utf-8"))
    mentees: list[str] = list(roster.get("mentees", []))
    raw_past_pairs: list[list[str]] = list(roster.get("past_pairs", []))
    past_pairs: set[Pair] = {canonical_pair(p[0], p[1]) for p in raw_past_pairs if len(p) == 2}

    if len(mentees) < 2 or len(mentees) % 2 != 0:
        print(f"Error: Expected an even number of mentees (>= 2), found {len(mentees)}.", file=sys.stderr)
        return 1

    group_count = len(mentees) // 2
    topics_path = resolve_topics_path(args.module, args.topics)
    try:
        ind_pool, grp_pool = load_topics(topics_path, len(mentees), group_count)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    seed = args.seed if args.seed is not None else secrets.randbelow(10**8)
    rng = random.Random(seed)

    pairs, repeat_count = find_non_repeating_pairs(mentees, past_pairs, rng)
    if repeat_count > 0:
        print(
            f"Warning: All unique pairings exhausted; minimized repeated pairs to {repeat_count}.",
            file=sys.stderr,
        )

    rng.shuffle(ind_pool)
    rng.shuffle(grp_pool)

    module_code = derive_module_code(args.module)
    individual_rows = [
        (idx, mentee, ind_pool[idx - 1], f"feat/{module_code}-ind-{slugify_mentee(mentee)}")
        for idx, mentee in enumerate(mentees, start=1)
    ]
    group_rows = [
        (idx, pair[0], pair[1], grp_pool[idx - 1], f"feat/{module_code}-grp-{idx}")
        for idx, pair in enumerate(pairs, start=1)
    ]

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    markdown = render_markdown(
        module_slug=args.module,
        seed=seed,
        timestamp=timestamp,
        individual_rows=individual_rows,
        group_rows=group_rows,
        repeat_count=repeat_count,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
        print(f"Wrote assignments to {output_path} (seed={seed}, repeats={repeat_count}).")
    else:
        print(markdown)

    if args.record_history:
        existing_canonical = set(past_pairs)
        for pair in pairs:
            key = canonical_pair(pair[0], pair[1])
            if key not in existing_canonical:
                raw_past_pairs.append(pair)
                existing_canonical.add(key)
        roster["past_pairs"] = raw_past_pairs
        history = list(roster.get("history", []))
        history.append(
            {
                "module": args.module,
                "seed": seed,
                "timestamp": timestamp,
                "pairs": pairs,
            }
        )
        roster["history"] = history
        roster_path.write_text(json.dumps(roster, indent=2) + "\n", encoding="utf-8")
        print(f"Updated pairing history in {roster_path}.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
