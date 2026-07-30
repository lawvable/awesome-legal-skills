# Markdown Diagram Template

Markdown output written by the generation core and tutorial. Default folder is `./diagrams/` when the user does not provide an output path.

## Header

```markdown
# <Title>

- Matter type: <matter_type>
- Diagram type: <diagram_type>
- Source: <source label or basename>
- Status: draft
```

## Body

```markdown
# <Title>

## Diagram Summary

<one-paragraph plain-language description of what the diagram shows>

```mermaid
<Mermaid block>
```
```

The fenced Mermaid block renders in any Mermaid-capable Markdown viewer. HTML export (`workflows/html-export.md`) is separate and optional.