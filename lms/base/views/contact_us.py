# def contactus_view(request):
#     sub = forms.ContactusForm()
#     if request.method == 'POST':
#         sub = forms.ContactusForm(request.POST)
#         if sub.is_valid():
#             email = sub.cleaned_data['Email']
#             name = sub.cleaned_data['Name']
#             message = sub.cleaned_data['Message']
#             send_mail(str(name) + ' || ' + str(email), message, EMAIL_HOST_USER, ['a@gmail.com'], fail_silently=False)
#             return render(request, 'base/contactussuccess.html')
#     return render(request, 'base/contactus.html', {'form': sub})
