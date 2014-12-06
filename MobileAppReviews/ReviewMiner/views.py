#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response

from ReviewMiner.Algorithm.reviewsProcessing import ReviewsProcessing
from ReviewMiner.Algorithm.categories import categories
import os

# Create your views here.
def appReview(request):
    template = loader.get_template('ReviewMiner/Home.html')
    context = RequestContext(request)
    return HttpResponse(template._render(context))


def appReviewUploadDone(request):
    #https://docs.djangoproject.com/en/1.7/topics/http/file-uploads/
    if request.method == 'POST':

        if 'file' in request.FILES:
            file1 = request.FILES['file']
            #with open('uploaded_files/ReviewMiner/Test2.csv', 'wb+') as destination:
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploaded_files/ReviewMiner/Test2.csv'), 'wb+') as destination:
            #with open('ReviewMiner/Algorithm/Test2.csv', 'wb+') as destination:
                for chunk in file1.chunks():
                    destination.write(chunk)

            categories.rating = request.POST.get('rating')

            callingClass = ReviewsProcessing()
            allReviews,allIndividualReviews = callingClass.getprocessedreviews()
            totalList = []
            chartData = {}
            chartData = [len(allReviews[0][0]),
                         len(allReviews[1][0]),
                         len(allReviews[2][0]),
                         len(allReviews[3][0]),
                         len(allReviews[4][0])]

            print(chartData)
            totalList.append(allReviews)
            totalList.append(allIndividualReviews)
            totalList.append(chartData)





            return render(request, 'ReviewMiner/Output.html', {'totalList':totalList})

        return render_to_response('ReviewMiner/Home.html')

def about(request):
    template = loader.get_template('ReviewMiner/About.html')
    context = RequestContext(request)
    return HttpResponse(template._render(context))