from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import File
import boto3
import io
s3 = boto3.client(
    's3',
    aws_access_key_id = settings.AWS_S3_ACCESS_KEY_ID, 
    aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY,
)
# to upload from local storage, use below
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

# # api book list view
# @api_view(["GET"])
# def get_book_list(request):
#     if request.method == "GET":
#         book_list = [BookSerializer(
#             item).data for item in Books.objects.all().order_by("domain")]
#         return Response(book_list, status=status.HTTP_200_OK)