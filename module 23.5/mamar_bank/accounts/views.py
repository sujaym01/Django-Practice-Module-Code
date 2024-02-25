from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import HttpResponseRedirect
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
#######################################################################################
class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
#..........................................................................................
# from django.views.generic import CreateView

# class UserRegistrationView1(CreateView):
#     template_name = 'accounts/user_registration.html'
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy('profile')
    
#     def form_valid(self,form):
#         print(form.cleaned_data)
#         user = form.save()
#         login(self.request, user)
#         print(user)
#         return super().form_valid(form) # form_valid function call hobe jodi sob thik thake  
#############################################################################################
    
# class UserLoginView(LoginView):
#     template_name = 'accounts/user_login.html'
#     def get_success_url(self):
#         return reverse_lazy('home')
#########################################################################
class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, "Login Successfully.Welcome Back!")
        return super().form_valid(form)
##########################################################################

# from django.views.generic import RedirectView
# from django.contrib.auth.mixins import LoginRequiredMixin
class UserLogoutView(LoginRequiredMixin,RedirectView):
    url = reverse_lazy('home')  # Redirect to home after logout

    def get(self, request, *args, **kwargs):
        # if self.request.user.is_authenticated: # Authenticate user na hole home page e nia jabe
            logout(self.request)
            messages.info(self.request, "Logout Successfully!")
            return super().get(request, *args, **kwargs)


# from django.shortcuts import HttpResponseRedirect
#can not work this code my site
# class UserLogoutView(LogoutView):
#     def get(self, request, *args, **kwargs):
#         logout(self.request)
#         messages.info(self.request, "Logout Successfully!")
#         return redirect(reverse_lazy('home'))
##############################################################################
    
from accounts.models import UserAddress, UserBankAccount 
class UserProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'
    def get(self, request):
        user_address = UserAddress.objects.filter(user=request.user).first()
        print(user_address.country, user_address.image)
        
        # user_address = UserAddress.objects.filter(user_id=request.user)
        # for i in user_address:
        #     print(i.country, i.user, i.city, i.street_address,i.postal_code, i.image)
          
        # user_bank_account = UserBankAccount.objects.filter(user_id =request.user)
        # for i in user_bank_account:
        #     print(i.user, i.account_no, i.account_type, i.balance, i.birth_date, i.gender, i.initial_deposite_date)
        return render(request, self.template_name,{'user_address':user_address})
    
#     def get(self, request):
#         borrowed_books = Book.objects.filter(borrowers=request.user)
#         # for book in borrowed_books:
#         #     print(book.title, book.price, book.categories)

#         # all_transactions = Transaction.objects.filter(account=request.user.account).order_by('-timestamp')
#         # for transaction in all_transactions:
#         #     print(transaction.amount, transaction.balance_after_transaction,transaction.transaction_type)

#         # Create a list to store book details along with their borrowing history
#         borrowed_books_details = []

#         for book in borrowed_books:
#             # Get the borrowing history for each book
#             details = Transaction.objects.filter(
#                 account=request.user.account, 
#                 amount=book.price,
#             ).order_by('-timestamp')

#             # Add book and its history to the list
#             borrowed_books_details.append({'book': book, 'details': details})

#             # Extract transaction details for each book
#             # transactions_for_book = [{'amount': transaction.amount, 'balance_after_transaction': transaction.balance_after_transaction}
#             #                 for transaction in borrowed_books_details]
            
#         context = {
#             'user': request.user,
#             # 'borrowed_books': borrowed_books,
#             'borrowed_books_details': borrowed_books_details,
#             # 'all_transactions': all_transactions,
#         }
#         return render(request, self.template_name, context=context)

###############################################################################
# class UserBankAccountUpdateView(View):
#     template_name = 'accounts/profile.html'

#     def get(self, request):
#         form = UserUpdateForm(instance=request.user)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(self.request, "Account Updated Successfully!")
#             return redirect('profile')  # Redirect to the user's profile page
#         return render(request, self.template_name, {'form': form})
    

from django.views.generic import UpdateView    
class UserBankAccountUpdateView(UpdateView):
    template_name = 'accounts/update_profile.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        # self.object = form.save()
        messages.success(self.request, "Account Updated Successfully!")
        return super().form_valid(form)

from django.contrib.auth import update_session_auth_hash   
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from transactions.views import send_transaction_email
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your password was successfully updated!')
                
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        send_transaction_email(
                    self.request.user,
                    '' ,
                    'Password Changed',
                    'accounts/password_change_mail.html'
                    )
        return super().form_valid(form)
    
    