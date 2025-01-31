from django.shortcuts import get_object_or_404
from Article.serializers import ArticleSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from Article.models import Article


class ArticleViewSet(viewsets.ModelViewSet):

	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

	#GET articles/ exists by default and returns the list of articles

	def create(self, request): #POST articles/ with Article object in body	
		queryset = Article.objects.all()
		try:
			Article.objects.create(article_title = request.data["article_title"], article_text = request.data["article_text"])
			return Response(status=200)
		except:
			return Response(status=400)
	

	def retrieve(self, request, pk=None): #GET articles/<id>/
		queryset = Article.objects.all()
		article = get_object_or_404(queryset, pk = pk)
		serializer = ArticleSerializer(article)
		return Response(serializer.data)

	
	def update(self, request, pk=None): #PUT articles/<id>/  with Article object in body
		queryset = Article.objects.all()
		article = get_object_or_404(queryset, pk = pk)
		try:
			article.article_title = request.data["article_title"]
			article.article_text = request.data["article_text"]
			article.save()
			return Response(status=200)
		except:
			return Response(status=400)

	def destroy(self, request, pk=None): #DELETE articles/<id>/
		queryset = Article.objects.all()
		article = get_object_or_404(queryset, pk = pk)
		try:
			article.delete()
			return Response(status=204)
		except:
			return Response(status=400)
