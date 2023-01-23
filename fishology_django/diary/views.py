from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta


from django.http import Http404
from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from fish.models import Fish
from aquarium.models import Aquarium

from diary.models import Diary, Weather, Mood
from diary.serializers import DiarySerializer, WeatherSerializer, MoodSerializer

# get diary from user


@api_view(['POST'])
def submitDiary(request):

    # print(request.data)

    diary = Diary.objects.create(
        author=request.user,
        aquarium=Aquarium.objects.get(id=request.data.pop('aquarium')),
        fish=Fish.objects.get(id=request.data.pop('fish')),
        mood=Mood.objects.get(name=request.data.pop('mood')),
        weather=Weather.objects.get(name=request.data.pop('weather')),
        ** request.data
    )
    diary.save()

    return Response(DiarySerializer(diary).data)


@api_view(['POST'])
def FilterDiary(request, aquarium_id):
    print('Filter Info: ' + str(request.data))
    filters = {}

    dateFrom = request.data.pop('dateFrom')
    dateTo = request.data.pop('dateTo')

    author = request.data.pop('author')

    for key, value in request.data.items():
        if value != '':
            filters[key] = value

    diaries = Diary.objects.filter(
        aquarium_id=aquarium_id,
        **filters)

    if (dateFrom != ''):
        dateFrom = datetime.strptime(dateFrom, '%Y-%m-%d')
        diaries = diaries.filter(created__gte=datetime.date(dateFrom))

    if (dateTo != ''):
        dateTo = datetime.strptime(dateTo, '%Y-%m-%d')
        diaries = diaries.filter(created__lt=datetime.date(dateTo))

    if (author != ''):
        diaries = diaries.filter(author__username=author)

    print("Date from: " + str(dateFrom) + " to: " + str(dateTo))

    for diary in diaries:
        print(diary.created)

    return Response(DiarySerializer(diaries, many=True).data)


class AquariumDiary(APIView):

    # GET ALL DIARIES

    # def get(self, request, format=None):
    #     diaries = Diary.objects.all()
    #     serializer = DiarySerializer(diaries, many=True)
    #     return Response(serializer.data)

    # GET AQUARIUM DIARIES

    def get_object(self, aquarium_id):
        try:
            return Diary.objects.filter(aquarium=aquarium_id)
        except Diary.DoesNotExist:
            raise Http404

    def get(self, request, aquarium_id, format=None):
        diaries = self.get_object(aquarium_id)
        serializer = DiarySerializer(diaries, many=True)
        return Response(serializer.data)

    # def post(self, request, aquarium_id, format=None):
    #     print(request.data)
    #     diaries = Diary.objects.all(author=request.user)
    #     return Response(DiarySerializer(diaries, many=True).data)


class WeatherList(APIView):
    def get(self, request, format=None):
        weathers = Weather.objects.all()
        serializer = WeatherSerializer(weathers, many=True)
        return Response(serializer.data)


class MoodList(APIView):
    def get(self, request, format=None):
        moods = Mood.objects.all()
        serializer = MoodSerializer(moods, many=True)
        return Response(serializer.data)


