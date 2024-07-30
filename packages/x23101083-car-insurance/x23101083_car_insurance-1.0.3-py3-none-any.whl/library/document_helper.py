from .exception.document_exception import DocumentException
class DocumentHelper():
    def upload(file, name, s3):
        if file is None:
            raise DocumentException("File is required")
        if name is None:
            raise DocumentException("Username is required")
        if s3 is None:
            raise DocumentException("S3 object is required")
        filename = name.username+"_picture.jpg"
        image_data = file
        try:
            object = s3.Object('x23101083-carinsurance', filename)
            val = object.put(ACL='public-read',Body=image_data,Key=filename)
            print('response from document upload: ', val)
            return filename
        except Exception as e:
            raise DocumentException("Error uploading image to s3")
        
    def upload_image_to_s3(requests, data, file):
        files = {'file':file.read()}
        response = requests.post(data['url'], data = data['fields'],files= files)
        if response.status_code == 200 or response.status_code== 204:
            return 'Image Uploaded successfully'
        else:
            raise DocumentException("Unable to upload profile picture")

    def get_presigned_url(requests, AWS_IMAGE_API_URL):
        response = requests.post(AWS_IMAGE_API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            raise DocumentException("Unable to upload profile image")