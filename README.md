# SE (UE23CS341A) Lab 5 Assignment

## Top 10 Known Issues (High Priority)

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Insecure `eval` (B307, W0123) | Security / Lint | 67 | Use of possibly insecure function / Use of eval | Use `ast.literal_eval`. |
| Bare Except / Pass (E722, B110, W0702) | Security / Lint | 21 | do not use bare 'except' / Try, Except, Pass detected | Specify exception; avoid `pass`. |
| Dangerous Default Value (W0102) | Lint (pylint) | 9 | Dangerous default value [] as argument | Use `None` as default. |
| `global` statement used (W0603) | Lint (pylint) | 31 | Using the global statement | Refactor to avoid `global`. |
| Use `with` for `open` (R1732) | Lint (pylint) | 30 | Consider using 'with' for resource-allocating operations | Use `with open(...)`. |
| `open` without encoding (W1514) | Lint (pylint) | 30 | Using open without explicitly specifying an encoding | Add `encoding="utf-8"`. |
| Use `with` for `open` (R1732) | Lint (pylint) | 37 | Consider using 'with' for resource-allocating operations | Use `with open(...)`. |
| `open` without encoding (W1514) | Lint (pylint) | 37 | Using open without explicitly specifying an encoding | Add `encoding="utf-8"`. |
| Unused Import (F401, W0611) | Style / Lint | 2 | 'logging' imported but unused / Unused import logging | Remove import. |
| Use f-string (C0209) | Lint (pylint) | 13 | Formatting a regular string which could be an f-string | Convert to f-string. |
