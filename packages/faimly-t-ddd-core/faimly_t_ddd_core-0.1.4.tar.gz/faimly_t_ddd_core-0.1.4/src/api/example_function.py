import azure.functions as func
import logging

example_func = func.Blueprint()

@example_func.route(route="get_example_func", auth_level=func.AuthLevel.FUNCTION)
def get_example_func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Create a response
    response = func.HttpResponse(
        "Welcome to Azure Functions!",
        status_code=200,
        mimetype="text/plain; charset=utf-8"
    )
    
    return response
