from pathlib import Path


BASE_DIR = Path(__file__).parent
KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge_base"
RAW_DIR = KNOWLEDGE_BASE_DIR / "raw"
WIKI_DIR = KNOWLEDGE_BASE_DIR / "wiki"
REPORT_PATH = KNOWLEDGE_BASE_DIR / "LINT_REPORT.md"

RAW_TO_WIKI = {
    "fpga_intro.txt": "FPGA.md",
    "cmsketch_intro.txt": "CMSketch.md",
    "transformer_inference_intro.txt": "Transformer_Inference.md",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has_real_content(markdown_text: str) -> bool:
    lines = []
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            lines.append(stripped)
    return bool(lines)


def expected_wiki_names(raw_file: Path) -> set[str]:
    mapped_name = RAW_TO_WIKI.get(raw_file.name)
    if mapped_name:
        return {mapped_name.lower()}

    stem = raw_file.stem.lower()
    names = {f"{stem}.md"}

    for suffix in ("_intro", "_notes", "_source", "_raw"):
        if stem.endswith(suffix):
            names.add(f"{stem.removesuffix(suffix)}.md")

    return names


def check_empty_wiki_pages(wiki_files: list[Path]) -> list[str]:
    problems = []
    for wiki_file in wiki_files:
        content = read_text(wiki_file)
        if not has_real_content(content):
            problems.append(f"- `{wiki_file.name}` 页面为空或只有标题。")
    return problems


def check_missing_source(wiki_files: list[Path]) -> list[str]:
    problems = []
    for wiki_file in wiki_files:
        content = read_text(wiki_file)
        if "## 来源" not in content:
            problems.append(f"- `{wiki_file.name}` 没有“## 来源”章节。")
    return problems


def check_pending_verification(wiki_files: list[Path]) -> list[str]:
    problems = []
    for wiki_file in wiki_files:
        content = read_text(wiki_file)
        if "待核实" in content:
            problems.append(f"- `{wiki_file.name}` 包含“待核实”标记。")
    return problems


def check_missing_wiki_pages(raw_files: list[Path], wiki_files: list[Path]) -> list[str]:
    problems = []
    wiki_names = {wiki_file.name.lower() for wiki_file in wiki_files}

    for raw_file in raw_files:
        content = read_text(raw_file).strip()
        if not content:
            continue

        expected_names = expected_wiki_names(raw_file)
        if wiki_names.isdisjoint(expected_names):
            expected_text = " 或 ".join(f"`{name}`" for name in sorted(expected_names))
            problems.append(
                f"- `{raw_file.name}` 有资料，但没有对应 wiki 页面：{expected_text}。"
            )

    return problems


def render_section(title: str, problems: list[str]) -> str:
    if problems:
        return f"## {title}\n\n" + "\n".join(problems)
    return f"## {title}\n\n未发现问题。"


def main() -> None:
    raw_files = sorted(RAW_DIR.glob("*.txt"))
    wiki_files = sorted(WIKI_DIR.glob("*.md"))

    sections = [
        "# Wiki 检查报告",
        render_section("空 wiki 页面", check_empty_wiki_pages(wiki_files)),
        render_section("缺少来源部分", check_missing_source(wiki_files)),
        render_section("待核实标记", check_pending_verification(wiki_files)),
        render_section("raw 与 wiki 对应关系", check_missing_wiki_pages(raw_files, wiki_files)),
    ]

    REPORT_PATH.write_text("\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"检查完成：{REPORT_PATH}")


if __name__ == "__main__":
    main()
