from functools import wraps
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def user_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if not request.user.is_active:
            return render(request, "login_usuario.html")
        return view_func(request, *args, **kwargs)
    return wrapper

def operator_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if not request.user.is_active:
            return render(request, "login_operador.html")
        return view_func(request, *args, **kwargs)
    return wrapper

def rol_requerido(rol_requerido):

    def decorator(view_func):
        @wraps(view_func)

        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.rol == rol_requerido:
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'error.html')
        return _wrapped_view
    return decorator


def operador_required(view_func):
    """
    Decorador para requerir que un usuario tenga el rol de "operador"
    para poder acceder a una vista específica.
    """
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.rol != 'operador':
            # Si el usuario no ha iniciado sesión o no tiene el rol de operador,
            # redirigir a una página de acceso denegado o cualquier otra página deseada
            return redirect('acceso_denegado')
        else:
            # Si el usuario tiene el rol de operador, mostrar la página solicitada
            return view_func(request, *args, **kwargs)

    return wrapper