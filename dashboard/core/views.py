from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)



class Login(View):
    template = 'login.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/password')
        else:
            return render(request, self.template, {'form': form}) 

class Index(LoginRequiredMixin, View):
    template = 'index.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template)