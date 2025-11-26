from pydantic import BaseModel, Field, model_validator

class MetricConfig(BaseModel):
    name: str
    threshold: float = 0.7
    parameters: dict[str, any] = {}

class EvaluationRequest(BaseModel):
    #
    metrics: list[MetricConfig]