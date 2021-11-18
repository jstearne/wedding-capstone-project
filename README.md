# wedding-capstone-project

Original Project: https://github.com/jstearne/wedding-site
Project Board 1: https://github.com/jstearne/wedding-site/projects/1

# Official Site
Final Project: https://github.com/jstearne/wedding-capstone-project
Project Board 2: https://github.com/jstearne/wedding-capstone-project/projects/1

Website Deployed: https://jo-and-jared.herokuapp.com/


# Wireframe (PNG available)
https://www.figma.com/file/J7vbI1CERgY6CZZwCYGhej/Wedding-Website?node-id=0%3A1

# ERD (PDF available)
https://app.diagrams.net/#Hjstearne%2Fwedding-site%2Fmain%2Ferd.drawio

# User Flow (PDF available)
https://app.diagrams.net/#Hjstearne%2Fwedding-site%2Fmain%2Ferd.drawio


This Heroku App is a fully functional, Django-powered full-stack website. The frontend is Bootstrap/CSS/HTML with a Python/Django backend and a Postgresql database for user, RSVP and guestbook message data. There are no additional technologies in the final production version. 

There were considerations for user image uploading (via Pillow), Honeyfund gift giving (via Stripe Checkout) and Google Maps API (for hotel data). But based on input (virtually 100% mobile device preferred and general family preference for in-person gifts), they were not a priority for release. 

To run locally, users will need Python3.8+, Django 3.2.9, psycopg2-binary 2.9.1

A number of design choices were made in an effort to present a website that is beautiful in mobile first, and functional on desktop, rather than the other way around. For example, we abandoned the two-column guestbook (posts on left, new message on right), and separated login and signup for simplicity on mobile. Fonts, colors, buttons, and images were all designed to be an enjoyable mobile experience (it works well on desktop too). We had CSS effects (leaves falling across the base.html) but this too was abandoned because it was too distracting and unnecessary on mobile devices - especially for older users!

In the future, allowing users to upload images via the photos page would be a priority in advance of the wedding date. Additional Icebox tasks include updated page transitions via CSS/Javascript, and further media inquiry work to make the site even more presentable on desktop. 


# User Stories

A user should be able to signup for the website

A user should be able to login to the website if already signed up

A user should be asked to RSVP at signup

A user should be able to change RSVP status once logged in

A user should be able to see splash page before auth

An authenticated should be able to create, edit and delete their own posts (Guestbook page)

An authenticated user should be able to view the accomodations page (auth protected)

An authenticated user should be able to view the schedule page (auth protected)

An authenticated user should be able to email me (ICEBOX)

An authenticated user should be able to contact me in regards to hotel room blocks

An authenticated user should be able to log out from any page

Error pages should be styled with simple resolutions for non-savvy users!!!!

