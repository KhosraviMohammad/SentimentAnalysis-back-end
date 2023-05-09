from rest_framework.decorators import api_view
from rest_framework.response import Response

from SentimentAnalysis.serializers import TextSerializer
from generic import funcs as g_funcs
from generic.funcs import api_view_serializer_class


@api_view_serializer_class(TextSerializer)
@api_view(['POST'])
def analyze_text(request):
    '''
    analyze text.
    '''
    text_serializer = TextSerializer(data=request.data)
    text_serializer.is_valid(raise_exception=True)
    result = g_funcs.analyze_sentiment(text_serializer.data.get('text'))
    return Response(data={'result': result})
