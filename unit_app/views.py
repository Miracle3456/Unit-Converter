from django.views.generic import TemplateView , FormView
from .forms import UnitForm


class UnitView(FormView):
    form_class = UnitForm
    template_name = 'index.html'

    def form_valid(self, form):
        result = form.CalculateUnit()
        return self.render_to_response(self.get_context_data(form = form , result = result))
