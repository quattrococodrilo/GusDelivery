# DRF
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

# Utils
import csv
import io

class FileUploadView(APIView):
    """ Permite cargar un archivo CSV. """

    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_uploaded = request.data['file']

        file_data = file_uploaded.chunks()

        for chunk in file_data:
            chunk_decoded = chunk.decode('ISO-8859-1')
            csv_reader = csv.reader(io.StringIO(chunk_decoded), delimiter='|')
            rows = [row for row in csv_reader]
            print(rows)
            

        #file_data = file_uploaded.read().decode('ISO-8859-1')
        #csv_reader = csv.reader(io.StringIO(file_data), delimiter='|')
        ##csv_reader = csv.DictReader(io.StringIO(file_data))
        #rows = [row for row in csv_reader]
             
        #print(rows[6])

        return Response(status=204)
