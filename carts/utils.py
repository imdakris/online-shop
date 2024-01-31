from carts.models import Cart


def get_user_carts(request):
    """
    Get the shopping carts associated with the current user or session.

    Parameters:
        - request: HttpRequest object.

    Returns:
        QuerySet: A QuerySet of Cart objects.

    If the user is authenticated, the function returns the shopping carts associated with that user.
    If the user is not authenticated, it checks for a session key. If no session key exists, it creates one.
    The function then returns the shopping carts associated with the session.

    Example:
    ```python
    user_carts = get_user_carts(request)
    ```
    """
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    
    if not request.session.session_key:
        request.session.create()

    return Cart.objects.filter(session_key=request.session.session_key)

