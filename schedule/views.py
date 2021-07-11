import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from schedule.forms import TicketForm, ScheduleForm, HallForm
from schedule.models import Schedule, Ticket
from user.models import UserProfile


class ScheduleListView(ListView):
    """Schedule list view implementation"""
    http_method_names = ["head", "options", "get", "post"]
    model = Schedule
    template_name = "schedule/schedule_list.html"

    def get_queryset(self):
        """Return a queryset for a list view"""

        queryset = Schedule.objects.filter(date_show=datetime.datetime.today()).filter(start_time__gte=datetime.datetime.now())

        return queryset


class ScheduleCreateView(CreateView):
    """Schedule create view implementation"""

    model = Schedule
    template_name = "schedule/schedule_form.html"
    form_class = ScheduleForm
    success_url = "film:list"

    def form_valid(self, form):
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            date_show = start_date
            day_count = (end_date - start_date).days
            for i in range(day_count + 1):
                obj = Schedule()
                obj.start_date = start_date
                obj.end_date = end_date
                obj.start_time = form.cleaned_data['start_time']
                obj.end_time = form.cleaned_data['end_time']
                obj.hall = form.cleaned_data['hall']
                obj.film = form.cleaned_data['film']
                obj.price = form.cleaned_data['price']
                obj.date_show = date_show
                obj.save()
                date_show += datetime.timedelta(days=1)
        return redirect('film:list')


class HallCreateView(CreateView):
    """Hall create view implementation"""
    form_class = HallForm
    http_method_names = ['get', 'post']
    template_name = "schedule/hall_form.html"
    success_url = "schedule:hall"


class TicketCreateView(LoginRequiredMixin, CreateView):
    """Ticket create view implementation"""

    form_class = TicketForm
    http_method_names = ['get', 'post']
    template_name = "schedule/ticket_form.html"
    success_url = "/"
    model = Ticket

    def form_valid(self, form):
        if form.is_valid():
            form.instance.customer = self.request.user
            balance = UserProfile.objects.get(user=form.instance.customer).balance
            total = form.instance.quantity * form.instance.schedule.price
            if total > balance:
                redirect_url = reverse_lazy("schedule:ticket")
                return HttpResponseRedirect(redirect_url)
        return super(TicketCreateView, self).form_valid(form)


class TicketUserView(LoginRequiredMixin, ListView):
    """Ticket of user view implementation"""

    model = Ticket
    http_method_names = ['get']
    template_name = "schedule/ticket_user.html"

    def get_queryset(self):
        queryset = super(TicketUserView, self).get_queryset()

        return queryset.filter(customer=self.request.user)





