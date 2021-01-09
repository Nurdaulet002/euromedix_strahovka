from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.admin.options import get_content_type_for_model
from django.http import JsonResponse
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, \
    DeleteView
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import ServiceFilter, HarmFilter
from .models import Tariffication, Service, Harm,\
    Regiment, ServiceRegiment, ServiceHarm
from .forms import ServiceGroupForm
from insurance.models import Insurer, Hospital


# Mixin для передачи url как дополнительный параметр
class UrlMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.request.GET.get('url', None)
        return context


class ServiceMixin(LoginRequiredMixin):
    model = Service
    fields = ['title', 'code']

    def get_queryset(self):
        insurance = self.request.user.profile.insurance
        qs = super().get_queryset()
        qs_filter = qs.filter(
            Q(insurance=insurance) | Q(insurance__isnull=True))
        service_filtered_list = ServiceFilter(
            self.request.GET, queryset=qs_filter)
        return service_filtered_list.qs

    def get_success_url(self):
        return reverse_lazy('tariffication:service_list')


class ServiceEditMixin(ServiceMixin, UrlMixin):
    template_name = 'service/form.html'

    def form_valid(self, form):
        insurance = self.request.user.profile.insurance
        form.instance.insurance = insurance
        return super().form_valid(form)


class ServiceListView(ServiceMixin, ListView):
    template_name = 'service/list.html'
    context_object_name = 'services'
    paginate_by = 5


class ServiceCreateView(ServiceEditMixin, CreateView):
    pass


class ServiceUpdateView(ServiceEditMixin, UpdateView):
    pass


class ServiceDeleteView(ServiceMixin, UrlMixin, DeleteView):
    template_name = 'service/delete.html'


# Миксин тарификатора
class TarifficationMixin(View, LoginRequiredMixin):

    def dispatch(self, *args, **kwargs):
        self.insurance = self.request.user.profile.insurance
        self.parent = self.kwargs.get('parent', None)
        self.insurer = self.request.GET.get('insurer', None)
        self.hospital = self.request.GET.get('lpu', None)
        if not self.insurer:
            self.insurer = None
        if not self.hospital:
            self.hospital = None
        self.tariffications = Tariffication.objects.filter(
            insurance=self.insurance, parent=self.parent,
            insurer=self.insurer, hospital=self.hospital)[:10]

        def get_success_url(self):
            return reverse_lazy('tariffication:tariffication_list',
                                kwargs={'insurer': self.kwargs.get('insurer')})
        return super().dispatch(*args, **kwargs)


# Список тарификаторов
class TarifficationListView(TarifficationMixin, TemplateResponseMixin):
    template_name = 'tariffication/list.html'
    service_group_form_class = ServiceGroupForm

    def get(self, request, *args, **kwargs):
        insurers = Insurer.objects.all()
        hospitals = Hospital.objects.all()
        service_group_form = self.service_group_form_class()
        return self.render_to_response(
            {'service_group_form': service_group_form,
             'insurers': insurers, 'hospitals': hospitals,
             'parent': self.parent,
             'tariffications': self.tariffications,
             'insurer_id': self.insurer})


# Ajax тарификатора
class TarifficationAjaxView(TarifficationMixin):

    def get(self, request, *args, **kwargs):
        paginator = Paginator(self.tariffications, 5)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        return render(request, 'tariffication/list_ajax.html',
                      {'page_obj': page_obj, 'parent': self.parent})

    def post(self, request, *args, **kwargs):
        parent = None
        id = request.POST.get('id', None)
        tariffication = get_object_or_404(Tariffication, id=id)
        for obj in tariffication.get_all_children():
            if obj.parent:
                try:
                    parent = Tariffication.objects.get(
                        copied=obj.parent, insurance=self.insurance,
                        insurer_id=self.insurer, hospital_id=self.hospital)
                except Tariffication.DoesNotExist:
                    parent = None
            Tariffication.objects.create(
                insurance=self.insurance, insurer_id=self.insurer,
                base_object=obj.base_object, copied=obj, parent=parent,
                hospital_id=self.hospital
            )
        return JsonResponse({"success": True})


# Ajax тарификатора
class TarifficationAjaxUpdateView(View):

    def post(self, request):
        id = request.POST.get('id', None)
        price = request.POST.get('price', None)
        # Tariffication.objects.filter(id=id).update(price=price)
        tariffication_obj = Tariffication.objects.get(id=id)
        tariffication_obj.price = price
        tariffication_obj.save()
        return JsonResponse({"success": True})


