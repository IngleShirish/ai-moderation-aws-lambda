from app.prompts.stage3_prompt import STAGE3_PROMPT
from app.bedrock.client import invoke_model
from app.bedrock.parser import extract_json


def run_stage3(req):

    prompt = STAGE3_PROMPT.format(
        headline=req.headline,
        summary=req.summary or "",
        comment=req.comment
    )

    body = {
        "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        "inferenceConfig": {
            "temperature": 0,
            "maxTokens": 200
        }
    }

    response = invoke_model(body)

    text = response["output"]["message"]["content"][0]["text"]

    parsed = extract_json(text)

    if parsed:
        parsed["stage"] = "ai_context"
        return parsed

    return {
        "safe": False,
        "category": "unknown",
        "severity": "medium",
        "confidence": 0.5,
        "reason": "invalid model response",
        "stage": "ai_context"
    }