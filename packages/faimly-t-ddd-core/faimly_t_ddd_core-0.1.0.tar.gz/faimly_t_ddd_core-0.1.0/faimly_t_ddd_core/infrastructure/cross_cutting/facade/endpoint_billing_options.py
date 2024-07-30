from pydantic import BaseModel

class EndPointsPaymentBillingOptions(BaseModel):
    http_endpoint: str
    api_header: str
    api_key: str

    class Config:
        fields = {
            'http_endpoint': 'HttpEndpoint',
            'api_header': 'ApiHeader',
            'api_key': 'ApiKey',
        }