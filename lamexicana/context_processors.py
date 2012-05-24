from datetime import datetime

def default(request):
    return {
        'year':datetime.today().year,
        'product_name':'La mexicana',
    }
