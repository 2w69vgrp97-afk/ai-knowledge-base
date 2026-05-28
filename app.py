from src.ollama_client import ask_ollama


def main() -> None:
    prompt = input("请输入你的问题: ")
    answer = ask_ollama(prompt)
    print("\n模型回复:")
    print(answer)


if __name__ == "__main__":
    main()
