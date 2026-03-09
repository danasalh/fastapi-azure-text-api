import requests as req

def call_text_analytics_api(headers, document, endpoint):

    url = "https://YOUR-ENDPOINT.cognitiveservices.azure.com/text/analytics/v3.0/" + endpoint

    response = req.post(
        url,
        headers=headers,
        json=document
    )

    return response.json()