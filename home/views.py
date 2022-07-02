from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import json
import random
from .forms import FeedbackForm
f = open('/Users/arshkumar/Desktop/IIT_INTERN/home/static/mscoco_val2014_annotations.json')
data = json.load(f)
q = open('/Users/arshkumar/Desktop/IIT_INTERN/home/static/OpenEnded_mscoco_val2014_questions.json')
dataq = json.load(q)
dictq = {}
for i in dataq['questions']:
    dictq[i['question_id']] = i['question']

f.close()
q.close()

def home(request):
    if request.user.is_authenticated:
        i = random.randint(0, len(data['annotations']) - 1)
        if request.method == 'POST':

            form = FeedbackForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.question_id = data['annotations'][i]['question_id']
                obj.image_id = data['annotations'][i]['image_id']
                obj.initial_answer = data['annotations'][i]['answers'][0]['answer']

                obj.save()
                return render(request, 'home.html', {'hell': 'images/1.png',  # boilerplate put location of img
                                                     'q': dictq[data['annotations'][i]['question_id']],
                                                     'a': data['annotations'][i]['answers'][0]['answer'],

                                                     'form': form
                                                     }
                              )
        else:
            form = FeedbackForm()
        return render(request, 'home.html', {'hell': 'images/1.png',  # boilerplate
                                             'q': dictq[data['annotations'][i]['question_id']],
                                             'a': data['annotations'][i]['answers'][0]['answer'],
                                             'form': form
                                             }
                      )
    else:
        return HttpResponseRedirect('accounts/login/')
