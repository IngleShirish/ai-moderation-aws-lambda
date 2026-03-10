PROFANITY = ["fuck", "bitch", "idiot"]


def run_stage1(comment):

    text = comment.lower()

    for word in PROFANITY:
        if word in text:
            return {
                "unsafe": True,
                "reason": "profanity detected"
            }

    return {"unsafe": False}