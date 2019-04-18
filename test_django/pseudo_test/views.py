from django.http import HttpResponse
from django.shortcuts import render
import boto3    

def send_answer(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        if (uploaded_file.name[-4:] == ".txt" or uploaded_file.name[-4:] == ".pdc"
            ) and uploaded_file.size < 1000000:
            s3 = boto3.resource('s3')
            s3.Bucket('pseudocodetester').put_object(Key='test.jpg', Body=uploaded_file)

    return render(request, 'pseudo_test/send_answer.html')