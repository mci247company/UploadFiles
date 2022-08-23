from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import File
import boto3
import io
# upload transfer from other source in binary mode, use below
s3 = boto3.client('s3')
# to upload from local storage, use below
# s3 = boto3.resource('s3')

# def upload(request):
#     if request.method == 'POST':  
#         print(request.POST)
#         file = request.FILES['file'].read()
#         fileName= request.POST['filename']
#         print(fileName)
#         existingPath = request.POST['existingPath']
#         end = request.POST['end']
#         nextSlice = request.POST['nextSlice']
        
#         if file=="" or fileName=="" or existingPath=="" or end=="" or nextSlice=="":
#             res = JsonResponse({'data':'Invalid Request'})
#             return res
#         else:
#             if existingPath == 'null':
#                 path = 'fileUploader/media/' + fileName
#                 # path = 'media/' + fileName
#                 with open(path, 'wb+') as destination: 
#                     destination.write(file)
#                 FileFolder = File()
#                 FileFolder.existingPath = fileName
#                 FileFolder.eof = end
#                 FileFolder.name = fileName
#                 FileFolder.save()
#                 if int(end):
#                     res = JsonResponse({'data':'Uploaded Successfully','existingPath': fileName})
#                 else:
#                     res = JsonResponse({'existingPath': fileName})
#                 return res

#             else:
#                 path = 'fileUploader/media/' + fileName
#                 # path = 'media/' + existingPath
#                 model_id = File.objects.get(existingPath=existingPath)
#                 if model_id.name == fileName:
#                     if not model_id.eof:
#                         with open(path, 'ab+') as destination: 
#                             destination.write(file)
#                         if int(end):
#                             model_id.eof = int(end)
#                             model_id.save()
#                             res = JsonResponse({'data':'Uploaded Successfully','existingPath':model_id.existingPath})
#                         else:
#                             res = JsonResponse({'existingPath':model_id.existingPath})    
#                         return res
#                     else:
#                         res = JsonResponse({'data':'EOF found. Invalid request'})
#                         return res
#                 else:
#                     res = JsonResponse({'data':'No such file exists in the existingPath'})
#                     return res
#     return render(request, 'upload.html')

def upload(request):
    if request.method == 'POST':  
        print(request.POST)
        file = request.FILES['file'].read()
        fo = io.BytesIO(file)
        fileName= "demo_22082022/" + request.POST['filename']
        # fileName= "hocvien/media/svideo/" + request.POST['filename']
        if file=="" or fileName=="":
            res = JsonResponse({'data':'Invalid Request'})
            return res
        else:
            s3.upload_fileobj(fo, settings.AWS_STORAGE_BUCKET_NAME, fileName)
            # s3.upload_fileobj(fo, 'privatemcialion', fileName)
            FileFolder = File()
            FileFolder.existingPath = fileName
            FileFolder.eof = 1
            FileFolder.name = fileName
            FileFolder.save()
            res = JsonResponse({'data':'Uploaded Successfully'})
            return res
    return render(request, 'upload.html')

def upload_multiple_files(request):
    if request.method == 'POST':  
        print(request.POST)
        file = request.FILES['file'].read()
        fo = io.BytesIO(file)
        fileName= "demo_22082022/" + request.POST['filename']
        if file=="" or fileName=="":
            res = JsonResponse({'data':'Invalid Request'})
            return res
        else:
            s3.upload_fileobj(fo, settings.AWS_STORAGE_BUCKET_NAME, fileName)
            FileFolder = File()
            FileFolder.existingPath = fileName
            FileFolder.eof = 1
            FileFolder.name = fileName
            FileFolder.save()
            res = JsonResponse({'data':'Uploaded Successfully'})
            return res
    return render(request, 'upload_multiple_files.html')