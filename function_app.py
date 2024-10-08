import azure.functions as func
import logging
from util import download_html_and_upload_to_blob, download_html_and_upload_to_blob_scrapingant

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="cra_scrapingant_to_cloud")
def cra_scrapingant_to_cloud(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python CRA HTTP trigger save_to_cloud function is processing a request.')

    url = req.params.get('url')
    name = req.params.get('name')
    
    if not url or not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')
            name = req_body.get('name')

    if url and name:
        logging.info(f"Received URL: {url}")
        logging.info(f"Received Name: {name}")
        message = download_html_and_upload_to_blob_scrapingant(url, name)
        if message:
            return func.HttpResponse(message)
        return func.HttpResponse(f"Received URL: {url} and Name: {name}. This CRA HTTP triggered function executed successfully. Product is now saved to blob storage")
    else:
        return func.HttpResponse(
             "This CRA HTTP triggered function executed successfully but no arguments were provided. Pass both url and name in the query string or in the request body.",
             status_code=200
        )

@app.route(route="cra_download_to_cloud")
def cra_download_to_cloud(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python CRA HTTP trigger save_to_cloud function is processing a request.')

    url = req.params.get('url')
    name = req.params.get('name')
    
    if not url or not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')
            name = req_body.get('name')

    if url and name:
        logging.info(f"Received URL: {url}")
        logging.info(f"Received Name: {name}")
        message = download_html_and_upload_to_blob(url, name)
        if message:
            return func.HttpResponse(message)
        return func.HttpResponse(f"Received URL: {url} and Name: {name}. This CRA HTTP triggered function executed successfully. Product is now saved to blob storage")
    else:
        return func.HttpResponse(
             "This CRA HTTP triggered function executed successfully but no arguments were provided. Pass both url and name in the query string or in the request body.",
             status_code=200
        )

