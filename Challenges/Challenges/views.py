from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january" : "30-Day Fitness Challenge: Commit to a daily workout routine for 30 days",
    "february":"No-Sugar Challenge: Eliminate all added sugars from your diet for a month.",
    "march":"Book-a-Week Challenge: Read one book per week for 12 weeks.",
    "april":"Photography Challenge: Take one photo a day, each day focusing on a different theme or subject.",
    "may":"Meditation Challenge: Meditate for at least 10 minutes every day for 30 days.",
    "june":"Language Learning Challenge: Practice a new language for 15 minutes daily for a month.",
    "july":"Minimalism Challenge: Declutter one area of your home each day for a month.",
    "august":"Creative Writing Challenge: Write a short story or a poem every day for a month.",
    "september":"Digital Detox Challenge: Limit your screen time to two hours per day for a week.", 
    "october":"Random Acts of Kindness Challenge: Perform a random act of kindness every day for a month.",
    "november":"Cooking Challenge: Cook a new recipe from a different cuisine every week for 12 weeks.",
    "december":"Gratitude Challenge: Write down three things you are grateful for each day for 30 days.",
    
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge" , args=[month])
        list_items +=  f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"
        
    return HttpResponse(response_data)



def monthly_challenge_by_number(request , month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month= months[month - 1]
    redirect_path = reverse('month-challenge' , args=[redirect_month])
    return HttpResponseRedirect('/' + redirect_month)

def monthly_challenge(request , month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Invalid Month")
