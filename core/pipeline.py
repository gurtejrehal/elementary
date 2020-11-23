from .models import UserProfile, User

# def save_profile_picture(backend, strategy, details, response,
#         user=None, *args, **kwargs):
#     url = None
#     profile = UserProfile.objects.get(user=user)
#     if backend.name == 'facebook':
#         url = "https://graph.facebook.com/%s/picture?type=large"%response['id']
#     if url:
#         profile.picture_url = url
#         profile.save()


def save_profile_picture(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = None
        if profile is None:
            user = User.objects.get_or_create(username=user.username)[0]
            profile = UserProfile.objects.get_or_create(user=user)[0]
            profile.picture_url = f"http://graph.facebook.com/{response['id']}/picture?type=large"
            profile.save()

    if backend.name == 'twitter':
        user = User.objects.get_or_create(username=user.username)[0]
        profile = UserProfile.objects.get_or_create(user=user)[0]
        url = response.get('profile_image_url', '').replace('_normal', '')
        print("image", url)

        if url:
            profile.picture_url = url
            profile.save()


