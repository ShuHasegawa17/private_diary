import logging
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import InquiryForm
from .models import Diary

logger = logging.getLogger(__name__)


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy("diary:inquiry")

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, "メッセージを送信しました")
        logger.info("inquiry sent by{}".format(form.cleaned_data["name"]))
        return super().form_valid(form)


class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = "diary_list.html"
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by("-created_at")
        return diaries


class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = "diary_detail.html"
    pk_url_kwarg = "id"
