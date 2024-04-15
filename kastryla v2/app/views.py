"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {

        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {

        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {

        }
    )

# Django view ��� �������� CITRUS
def CITRUS(request):
    """Renders the CITRUS page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/CITRUS.html',
        {
            # ����� ����� ���� �������� ����������� ������, ���� ��� ����������
        }
    )
def order(request):
    """Renders the order page."""
    assert isinstance(request, HttpRequest)
    product_name = request.GET.get('product', '')  # �������� �������� ������ �� ���������� �������
    return render(
        request,
        'app/order.html',
        {
            'product_name': product_name  # �������� �������� ������ � ��������
        }
    )
def MEAT_GRINDER_FLEISCHWOLF(request):
    """Renders the CITRUS page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/meat.html',
        {
            # ����� ����� ���� �������� ����������� ������, ���� ��� ����������
        }
    )
def NUT_TART(request):
    """Renders the CITRUS page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/nut.html',
        {
            # ����� ����� ���� �������� ����������� ������, ���� ��� ����������
        }
    )
def ZERKIENERER_CHOPPER(request):
    """Renders the CITRUS page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/chopper.html',
        {
            # ����� ����� ���� �������� ����������� ������, ���� ��� ����������
        }
    )
def JUICE_EXTRACTOR(request):
    """Renders the CITRUS page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/juice.html',
        {
            # ����� ����� ���� �������� ����������� ������, ���� ��� ����������
        }
    )
def MEAT_GRINDER_FLEISHWOLF_2(request):
    """Renders the CITRUS page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/grinder.html',
        {
            # ����� ����� ���� �������� ����������� ������, ���� ��� ����������
        }
    )

