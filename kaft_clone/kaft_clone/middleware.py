def session_check_middleware(get_response):
    def middleware(request):
        if not request.session.session_key:
            request.session.save()
        
        print(f"SESSION KEY:{request.session.session_key}")
        response = get_response(request)

        return response

    return middleware