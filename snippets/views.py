from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request, format= None):
    """
    List all snippets, or create a new one.
    """
    try:
        if request.method == 'GET':
            snippets = Snippet.objects.all()
            serializer = SnippetSerializer(snippets, many = True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = SnippetSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message":"Internal Error", "error": str(e)}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk,format= None):
    """
    Retreive, Update or Delete a snippet.
    """
    try:
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

    
        if request.method == 'GET':
            serializer = SnippetSerializer(snippet)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = SnippetSerializer(snippet, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            snippet.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)

    except Exception as e:
            return Response({"message":"Internal Error", "error": str(e)}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)





