from rest_framework import serializers

from articles.serializers.card import CardSerializer
from .comment import CommentSerializer
from ..models import Article, Card

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)


class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    cards = CardSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
