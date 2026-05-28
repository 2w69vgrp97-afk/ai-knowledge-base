# 本地网页浏览

本项目使用 MkDocs Material 将 `knowledge_base/wiki/` 下的 Markdown 页面生成成本地可浏览网站。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 本地启动

```bash
mkdocs serve
```

启动后在电脑浏览器访问：

```text
http://127.0.0.1:8000
```

## 手机局域网访问

```bash
mkdocs serve -a 0.0.0.0:8000
```

说明：

- 电脑和手机必须在同一个 Wi-Fi。
- Windows 用 `ipconfig` 查询 IPv4 地址。
- 手机访问 `http://电脑IPv4地址:8000`。
- Windows 防火墙可能阻止访问。
- 电脑关机或停止命令后，手机不能继续访问。

## 备注

- 文档目录由 `mkdocs.yml` 中的 `docs_dir: knowledge_base/wiki` 指定。
- Obsidian 的 `[[WikiLink]]` 暂时保留原样，没有批量替换。
- 生成的静态站点输出到 `site/`，该目录已在 `.gitignore` 中忽略。
