#!/usr/bin/env python3
"""
Intelligently chunk a law review article into manageable sections.
Respects article structure (sections, subsections) and word count limits.
"""

import re
import sys
from typing import List, Dict, Tuple


def parse_article_structure(text: str) -> List[Dict]:
    """
    Parse article into hierarchical sections based on common law review formatting.
    Detects: Roman numerals, letters, numbers, and descriptive headers.
    """
    sections = []
    
    # Common section header patterns in law review articles
    patterns = [
        (r'^([IVX]+)\.\s+(.+)$', 1, 'roman'),  # I., II., III., IV.
        (r'^([A-Z])\.\s+(.+)$', 2, 'letter'),  # A., B., C.
        (r'^(\d+)\.\s+(.+)$', 3, 'number'),    # 1., 2., 3.
        (r'^(Introduction|Abstract|Conclusion|Bibliography|References)\s*$', 0, 'special'),
    ]
    
    lines = text.split('\n')
    current_text = []
    current_header = None
    current_level = None
    start_line = 0
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        
        # Check if this line matches any section header pattern
        matched = False
        for pattern, level, type_name in patterns:
            match = re.match(pattern, line_stripped, re.IGNORECASE)
            if match:
                # Save previous section
                if current_header is not None:
                    sections.append({
                        'header': current_header,
                        'level': current_level,
                        'text': '\n'.join(current_text),
                        'start_line': start_line,
                        'end_line': i - 1,
                        'word_count': len(' '.join(current_text).split())
                    })
                
                # Start new section
                if type_name == 'special':
                    current_header = match.group(1)
                else:
                    current_header = line_stripped
                current_level = level
                current_text = []
                start_line = i
                matched = True
                break
        
        if not matched:
            current_text.append(line)
    
    # Add final section
    if current_header is not None:
        sections.append({
            'header': current_header,
            'level': current_level,
            'text': '\n'.join(current_text),
            'start_line': start_line,
            'end_line': len(lines) - 1,
            'word_count': len(' '.join(current_text).split())
        })
    
    # If no sections detected, treat entire document as one section
    if not sections:
        sections.append({
            'header': 'Full Article',
            'level': 0,
            'text': text,
            'start_line': 0,
            'end_line': len(lines) - 1,
            'word_count': len(text.split())
        })
    
    return sections


def chunk_by_word_limit(sections: List[Dict], max_words: int = 8000) -> List[Dict]:
    """
    Group sections into chunks that don't exceed max_words.
    Tries to keep related sections together while respecting size limits.
    """
    chunks = []
    current_chunk = {
        'sections': [],
        'text_parts': [],
        'word_count': 0,
        'start_section': None,
        'end_section': None
    }
    
    for section in sections:
        section_words = section['word_count']
        
        # If single section exceeds limit, it becomes its own chunk
        if section_words > max_words:
            # Save current chunk if it has content
            if current_chunk['sections']:
                chunks.append(current_chunk)
            
            # Large section becomes its own chunk
            chunks.append({
                'sections': [section],
                'text_parts': [section['text']],
                'word_count': section_words,
                'start_section': section['header'],
                'end_section': section['header'],
                'oversized': True
            })
            
            # Reset current chunk
            current_chunk = {
                'sections': [],
                'text_parts': [],
                'word_count': 0,
                'start_section': None,
                'end_section': None
            }
        
        # If adding this section would exceed limit, save current chunk and start new one
        elif current_chunk['word_count'] + section_words > max_words:
            if current_chunk['sections']:
                chunks.append(current_chunk)
            
            current_chunk = {
                'sections': [section],
                'text_parts': [section['text']],
                'word_count': section_words,
                'start_section': section['header'],
                'end_section': section['header']
            }
        
        # Otherwise add section to current chunk
        else:
            if not current_chunk['sections']:
                current_chunk['start_section'] = section['header']
            current_chunk['sections'].append(section)
            current_chunk['text_parts'].append(section['text'])
            current_chunk['word_count'] += section_words
            current_chunk['end_section'] = section['header']
    
    # Add final chunk
    if current_chunk['sections']:
        chunks.append(current_chunk)
    
    return chunks


