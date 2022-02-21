from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
  """Test API View"""

  def get(self, request, format=None):
    """Returns a list of APIView features"""
    an_apiview = [
      "Uses HTTP methods as function (get, post, patch, put, delete)",
      "is similar to traditional django view",
      "gives you most control over you application logic",
      "is mapped manually to the URLs",
    ]
    return Response({'message': "Hello!", 'an_apiview': an_apiview})
