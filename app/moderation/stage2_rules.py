import json
from app.prompts.stage2_prompt import  STAGE2_PROMPT
from app.bedrock.client import invoke_model
from app.bedrock.parser import extract_json


def run_stage2(req):

    prompt = STAGE2_PROMPT.format(
        headline=req.headline,
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
            "maxTokens": 150
        }
    }

    response = invoke_model(body)

    text = response["output"]["message"]["content"][0]["text"]

    parsed = extract_json(text)

    if parsed:
        parsed["stage"] = "ai_basic"
        return parsed

    return {
        "safe": False,
        "category": "unknown",
        "severity": "medium",
        "confidence": 0.5,
        "reason": "invalid model response",
        "stage": "ai_basic"
    }