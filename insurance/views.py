from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, \
    DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import PersonificationFilter, HospitalFilter, \
    ProfessionFilter
from .models import Insurer, Personification, Hospital,\
    Profession


# Mixin для передачи url как дополнительный параметр
class UrlMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.request.GET.get('url', None)
        return context


class InsurerListView(LoginRequiredMixin, ListView):
    model = Insurer
    context_object_name = 'insurers'
    template_name = 'insurer/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insurer'] = self.kwargs.get('insurer', None)
        return context


class InsurerMixin(LoginRequiredMixin):

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(insurer=self.kwargs.get('insurer'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insurers'] = Insurer.objects.all()
        context['insurer_id'] = self.kwargs.get('insurer', None)
        return context


class InsurerEditMixin(object):

    def form_valid(self, form):
        form.instance.insurer = get_object_or_404(
            Insurer, pk=self.kwargs.get('insurer'))
        return super().form_valid(form)


class PersonificationMixin(InsurerMixin):
    model = Personification
    fields = ['last_name', 'first_name', 'patronymic',
              'iin', 'gender', 'profession']

    def get_success_url(self):
        return reverse_lazy('insurance:personification_list',
                            kwargs={'insurer': self.kwargs.get('insurer')})


class PersonificationEditMixin(
        PersonificationMixin, InsurerEditMixin, UrlMixin):
    template_name = 'personification/form.html'


class PersonificationListView(PersonificationMixin, ListView):
    template_name = 'personification/list.html'
    context_object_name = 'personifications'
    paginate_by = 5

    def get_queryset(self):
        qs = self.model.objects.all()
        personification_filtered_list = PersonificationFilter(
            self.request.GET, queryset=qs)
        return personification_filtered_list.qs


class PersonificationCreateView(PersonificationEditMixin, CreateView):
    pass


class PersonificationUpdateView(PersonificationEditMixin, UpdateView):
    pass


class PersonificationDeleteView(PersonificationMixin, UrlMixin, DeleteView):
    template_name = 'personification/delete.html'


class HospitalMixin(LoginRequiredMixin):
    model = Hospital
    fields = ['title', 'address', 'email', 'phone',
              'city', 'bin']

    def get_success_url(self):
        return reverse_lazy('insurance:hospital_list')


class HospitalEditMixin(HospitalMixin, UrlMixin):
    template_name = 'hospital/form.html'


class HospitalListView(HospitalMixin, ListView):
    template_name = 'hospital/list.html'
    context_object_name = 'hospitals'
    paginate_by = 5

    def get_queryset(self):
        qs = self.model.objects.all()
        hospital_filtered_list = HospitalFilter(
            self.request.GET, queryset=qs)
        return hospital_filtered_list.qs


class HospitalCreateView(HospitalEditMixin, CreateView):
    pass


class HospitalUpdateView(HospitalEditMixin, UpdateView):
    pass


class HospitalDeleteView(HospitalMixin, UrlMixin, DeleteView):
    template_name = 'hospital/delete.html'


class ProfessionMixin(LoginRequiredMixin):
    model = Profession
    fields = ['title']

    def get_success_url(self):
        return reverse_lazy('insurance:profession_list')


class ProfessionEditMixin(ProfessionMixin, UrlMixin):
    template_name = 'profession/form.html'


class ProfessionListView(ProfessionMixin, ListView):
    template_name = 'profession/list.html'
    context_object_name = 'professions'
    paginate_by = 5

    def get_queryset(self):
        qs = self.model.objects.all()
        profession_filtered_list = ProfessionFilter(
            self.request.GET, queryset=qs)
        return profession_filtered_list.qs


class ProfessionCreateView(ProfessionEditMixin, CreateView):
    pass


class ProfessionUpdateView(ProfessionEditMixin, UpdateView):
    pass


class ProfessionDeleteView(ProfessionMixin, UrlMixin, DeleteView):
    template_name = 'profession/delete.html'
