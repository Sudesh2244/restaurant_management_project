from django.views.generic import ListView
from .models import Note
from django.http import HttpResponse

class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        # Return only notes belonging to the current user
        return Note.objects.filter(user=self.request.user)
from django.contrib.auth.decorators import login_required

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, "notes/note_list.html", {"notes": notes})
def home(request):
    return HttpResponse("Welcome to the Home page")