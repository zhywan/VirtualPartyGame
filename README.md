# VirtualPartyGame

A game application for a group of people to play virtual party games.

<img src="https://github.com/zhywan/VirtualPartyGame/blob/master/Cher_Ami_logo.png?raw=true" width="200">

**Project Title**: *Cher Ami* for social networking via gaming.

**Project Motivation**: The new social experience will lead you from online to offline, and allow you: 1) No longer worry about meeting neighbors you don’t know, and 2) No longer afraid of not meeting the right person.

This is a hackaton project for [2020 UNICODE SC+ Hackathon](https://www.copell.cn/baseInfo?id=13), finished within 36 hours by a team of 4 members.

**Main Direction**: Promote more natural offline social interaction, and combine online social platforms and social game directions at the same time.

**Programming Languages**: Python, HTML, MySQL.

**Application Form**: Web application.

Here is [an example of the website interface](https://preview.webflow.com/preview/rachels-ultra-awesome-project-223052?utm_medium=preview_link&utm_source=dashboard&utm_content=rachels-ultra-awesome-project-223052&preview=a92c0e0d1c9b4b43c95f12233fd333bc).

<img src="https://github.com/zhywan/VirtualPartyGame/blob/master/webpages/home_page_1.JPG?raw=true" width="200"><img src="https://github.com/zhywan/VirtualPartyGame/blob/master/webpages/home_page_3.JPG?raw=true" width="200"><img src="https://github.com/zhywan/VirtualPartyGame/blob/master/webpages/home_page_4.JPG?raw=true" width="200"><img src="https://github.com/zhywan/VirtualPartyGame/blob/master/webpages/home_page_5.JPG?raw=true" width="200">

<img src="https://github.com/zhywan/VirtualPartyGame/blob/master/webpages/home_page_2.JPG?raw=true" width="200"><img src="https://github.com/zhywan/VirtualPartyGame/blob/master/webpages/home_page_6.JPG?raw=true" width="200">

<img src="https://github.com/zhywan/VirtualPartyGame/blob/master/webpages/faq_page.JPG?raw=true" width="200"><img src="https://github.com/zhywan/VirtualPartyGame/blob/master/webpages/breakroom_page_large.JPG?raw=true" width="500">

## **Introduction**:

### Background

In modern society, the relationships between people are getting farther and farther. As the saying goes, “distant relatives are not as good as close neighbors”, but today, the Internet has shortened the physical distance, but the physical distance in reality has become an insurmountable gap in interpersonal communication. Once upon a time, a small wall separated the relationship between neighbors. In steel forests, how many people know the last name of the person living the next door?

The ever-increasing social survival pressure and the ever-increasing overtime work hinder the expansion of young people's social circles, which has led to the increasing phenomenon of young people's late marriage. The traditional family appointment arrangements and the selection of existing dating software are too blind, matching with massive data and icy objective conditions, resulting in low adaptability and excessive random matching.

### Vision

Cher Ami originally means "dear friend" and is named after the French heroic pigeon in the Battle of Verdun. It has braved heavy artillery fire to communicate the location of the troops, thus saving about 200 American soldiers surrounded by the Germans.

We hope that our website can, like Cher Ami, convey the desire for communication for people trapped at home due to the epidemic, so that the epidemic will no longer be a common stumbling block to people.

At the same time, we also hope that Cher Ami can open a channel from online communication to offline communication, so that modern communication channels are no longer limited within one screen.

### Functionality

#### Function 1

In "neighbor mode", users will group with other users within a certain range. (E.g. 1km for the densely populated area, and 5km for the sparse area.) Users can create rooms by themselves or join the system to randomly allocate rooms for interaction.

The product does not set a common friend mode, but encourages users to interact and communicate with strangers.

The ice-breaking interactive games included in the product are mainly simple and easy to understand mini party games, such as "you draw and I guess", "guess the name of the song", etc., and also include games that are more popular and attract specific groups of people, such as "Werewolf" and "Mahjong".

The chat plug-in helps users who have met through online games to communicate further, so that they have a basic understanding when they meet offline and generate some common topics.

#### Function 2

The traditional dating matching model is one-to-one, and matching is based on a series of objective conditions such as age, income, etc., which is too cold. The communication between people should be warm, and the acquaintance of two people should be in agreement rather than whether one person is in possesion of a house or a car.

In Cher Ami's "dating mode", in addition to traditional standard matching, we encourage 5v5 group activities, and set up quiz games to enhance mutual understanding and coordination games to test cooperation, such as "guessing words", "You draw and I guess". It allows all participants to promote mutual understanding through games, and let your feelings tell you who is the one you are willing to learn more about!

### Features

#### Feature 1: Stay Connected with your neighborhood

In Neighborhood Mode, the system will locate a user based on the client's login IP address, and find nearby users.

#### Feature 2: Innovating Dating Experience

The innovative 5V5 dating mode, each game room is limited to 5 men and 5 women, users can choose the one with whom they cooeprated well and about whon they want to learn more.

#### Feature 3: New game is Online

Brand new online werewolf killing game experience, through the game, understand the people around you! Play online during the epidemic, and it will be easier to team up offline after the epidemic! 

Don't understand the rules of werewolf killing? No problem, the robot judge will take you step by step!

## **Design Framework of the Prototype**

### User registration

Several attributes of each user are collected by the client and sent to the server. These attributes are personal attributes such as name, gender, age, zodiac, city, state, zipcode, and profile picuture. In addition, user will selects his purpose: "neighbor mode" or "dating mode". At last, some preferences in terms of music and movie, etc, will be asked to better cluster users into groups. All information will be saved to MySQL database.

### User login/logout

When a user login, his or her ID wlil be used to maintain an active set of users.

### Game loop

After the server starts running, it waits until the number of active users exceeds a certain threshold, such as 10. Otherwise, it will wait for a certain time period, such as 10 seconds. If the number of active users satisfies the condition for beginning games, a fixed number of users such as 10, will be selected to begin games. The selection are according to a certain of rules that make sure the selected group of users are most similiar. Next, they can select the game they want to play and choose a set of game settings. Then the game will begin...

### Collection of user infomation from the web interface

User can register their account and modify their account through the website interface. And all these information will be saved to a MySQL database.

## **Descriptions of Files**

Cher_Ami_logo.png: logo for the project/appliction.

Hackathon_Project_Final.pptx: presentation slides for the hackathon.

README.md: introduction.

### prototype files (to be improved)

chat_client.py: the client script.

chat_server.py: the server script.

ip_mapper.py: a module used by the server to create a map html file based on Google Map API and other APIs.

map.html: temp file for map module.

user_info.ipynb: ipython notebook file for getting user info from website interface.

狼人杀.ipynb: Ipython notebook file for playing the werewolf killing game (with very basic functions).

### data folder

ip_list.txt: a file to save the ip and port of each connected client.

### webpages folder

home_page_1.JPG: a screenshot of the first part of a demo home page of the web application.

home_page_2.JPG: a screenshot of the second part of a demo home page of the web application.

home_page_3.JPG: a screenshot of the third part of a demo home page of the web application.

home_page_4.JPG: a screenshot of the fourth part of a demo home page of the web application.

home_page_5.JPG: a screenshot of the fifth part of a demo home page of the web application.

home_page_6.JPG: a screenshot of the sixth part of a demo home page of the web application.

breakroom_page.JPG: a screenshot of a demo breakroom page of the web application.

breakroom_page_large.JPG: a screenshot of a demo breakroom page of the web application. (Large version)

faq_page.JPG: a screenshot of a demo FAQ page of the web application.

## **Summary**

### Advantages

* Widely applicable and suitable for most countries and regions and most age groups (the dating mode is only available to ages of 18 and above)

* Encourage to break the traditional social networking circle, expand your social circle to those you are not afamiliar with but around you, and bring the social circle back into reality

* In the form of games, the efficiency and effectiveness of group dating is greatly improved, so that users can have a realistic understanding and perceptual knowledge of the potential partner at the beginning of the date.

### Future works

* This product can be extended to APP, applet, website and other applications.

* Bideo and voice functionalies can gradually be added to the product to promote further understandings among users.

* Since the product is aimed at promoting online communication to offline communication, future products can be added with functions that can only be offline solutions, such as *recommending offline restaurants* for neighbors or dating parties.

* In the future, a scoring mechanism can be added, and users can directly express their likes to other users in the form of sending flowers

* The problems targeted by the product are universal and are gradually highlighted all over the world. The application of Cher Ami can be extended to many countries and regions in the future.

(Team members: Rachel Ren, Zhiyu Wan, Haoran Zheng, Shizhuo Sun)
