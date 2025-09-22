import string 
import secrets
from .models import Coupon

def generate_couponcode(lenght=10):

    chartacters = string.ascii_uppercase + string.digits

    while True:
        code ''.join(secrets.choice(chartacters) for _ in range(lenght))


        if not Coupon.objects.filter(code=code).exits():

            return code