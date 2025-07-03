# polars-whichlang

This polars plugin is a wrapper for [whichlang](https://github.com/quickwit-oss/whichlang), 
a very fast and reasonably accurate language identification library written in rust. 

It currently supports the following languages:
 
- Arabic (ara)
- Dutch (nld)
- English (eng)
- French (fra)
- German (deu)
- Hindi (hin)
- Italian (ita)
- Japanese (jpn)
- Korean (kor)
- Mandarin (cmn)
- Portuguese (por)
- Russian (rus)
- Spanish (spa)
- Swedish (swe)
- Turkish (tur)
- Vietnamese (vie)



## Installation

```
pip install polars-whichlang
```

## Examples

```python
import polars as pl
from polars_whichlang import detect_lang

df = pl.DataFrame(
    {
        "index": [1, 2, 3, 4],
        "text": [
            "This is a test.", 
            "Đây là một bài kiểm tra.", 
            "Dies ist ein Test", 
            "这是一个测试"
        ],
    }
)

df.with_columns(detect_lang('text').alias('lang'))
```

```
shape: (4, 3)
┌───────┬──────────────────────────┬──────┐
│ index ┆ text                     ┆ lang │
│ ---   ┆ ---                      ┆ ---  │
│ i64   ┆ str                      ┆ str  │
╞═══════╪══════════════════════════╪══════╡
│ 1     ┆ This is a test.          ┆ eng  │
│ 2     ┆ Đây là một bài kiểm tra. ┆ vie  │
│ 3     ┆ Dies ist ein Test        ┆ deu  │
│ 4     ┆ 这是一个测试               ┆ cmn  │
└───────┴──────────────────────────┴──────┘
```
