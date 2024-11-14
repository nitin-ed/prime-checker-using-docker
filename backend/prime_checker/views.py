from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
@api_view(['POST'])
def check_prime(request):
    print("Request received at check_prime")
    
    # Ensure 'number' is in the request data
    try:
        number = request.data.get('number')
        if number is None:
            return Response({'error': 'Number is required'}, status=400)
        
        number = int(number)  # Convert to int
        
        # Prime-checking logic
        if number < 2:
            is_prime = False
        else:
            is_prime = all(number % i != 0 for i in range(2, int(number**0.5) + 1))

        # Send back the result
        return Response({'is_prime': is_prime})

    except (ValueError, TypeError):
        return Response({'error': 'Invalid number'}, status=400)
