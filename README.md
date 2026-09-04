# IPIntel

> Small, practical IPv4 and IPv6 utilities for local tooling.

IPIntel provides helpers for parsing, classifying, and formatting IP addresses without requiring a network service.

## Highlights

- IPv4 and IPv6 parsing
- Address classification
- Normalized formatting
- Useful primitives for network tooling
- Local, dependency-light processing

## Example

```python
from ipintel import classify

print(classify("192.168.1.10"))
```

## Use Cases

- Network utilities
- Address validation
- Configuration tooling
- Diagnostics
- Building higher-level networking applications

## Design

```text
raw address
     ↓
   parse
     ↓
 classify / normalize
     ↓
 structured result
```

IPIntel works on address data supplied to it. It does not perform network discovery or remote scanning.

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
