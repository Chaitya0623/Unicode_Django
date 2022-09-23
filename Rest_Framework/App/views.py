from urllib import response
from django.shortcuts import render, HttpResponse
import requests

from .models import Info
from .forms import InfoForm

# Create your views here.

def home(request):
    return render(request, 'index.html')
    
def mission(request):
    import requests

    url = "https://demo.stepzen.net/studio/spacex/__graphql"

    payload="{\"query\":\"query MyQuery {\\n  spacex_missions(limit: 10) {\\n    id\\n    manufacturers\\n    name\\n  }\\n}\",\"variables\":{}}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    data = response.get('data').get('spacex_missions')

    form = InfoForm()
    mission = request.POST.get('mission_name', 'default')
    print(mission)

    if request.method == 'POST':
        print(request.POST)
        form = InfoForm(request.POST)
        if form.is_valid():
            for i in data:
                if(i['name'] == mission):
                    op1=i['manufacturers']
                    op2=i['id']
                    # cou = Info.objects.get(count=op3)
                    # cou.count = cou.count + 1
            fm = Info(mission_name=form.cleaned_data['mission_name'],manufacturers=op1,mission_id=op2)
            fm.save()

    text = Info.objects.all()

    return render(request, 'index.html',{'data':data, 'form':form, 'mission':mission, 'text':text})