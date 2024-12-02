from django.shortcuts import redirect

class EnforcePasswordChangeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Logic for enforcing password change goes here
        if request.user.is_authenticated and hasattr(request.user, 'employee'):
            if not request.user.employee.password_changed:
                return redirect('/employee/change_password/')
        return self.get_response(request)