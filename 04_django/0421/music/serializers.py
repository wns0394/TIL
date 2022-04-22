from rest_framework import serializers
from . models import Artist, Music


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name', )


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    # 이 가수가 가지고 있는 음악 정보
    # music_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    music_set = MusicSerializer(many=True, read_only=True)
    # 음악 정보 개수
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'