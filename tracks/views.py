from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Track

def track_view(request, title):
	# try:
	# 	track = Track.objects.get(title = title)
	# except Track.DoesNotExist:
	# 	raise Http404

	# track = get_object_or_404(Track, title = title)
	# return HttpResponse('Ok')

	track = get_object_or_404(Track, title = title)
	return render(request, 'track.html', {'track':track})