class DiaryMoodList(APIView):

    def get(self, request, aquarium_id, range_type, index, format=None):

        result_dict = {}
        flag = False  # DETERMINE IF EARLIESTS RECORD REACHED

        MONTHS = [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'June',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec'
        ]

        oldestDiary = Diary.objects.filter(
            author=request.user).earliest('created')

        if (range_type == 'Week'):
            today = datetime.now(timezone.utc) - timedelta(days=index * 7)

            for i in range(0, 7):

                filterDate = today - timedelta(days=(6-i))

                # Check IF REACH EARLIEST DATE
                if (filterDate <= oldestDiary.created):
                    print("Oldest Diary Reached!")
                    flag = True

                diaries = Diary.objects.filter(
                    author=request.user,
                    aquarium_id=aquarium_id,
                    created__year=filterDate.year,
                    created__month=filterDate.month,
                    created__day=filterDate.day)

                moodTotal = diaries.aggregate(Sum('mood__value'))[
                    'mood__value__sum']

                if (moodTotal == None):
                    result_dict[str(filterDate.day) + '/' +
                                str(filterDate.month)] = None
                else:
                    result_dict[str(filterDate.day) + '/' +
                                str(filterDate.month)] = moodTotal/diaries.count()

        elif (range_type == 'Month'):

            today = datetime.now(timezone.utc) - relativedelta(months=index*12)

            for i in range(0, 12):
                filterDate = today - relativedelta(months=(11-i))

                # Check IF REACH EARLIEST DATE

                if (filterDate <= oldestDiary.created):
                    print("Oldest Diary Reached!")
                    flag = True

                diaries = Diary.objects.filter(author=request.user, aquarium_id=aquarium_id, created__year=filterDate.year,
                                               created__month=filterDate.month)

                moodTotal = diaries.aggregate(Sum('mood__value'))[
                    'mood__value__sum']

                if (moodTotal == None):
                    result_dict[str(MONTHS[filterDate.month-1]) + " '" +
                                str(filterDate.year)[-2:]] = None
                else:
                    result_dict[str(MONTHS[filterDate.month-1]) + " '" +
                                str(filterDate.year)[-2:]] = moodTotal/diaries.count()

        elif (range_type == 'Year'):

            today = datetime.now(timezone.utc) - relativedelta(years=index)

            for i in range(0, 5):
                filterDate = today - relativedelta(years=(4-i))

                # Check IF REACH EARLIEST DATE

                if (filterDate <= oldestDiary.created):
                    print("Oldest Diary Reached!")
                    flag = True

                diaries = Diary.objects.filter(
                    author=request.user, aquarium_id=aquarium_id, created__year=filterDate.year)

                moodTotal = diaries.aggregate(Sum('mood__value'))[
                    'mood__value__sum']

                if (moodTotal == None):
                    result_dict[str(filterDate.year)] = None
                else:
                    result_dict[str(filterDate.year)
                                ] = moodTotal/diaries.count()

        print(result_dict)

        return Response({"results": result_dict, "flag": flag})


class DiaryCountList(APIView):

    def get(self, request, aquarium_id, range_type, index, format=None):

        result_dict = {}
        flag = False  # DETERMINE IF EARLIEST RECORD REACHED

        MONTHS = [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'June',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec'
        ]

        oldestDiary = Diary.objects.filter(
            author=request.user).earliest('created')

        if (range_type == 'Week'):
            today = datetime.now(timezone.utc) - timedelta(days=index * 7)
            # print('index: ' + str(index) + " today: " + str(today))

            for i in range(0, 7):

                filterDate = today - timedelta(days=(6-i))

                # Check IF REACH EARLIEST DATE

                if (filterDate <= oldestDiary.created):
                    print("Oldest Diary Reached!")
                    flag = True

                print(aquarium_id)

                diary = Diary.objects.filter(
                    author=request.user,
                    aquarium__id=aquarium_id,
                    created__year=filterDate.year,
                    created__month=filterDate.month,
                    created__day=filterDate.day).count()

                print(str(filterDate) + " - " + str(diary))

                result_dict[str(filterDate.day) + '/' +
                            str(filterDate.month)] = diary

        elif (range_type == 'Month'):

            today = datetime.now(timezone.utc) - relativedelta(months=index*12)

            for i in range(0, 12):
                filterDate = today - relativedelta(months=(11-i))

                # Check IF REACH EARLIEST DATE

                if (filterDate <= oldestDiary.created):
                    print("Oldest Diary Reached!")
                    flag = True

                diary = Diary.objects.filter(author=request.user, aquarium_id=aquarium_id, created__year=filterDate.year,
                                             created__month=filterDate.month).count()

                print(MONTHS[filterDate.month-1] + " - " + str(diary))

                result_dict[str(MONTHS[filterDate.month-1]) + " '" +
                            str(filterDate.year)[-2:]] = diary

        elif (range_type == 'Year'):

            today = datetime.now(timezone.utc) - relativedelta(years=index)

            for i in range(0, 5):
                filterDate = today - relativedelta(years=(4-i))

                # Check IF REACH EARLIEST DATE

                if (filterDate <= oldestDiary.created):
                    print("Oldest Diary Reached!")
                    flag = True

                diary = Diary.objects.filter(
                    author=request.user, aquarium_id=aquarium_id, created__year=filterDate.year).count()

                print(str(filterDate.year) + " - " + str(diary))

                result_dict[str(filterDate.year)] = diary

        print(result_dict)
        return Response({"results": result_dict, "flag": flag})