def format_chunk_summary(chunks: List[Dict]) -> str:
    """Format a summary of the chunks for review."""
    summary = f"Article divided into {len(chunks)} chunks:\n\n"
    
    for i, chunk in enumerate(chunks, 1):
        summary += f"Chunk {i}: {chunk['word_count']:,} words\n"
        summary += f"  Sections: {chunk['start_section']}"
        if chunk['start_section'] != chunk['end_section']:
            summary += f" → {chunk['end_section']}"
        summary += "\n"
        if chunk.get('oversized'):
            summary += "  ⚠️ Single section exceeds word limit\n"
        summary += f"  Contains {len(chunk['sections'])} section(s)\n\n"
    
    return summary



def read_source(path: str) -> str:
    """Read an article from .docx or plain text.

    .docx is a zip of XML; paragraph text is extracted with the standard
    library only, so no third-party dependency is required. Footnotes are
    appended after the body so citation review can see them.
    """
    if path.lower().endswith(('.docx', '.dotx')):
        import zipfile
        try:
            z = zipfile.ZipFile(path)
        except zipfile.BadZipFile:
            raise SystemExit(f"Error: '{path}' is not readable as a .docx file.")
        parts = []
        for member, label in (('word/document.xml', None),
                              ('word/footnotes.xml', 'FOOTNOTES'),
                              ('word/endnotes.xml', 'ENDNOTES')):
            if member not in z.namelist():
                continue
            xml = z.read(member).decode('utf-8', 'ignore')
            # drop Word field instructions (TOC entries arrive as PAGEREF
            # codes and would otherwise be parsed as real headings)
            xml = re.sub(r'<w:instrText[^>]*>.*?</w:instrText>', '', xml, flags=re.S)
            xml = re.sub(r'<w:fldSimple[^>]*w:instr="[^"]*"[^>]*>', '<w:fldSimple>', xml)
            # paragraph breaks, then strip tags
            xml = re.sub(r'</w:p>', '\n', xml)
            xml = re.sub(r'<w:tab[^>]*/>', '\t', xml)
            txt = re.sub(r'<[^>]+>', '', xml)
            txt = (txt.replace('&amp;', '&').replace('&lt;', '<')
                      .replace('&gt;', '>').replace('&quot;', '"')
                      .replace('&apos;', "'"))
            txt = '\n'.join(line.rstrip() for line in txt.splitlines())
            # drop table-of-contents lines ("I. Heading<tab>4"), which would
            # otherwise be parsed as empty duplicates of the real headings
            txt = '\n'.join(l for l in txt.splitlines()
                             if not re.match(r'^.+\t\s*\d+\s*$', l))
            txt = re.sub(r'\n{3,}', '\n\n', txt).strip()
            if not txt:
                continue
            parts.append(txt if label is None else f"\n\n## {label}\n\n{txt}")
        if not parts:
            raise SystemExit(f"Error: no readable text found in '{path}'.")
        return '\n'.join(parts)

    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python chunk_article.py <article_file> [max_words_per_chunk]")
        sys.exit(1)
    
    article_file = sys.argv[1]
    max_words = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
    
    text = read_source(article_file)
    
    print(f"Analyzing article structure...\n")
    sections = parse_article_structure(text)
    
    print(f"Found {len(sections)} sections:")
    for section in sections:
        indent = "  " * section['level']
        print(f"{indent}{section['header']}: {section['word_count']:,} words")
    
    print(f"\n{'='*60}\n")
    print(f"Creating chunks with max {max_words:,} words per chunk...\n")
    
    chunks = chunk_by_word_limit(sections, max_words)
    print(format_chunk_summary(chunks))
    
    # Write chunks to separate files
    base_name = article_file.rsplit('.', 1)[0]
    for i, chunk in enumerate(chunks, 1):
        chunk_file = f"{base_name}_chunk_{i}.txt"
        with open(chunk_file, 'w', encoding='utf-8') as f:
            f.write(f"CHUNK {i} OF {len(chunks)}\n")
            f.write(f"Sections: {chunk['start_section']}")
            if chunk['start_section'] != chunk['end_section']:
                f.write(f" → {chunk['end_section']}")
            f.write(f"\n{'='*60}\n\n")
            f.write('\n\n'.join(chunk['text_parts']))
        print(f"✓ Wrote {chunk_file}")


if __name__ == '__main__':
    main()
