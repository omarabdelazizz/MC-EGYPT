import graphene
from graphene_django.types import DjangoObjectType
from TM_APP.models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay, ObjectType
from .Forms import *

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
    get_answers = relay.Node.Field(answersNode)

#comments
class commentType (DjangoObjectType):
    class Meta:
        model = comments
class CreatecommentsMutaion(DjangoModelFormMutation):
    #creat object from comment form
    comment = graphene.Field(commentType)

    class Meta:
        form_class =CreateCommentsForm
        input_field_name = 'text'
        return_field_name = 'text'

#posts
class postType (DjangoObjectType):
    class Meta:
        model = posts
class CreatepostsMutaion(DjangoModelFormMutation):
    #creat object from comment form
    post = graphene.Field(postType)

    class Meta:
        form_class =CreateCommentsForm
        input_field_name = 'comments'
        return_field_name = 'comments'

#coursres
class coursreType (DjangoObjectType):
    class Meta:
        model = coursres
class CreateCoursresMutaion(DjangoModelFormMutation):
    #creat object from comment form
    coursre = graphene.Field(coursreType)

    class Meta:
        form_class =CreateCoursresForm
        input_field_name = 'name'
        return_field_name = 'name'

#video
class videoType (DjangoObjectType):
    class Meta:
        model = video
class CreatevideoMutaion(DjangoModelFormMutation):
    #creat object from comment form
    video = graphene.Field(videoType)

    class Meta:
        form_class =CreateVideoForm
        input_field_name = 'url'
        return_field_name = 'url'

#document
class documentType (DjangoObjectType):
    class Meta:
        model = document
class CreatedocumentMutaion(DjangoModelFormMutation):
    #creat object from comment form
    document = graphene.Field(documentType)

    class Meta:
        form_class =CreateDocumentForm
        input_field_name = 'name'
        return_field_name = 'name'

#quiz
class quizType (DjangoObjectType):
    class Meta:
        model = quiz
class CreatequizMutaion(DjangoModelFormMutation):
    #creat object from comment form
    quiz = graphene.Field(quizType)

    class Meta:
        form_class =CreateQuizForm
        input_field_name = 'coursre'
        return_field_name = 'coursre'


#questions
class questionType (DjangoObjectType):
    class Meta:
        model = questions
class CreatequestionMutaion(DjangoModelFormMutation):
    #creat object from comment form
    question = graphene.Field(questionType)

    class Meta:
        form_class =CreateQuestionsForm
        input_field_name = 'quiz',
        return_field_name = 'quiz'


#answers
class answerType (DjangoObjectType):
    class Meta:
        model = quiz
class CreateanswerMutaion(DjangoModelFormMutation):
    #creat object from comment form
    answer = graphene.Field(answerType)

    class Meta:
        form_class =CreateAnswersForm
        input_field_name = 'question'
        return_field_name = 'question'


class Mutation(ObjectType):
    create_comment = CreatecommentsMutaion.Field()
    create_post = CreatepostsMutaion.Field()
    create_course = CreateCoursresMutaion.Field()
    create_video = CreatevideoMutaion.Field()
    create_document = CreatedocumentMutaion.Field()
    create_quiz = CreatequizMutaion.Field()
    create_question = CreatequestionMutaion.Field()
    create_answer = CreateanswerMutaion.Field()
