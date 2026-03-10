from app.moderation.stage1_rules import run_stage1
from app.moderation.stage2_rules import run_stage2
from app.moderation.stage3_rules import run_stage3


def moderate_pipeline(req):

    # Stage 1
    stage1 = run_stage1(req.comment)

    if stage1["unsafe"]:
        return {
            "safe": False,
            "category": "rule_violation",
            "severity": "high",
            "confidence": 1.0,
            "reason": stage1["reason"],
            "stage": "rules"
        }

    # Stage 2
    stage2 = run_stage2(req)

    if stage2["safe"] is False:
        return stage2

    if stage2["confidence"] > 0.8:
        return stage2

    # Stage 3
    return run_stage3(req)