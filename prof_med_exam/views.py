from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, \
    DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Harm
from .filters import HarmFilter


class HarmMixin(LoginRequiredMixin):
    model = Harm
    fields = ['title']

    def get_success_url(self):
        return reverse_lazy('prof_med_exam:harm_list')


class HarmEditMixin(HarmMixin):
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


class HarmDeleteView(HarmMixin, DeleteView):
    template_name = 'harm/delete.html'
