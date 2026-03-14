# Affinity n=50 — App-facing Outputs v1 — Report Example

## Canonical ranking
- score: `E_eff`
- top_k: `10`

### Top-k (by E_eff)

| rank | node_index | student_id | E_eff | intrinsic_component | network_component |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | 49 | urn:qc:person:ulid:01KFHJVET89HH9D26B0SGFQJ2H | 1.833333333333333 | 1 | 0.8333333333333335 |
| 2 | 0 | urn:qc:person:ulid:01KFHJVET7C3NPVJJASQ6XBHNS | 1.833333333333333 | 1 | 0.8333333333333333 |
| 3 | 6 | urn:qc:person:ulid:01KFHJVET8ZCCXS2Z6AD52ZE65 | 1.833333333333333 | 1 | 0.8333333333333333 |
| 4 | 11 | urn:qc:person:ulid:01KFHJVET7CHHWD5K7BTK7N5P1 | 1.833333333333333 | 1 | 0.8333333333333333 |
| 5 | 48 | urn:qc:person:ulid:01KFHJVET8RCSK1ERH54T5KXMM | 1.833333333333333 | 1 | 0.8333333333333333 |
| 6 | 1 | urn:qc:person:ulid:01KFHJVET7FCS04EY72A91H291 | 1.833333333333333 | 1 | 0.833333333333333 |
| 7 | 2 | urn:qc:person:ulid:01KFHJVET87QPW012QEP4K876X | 1.833333333333333 | 1 | 0.833333333333333 |
| 8 | 3 | urn:qc:person:ulid:01KFHJVET830R2DFB3X062V2Q9 | 1.833333333333333 | 1 | 0.833333333333333 |
| 9 | 4 | urn:qc:person:ulid:01KFHJVET856H2A0RVBC0SZSZ2 | 1.833333333333333 | 1 | 0.833333333333333 |
| 10 | 5 | urn:qc:person:ulid:01KFHJVET802Q3ZCEM1ZGMPWTG | 1.833333333333333 | 1 | 0.833333333333333 |

## Explanation field example (single student)

```json
{
  "node_index": 49,
  "student_id": "urn:qc:person:ulid:01KFHJVET89HH9D26B0SGFQJ2H",
  "s": 1.0,
  "v": 0.8333333333333334,
  "E": 1.8333333333333335,
  "E_eff": 1.8333333333333335,
  "explanation": {
    "intrinsic_component": 1.0,
    "network_component": 0.8333333333333335,
    "formula": "E_eff = beta0*s + beta1*(rho \u2299 v)"
  }
}
```
