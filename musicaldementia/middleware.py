"""musicaldementia middleware"""

# Django
from django.shortcuts import redirect, reverse



class Simple_Middleware:
    def __init__(self,get_reponse):
        self.get_response = get_reponse


    def __call__(self,request):
        # print(request.user)        


        if not request.user.is_anonymous:
            the_profile = request.user.profile

            if not the_profile.phone_number or not the_profile.photo or not the_profile.interest:
                if request.path not in [reverse('users:update'),reverse('users:logout'),'admin/']:
                    return redirect('users:update')

        response = self.get_response(request)


        return response 