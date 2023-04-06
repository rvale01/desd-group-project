from datetime import datetime, timedelta
from django.contrib.auth import logout

# THhis 
class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated and if the session variable exists
        if request.user.is_authenticated and 'last_activity' in request.session:
            # Get the current time and the time of the user's last activity
            current_time = datetime.now()
            last_activity = datetime.strptime(request.session['last_activity'], '%Y-%m-%d %H:%M:%S')

            # Check if 20 minutes have passed since the user's last activity
            if current_time - last_activity > timedelta(seconds=1200):
                logout(request)

        # Update the last_activity session variable to the current time
        request.session['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        response = self.get_response(request)

        return response