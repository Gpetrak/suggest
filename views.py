from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from crete_gis.suggest.forms import SuggestForm
from crete_gis.suggest.models import Suggestion
from django.template import RequestContext
from django.http import HttpResponse

class SuggestView(FormView):
    # template that is rendered when the form is valid
    template_name = 'suggest/suggestResults.html'

    form_class = SuggestForm
    
    def get(self, request):
        return render_to_response('suggest/suggest.html', RequestContext(request))

    def form_valid(self, form):
        # Get data
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        organization = form.cleaned_data['organization']
        area = form.cleaned_data['area']
        email = form.cleaned_data['email']
        date = form.cleaned_data['date']
        suggestion = form.cleaned_data['suggestion']

        e1 = Suggestion(
                 first_name = first_name,
                 last_name = last_name,
                 organization = organization,
                 area = area,
                 email = email,
                 date = date,
                 suggestion = suggestion,
                )


        e1.save()
        # check if e1 saved
        if e1.pk is None:
            result = 'failed'
            return self.render_to_response({
                'result': result
                })
        else:
            result = 'success'
            return self.render_to_response({
                'result': result
                })

    #def form_invalid(self, form):
    #    return HttpResponse(form.errors)
