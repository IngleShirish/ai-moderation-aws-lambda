from fastapi import FastAPI
from app.models import CommentRequest
from app.moderation.pipeline import moderate_pipeline
from mangum import Mangum

app = FastAPI()


@app.get("/")
def health():
    return {"status": "moderation service running"}


@app.post("/moderate")
def moderate(req: CommentRequest):

    result = moderate_pipeline(req)

    if req.comment_id:
        result["comment_id"] = req.comment_id

    return result

# -------------------------
# Lambda handler via Mangum
# -------------------------


# This is the handler Lambda will use
handler = Mangum(app)