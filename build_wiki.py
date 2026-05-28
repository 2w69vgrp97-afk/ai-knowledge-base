from pathlib import Path

from src.ollama_client import ask_ollama


BASE_DIR = Path(__file__).parent
KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge_base"
RAW_DIR = KNOWLEDGE_BASE_DIR / "raw"
WIKI_DIR = KNOWLEDGE_BASE_DIR / "wiki"

RAW_TO_WIKI = {
    "fpga_intro.txt": ("FPGA.md", "FPGA"),
    "cmsketch_intro.txt": ("CMSketch.md", "Count-Min Sketch"),
    "transformer_inference_intro.txt": (
        "Transformer_Inference.md",
        "Transformer Inference",
    ),
}


def source_path(raw_file: Path) -> str:
    return raw_file.relative_to(BASE_DIR).as_posix()


def wiki_target_for(raw_file: Path) -> tuple[Path, str]:
    wiki_name, title = RAW_TO_WIKI.get(
        raw_file.name,
        (f"{raw_file.stem}.md", raw_file.stem.replace("_", " ").title()),
    )
    relative_raw_file = raw_file.relative_to(RAW_DIR)
    return WIKI_DIR / relative_raw_file.parent / wiki_name, title


def ensure_source_section(markdown_text: str, source: str) -> str:
    if "## 来源" in markdown_text:
        return markdown_text

    return markdown_text.rstrip() + f"\n\n## 来源\n- {source}\n"


def build_fallback_note(raw_text: str, title: str, source: str) -> str:
    return f"""# {title}

## 1. 核心概念
{raw_text}

## 2. 关键要点
- 本页由原始资料整理而来，只保留 raw 文件中已有的信息。
- 后续可继续补充术语解释、应用场景和实现细节。

## 3. 关联问题
- 这个主题的核心流程可以怎样画成框图？
- 它和硬件实现之间有哪些资源、时延或吞吐量权衡？

## 来源
- {source}
"""


def build_prompt(raw_text: str, title: str, source: str) -> str:
    return f"""
请把下面的原始资料整理成结构化 Markdown 知识页。

要求：
1. 只根据 raw 原始资料整理，不要编造 raw 中没有的事实。
2. 不确定的内容标注“待核实”。
3. 内容清晰，适合初学者理解。
4. 必须包含“## 来源”章节，并写入：
   - {source}
5. 建议使用下面结构：
# {title}
## 1. 核心概念
## 2. 为什么重要
## 3. 物理/系统图像
## 4. 核心因果链
## 5. 前置知识
使用 Obsidian 风格链接，例如 [[Band_Theory]]
## 6. 相关概念
使用 Obsidian 风格链接，例如 [[Fermi_Level]]
## 7. 后续影响
使用 Obsidian 风格链接，例如 [[PN_Junction]]
## 8. 待追问问题
## 来源
- {source}

原始资料：
{raw_text}
"""


def build_wiki_page(raw_file: Path) -> Path:
    raw_text = raw_file.read_text(encoding="utf-8").strip()
    wiki_file, title = wiki_target_for(raw_file)
    source = source_path(raw_file)

    try:
        markdown_note = ask_ollama(build_prompt(raw_text, title, source))
    except OSError as error:
        print(f"本地模型暂时不可用，改用简单规则生成：{raw_file.name} ({error})")
        markdown_note = build_fallback_note(raw_text, title, source)
    else:
        if not markdown_note.strip() or markdown_note.lstrip().startswith("调用 Ollama 失败"):
            print(f"本地模型未返回有效结果，改用简单规则生成：{raw_file.name}")
            markdown_note = build_fallback_note(raw_text, title, source)

    markdown_note = ensure_source_section(markdown_note, source)

    wiki_file.parent.mkdir(parents=True, exist_ok=True)
    wiki_file.write_text(markdown_note, encoding="utf-8")
    return wiki_file


def main() -> None:
    raw_files = sorted(RAW_DIR.rglob("*.txt"))
    if not raw_files:
        print(f"未找到原始资料：{RAW_DIR}")
        return

    for raw_file in raw_files:
        wiki_file = build_wiki_page(raw_file)
        print(f"已生成 {wiki_file.relative_to(BASE_DIR).as_posix()}")


if __name__ == "__main__":
    main()
