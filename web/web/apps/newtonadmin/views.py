from django.shortcuts import render, redirect

def show_login_view(request):
    return render(request, "login.html", locals())

def post_login(request):
    return redirect("/newtonadmin/")

def logout(request):
    return redirect("/")

def index(request):
    return render(request, "newtonadmin/welcome.html", locals())

def kyc_admin(request):
    return render(request, "newtonadmin/kycindex.html", locals())

def kyc_id_confirm(request):
    return render(request, "newtonadmin/kyc-id-confirm.html", locals())

def kyc_amount_confirm(request):
    return render(request, "newtonadmin/kyc-amount-confirm.html", locals())

def kyc_email_confirm(request):
    return render(request, "newtonadmin/kyc-email-confirm.html", locals())

def kyc_email_list(request):
    return render(request, "newtonadmin/kyc-email-list.html", locals())

def kyc_step_one(request):
    return render(request, "newtonadmin/kyc-step-one.html", locals())

def kyc_step_two(request):
    return render(request, "newtonadmin/kyc-step-two.html", locals())

def kyc_step_three(request):
    return render(request, "newtonadmin/kyc-step-three.html", locals())

def kyc_update_id(request):
    update_info = "Update Successed!"
    return render(request, "newtonadmin/kyc-step-one.html", locals());

def kyc_update_amount(request):
    update_info = "Update Successed!"
    return render(request, "newtonadmin/kyc-step-two.html", locals());

def kyc_update_email(request):
    update_info = "Send Successed!"
    return render(request, "newtonadmin/kyc-step-three.html", locals());

def kyc_send_one_email(request):
    update_info = "Send Successed!"    
    return render(request, "newtonadmin/kyc-step-three.html", locals());

def kyc_send_email(request):
    update_info = "Send Successed!"    
    return render(request, "newtonadmin/kycindex.html", locals());

def kyc_export_csv(request):
    update_info = "Export Successed!"    
    return render(request, "newtonadmin/kycindex.html", locals());

def blog_admin(request):
    return render(request, "index.html", locals())
