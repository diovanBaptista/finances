from djoser.email import PasswordResetEmail
from django.conf import settings
from urllib.parse import urlparse, urljoin

class CustomPasswordResetEmail(PasswordResetEmail):
    template_name = "djoser/email/password_reset.html"
    
    def get_context_data(self):
        context = super().get_context_data()
        
        original_url = context.get("url")
        parsed_url = urlparse(original_url)
        path = parsed_url.path
        
        context["url"] = urljoin(settings.SITE_URL, path.lstrip("/"))
        
        print("URL final no email:", context["url"])
        
        return context
