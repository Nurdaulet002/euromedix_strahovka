from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, \
    DeleteView
from .filters import DrugFilter
from .models import Drug


# Mixin для передачи url как дополнительный параметр
class UrlMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.request.GET.get('url', None)
        return context


class DrugMixin(LoginRequiredMixin):
    model = Drug
    fields = ['title', 'code']

    def get_queryset(self):
        insurance = self.request.user.profile.insurance
        qs = super().get_queryset()
        qs_filter = qs.filter(
            Q(insurance=insurance) | Q(insurance__isnull=True))
        drug_filtered_list = DrugFilter(
            self.request.GET, queryset=qs_filter)
        return drug_filtered_list.qs

    def get_success_url(self):
        return reverse_lazy('drug:drug_list')


class DrugEditMixin(DrugMixin, UrlMixin):
    template_name = 'drug/form.html'

    def form_valid(self, form):
        insurance = self.request.user.profile.insurance
        form.instance.insurance = insurance
        return super().form_valid(form)


class DrugListView(DrugMixin, ListView):
    template_name = 'drug/list.html'
    context_object_name = 'drugs'
    paginate_by = 5


class DrugCreateView(DrugEditMixin, CreateView):
    pass


class DrugUpdateView(DrugEditMixin, UpdateView):
    pass


class DrugDeleteView(DrugMixin, UrlMixin, DeleteView):
    template_name = 'service/delete.html'
