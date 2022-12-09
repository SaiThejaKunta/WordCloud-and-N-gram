#!/usr/bin/env python
# coding: utf-8

# # Word Cloud
# Word Cloud is a data visualization technique used for representing text data in which the size of each word indicates its frequency or importance. Significant textual data points can be highlighted using a word cloud. Word clouds are widely used for analyzing data from social network websites
# In[2]:

pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
text=''' What is Google Developer Student Clubs (GDSC)?
Developer Student Clubs (DSC) are university-based community groups powered by Google Developers for students interested in Technology. The aim is to help students bridge the gap between theory and practice. By joining a GDSC, students grow their knowledge in a peer-to-peer learning environment and build solutions for local businesses and their community.

Who are we?
We are a group of students who are passionate about Technology. Our goal is to bring together students from various backgrounds who love learning and applying their skills to solve real-world problems. And make you connect with different developers across the world.

Why join Google Developer Student Club @ GNITC?
Google Developer Student Club at GNITC organizes and facilitates workshops, hackathons, speaker sessions and Study Jams to provide students with technical development skills. By joining, you can:

Attend workshops, webinars, hackathons and other exciting events.
Expand your technical skills through a peer-to-peer learning environment.
Collaborate and apply the acquired skills by helping build solutions for the local community.
Participate in the annual Solution Challenge competition with the chance of winning prizes from Google.
Expand your network by meeting Tech leaders and professionals.
Have fun and meet other students interested in developer technologies.
How to be part of the Developer Student Club @ GNITC?
Every student from any degree with an interest in growing as a developer is welcome. The only requirement is to be passionate about Technology!

Become a member by clicking on the "Join" button above the About section.

Join us to get a chance to explore Google Technologies, build projects and sky rocket your thoughts into actions!  '''
wc = WordCloud(width=500, height=500, max_words=200,background_color="white").generate(text)
plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()




#background_color="white",colormap="Oranges_r",max_font_size=20, min_font_size=10,
#interpolation="bilinear"





