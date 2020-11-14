from django.shortcuts import render, HttpResponse, redirect, reverse
from core.models import Level, UserProfile, QuizTakers, Answer, Response, LevelPublish, Notification
from django.contrib.auth.models import User
from django.contrib.auth import logout
from core.forms import ContactusForm, UserProfileForm
from django.db.models import Q
from django.contrib import messages
import json
from random import randint


COLOR = {
        'purple': 'purple',
        'orange': 'orange',
        'blue': 'blue',
        'teal': 'teal',
        'yellow': 'yellow',
        'red': 'red'
    }

def index(request):
    """

    :param request:
    :return:

    Homepage rendering
    Leaderboard update
    Contact us form
    """

    context_dict = {}

    levels = Level.objects.order_by("created")

    try:
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get_or_create(user=user)[0]
        quiztaker = QuizTakers.objects.get_or_create(user=userprofile)[0]
        loop = range(1, quiztaker.correct_answers + 1)

        context_dict["userprofile"] = userprofile
        context_dict["quiztaker"] = quiztaker
        context_dict["loop"] = loop
        context_dict["dark_mode"] = userprofile.dark_mode
        context_dict["color_mode"] = userprofile.color_mode

        if userprofile.is_previously_logged:
            all_levelpublish = LevelPublish.objects.filter(userprofile=userprofile)[::-1]
            context_dict["all_levelpublish"] = all_levelpublish

    except User.DoesNotExist:
        pass

    ranks = QuizTakers.objects.filter(user__user__is_staff=False).order_by("-correct_answers")
    top_ranks = ranks[:3]
    rest_ranks = ranks[3:]

    context_dict['top_ranks'] = top_ranks
    context_dict['rest_ranks'] = rest_ranks

    form = ContactusForm()
    if 'contact' in request.POST:
        form = ContactusForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponse(
                json.dumps({'status': "Congratulation", 'message': "Submitted"}), content_type="application/json"
            )
        else:
            print(form.errors)
            return HttpResponse(
                json.dumps({'status': "Error", 'message': "Try again"}), content_type="application/json"
            )

    value = randint(1, 2)

    notifications = Notification.objects.order_by("-pub_date")

    context_dict["notifications"] = notifications
    context_dict["value"] = value
    context_dict["levels"] = levels
    context_dict["form"] = form

    return render(request, "core/index.html", context=context_dict)


def answer(request):
    """

    :param request:
    :return:

    Check answers, update level cleared and publish next level.
    """
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        ip = request.META.get('REMOTE_ADDR')
        messages.info(request, f"Bakchodi nai. Remember, I can track your IP {ip} :)")
        return redirect('core:index')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    quiztaker = QuizTakers.objects.get_or_create(user=userprofile)[0]

    if request.method == 'POST':

        level_no = int(request.POST['level_no'])
        current_level = Level.objects.get(number=level_no)
        level_answer = Answer.objects.get(level=current_level)
        ans = request.POST['answer']

        if str(ans).lower() == level_answer.text:

            if not current_level.is_last:
                next = Level.objects.get(number=(level_no + 1))

            else:
                next = Level.objects.get(number=99)

            levelpublish = LevelPublish.objects.get_or_create(userprofile=userprofile, level=next)[0]
            levelpublish.publish = True
            levelpublish.save()

            quiztaker.correct_answers = quiztaker.correct_answers + 1

            userprofile.clear = userprofile.clear + 1
            userprofile.save()

            response = Response.objects.get_or_create(quiztaker=quiztaker, level=current_level, answer=level_answer)[0]
            response.save()

            if current_level.is_last:
                quiztaker.completed = True
                messages.success(request, f"You cleared final level. Check out the leaderboards!",
                                 extra_tags='last_level')
            else:
                messages.success(request,
                                 f"You cleared level {level_no + 1}. Keep up and be on the top of leaderboards!",
                                 extra_tags='normal_level')

            quiztaker.save()
            # return HttpResponse(
            #     json.dumps({'status': "success"}), content_type="application/json"
            # )
        else:
            messages.warning(request, f"Your answer {ans} is wrong. Think harder!")
    return redirect('core:index')


def settings(request):
    """

    :param request:
    :return:

    Initialize core for first time logged in user.
    """
    context_dict = {}


    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return redirect('core:index')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    context_dict['userprofile'] = userprofile

    if userprofile.is_previously_logged:
        try:
            levels = Level.objects.order_by("created")
            for level in levels:
                new_levelpublish = LevelPublish.objects.get_or_create(userprofile=userprofile, level=level)
                if new_levelpublish[1]:
                    new_levelpublish[0].publish = False
                    new_levelpublish[0].save()
        except:
            print("Levels not added")
        return redirect('core:index')

    else:
        try:
            levels = Level.objects.order_by("created")
            for level in levels:
                levelpublish = LevelPublish.objects.get_or_create(userprofile=userprofile, level=level)[0]
                levelpublish.publish = False
                levelpublish.save()
                userprofile.clear = 0
                userprofile.save()

                first_level = levels.first()
                first_level.publish = True
                first_level.save()

                all_levelpublish = LevelPublish.objects.filter(userprofile=userprofile)
                first_levelpublish = all_levelpublish[0]
                first_levelpublish.publish = True
                first_levelpublish.save()
        except:
            print("Levels not added")

    userprofile.is_previously_logged = True
    # userprofile.save()

    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)

        if form.is_valid():
            form.save()
            print(request.POST.get('firstname'))
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            user.save()
            print(user.first_name)

            return redirect('core:index')
        else:
            print(form.errors)

    return render(request, 'core/settings.html', context=context_dict)


def profile(request, username):
    """

    :param request:
    :param username:
    :return:

    Personal Profile page
    """

    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    quiztaker = QuizTakers.objects.get(user=userprofile)
    loop = range(1, quiztaker.correct_answers + 1)

    context_dict = {
        'quiztaker': quiztaker,
        'loop': loop
    }
    return render(request, 'core/profile.html', context=context_dict)


def search(request):
    """

    :param request:
    :return:

    AJAX search for players
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            query = str(request.POST['query'])
        else:
            query = ""

        result_profiles = UserProfile.objects.filter(user__is_staff=False).filter(Q(user__first_name__contains=query) |
                                                                                  Q(user__username__contains=query) | Q(
            user__email__contains=query))
        context = {
            "result_profiles": result_profiles
        }
    else:
        ip = request.META.get('REMOTE_ADDR')
        messages.info(request, f"Bakchodi nai. Remember, I can track your IP {ip} :)")
        return redirect('core:index')

    return render(request, 'core/search.html', context=context)


def notifications(request):
    notifications = Notification.objects.order_by("-pub_date")
    context = {
        'notifications': notifications
    }
    return render(request, 'core/notifications.html', context=context)


def toggle_mode(request):
    """

    :param request:
    :return:

    Saves the dark/white mode preference
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            mode = str(request.POST['dark_mode'])
        else:
            mode = ""

        userprofile = UserProfile.objects.get(user=request.user)
        if mode == "on":
            userprofile.dark_mode = True
        else:
            userprofile.dark_mode = False
        userprofile.save()
    return HttpResponse("success")


def color_mode_toggle(request):
    """

    :param request:
    :return:

    Saves the color preference
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            mode = str(request.POST['color_mode'])
        else:
            mode = ""

        userprofile = UserProfile.objects.get(user=request.user)
        userprofile.color_mode = COLOR[mode]
        userprofile.save()
    return HttpResponse("success")


def logout_view(request):
    """

    :param request:
    :return:

    Logout user successfully
    """
    logout(request)
    return redirect(reverse('core:index'))
