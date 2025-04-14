from fastapi import FastAPI
import random

app = FastAPI()  # all fast apoi function methods stored in app variable
# requirement of making apis
# we will build two get endpoint
# side hustle api
# money quotes

side_hustles = [
    "Freelance writing – Blog posts, articles, or copy for businesses.",
    "Graphic design – Logos, social media posts, posters.",
    "Virtual assistant – Help businesses with tasks like emails, scheduling, or customer support.",
    "Online tutoring – Teach subjects like math, English, or coding.",
    "Transcription – Type out audio or video into text.",
    "Print on Demand – Sell custom T-shirts, mugs, or phone cases.",
    "Affiliate marketing – Earn money by recommending products online.",
    "Sell digital products – eBooks, planners, templates, music, etc.",
    "Video editing – For YouTubers, businesses, or influencers.",
    "Start a YouTube channel or podcast – Monetize through ads or sponsorships.",
]

money_quotes = [
    "Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like. – Will Rogers",
    "It’s not your salary that makes you rich, it’s your spending habits. – Charles A. Jaffe",
    "The more you learn, the more you earn. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "Rich people have small TVs and big libraries. Poor people have small libraries and big TVs. – Zig Ziglar",
    "The goal isn’t more money. The goal is living life on your terms. – Chris Brogan",
    "Financial freedom is available to those who learn about it and work for it. – Robert Kiyosaki",
    "Don’t work for money. Make money work for you. – Robert Kiyosaki",
    "I love money. I love everything about it. I bought some pretty good stuff. Got me a $300 pair of socks. – Steve Martin",
    "Money can’t buy happiness, but it can buy ice cream, which is pretty much the same thing. – Unknown",
    "If you think nobody cares if you're alive, try missing a couple of payments. – Earl Wilson",
    "The safest way to double your money is to fold it over and put it in your pocket. – Kin Hubbard",
    "I’m so poor I can’t even pay attention. – Ron Kittle",
]


@app.get("/side_hustles")
# help to live api end point
def get_side_hustles(apiKey: str):
    """Return a random side hustles"""
    if apiKey != "12345":
        return {"error": "Invalid API key"}
    return {"side_hustles": random.choice(side_hustles)}  # we will return into object


@app.get("/money_quotes")
def get_money_quotes(apiKey):
    """Return a random money quotes"""
    if apiKey != "12345":
        return {"error": "Invalid API key"}
    return {"money_quotes": {random.choice(money_quotes)}}
