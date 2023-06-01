# from django.core.cache import cache
# from django.shortcuts import render
# import requests

# def say_hello(request):
#     key = 'httpbin_result'
#     if cache.get(key) is None:
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         cache.set(key, data)
#     return render(request, "hello.html", {"name": cache.get(key)})


from django.core.cache import cache
from django.shortcuts import render
import requests
from json.decoder import JSONDecodeError

def say_hello(request):
    key = 'httpbin_result'
    cached_data = cache.get(key)
    if cached_data is None:
        try:
            response = requests.get('https://httpbin.org/delay/2')
            response.raise_for_status()  # Check for request errors
            data = response.json()
            cache.set(key, data)
        except (requests.RequestException, JSONDecodeError) as e:
            # Handle the error gracefully
            data = None  # or any other default value or error message
    else:
        data = cached_data

    return render(request, "hello.html", {"name": data})
