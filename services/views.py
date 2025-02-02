from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView
from django.contrib import messages
from .models import Service, ServiceRequest
from .forms import ServiceRequestForm

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    paginate_by = 6

    def get_queryset(self):
        return Service.objects.filter(available=True).order_by('-created_at')

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ServiceRequestForm(initial={'service': self.object})
        return context

class ServiceRequestView(FormView):
    form_class = ServiceRequestForm
    template_name = 'services/service_request.html'

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('account_login')
        
        service_request = form.save(commit=False)
        service_request.user = self.request.user
        service_request.service = get_object_or_404(
            Service, 
            id=self.kwargs['pk']
        )
        service_request.save()
        
        messages.success(self.request, 'Your service request has been submitted!')
        return redirect('services:service_detail', pk=self.kwargs['pk'])