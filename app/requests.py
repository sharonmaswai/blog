# import urllib.request, json
# from .models import Quote

# api_key = None

# def configure_request(app):
#     global api_key
#     api_key = app.config['QUOTES_API_KEY']

# def display_random_quote():
    
#     with urllib.request.urlopen(api_key) as url:
#         quote_raw_data = url.read()
#         quote_json = json.loads(quote_raw_data)
#         quote_results = None
#         if quote_json:
#             quote_item = quote_json
#             quote_result = process_quotes(quote_item)
#     return quote_results

# def process_quotes(source_list):
    
#     quotes = []
#     quote = source_list['quote']
#     author = source_list['author']
#     new_quote = Quote(quote, author)
#     print('PROCESSED QUOTE',new_quote)
#     quotes.append(new_quote)
#     return quotes
