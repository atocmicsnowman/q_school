from django.shortcuts import redirect


def redirect_to_user_page(request):
    if hasattr(request, "user") and hasattr(getattr(request, "user"), "pax"):
        return redirect('member_management', user_id=request.user.id)
    return redirect("/admin")

