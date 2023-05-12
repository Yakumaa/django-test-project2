from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage(
            "subject", "message", "from@seveneleven.com", ["user@seveneleven.com"]
        )
        message.attach_file("playground/static/images/Capture.png")
        message.send()
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Mosh"})
