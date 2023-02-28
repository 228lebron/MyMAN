import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import base64
from io import BytesIO
import openpyxl
from .models import Quota, Part, Request, RequestQuotaResult

def create_quotas_from_xlsx(file):
    wb = openpyxl.load_workbook(file)
    ws = wb.active

    quotas = []
    for row in ws.iter_rows(values_only=True):
        part_number, brand, quantity, price, datecode, lead_time, supplier, date = row
        try:
            part = Part.objects.get(number=part_number, brand=brand)
        except Part.DoesNotExist:
            part = Part.objects.create(number=part_number, series=f"Введите серию {part_number[:6]}", brand=brand)
        quotas.append(Quota(part=part, quantity=quantity, price=price, datecode=datecode, supplier=supplier,
                            lead_time=lead_time, date=date))
    Quota.objects.bulk_create(quotas)

def get_price_data(part):
    quotas = Quota.objects.filter(part=part)
    requests = Request.objects.filter(part=part)
    prices = []
    suppliers = []
    dates = []
    lead_times = []
    quantity = []
    for quota in quotas:
        prices.append(float(quota.price))
        dates.append(quota.date)
        suppliers.append(quota.supplier)
        lead_times.append(quota.lead_time)
        quantity.append(quota.quantity)
    return prices, dates, suppliers, lead_times, quantity

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y, title, xlabel, ylabel):
    plt.switch_backend('AGG')
    plt.figure(figsize=(9,5))
    plt.title(title)
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_box_plot(x, title):
    plt.switch_backend('AGG')
    plt.figure(figsize=(9,5))
    plt.title(title)
    plt.boxplot(x)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_bar(x, y, title, ylabel, xlabel):
    plt.switch_backend('AGG')
    plt.figure(figsize=(9, 5))
    plt.title(title)
    plt.bar(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    graph = get_graph()
    return graph



