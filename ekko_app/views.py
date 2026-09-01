from django.shortcuts import render
from ekko_app.cerebrum_client import get_contactinfo_list
from ekko_app.models import Ansatt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import redirect
from ekko_app.forms import SMSForm 
from ekko_app.sms import send_sms

@staff_member_required
def index(request):

    if request.method == "POST":
        form = SMSForm(request.POST)

        sent = 0    
        failed = 0

        if form.is_valid():
            recipients = form.cleaned_data.get('recipients')
            message = form.cleaned_data.get('message')

            for recipient in recipients:
                try:
                    status = send_sms(recipient.phone_number, message)
                    print(recipient.username, "->", status, "\n")
                    if status["success"]:
                        sent += 1
                    else:
                        failed += 1
                except Exception as e:
                    print(f"FEIL ved sending til {recipient.username}: {e}")
                    failed += 1

            messages.success(request, f'Sendt til {sent} av {sent + failed} mottakere')
            print(message.encode("utf-8"))
                
            return redirect("index")


    else:
        form = SMSForm()

    return render(request, "send_form.html", {"form" : form})

@staff_member_required
def ansatt_sync_view(request):
    if request.method == "POST":
        it_hjelp_result = ansatt_sync("it-hjelp-saksbehandler", "is_it_hjelp")
        vaktleder_result = ansatt_sync("it-hjelp-vaktleder", "is_vaktleder")
        messages.success(request, 
                        f'Oppdatert: Nye: {it_hjelp_result["created"]}, Oppdatert: {it_hjelp_result["updated"]}, Hoppet over: {it_hjelp_result["skipped"]}\n'
                        f'Oppdatert: Nye: {vaktleder_result["created"]}, Oppdatert: {vaktleder_result["updated"]}, Hoppet over: {vaktleder_result["skipped"]}\n'
                        f'TEST: {Ansatt.objects.filter(is_vaktleder=True)}')
    return redirect(index)
                         

def ansatt_sync(group_name, field_name):
    contact_info = get_contactinfo_list(group_name)

    created_count = 0
    updated_count = 0
    skipped_count = 0

    for username, phone in contact_info.items():
        if phone is None:
            print(f'Ingen mobilnummer for {username} funnet, hopper over')
            skipped_count += 1
            continue
        _, created = Ansatt.objects.update_or_create(
            username=username, 
            defaults={"phone_number": phone, field_name: True})

        if created:
            created_count += 1
        else: 
            updated_count += 1

    return {"created" : created_count, "updated" : updated_count, "skipped" : skipped_count}



