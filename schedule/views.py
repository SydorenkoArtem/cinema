from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from schedule.forms import TicketForm
from schedule.models import Schedule


class ScheduleListView(ListView):
    """Schedule list view implementation"""
    http_method_names = ["head", "options", "get"]
    model = Schedule
    template_name = "schedule/schedule_list.html"


class TicketCreateView(LoginRequiredMixin, CreateView):
    """Ticket create view implementation"""

    form_class = TicketForm
    http_method_names = ['get', 'post']
    template_name = "schedule/ticket_form.html"
    success_url = "list"

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super(TicketCreateView, self).form_valid(form)
