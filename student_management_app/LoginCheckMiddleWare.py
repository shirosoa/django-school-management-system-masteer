from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse

class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        allowed_modules = {
            '1': 'student_management_app.HodViews',
            '2': 'student_management_app.StaffViews',
            '3': 'student_management_app.StudentViews',
        }
        allowed_paths = [
            'student_management_app.views',
            'django.views.static',
        ]

        user = request.user

        # Redirect if user is not authenticated
        if not user.is_authenticated:
            if request.path not in [reverse("login"), reverse("doLogin")]:
                return redirect("login")
            return None

        # Check user type and module access
        if user.user_type in allowed_modules:
            if modulename not in allowed_modules[user.user_type] and modulename not in allowed_paths:
                return redirect(f"{user.user_type.lower()}_home")
        else:
            return redirect("login")

        return None