# Сохранить группировку услуг
class ServiceGroupCreateView(View, LoginRequiredMixin, TemplateResponseMixin):
    service_group_form_class = ServiceGroupForm

    def post(self, request, *args, **kwargs):
        insurance = request.user.profile.insurance
        parent = self.kwargs.get('parent', None)
        insurer = request.POST.get('insurer', None)
        service_group_form = self.service_group_form_class(request.POST)
        if service_group_form.is_valid():
            service_group = service_group_form.save()
            self.tariffication_submit(
                request, service_group, insurance, insurer, parent)
            messages.add_message(request, messages.SUCCESS,
                                 'Группировка услуг, успешно сохранен!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Не удалось сохранить, группировку услуг!')
        if parent:
            return redirect('tariffication:tariffication_list', parent)
        return redirect('tariffication:tariffication_list')

    def tariffication_submit(self, request,
                             base_object, insurance, insurer, parent):
        return Tariffication.objects.create(
            base_object=base_object, insurance=insurance,
            insurer_id=insurer, parent_id=parent)


class ServiceAjaxView(View, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search', None)
        service_list = Service.objects.all()
        if search:
            service_list = service_list.filter(title__icontains=search)
        paginator = Paginator(service_list, 2)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        return render(request, 'service/list_ajax.html',
                      {'page_obj': page_obj})

    def post(self, request, *args, **kwargs):
        insurance = request.user.profile.insurance
        parent = self.kwargs.get('parent', None)
        id = request.POST.get('id', None)
        insurer = request.POST.get('insurer', None)
        service = get_object_or_404(Service, id=id)
        if not insurer:
            insurer = None
        try:
            Tariffication.objects.get(
                content_type=get_content_type_for_model(service),
                object_id=service.pk, insurance=insurance,
                parent_id=parent, insurer_id=insurer).delete()
        except Tariffication.DoesNotExist:
            Tariffication.objects.create(
                base_object=service, insurance=insurance,
                parent_id=parent, insurer_id=insurer)
        return JsonResponse({"success": True})


class HarmMixin(LoginRequiredMixin):
    model = Harm
    fields = ['title']

    def get_success_url(self):
        return reverse_lazy('tariffication:harm_list')


class HarmEditMixin(HarmMixin, UrlMixin):
    template_name = 'harm/form.html'


class HarmListView(HarmMixin, ListView):
    template_name = 'harm/list.html'
    context_object_name = 'harms'
    paginate_by = 5

    def get_queryset(self):
        qs = self.model.objects.all()
        harm_filtered_list = HarmFilter(
            self.request.GET, queryset=qs)
        return harm_filtered_list.qs


class HarmCreateView(HarmEditMixin, CreateView):
    pass


class HarmUpdateView(HarmEditMixin, UpdateView):
    pass


class HarmDeleteView(HarmMixin, UrlMixin, DeleteView):
    template_name = 'harm/delete.html'


# Страница пакета ОМО
class CompulsoryPackage(TarifficationMixin, TemplateResponseMixin):
    template_name = 'compulsory_package/list.html'

    def get(self, request, *args, **kwargs):
        regiment = self.kwargs.get('regiment', None)
        regiments = Regiment.objects.all()
        service_regiments = ServiceRegiment.objects.all()
        if regiment:
            service_regiments = service_regiments.filter(regiment=regiment)
        return self.render_to_response(
            {'insurers': self.insurers, 'parent': self.parent,
             'tariffications': self.tariffications, 'regiments': regiments,
             'service_regiments': service_regiments})


# Страница пакета ОПМО
class CompulsoryProfessionPackage(TarifficationMixin, TemplateResponseMixin):
    template_name = 'compulsory_profession_package/list.html'

    def get(self, request, *args, **kwargs):
        harm = self.kwargs.get('harm', None)
        insurer = request.GET.get('insurer', None)
        harms = Harm.objects.all()
        service_harms = ServiceHarm.objects.filter(
            insurance=request.user.profile.insurance).all()
        if insurer:
            service_harms = service_harms.filter(insurer=insurer)
        if harm:
            service_harms = service_harms.filter(harm=harm)
        return self.render_to_response({
            'insurers': self.insurers, 'parent': self.parent,
            'tariffications': self.tariffications,
            'harms': harms, 'service_harms': service_harms})
