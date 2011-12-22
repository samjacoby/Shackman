from btype.models import Typeface, Variant
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import simplejson
import random
import string

def update(request):
	t = TypefacePackage()
	params = { 'typefaces_list': t.typefaces,
	    'question': t.selected.typeface.name, 
	    'file_url': t.file_url }
	return render_to_response('btype/index.html', 
	    params,
	    context_instance=RequestContext(request))


class TypefacePackage:
    def __init__(self, parent=None):
        case = ['u']
        random_case = random.choice(case)
        # Select four random typefaces that share the same param.
        self.typefaces = Variant.objects.all().filter(case__startswith=random_case).order_by('?')[:4]
        self.selected = random.choice(self.typefaces)
        # Build a random case/letter file locator 
        self.file_url = random_case + "_" + random.choice(string.ascii_lowercase)

