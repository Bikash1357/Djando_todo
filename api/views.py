import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import UserContact


@csrf_exempt
@require_http_methods(["POST"])
def submit_user(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body."}, status=400)

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()

    if not name:
        return JsonResponse({"error": "Name is required."}, status=400)
    if not email:
        return JsonResponse({"error": "Email is required."}, status=400)

    if UserContact.objects.filter(email=email).exists():
        return JsonResponse({"error": "Email already exists."}, status=409)

    user = UserContact.objects.create(name=name, email=email)
    return JsonResponse({
        "message": "User created successfully.",
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "created_at": user.created_at.isoformat(),
        }
    }, status=201)


@require_http_methods(["GET"])
def get_users(request):
    users = UserContact.objects.all()
    data = [
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "created_at": u.created_at.isoformat(),
        }
        for u in users
    ]
    return JsonResponse({"count": len(data), "data": data}, status=200)
