import graphene
from graphene_django.types import DjangoObjectType
from TM_APP.models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay, ObjectType

class postsNode(DjangoObjectType):
    class Meta:
        model = posts
        filter_fields = ['comments']
        interfaces = (relay.Node,)
        # fields = ('id', 'first_name', 'email')

class commentsNode(DjangoObjectType):
    class Meta:
        model = comments
        filter_fields = ['text']
        interfaces = (relay.Node,)

class coursresNode(DjangoObjectType):
    class Meta:
        model = coursres
        filter_fields = ['name']
        interfaces = (relay.Node,)

class videoNode(DjangoObjectType):
    class Meta:
        model = video
        filter_fields = ['url']
        interfaces = (relay.Node,)


class quizNode(DjangoObjectType):
    class Meta:
        model = quiz
        filter_fields = ['coursre']
        interfaces = (relay.Node,)

class questionsNode(DjangoObjectType):
    class Meta:
        model = questions
        filter_fields = ['quiz','text']
        interfaces = (relay.Node,)

class answersNode(DjangoObjectType):
    class Meta:
        model = answers
        filter_fields = ['question','text','is_correct']
        interfaces = (relay.Node,)

class documentNode(DjangoObjectType):
    class Meta:
        model = document
        filter_fields = ['name']
        interfaces = (relay.Node,)
        #fields = ['attatchment']

class Query(ObjectType):
    all_posts = DjangoFilterConnectionField(postsNode)
    all_comments = DjangoFilterConnectionField(commentsNode)
    all_courses = DjangoFilterConnectionField(coursresNode)
    all_video = DjangoFilterConnectionField(videoNode)
    all_document = DjangoFilterConnectionField(documentNode)
    all_quiz = DjangoFilterConnectionField(quizNode)
    all_quesions = DjangoFilterConnectionField(questionsNode)
    all_answers = DjangoFilterConnectionField(answersNode)

    get_posts = relay.Node.Field(postsNode)
    get_comments = relay.Node.Field(commentsNode)
    get_courses = relay.Node.Field(coursresNode)
    get_video = relay.Node.Field(videoNode)
    get_document = relay.Node.Field(documentNode)
    get_quiz = relay.Node.Field(quizNode)
    get_questions = relay.Node.Field(questionsNode)
    get_answer = relay.Node.Field(answersNode)


class postsInput(graphene.InputObjectType):
    comments = graphene.String(required=True)

class Createposts(graphene.Mutation):
    class Arguments:
        post_data = postsInput(required=True)
        post = graphene.String(posts)

    @staticmethod
    def mutate(root, info, post_data=None):
        post = posts(
            comments=post_data.comments,
        )
        return Createposts(post=post)
