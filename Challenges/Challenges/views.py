from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect

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

def monthly_challenge_by_number(request , month):
    months = list(monthly_challenges.keys())
    redirect_month= months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request , month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Invalid Month")
