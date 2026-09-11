# Mouse ATAC feature strategies

| Strategy | Compatible use | Consequence / risk | Cost |
|---|---|---|---|
| A per-stage native peaks | within-stage models | no direct cross-stage peak coordinates | LOW |
| B union peak space | shared-column models | many structural zeros; leakage if union learned from test stages | MODERATE/HIGH |
| C consensus/recalled peaks | controlled cross-stage space | requires fragment/raw evidence and calling policy | HIGH/UNKNOWN |
| D coordinate overlap mapping | interval-aware methods | many-to-many mappings and boundary loss | MODERATE |
| E gene activity | gene-shared methods | loses distal/regulatory detail; mapping assumptions | MODERATE |
| F method-native handling | MultiVI/scGLUE/Cobolt where supported | behavior and feature contract must be verified | UNKNOWN |

No strategy is selected or executed. Training-only construction is required to avoid test-stage leakage.
