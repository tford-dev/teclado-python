import time
from libs.openexchange import OpenExchangeClient

APP_ID = '97894dc1419b40208bb130cde916673a'

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(end - start);

print(f"USD{usd_amount} is GBP{gbp_amount}")