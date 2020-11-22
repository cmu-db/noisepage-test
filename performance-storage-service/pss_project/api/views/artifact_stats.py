from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.status import (HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST,
                                   HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED)
from rest_framework.authentication import BasicAuthentication
from pss_project.api.serializers.rest.ArtifactStatsSerializer import ArtifactStatsSerializer
from pss_project.api.serializers.database.ArtifactStatsResultSerializer import ArtifactStatsResultSerializer


class ArtifactStatsViewSet(ViewSet):

    def create(self, request):
        """
        Store new artifact stats result in the database
        """
        user = BasicAuthentication().authenticate(request)
        if user is None:
            return Response({'message': 'Forbidden'}, status=HTTP_403_FORBIDDEN)

        data = JSONParser().parse(request)
        api_serializer = ArtifactStatsSerializer(data=data)
        if not api_serializer.is_valid():
            return Response(api_serializer.errors, status=HTTP_400_BAD_REQUEST)

        api_serializer.save()
        db_serializer = ArtifactStatsResultSerializer(data=api_serializer.instance.convert_to_db_json())
        if not db_serializer.is_valid():
            return Response(db_serializer.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)
        try:
            db_serializer.save()
        except Exception as e:
            return Response({'message': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(api_serializer.validated_data, status=HTTP_201_CREATED)