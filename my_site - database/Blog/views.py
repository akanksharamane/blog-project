from django.shortcuts import render
from datetime import date


# Create your views here.

all_posts=[
    {"slug":"ek-lavya",
    "image":"Eklavya.jpg",
    "author":"Akanksha",
    "date": date(2021,7,21),
    "title":"Eklavya",
    "extract":"Focusing On Over All Growth Of School And College Student.",
    "content":"""Project Eklavya Under project EKLAVYA, we are focusing on overall growth of school and college students by providing them training in sports like football, Hockey and Athletics.This training involves both soft skill and physical training in order to develop an overall personality of the students."""
    },
    {"slug":"lakshya",
    "image":"Lakshya.jpg",
    "author":"Ankita",
    "date": date(2021,7,21),
    "title":"Lakshya",
    "extract":"Development of Underprivileged Youth From Urban Area..",
    "content":"""Project LAKSHYA emphasizes on development underprivileged of youth from urban areas. Under this program we run foundationprogram of comprising of life & soft skills and then the participant get to choose the skilling course of their choice. They also receive placement support after completion of course through tie ups that iExcel foundation made with companies."""
    },
    {"slug":"sanmaan",
    "image":"Sanmaan.jpg",
    "author":"",
    "date": date(2021,7,21),
    "title":"Sanmaan",
    "extract":"Transgender Empowerment Through Entrepreneurship",
    "content":"""Transgender community in India is neglected for a long time. Despite possessing immense potential and talent they don’t have 
                 acceptance by society and lack opportunities for their overall development. We provide them a skilling platform through which they can learn
                 courses and start their own venture."""
    },
    {"slug":"vyapari-unnati",
    "image":"Vyapari_Unnati.jpg",
    "author":"Twinkle",
    "date": date(2021,7,21),
    "title":"Vyapari Unnati",
    "extract":"Supporting Early Stage Entreprenures To Help Them.",
    "content":"""Under Project Vyapari Unnati, we are focusing on supporting early stage entrepreneurs to help them in taking their current business to new level.
                 We have moved into the world of digital revolution but small scale entrepreneurs are still not embracing these digital tools which can transform 
                 their small business."""
    },
    {"slug":"gram-utthan",
    "image":"Gram utthan.jpg",
    "author":"Sanket",
    "date": date(2021,7,21),
    "title":"Gram Utthan",
    "extract":"Supporting Farmers Childrens In Tuljapur Town.",
    "content":"""Tuljapur town situated in district of Osmanabad, famous for Temple of Goddess Tulja Bhavani lies in dry Marathwada region. Except the famous temple
                 there is no other significant development that has taken place in this part of Maharashtra. Naturally there is very less monsoon rainfall in Tuljapur
                 hence agriculture is not so productive, plus there are no industrial complexes which can create employment opportunities for the youth due to lack of 
                 electricity and water facilities."""
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
        sorted_posts = sorted(all_posts,key=get_date)
        latest_posts = sorted_posts[-5:]
        return render(request,'Blog/start-page.html',{"posts":latest_posts})
    

def post_page(request):
    return render(request,'Blog/all-posts.html',{"all_posts":all_posts})

def postdetail_page(request,slug):
    identified_post = next(post for post in all_posts if post["slug"]==slug)
    return render(request,"Blog/post-detail.html",{
                "postdetail":identified_post})