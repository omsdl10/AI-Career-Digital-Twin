from pydantic import BaseModel, ValidationError

class ResponseModel(BaseModel):
    answer: str
    confidence: float

def validate_output(answer, sources):
    confidence = min(1.0, len(sources) / 3)

    try:
        response = ResponseModel(
            answer=answer,
            confidence=confidence
        )
        return response
    except ValidationError:
        return ResponseModel(answer="Invalid output", confidence=0.0)