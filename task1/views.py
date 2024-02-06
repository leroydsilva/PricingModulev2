from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PricingConfiguration
import json

@csrf_exempt
def calculate_price(request):
    # Extract parameters from the request (e.g., distance traveled, time, etc.)
    if request.method == 'POST':
        data = json.loads(request.body)
        distance = float(data.get("distance", 0))
        time = float(data.get("time",0))

        config = PricingConfiguration.objects.filter(enabled=True).first()

        base_price = config.dbp
        print("baseprice",base_price)
        additional_price = distance * config.dap
        print("additional price",additional_price)
        time_multiplier = time * config.tmf
        print("time_multiplier",time_multiplier)
        waiting_charge = time * config.wc
        print("waiting charge",waiting_charge)

        total_price = (base_price + additional_price) + time_multiplier + waiting_charge
        return JsonResponse({'price': total_price})
        # Return the calculated price as a JSON response
    return JsonResponse({'message': 'invalid-request'})
